import base64
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).parents[1]
    / "ian-xiaohei-illustrations"
    / "scripts"
    / "minimax_image_generation.py"
)
SPEC = importlib.util.spec_from_file_location("minimax_image_generation", SCRIPT)
assert SPEC and SPEC.loader
image_generation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(image_generation)


class FakeResponse:
    def __init__(self, content: bytes):
        self.content = content

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def read(self) -> bytes:
        return self.content


class MiniMaxImageGenerationTests(unittest.TestCase):
    def test_build_payload_uses_dimensions_instead_of_aspect_ratio(self):
        payload = image_generation.build_payload(
            "A clean hand-drawn scene",
            subject_references=["https://example.test/character.png"],
            width=1280,
            height=720,
            seed=42,
            count=2,
            prompt_optimizer=True,
        )

        self.assertEqual(payload["width"], 1280)
        self.assertEqual(payload["height"], 720)
        self.assertNotIn("aspect_ratio", payload)
        self.assertEqual(
            payload["subject_reference"],
            [
                {
                    "type": "character",
                    "image_file": "https://example.test/character.png",
                }
            ],
        )
        self.assertEqual(payload["seed"], 42)
        self.assertEqual(payload["n"], 2)
        self.assertTrue(payload["prompt_optimizer"])

    def test_request_images_uses_global_endpoint_by_default(self):
        captured = {}
        response_body = {
            "data": {"image_urls": ["https://example.test/generated.png"]},
            "base_resp": {"status_code": 0},
        }

        def opener(request, timeout):
            captured["url"] = request.full_url
            return FakeResponse(json.dumps(response_body).encode("utf-8"))

        image_generation.request_images(
            "test-key",
            {"model": "image-01", "prompt": "test"},
            opener=opener,
        )

        self.assertEqual(captured["url"], image_generation.ENDPOINTS["global_en"])

    def test_request_images_routes_to_china_endpoint(self):
        captured = {}
        response_body = {
            "data": {"image_urls": ["https://example.test/generated.png"]},
            "base_resp": {"status_code": 0},
        }

        def opener(request, timeout):
            captured["request"] = request
            captured["timeout"] = timeout
            return FakeResponse(json.dumps(response_body).encode("utf-8"))

        entries = image_generation.request_images(
            "test-key",
            {"model": "image-01", "prompt": "test"},
            region="cn_zh",
            timeout=15,
            opener=opener,
        )

        self.assertEqual(entries, ["https://example.test/generated.png"])
        self.assertEqual(captured["request"].full_url, image_generation.ENDPOINTS["cn_zh"])
        self.assertEqual(captured["request"].get_header("Authorization"), "Bearer test-key")
        self.assertEqual(captured["timeout"], 15)

    def test_request_images_reads_base64_response_field(self):
        encoded = base64.b64encode(b"image-content").decode("ascii")
        response_body = {
            "data": {"image_base64": [encoded]},
            "base_resp": {"status_code": 0},
        }

        entries = image_generation.request_images(
            "test-key",
            {
                "model": "image-01",
                "prompt": "test",
                "response_format": "base64",
            },
            opener=lambda request, timeout: FakeResponse(
                json.dumps(response_body).encode("utf-8")
            ),
        )

        self.assertEqual(entries, [encoded])

    def test_save_images_decodes_base64_entries(self):
        expected = b"png-image-content"
        encoded = base64.b64encode(expected).decode("ascii")

        with tempfile.TemporaryDirectory() as directory:
            paths = image_generation.save_images(
                [encoded],
                response_format="base64",
                output_dir=Path(directory),
                prefix="article",
            )

            self.assertEqual(paths[0].name, "article-01.png")
            self.assertEqual(paths[0].read_bytes(), expected)

    def test_save_images_downloads_url_entries(self):
        requested = []

        def opener(request, timeout):
            requested.append((request.full_url, timeout))
            return FakeResponse(b"downloaded-image")

        with tempfile.TemporaryDirectory() as directory:
            paths = image_generation.save_images(
                ["https://example.test/generated.webp?temporary=1"],
                response_format="url",
                output_dir=Path(directory),
                timeout=10,
                opener=opener,
            )

            self.assertEqual(paths[0].name, "illustration-01.webp")
            self.assertEqual(paths[0].read_bytes(), b"downloaded-image")
            self.assertEqual(requested, [("https://example.test/generated.webp?temporary=1", 10)])

    def test_request_images_rejects_api_error(self):
        response_body = {
            "base_resp": {"status_code": 1001, "status_msg": "invalid request"}
        }

        with self.assertRaisesRegex(image_generation.ImageGenerationError, "1001"):
            image_generation.request_images(
                "test-key",
                {"model": "image-01", "prompt": "test"},
                opener=lambda request, timeout: FakeResponse(
                    json.dumps(response_body).encode("utf-8")
                ),
            )


if __name__ == "__main__":
    unittest.main()

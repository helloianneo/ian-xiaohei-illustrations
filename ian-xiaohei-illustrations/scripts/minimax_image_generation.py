#!/usr/bin/env python3
"""Generate and save images with the MiniMax image generation API."""

from __future__ import annotations

import argparse
import base64
import binascii
import json
import os
import sys
from pathlib import Path
from typing import Any, Callable, Iterable
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ENDPOINTS = {
    "global_en": "https://api.minimax.io/v1/image_generation",
    "cn_zh": "https://api.minimaxi.com/v1/image_generation",
}
DEFAULT_MODEL = "image-01"
DEFAULT_ASPECT_RATIO = "16:9"
OpenUrl = Callable[..., Any]


class ImageGenerationError(RuntimeError):
    """Raised when an image generation response cannot be used."""


def build_payload(
    prompt: str,
    *,
    model: str = DEFAULT_MODEL,
    subject_references: Iterable[str] | None = None,
    aspect_ratio: str | None = DEFAULT_ASPECT_RATIO,
    width: int | None = None,
    height: int | None = None,
    response_format: str = "url",
    seed: int | None = None,
    count: int = 1,
    prompt_optimizer: bool = False,
) -> dict[str, Any]:
    """Build a text-to-image request and validate paired dimensions."""
    if not prompt.strip():
        raise ValueError("prompt must not be empty")
    if (width is None) != (height is None):
        raise ValueError("width and height must be provided together")
    if not 1 <= count <= 9:
        raise ValueError("count must be between 1 and 9")
    if response_format not in {"url", "base64"}:
        raise ValueError("response_format must be url or base64")

    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "response_format": response_format,
        "n": count,
        "prompt_optimizer": prompt_optimizer,
    }
    references = list(subject_references or [])
    if references:
        payload["subject_reference"] = [
            {"type": "character", "image_file": image_file}
            for image_file in references
        ]
    if width is not None and height is not None:
        payload.update({"width": width, "height": height})
    elif aspect_ratio:
        payload["aspect_ratio"] = aspect_ratio
    if seed is not None:
        payload["seed"] = seed
    return payload


def request_images(
    api_key: str,
    payload: dict[str, Any],
    *,
    region: str = "global_en",
    timeout: float = 120.0,
    opener: OpenUrl | None = None,
) -> list[str]:
    """Submit one generation request and return its image entries."""
    if region not in ENDPOINTS:
        raise ValueError(f"unsupported region: {region}")
    if not api_key:
        raise ValueError("MINIMAX_API_KEY is required")

    request = Request(
        ENDPOINTS[region],
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    open_url = opener or urlopen
    with open_url(request, timeout=timeout) as response:
        result = json.loads(response.read().decode("utf-8"))

    base_response = result.get("base_resp") or {}
    status_code = base_response.get("status_code")
    if status_code not in (None, 0):
        message = base_response.get("status_msg") or "image generation failed"
        raise ImageGenerationError(f"MiniMax API error {status_code}: {message}")

    response_format = payload.get("response_format", "url")
    response_field = "image_base64" if response_format == "base64" else "image_urls"
    data = result.get("data") or {}
    image_entries = data.get(response_field)
    if response_format == "base64" and image_entries is None:
        image_entries = data.get("image_urls")
    if not isinstance(image_entries, list) or not image_entries or not all(
        isinstance(item, str) and item for item in image_entries
    ):
        raise ImageGenerationError(f"response did not include data.{response_field}")
    return image_entries


def _decode_base64_image(value: str) -> bytes:
    encoded = value.split(",", 1)[1] if value.startswith("data:") and "," in value else value
    try:
        return base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise ImageGenerationError("response included invalid base64 image data") from exc


def _url_suffix(url: str) -> str:
    suffix = Path(urlparse(url).path).suffix.lower()
    return suffix if suffix in {".png", ".jpg", ".jpeg", ".webp"} else ".png"


def save_images(
    image_entries: Iterable[str],
    *,
    response_format: str,
    output_dir: Path,
    prefix: str = "illustration",
    timeout: float = 120.0,
    opener: OpenUrl | None = None,
) -> list[Path]:
    """Persist generated URL or base64 image entries to local files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    open_url = opener or urlopen
    saved: list[Path] = []

    for index, entry in enumerate(image_entries, start=1):
        if response_format == "base64":
            content = _decode_base64_image(entry)
            suffix = ".png"
        else:
            download = Request(entry, headers={"User-Agent": "ian-xiaohei-illustrations"})
            with open_url(download, timeout=timeout) as response:
                content = response.read()
            suffix = _url_suffix(entry)
        destination = output_dir / f"{prefix}-{index:02d}{suffix}"
        destination.write_bytes(content)
        saved.append(destination)
    return saved


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", help="Text description for the image")
    parser.add_argument(
        "--region",
        choices=sorted(ENDPOINTS),
        default=os.getenv("MINIMAX_REGION", "global_en"),
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument(
        "--subject-reference",
        action="append",
        default=[],
        metavar="URL_OR_DATA_URL",
        help="Character reference image; may be repeated",
    )
    parser.add_argument("--aspect-ratio", default=DEFAULT_ASPECT_RATIO)
    parser.add_argument("--width", type=int)
    parser.add_argument("--height", type=int)
    parser.add_argument("--response-format", choices=("url", "base64"), default="url")
    parser.add_argument("--seed", type=int)
    parser.add_argument("-n", "--count", type=int, default=1)
    parser.add_argument("--prompt-optimizer", action="store_true")
    parser.add_argument("--output-dir", type=Path, default=Path("generated"))
    parser.add_argument("--prefix", default="illustration")
    parser.add_argument("--timeout", type=float, default=120.0)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        payload = build_payload(
            args.prompt,
            model=args.model,
            subject_references=args.subject_reference,
            aspect_ratio=args.aspect_ratio,
            width=args.width,
            height=args.height,
            response_format=args.response_format,
            seed=args.seed,
            count=args.count,
            prompt_optimizer=args.prompt_optimizer,
        )
        image_entries = request_images(
            os.getenv("MINIMAX_API_KEY", ""),
            payload,
            region=args.region,
            timeout=args.timeout,
        )
        paths = save_images(
            image_entries,
            response_format=args.response_format,
            output_dir=args.output_dir,
            prefix=args.prefix,
            timeout=args.timeout,
        )
    except (ImageGenerationError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Image generation failed: {exc}", file=sys.stderr)
        return 1

    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

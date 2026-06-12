# 🦕 Dinosaur API Implementation

## Description
This PR introduces a complete REST API for serving black and white hand-drawn dinosaur illustrations with comprehensive filtering and search capabilities.

## Features Added
- ✅ Express.js server with CORS support
- ✅ 8 dinosaurs with detailed metadata (scientific names, eras, diet types, dimensions)
- ✅ API endpoints for:
  - Get all dinosaurs
  - Get dinosaur by ID
  - Search by name/scientific name
  - Filter by era, diet type, tags
  - Get random dinosaur(s)
  - Browse available filters
- ✅ Utility functions for filtering and searching
- ✅ Error handling and validation
- ✅ Complete API documentation

## Files Added
- `api/server.js` - Express server configuration
- `api/routes/dinosaurs.js` - API route handlers
- `api/utils/helpers.js` - Utility functions
- `api/data/dinosaurs.json` - Dinosaur database (8 species)
- `api/package.json` - Dependencies configuration
- `api/.env.example` - Environment variables template
- `api/.gitignore` - Git ignore rules
- `api/README.md` - Complete API documentation

## API Endpoints
- `GET /api/dinosaurs` - Get all dinosaurs
- `GET /api/dinosaurs/:id` - Get specific dinosaur
- `GET /api/dinosaurs?search=query` - Search dinosaurs
- `GET /api/dinosaurs?era=Cretaceous` - Filter by era
- `GET /api/dinosaurs?dietType=Carnivore` - Filter by diet
- `GET /api/dinosaurs/random/one?count=1` - Get random dinosaur(s)
- `GET /api/dinosaurs/filters/eras` - Available eras
- `GET /api/dinosaurs/filters/diets` - Available diet types

## Dinosaurs Included
1. Tyrannosaurus Rex (Cretaceous)
2. Triceratops (Cretaceous)
3. Stegosaurus (Jurassic)
4. Velociraptor (Cretaceous)
5. Brachiosaurus (Jurassic)
6. Ankylosaurus (Cretaceous)
7. Parasaurolophus (Cretaceous)
8. Pteranodon (Cretaceous)

## Next Steps
- [ ] Create SVG/PNG dinosaur illustrations
- [ ] Add illustrations to `/assets/dinosaurs/`
- [ ] Test API endpoints
- [ ] Deploy to production

## Related Issues
Closes #0

## Type of Change
- [x] New feature (non-breaking change which adds functionality)

## Testing
```bash
cd api
npm install
npm run dev
# Visit http://localhost:3000 to see API documentation
```

## Checklist
- [x] My code follows the style guidelines
- [x] I have commented my code
- [x] I have made corresponding changes to the documentation
- [x] My changes generate no new warnings

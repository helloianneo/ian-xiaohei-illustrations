# 🦕 Dinosaur API

A RESTful API for black and white hand-drawn dinosaur illustrations, providing detailed information about 8 iconic dinosaurs.

## Features

- ✅ Get all dinosaurs or filter by era, diet type, and tags
- ✅ Search dinosaurs by name or scientific name
- ✅ Get random dinosaur(s)
- ✅ Browse available eras and diet types
- ✅ CORS enabled for cross-origin requests
- ✅ Clean, well-documented JSON responses

## Quick Start

### Installation

```bash
cd api
npm install
```

### Development

```bash
npm run dev
```

The API will start at `http://localhost:3000`

### Production

```bash
npm start
```

## API Endpoints

### Get All Dinosaurs
```
GET /api/dinosaurs
```

### Get Specific Dinosaur
```
GET /api/dinosaurs/:id
```

### Search Dinosaurs
```
GET /api/dinosaurs?search=query
```

### Filter by Era
```
GET /api/dinosaurs?era=Cretaceous
```

### Filter by Diet Type
```
GET /api/dinosaurs?dietType=Carnivore
```

### Filter by Tag
```
GET /api/dinosaurs?tag=iconic
```

### Get Random Dinosaur(s)
```
GET /api/dinosaurs/random/one?count=1
```

### Get Available Eras
```
GET /api/dinosaurs/filters/eras
```

### Get Available Diet Types
```
GET /api/dinosaurs/filters/diets
```

## Dinosaur Database

Includes 8 dinosaurs:

1. **Tyrannosaurus Rex** - Fierce Cretaceous predator
2. **Triceratops** - Three-horned defensive herbivore
3. **Stegosaurus** - Plated Jurassic herbivore
4. **Velociraptor** - Agile Cretaceous hunter
5. **Brachiosaurus** - Giant sauropod from Jurassic
6. **Ankylosaurus** - Armored Cretaceous herbivore
7. **Parasaurolophus** - Crested Cretaceous hadrosaur
8. **Pteranodon** - Flying Cretaceous reptile

## Project Structure

```
api/
├── server.js              # Main Express server
├── package.json           # Dependencies
├── .env.example          # Environment variables template
├── routes/
│   └── dinosaurs.js      # API route handlers
├── utils/
│   └── helpers.js        # Utility functions
├── data/
│   └── dinosaurs.json    # Dinosaur database
└── README.md             # This file
```

## Configuration

Create a `.env` file based on `.env.example`:

```env
PORT=3000
NODE_ENV=development
API_BASE_URL=http://localhost:3000
```

## License

MIT License

/**
 * Dinosaur API Server
 * Black & White Dinosaur Illustration API
 */

require('dotenv').config();
const express = require('express');
const cors = require('cors');
const path = require('path');

const dinosaurRoutes = require('./routes/dinosaurs');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Static files
app.use('/assets', express.static(path.join(__dirname, '../assets')));

// API Routes
app.use('/api/dinosaurs', dinosaurRoutes);

// Health check endpoint
app.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    name: 'Dinosaur API',
    version: '1.0.0',
    description: 'Black & White Dinosaur Illustration API',
    endpoints: {
      getAllDinosaurs: 'GET /api/dinosaurs',
      getDinosaur: 'GET /api/dinosaurs/:id',
      getRandomDinosaur: 'GET /api/dinosaurs/random/one?count=1',
      getAvailableEras: 'GET /api/dinosaurs/filters/eras',
      getAvailableDiets: 'GET /api/dinosaurs/filters/diets',
      healthCheck: 'GET /health'
    },
    queryParams: {
      search: 'Search by name or scientific name (GET /api/dinosaurs?search=T-Rex)',
      era: 'Filter by era (GET /api/dinosaurs?era=Cretaceous)',
      dietType: 'Filter by diet type (GET /api/dinosaurs?dietType=Carnivore)',
      tag: 'Filter by tag (GET /api/dinosaurs?tag=iconic)'
    }
  });
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({
    success: false,
    error: 'Endpoint not found'
  });
});

// Error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    success: false,
    error: 'Internal server error'
  });
});

// Start server
app.listen(PORT, () => {
  console.log(`🦕 Dinosaur API running on http://localhost:${PORT}`);
  console.log(`📚 API Documentation: http://localhost:${PORT}`);
});

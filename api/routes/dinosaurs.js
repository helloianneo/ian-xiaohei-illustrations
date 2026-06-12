/**
 * Dinosaur API Routes
 */

const express = require('express');
const router = express.Router();
const dinosaurData = require('../data/dinosaurs.json');
const {
  filterDinosaurs,
  searchDinosaurs,
  getRandomDinosaur,
  getUniqueEras,
  getUniqueDietTypes
} = require('../utils/helpers');

/**
 * GET /api/dinosaurs
 * Get all dinosaurs or filter by query parameters
 */
router.get('/', (req, res) => {
  try {
    const { era, dietType, tag, search } = req.query;
    let result = dinosaurData;

    // Apply search if provided
    if (search) {
      result = searchDinosaurs(result, search);
    } else {
      // Apply filters if provided
      const filters = {};
      if (era) filters.era = era;
      if (dietType) filters.dietType = dietType;
      if (tag) filters.tag = tag;

      if (Object.keys(filters).length > 0) {
        result = filterDinosaurs(result, filters);
      }
    }

    res.json({
      success: true,
      count: result.length,
      data: result
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * GET /api/dinosaurs/:id
 * Get a specific dinosaur by ID
 */
router.get('/:id', (req, res) => {
  try {
    const { id } = req.params;
    const dinosaur = dinosaurData.find(d => d.id === id);

    if (!dinosaur) {
      return res.status(404).json({
        success: false,
        error: `Dinosaur with ID "${id}" not found`
      });
    }

    res.json({
      success: true,
      data: dinosaur
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * GET /api/dinosaurs/random/one
 * Get random dinosaur(s)
 */
router.get('/random/one', (req, res) => {
  try {
    const { count = 1 } = req.query;
    const numCount = Math.min(parseInt(count) || 1, dinosaurData.length);
    const random = getRandomDinosaur(dinosaurData, numCount);

    res.json({
      success: true,
      count: Array.isArray(random) ? random.length : 1,
      data: random
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * GET /api/dinosaurs/filters/eras
 * Get all available eras
 */
router.get('/filters/eras', (req, res) => {
  try {
    const eras = getUniqueEras(dinosaurData);
    res.json({
      success: true,
      data: eras
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

/**
 * GET /api/dinosaurs/filters/diets
 * Get all available diet types
 */
router.get('/filters/diets', (req, res) => {
  try {
    const diets = getUniqueDietTypes(dinosaurData);
    res.json({
      success: true,
      data: diets
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message
    });
  }
});

module.exports = router;

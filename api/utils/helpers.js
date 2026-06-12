/**
 * Utility functions for the Dinosaur API
 */

/**
 * Filter dinosaurs by criteria
 * @param {Array} dinosaurs - Array of dinosaur objects
 * @param {Object} filters - Filter criteria
 * @returns {Array} Filtered dinosaurs
 */
function filterDinosaurs(dinosaurs, filters) {
  return dinosaurs.filter(dino => {
    if (filters.era && dino.era !== filters.era) return false;
    if (filters.dietType && dino.dietType !== filters.dietType) return false;
    if (filters.tag && !dino.tags.includes(filters.tag)) return false;
    return true;
  });
}

/**
 * Search dinosaurs by name or scientific name
 * @param {Array} dinosaurs - Array of dinosaur objects
 * @param {String} query - Search query
 * @returns {Array} Matching dinosaurs
 */
function searchDinosaurs(dinosaurs, query) {
  const lowerQuery = query.toLowerCase();
  return dinosaurs.filter(dino => 
    dino.name.toLowerCase().includes(lowerQuery) ||
    dino.scientificName.toLowerCase().includes(lowerQuery)
  );
}

/**
 * Get random dinosaur(s)
 * @param {Array} dinosaurs - Array of dinosaur objects
 * @param {Number} count - Number of random dinosaurs to return (default: 1)
 * @returns {Array|Object} Random dinosaur(s)
 */
function getRandomDinosaur(dinosaurs, count = 1) {
  if (count === 1) {
    return dinosaurs[Math.floor(Math.random() * dinosaurs.length)];
  }
  
  const shuffled = [...dinosaurs].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, Math.min(count, dinosaurs.length));
}

/**
 * Get unique eras from dinosaurs
 * @param {Array} dinosaurs - Array of dinosaur objects
 * @returns {Array} Unique eras
 */
function getUniqueEras(dinosaurs) {
  return [...new Set(dinosaurs.map(d => d.era))];
}

/**
 * Get unique diet types from dinosaurs
 * @param {Array} dinosaurs - Array of dinosaur objects
 * @returns {Array} Unique diet types
 */
function getUniqueDietTypes(dinosaurs) {
  return [...new Set(dinosaurs.map(d => d.dietType))];
}

module.exports = {
  filterDinosaurs,
  searchDinosaurs,
  getRandomDinosaur,
  getUniqueEras,
  getUniqueDietTypes
};

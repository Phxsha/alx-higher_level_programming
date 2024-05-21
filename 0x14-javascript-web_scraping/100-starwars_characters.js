#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (movieId) {
  // Make a GET request to the API
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    // Parse the response body as JSON
    const data = JSON.parse(body);
    // Print the characters of the movie
    data.characters.forEach(character => {
      // Make a GET request to fetch character details
      request(character, (err, res, body) => {
        if (err) {
          console.error('Error:', err);
          return;
        }
        // Parse character details as JSON
        const characterData = JSON.parse(body);
        // Print the character name
        console.log(characterData.name);
      });
    });
  });
} else {
  console.error('Usage: ./100-starwars_characters.js <movieId>');
}

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
    const film = JSON.parse(body);
    // Create a list to store character URLs
    const characterUrls = film.characters;

    // Function to fetch and print character names
    const printCharacterName = (urlIndex) => {
      // Check if all character names are printed
      if (urlIndex === characterUrls.length) {
        return;
      }
      // Make a GET request to fetch character details
      request(characterUrls[urlIndex], (err, res, body) => {
        if (err) {
          console.error('Error:', err);
          return;
        }
        // Parse character details as JSON
        const characterData = JSON.parse(body);
        // Print the character name
        console.log(characterData.name);
        // Call the function recursively to print the next character name
        printCharacterName(urlIndex + 1);
      });
    };

    // Start printing character names
    printCharacterName(0);
  });
} else {
  console.error('Usage: ./101-starwars_characters.js <movieId>');
}

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
    // Print the title of the movie
    console.log(data.title);
  });
} else {
  console.error('Usage: ./3-starwars_title.js <movieId>');
}

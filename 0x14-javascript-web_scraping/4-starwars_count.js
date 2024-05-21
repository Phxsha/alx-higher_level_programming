#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

if (apiUrl) {
  // Make a GET request to the API
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    // Parse the response body as JSON
    const data = JSON.parse(body);
    let count = 0;
    // Iterate over the films and count the ones with Wedge Antilles (character ID 18)
    data.results.forEach(film => {
      if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        count++;
      }
    });
    // Print the count
    console.log(count);
  });
} else {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
}

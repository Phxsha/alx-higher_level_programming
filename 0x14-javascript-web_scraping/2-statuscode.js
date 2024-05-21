#!/usr/bin/node

const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

if (url) {
  // Make a GET request to the URL
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    // Print the status code
    console.log('code:', response.statusCode);
  });
} else {
  console.error('Usage: ./2-statuscode.js <URL>');
}

#!/usr/bin/node

const fs = require('fs');
const request = require('request');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

if (url && filePath) {
  // Make a GET request to the URL
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }
    // Write the response body to the file
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
        return;
      }
      console.log('Response body saved to', filePath);
    });
  });
} else {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
}

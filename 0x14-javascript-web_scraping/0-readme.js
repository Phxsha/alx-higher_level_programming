#!/usr/bin/node

const fs = require('fs');

// Get the file path from the first argument
const filePath = process.argv[2];

if (!filePath) {
  console.error('Please provide a file path as an argument.');
  process.exit(1); // Exit with an error code
}

// Read the file content in UTF-8 encoding
fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error('Error reading file:', error);
  } else {
    console.log(data.trim()); // Print the content without leading/trailing whitespaces
  }
});

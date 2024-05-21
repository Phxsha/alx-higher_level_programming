#!/usr/bin/node

const fs = require('fs');

// Get file path and string content from arguments
const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Please provide both file path and content as arguments.');
  process.exit(1); // Exit with an error code
}

// Write the content to the file in UTF-8 encoding
fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});

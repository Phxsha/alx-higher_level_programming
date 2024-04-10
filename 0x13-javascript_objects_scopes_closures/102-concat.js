#!/usr/bin/node

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the contents of sourceFile1
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    return;
  }

  // Read the contents of sourceFile2
  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      return;
    }

    // Concatenate the contents of both files
    const concatenatedData = `${data1}${data2}`;

    // Write the concatenated data to the destination file
    fs.writeFile(destinationFile, concatenatedData, err => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Concatenated files ${sourceFile1} and ${sourceFile2} into ${destinationFile}`);
    });
  });
});

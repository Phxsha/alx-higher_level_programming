#!/usr/bin/node

// Check if the first argument can be converted to an integer
const num = parseInt(process.argv[2]);

// Check if the result is a number
if (!isNaN(num)) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}

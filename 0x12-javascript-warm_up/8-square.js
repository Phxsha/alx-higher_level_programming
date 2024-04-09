#!/usr/bin/node

// Check if the first argument is provided and convert it to an integer
const size = parseInt(process.argv[2]);

// Check if the argument is a valid positive integer
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // Loop to print the square
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}

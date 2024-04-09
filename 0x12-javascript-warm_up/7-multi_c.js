#!/usr/bin/node

// Check if the first argument is provided and convert it to an integer
const x = parseInt(process.argv[2]);

// Check if the argument is a valid number
if (isNaN(x) || x <= 0) {
  console.log('Missing number of occurrences');
} else {
  // Loop x times and print "C is fun"
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

#!/usr/bin/node

// Define the function add
function add(a, b) {
  return parseInt(a) + parseInt(b);
}

// Get the arguments
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Check if both arguments are provided and are integers
if (!arg1 || !arg2 || isNaN(arg1) || isNaN(arg2)) {
  console.log("NaN");
} else {
  // Call the add function and print the result
  console.log(add(arg1, arg2));
}

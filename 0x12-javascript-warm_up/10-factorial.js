#!/usr/bin/node

// Define the factorial function recursively
function factorial(n) {
  // Base case: if n is NaN or less than 0, return 1
  if (isNaN(n) || n < 0) {
    return 1;
  }
  // Base case: if n is 0, return 1
  if (n === 0) {
    return 1;
  }
  // Recursive case: compute factorial using recursion
  return n * factorial(n - 1);
}

// Get the argument
const arg = process.argv[2];

// Calculate the factorial and print the result
console.log(factorial(parseInt(arg)));

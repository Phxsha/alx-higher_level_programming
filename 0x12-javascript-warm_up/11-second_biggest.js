#!/usr/bin/node

// Get the arguments, convert them to integers, and filter out non-integer values
const numbers = process.argv.slice(2).map(Number).filter(num => !isNaN(num));

// Check the length of the filtered array
if (numbers.length <= 1) {
  // If there are no arguments or only one argument, print 0
  console.log(0);
} else {
  // Sort the array in ascending order
  numbers.sort((a, b) => a - b);
  // Print the second last element
  console.log(numbers[numbers.length - 2]);
}

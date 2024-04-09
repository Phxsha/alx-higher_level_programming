#!/usr/bin/node

// Define the function addMeMaybe
function addMeMaybe (number, theFunction) {
  // Increment the number
  const newValue = number + 1;
  // Call the function with the incremented value
  theFunction(newValue);
}

// Export the addMeMaybe function
module.exports.addMeMaybe = addMeMaybe;

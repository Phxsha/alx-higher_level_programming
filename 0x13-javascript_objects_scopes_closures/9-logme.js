#!/usr/bin/node

let count = 0; // Keep track of the number of arguments printed

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};

#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  // Define the incr function
  incr: function () {
    // Increment the value property
    this.value++;
  }
};

console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

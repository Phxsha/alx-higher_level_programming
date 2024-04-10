#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call Rectangle's constructor with size for both width and height
  }
}

module.exports = Square;

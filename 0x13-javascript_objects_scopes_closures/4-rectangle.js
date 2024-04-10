#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return {}; // Return empty object if width or height is not positive
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // Swap width and height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Double the width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

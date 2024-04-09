#!/usr/bin/node

const Rectangle = require('./4-rectangle'); // Import the Rectangle class

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call Rectangle constructor with size for both width and height
  }

  double () {
    super.double();
  }
}

module.exports = Square;

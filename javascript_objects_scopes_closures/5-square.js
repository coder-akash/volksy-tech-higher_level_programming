#!/usr/bin/node

class Square extends require('./4-rectangle.js') {
  constructor (s) {
    super(s, s);
  }
}
module.exports = Square;

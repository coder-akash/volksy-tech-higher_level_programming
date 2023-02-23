#!/usr/bin/node

class Square extends require('./4-rectangle.js') {
  constructor (s) {
    super(s, s);
  }

  charPrint (c) {
    if (typeof c !== 'undefined') {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;

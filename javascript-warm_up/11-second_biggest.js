#!/usr/bin/node

const x = process.argv.slice(2);
// console.log(x)
if (x.length === 0 || (x.length === 1 && x[0] === '1')) {
  console.log(0);
} else {
  console.log(Math.max.apply(null, x));
}

#!/usr/bin/node
const x = process.argv.length;
console.log(x == 3 ? 'Argument found' : x > 3 ? 'Arguments found' : 'No argument');

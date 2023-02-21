#!/usr/bin/node
x = process.argv.length
console.log(x == 3 ? "Argument found" : x > 3 ? "Arguments found" : "No argument")

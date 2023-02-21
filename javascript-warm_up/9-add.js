#!/usr/bin/node
function add () {
  console.log(Number.parseInt(process.argv[2]) + Number.parseInt(process.argv[3]));
}
add();

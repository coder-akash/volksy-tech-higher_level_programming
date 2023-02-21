#!/usr/bin/node
const x = Number.parseInt(process.argv[2]);
const f = 1;
function fact (num, f) {
  // console.log(num, f)
  if (num > 1) {
    f = f * num;
    fact(num - 1, f);
  } else {
    console.log(f);
  }
}
fact(x, f);

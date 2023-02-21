#!/usr/bin/node

let x = process.argv.slice(2)
    //console.log(x)
if (x.length === 0 || (x.length === 1 && x[0] === '1')) {
    console.log(0)
} else {
    x.sort().reverse()
    console.log(x[1])
}

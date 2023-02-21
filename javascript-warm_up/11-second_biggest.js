#!/usr/bin/node

let x = process.argv.slice(2)
    //console.log(x)
if (x.length === 0 || (x.length === 1 && x[0] === '1')) {
    console.log(0)
} else {
    for (let i in x) {
        x[i] = Number.parseInt(x[i])
    }
    console.log(x.sort(function(a, b) { return b - a })[1])
}

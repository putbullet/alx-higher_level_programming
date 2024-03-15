#!/usr/bin/node

let n = parseInt(process.argv[2]);

function factorial(x) {
    if (isNaN(x)) {
        return 1; // Factorial of NaN is 1
    }
    if (x === 0) {
        return 1; // Base case: 0! = 1
    } else {
        return x * factorial(x - 1); // Recursive case
    }
}

console.log(factorial(n));

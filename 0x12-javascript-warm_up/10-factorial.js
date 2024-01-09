#!/usr/bin/node
const num = parseInt(process.argv[2]);

function factorial (num) {
  if (Number.isNaN(num) || num === 0 || num === 1) {
    return (1);
  }

  if (num > 0) {
    return (num * factorial(num - 1));
  }
}

const result = factorial(num);
console.log(result);

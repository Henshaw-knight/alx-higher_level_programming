#!/usr/bin/node
const args = process.argv;
let max = parseInt(process.argv[2]);
let max2 = parseInt(process.argv[3]);

if (args.length < 3 || !Number.isInteger(max)) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    const currentNum = parseInt(args[i]);
    if (currentNum > max) {
      max2 = max;
      max = currentNum;
    }

    if (currentNum > max2 && currentNum < max) {
      max2 = currentNum;
    }
  }
  console.log(max2);
}

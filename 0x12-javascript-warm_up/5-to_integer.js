#!/usr/bin/node

const firstArg = process.argv[2];

if (isNaN(Number(firstArg))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(firstArg)}`);
}

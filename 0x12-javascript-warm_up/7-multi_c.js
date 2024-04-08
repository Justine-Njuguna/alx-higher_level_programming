#!/usr/bin/node

const firstArg = process.argv[2];

if (isNaN(Number(firstArg))) {
  console.log('Missing number of occurrences');
} else {
  const numIterations = parseInt(firstArg);
  for (let i = 0; i < numIterations; i++) {
    console.log('C is fun');
  }
}

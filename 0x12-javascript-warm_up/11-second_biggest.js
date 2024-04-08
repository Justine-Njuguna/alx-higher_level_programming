#!/usr/bin/node

function findSecondLargest (numbers) {
  if (numbers.length === 0) {
    return 0;
  } else if (numbers.length === 1) {
    return 0;
  }

  // Sort the array in descending order
  numbers.sort((a, b) => b - a);

  // Remove duplicates (optional for efficiency, not strictly required by task)
  const uniqueNumbers = [...new Set(numbers)];

  // Second largest element (if it exists) is at index 1 after sorting
  return uniqueNumbers[1] !== undefined ? uniqueNumbers[1] : 0;
}

const args = process.argv.slice(2).map(Number);

const secondLargest = findSecondLargest(args);
console.log(secondLargest);

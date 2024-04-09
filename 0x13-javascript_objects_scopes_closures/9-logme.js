#!/usr/bin/node

let printedCount = 0; // Variable to track the number of arguments printed

exports.logMe = function (item) {
  console.log(`${printedCount++}: ${item}`); // Use template literal for formatting
};

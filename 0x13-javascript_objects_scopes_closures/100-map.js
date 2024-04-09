#!/usr/bin/node

// Import the list from 100-data.js
const list = require('./100-data').list;

// Create a new list using map
const newList = list.map((element, index) => element * index);

// Print the original list
console.log(list);

// Print the new list
console.log(newList);

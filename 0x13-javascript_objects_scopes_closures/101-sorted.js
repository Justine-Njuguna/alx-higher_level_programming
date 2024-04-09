#!/usr/bin/node

// Import the dictionary from 101-data.js
const dict = require('./101-data').dict;

// Create a new dictionary to store user IDs by occurrence
const usersByOccurrence = {};

// Loop through the original dictionary
for (const userId in dict) {
  const occurrence = dict[userId]; // Get the occurrence count for the current user

  // Check if an entry for this occurrence exists in the new dictionary
  if (!usersByOccurrence[occurrence]) {
    usersByOccurrence[occurrence] = []; // Initialize an empty list for this occurrence
  }

  // Add the current user ID to the list for this occurrence
  usersByOccurrence[occurrence].push(userId);
}

// Print the new dictionary
console.log(usersByOccurrence);

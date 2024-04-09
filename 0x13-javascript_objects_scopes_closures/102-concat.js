#!/usr/bin/node

const fs = require('fs');

// Get file paths from command line arguments
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Function to read and concatenate file content
function concatenateFiles (source1, source2, destination) {
  let content = '';
  fs.promises.readFile(source1, 'utf8')
    .then(data => {
      content += data; // Append content from source1
      return fs.promises.readFile(source2, 'utf8');
    })
    .then(data => {
      content += data; // Append content from source2
      return fs.promises.writeFile(destination, content, 'utf8');
    })
    .catch(err => {
      console.error('Error:', err);
    });
}

// Call the function with provided file paths
concatenateFiles(sourceFile1, sourceFile2, destinationFile);

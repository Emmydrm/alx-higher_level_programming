#!/usr/bin/node
// writes a string to a file
const fs = require('fs');
const filepath = process.argv[2];
const string = process.argv[3];

fs.writeFile(filepath, string, (error) => {
  if (error) {
    console.error(error);
  }
});

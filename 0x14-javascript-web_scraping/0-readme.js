#!/usr/bin/node
// prints the content of a file
const fs = require('fs');

const filepath = process.argv[2];

fs.readFile(filepath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});

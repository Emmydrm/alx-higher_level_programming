#!/usr/bin/node
// Gets the content of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

// request url
request(url, (error, response, body) => {
  if (error) { console.error(error); }
  if (response.statusCode === 200) {
    // store in file
    fs.writeFile(filePath, body, (error) => {
      if (error) {
        console.error(error);
      }
    });
  }
});

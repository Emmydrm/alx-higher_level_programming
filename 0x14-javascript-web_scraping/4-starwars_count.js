#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present
const request = require('request');

const url = process.argv[2];
let movies = 0;

if (url !== undefined) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const results = JSON.parse(body).results;
      results.forEach(element => {
        element.characters.forEach(character => {
          // check for character
          if (character.includes('18')) {
            movies++;
          }
        });
      });
      console.log(movies);
    }
  });
}

#!/usr/bin/node
// prints all characters of a star wars movie
const request = require('request');
const id = process.argv[2];

if (id) {
  const url = `https://swapi-api.hbtn.io/api/films/${id}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const characters = JSON.parse(body).characters;
      characters.forEach(character => {
        request(character, (error, response, body) => {
          if (error == null) {
            console.log(JSON.parse(body).name);
          }
        });
      });
    }
  });
}

#!/usr/bin/node
// Computes the number of tasks completed by user id
const request = require('request');

const url = process.argv[2];
const data = {};

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  if (response.statusCode === 200) {
    JSON.parse(body).forEach(task => {
      if (task.userId in data && task.completed === true) {
        data[`${task.userId}`]++;
      } else if (task.completed === true) {
        data[`${task.userId}`] = 1;
      }
    });
    // console.log(body);
  }
  console.log(data);
});

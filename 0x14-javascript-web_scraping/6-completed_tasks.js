#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const completed = {};
    const json = JSON.parse(body);
    for (let i = 0; i < json.length; i++) {
      if (json[i].completed === true) {
        if (completed[json[i].userId] === undefined) {
          completed[json[i].userId] = 0;
        }
        completed[json[i].userId]++;
      }
    }
    console.log(completed);
  }
});

#!/usr/bin/node
const dict = require('./101-data').dict;

const storage = {};

for (const item in dict) {
  if (!storage[dict[item]]) {
    storage[dict[item]] = [];
  }
  storage[dict[item]].push(item);
}

console.log(storage);

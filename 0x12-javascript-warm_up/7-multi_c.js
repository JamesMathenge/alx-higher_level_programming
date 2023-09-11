#!/usr/bin/node

const process = require('process');
const Arg = process.argv[2];

const x = parseInt(Arg);

if (!isNaN(x)) {
  for (let z = 0; z < x; z++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

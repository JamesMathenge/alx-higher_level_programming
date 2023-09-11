#!/usr/bin/node

const process = require('process');

const Args = process.argv;
if (Args[2]) {
  console.log(Args[2]);
} else {
  console.log('No argument');
}

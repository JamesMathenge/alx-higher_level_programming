#!/usr/bin/node

const Count = process.argv.length - 2;

if (Count === 0) {
  console.log('No argument');
} else if (Count === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

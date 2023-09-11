#!/usr/bin/node

const arguments_Count = process.argv.length - 2;

if (arguments_Count === 0) {
  console.log('No argument');
} else if (arguments_Count === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

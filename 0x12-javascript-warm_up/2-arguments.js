#!/usr/bin/node

const list = process.argv.length-2;


if (list === 0) {
	console.log('No argument');
} else {
	console.log('Arguments found');
}

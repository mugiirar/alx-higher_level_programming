#!/usr/bin/node

const list = process.argv.length;

let num = list - 2;

if (num === 0)
{
	console.log('No argument');
}
else
{
	console.log('Arguments found');
}

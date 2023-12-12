#!/usr/bin/node

let args = process.argv;

let num = Number(args[2]);

let integ = parseInt(num);
if (isNaN(num)) {
	console.log("Not a number");
} else {
	console.log("My number: " + String(integ));
}

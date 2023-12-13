#!/usr/bin/node
const args = process.argv.slice(2);
let limit = 0;
if (args.length > 1) {
	limit = args.sort()[args.length - 2];
}
console.log(limit);

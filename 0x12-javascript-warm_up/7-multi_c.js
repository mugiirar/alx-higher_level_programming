#!/usr/bin/node
const limit = parseInt(process.argv[2]);

if (isNaN(limit)) {
	console.log("Missing number of occurrences");
} else if (limit > 0)
{
	let count = 0;
	while (count < limit) {
		console.log("C is fun");
		count = count + 1;
	}
} else {
}


#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let num = 0;
	for (const i of list) {
		if (i === searchElement) {
			num++;
		}
	}
	return num;
};

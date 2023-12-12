#!/usr/bin/node
module.exports = class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			[this.width, this.height] = [w, h];
		}
	}
	print() {
		let row = 'X'.repeat(this.width);
		for (let i = 0; i < this.height; i++) {
			console.log(row);
		}
	}
	rotate() {
		[this.width, this.height] = [this.height, this.width];
  }
	double() {
		[this.width, this.height] = [this.width * 2, this.height * 2];
	}
};


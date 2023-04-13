#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		let concat = '';
		for (let i = 0; i < this.height; i++) {
			for (let j = 0; j < this.width; j++) {
				concat = concat + 'X';
			}
			console.log(concat);
			concat = '';
		}
	}

	rotate () {
		const tempWidth = this.width;
		this.width = this.height;
		this.height = tempWidth;
	}

	double () {
		this.width = 2 * this.width;
		this.height = 2 * this.height;
	}
}
module.exports = Rectangle;

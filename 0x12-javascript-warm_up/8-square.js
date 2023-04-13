#!/usr/bin/node

const args = process.argv;
const size = parseInt(args[2]);

if (isNaN(size)) {
	console.log('Missing size');
} else {
	let xaxis = '';

	for (let i = 0; i < size; i++) {
		xaxis += 'X';
	}

	for (let i = 0; i < size; i++) {
		console.log(xaxis);
	}
}

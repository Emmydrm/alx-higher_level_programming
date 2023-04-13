#!/usr/bin/node

const args = process.argv;

function add (a, b) {
	console.log(a + b);
}

const first = parseInt(args[2]);
const second = parseInt(args[3]);
add(first, second);

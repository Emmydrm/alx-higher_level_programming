#!/usr/bin/node

const args = process.argv;

function factorial (number) {
	if (isNaN(number) || number === 0) {
		return 1;
	}

	return number * factorial(number - 1);
}

const number = parseInt(args[2]);
console.log(factorial(number));

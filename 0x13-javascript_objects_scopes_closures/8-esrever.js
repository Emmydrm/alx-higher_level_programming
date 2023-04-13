#!/usr/bin/node
exports.esrever = function (list) {
	const reverseArr = [];
	const arrLen = list.length;
	for (let i = 0; i < arrLen; i++) {
		reverseArr[i] = list[arrLen - 1 - i];
	}
	return reverseArr;
};

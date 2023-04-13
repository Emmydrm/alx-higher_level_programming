#!/usr/bin/node

exports.converter = function (base) {
	function myConvertor (value) {
		return (value.toString(base));
	}
	return myConvertor;
};

#include "Python.h"
#include <stdio.h>

/**
 * print_python_float - prints basic info about Python float objects
 * @p: Python object (bytes)
 */
void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}
/**
 * print_python_bytes - prints basic info about Python bytes
 * @p: Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
	ssize_t i;
	ssize_t size;
	char *string;
	int current;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = (ssize_t)PyBytes_Size(p);
	string = (char *)((PyBytesObject *)p)->ob_sval;
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	if (size > 10)
		size = 10;
	else
		size++;
	printf("  first %zd bytes: ", size);
	for (i = 0; i < size; i++)
	{
		current = string[i];
		if (current >= 0 && current < 16)
			printf("0%x", current);
		else
			printf("%hhx", current);
		if (i < size - 1)
			printf(" ");
	}
	printf("\n");
	fflush(stdout);
}

/**
 * print_python_list - prints basic info about Python lists
 * @p: Python object (list)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

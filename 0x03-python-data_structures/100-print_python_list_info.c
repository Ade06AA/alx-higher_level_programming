#include <Python.h>
#include <listobject.h>
#include <object.h>
/**
* print_python_list_info - func name
* @p: PyObject pointer
* Return: void
*/
void print_python_list_info(PyObject *p)
{
	long int size_of_list = Py_SIZE(p), i;
	PyListObject *list_object = (PyListObject *) p;

	printf("[*] Size of the Python List = %ld\n", size_of_list);
	printf("[*] Alloccated = %ld\n", list_object->allocated);
	for (i = 0; i < size_of_list; i++)
		printf("Element %ld: %s\n", i,
				Py_TYPE(PyList_GetItem(p, i))->tp_name);
}

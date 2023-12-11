#include <python.h>
#include <objet.h>
#include <listobject.h>

void print_python_list_info(pyObject *p)
{
	long int size = pyList_Size(p);
	int i;
	pyListObject *obj = (pyListObject *)p;

	printf("[*] Size of the python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Elementt %i: %s\n", i, py_TYPE(obj->ob_item[i])->tp_name);
}

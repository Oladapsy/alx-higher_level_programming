#include "list.h"

/**
 * check_cycle - function that check for cycle in a linked list
 *
 * @list: list of parameter
 *
 * Return: 1 if there is no cycle o 0 if there is cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *x2, *x1;

	if (!list || list->next)
	{
		return (0);
	}
	x2 = list->next->next;
	x1 = list;

	while (x1 && x2 && x2->next)
	{
		if (x1 == x2)
		{
			return (1);
		}
		x1 = x1->next;
		x2 = x2->next->next;
	}
	return (0);
}

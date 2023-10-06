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
	listint_t *fast, *slow;

	if (!list || !list->next)
		return (0);
	fast = list->next->next;
	slow = list;

	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);


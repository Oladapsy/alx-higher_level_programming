#include "lists.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * check_cycle - function that checks if a
 * linked list has a cycle in it
 *
 * @list: list of parameters
 * Return: 1 if there is no cycle, 0 if there is a cycle
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
}

#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 */

int check_cycle(listint_t *list)
{
	listint_t *fhead, *nhead;

	if (list == NULL || list->next == NULL)
		return (0);

	fhead = list->next;
	nhead = list->next->next;

	while (fhead && nhead && nhead->next)
	{
		if (fhead == nhead)
			return (1);

		fhead = fhead->next;
		nhead = nhead->next->next;
	}

	return (0);
}

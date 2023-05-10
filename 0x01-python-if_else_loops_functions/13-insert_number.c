#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert new node
 * @head: pointer to head of list
 * @number: no of nodes
 * Return: success
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *added;

	added = malloc(sizeof(listint_t));
	if (added == NULL)
		return (NULL);
	added->n = number;

	if (current == NULL || current->n >= number)
	{
		added->next = current;
		*head = added;
		return (added);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	added->next = current->next;
	current->next = added;

	return (added);
}

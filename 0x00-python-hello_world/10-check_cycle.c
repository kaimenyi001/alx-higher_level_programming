#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle,
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *i;
	listint_t *j;

	i = list;
	j = list;
	if (list == NULL || list->next == NULL)
		return (0);
	do {
		i = i->next;
		j = j->next->next;

		if (i == j)
			return (1);
	}
	while (j != NULL && j->next != NULL);

	return (0);
}

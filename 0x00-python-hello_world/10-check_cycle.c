#include "lists.h"

/**
 * check_cycle - Checks if a SLL has a cycle.
 * @list: ptr to the head of the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = hare = list;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
			return (1);
	}

	return (0);
}

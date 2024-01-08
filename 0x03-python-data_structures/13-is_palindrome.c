#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: double ptr to the head of the linked list
 *
 * Return: 1 if palindrome else 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL, *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (is_palindrome);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		listint_t *next_slow = slow->next;

		slow->next = prev_slow;
		prev_slow = slow;
		slow = next_slow;
	}

	if (fast != NULL)
		slow = slow->next;

	second_half = slow;

	while (prev_slow != NULL && second_half != NULL)
	{
		if (prev_slow->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		prev_slow = prev_slow->next;
		second_half = second_half->next;
	}

	return (is_palindrome);
}

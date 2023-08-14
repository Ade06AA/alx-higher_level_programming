#include <stddef.h> /* NULL */
#include "lists.h"

/**
* is_palindrome - this fuinction checkes if a single
 * linked list is palindrome
* @head: the head of the linked list
* Return: 1 if it is palindrome else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *x, *y, *z;

	x = *head;
	y = *head;
	while (x->next != NULL)
	{
		z = x;
		while (z->next != NULL)
		{
			z = z->next;
			y = y->next;
		}
		if (x->n != y->n)
			return (0);
		if (x == y || x->next == y)
			return (1);
		x = x->next;
	}
	return (1);
}

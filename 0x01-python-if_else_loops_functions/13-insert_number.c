#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - insert a number in an orderd
* linked list while maintaning the order
* @head: the head pointer of the linked list
* @num: the number to be inserted
* Return: the head pointer
*/
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (*head);
	new->n = num;
	new->next = NULL;
	temp = *head;
	if (*head == NULL)
		*head = new;
	else
	{
		while (temp->next != NULL && temp->next->n < num)
			temp = temp->next;
		new->next = temp->next;
		temp->next = new;
	}
	return (*head);
}

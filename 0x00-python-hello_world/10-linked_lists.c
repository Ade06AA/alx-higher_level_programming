#include "lists.h"

/**
* print_listint - func name
* @h: head
* Return: size_t
*/
size_t print_listint(const listint_t *h)
{
	unsigned i;
	const listint_t *temp;

	if (h == NULL)
		return (0);
	temp = h;
	for (i = 0; temp != NULL; i++)
	{
		printf("%i\n", temp->n);
		temp = temp->next;
	}
	return (i);
}

/**
* add_nodeint - func name
* @head: head
* Return: listint_t
*/
listint_t *add_nodeint(listint_t **head, const int l)
{
	int i;
	listint_t *temp;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	new->n = l;
	new->next = *head;
	*head = new;
	return (new);
}

/**
* free_listint - func name
* @head: head
* Return: void
*/
void free_listint(listint_t *head)
{
	listint_t *temp;

	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free(temp);
	}
}

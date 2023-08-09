#include "lists.h"

/**
* check_cycle - checkes if there is a link has a cycle
* @list: list head
* Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *temp, *temp2;

	temp = list;
	temp = list;
	while (temp != NULL)
	{
		while (temp2 != NULL)
		{
			if (temp == temp2)
				return (1);
			if (temp2 == NULL)
				return (0);
			temp2 = temp2->next;
		}
		temp = temp->next;
	}
	return (0);
}

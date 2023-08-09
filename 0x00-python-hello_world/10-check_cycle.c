#include "lists.h"

/**
* check_cycle - checkes if there is a link has a cycle
* @list: list head
* Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *temp, *temp2;
	int c;

	temp = list;
	temp2 = list;
	while (temp != NULL)
	{
		c = 0;
		while (temp2 != NULL)
		{
			if (temp == temp2)
				c += 1;
			if (c == 2)
				return (1);
			temp2 = temp2->next;
		}
		temp = temp->next;
	}
	return (0);
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_node - inserts a number in a sorted singly linked list
 * @head: singly linked list
 * @number: number to be inserted
 * Return: pointer to node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp = *head, *list = *head;
	int i = 0;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (list == NULL) /* empty list */
	{

		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	while (list->next != NULL) /* traverse head */
	{
		if (list->n < number)

		{
			temp = list;
			list = list->next;
			if (list->next == NULL)
			{
				new_node->next = NULL;
				list->next = new_node;
				break;
			}
		}
		else
		{
			if (i == 0)
			{
				new_node->next = list;
				*head = new_node;
			} else
			{
				new_node->next = list;
				temp->next = new_node;
			}
			break;
		}
		i++;
	}
	return (new_node);
}

#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - functon that inserts a number into a sorted
 * singly linked list
 *
 * @head: pointer to a pointer of first node of the list
 * @number: integer to be included in the new node
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = malloc(sizeof(listint_t));
	listint_t *ptr, *tp;

	if (temp == NULL)
	{
		free(temp);
		return (NULL);
	}
	temp->n = number;
	temp->next = NULL;

	ptr = *head;

	while (ptr->n < number)
	{
		tp = ptr;
		ptr = ptr->next;
	}
	temp->next = ptr;
	tp->next = temp;

	return (temp);
}

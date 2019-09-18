#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: double pointer, pointer to pointer to head defined in main
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int /*count = 1, */i = 0, len = 0;
	listint_t *temp = NULL;
	int *array = NULL;

	if (!head)
		return (0);
	if (!(*head))
		return (1);
	temp = *head;
	while (temp != NULL)
		temp = temp->next, /*count++*/i++;
	len = /*count*/(i + 1) - 1;

	array = malloc(sizeof(int) * ((len / 2) + 1));
	if (array == NULL)
		return (-1);
	i = 0, temp = *head;
	while (i < (len / 2))
	{
		array[i] = temp->n;
		temp = temp->next, i++;
	}
	i = 0;
	if (len % 2 != 0)
		temp = temp->next;
	while (temp != NULL)
	{
		if (temp->n == array[((len / 2) - 1) - i])
		{
			temp = temp->next, i++;
			continue;
		}
		else
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}

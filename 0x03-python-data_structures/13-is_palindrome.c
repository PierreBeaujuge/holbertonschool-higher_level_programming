#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 *
 */

int is_palindrome(listint_t **head)
{
	int count = 1, i = 0, len = 0;
	listint_t *temp = NULL;
	int *array = NULL;

	if (!head || !(*head))
		return 1;

	temp = *head;
	while (temp != NULL)
		temp = temp->next, count++;
	len = count - 1;

	array = malloc(sizeof(int) * ((len / 2) + 1));
		if (array == NULL)
			return (-1);
	temp = *head;
	while (i < (len / 2))
	{
		array[i] = temp->n;
/*		printf("temp->n = %i\n", temp->n);
		printf("array[i] = %i\n", array[i]);*/
		temp = temp->next, i++;
	}
/*	i = 0;
	while (i < (len / 2))
	printf("array[i] = %i\n", array[i]), i++;*/
	i = 0;
	while(temp != NULL)
	{
/*		printf("i = %i\n", i);
		printf("(len / 2) - i = %i\n", (len / 2) - i);
		printf("temp->n = %i\n", temp->n);
		printf("array[i] = %i\n", array[((len / 2) - 1) - i]);*/
		if (temp->n == array[((len / 2) - 1) - i])
		{
/*			printf("temp->n = %i\n", temp->n);
			printf("array[i] = %i\n", array[i]);*/
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
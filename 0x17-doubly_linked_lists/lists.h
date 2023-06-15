#ifndef LIST_H
#define LIST_H

typedef struct dlistint
{
	int n;
	struct dlistint *prev;
	struct dlistint *next;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h);

#endif

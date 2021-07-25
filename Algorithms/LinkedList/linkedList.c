#include<stdio.h>
#include<stdlib.h>

typedef struct node {
	int data;
	struct node *next;
} node_t;

void add_node(node_t **head, int data) {
	node_t *node = malloc(sizeof(node_t));
	node->data = data;
	node->next = NULL;
	node_t *mover = *head;

	if (*head == NULL) {
		*head = node;
	} else {
		while (mover->next) {
			mover = mover->next;
		}
		mover->next = node;
	}
}

void print_ll(node_t *head) {
	while (head) {
		printf("%d->", head->data);
		head = head->next;
	}
	printf("\n");
}

void reverse_ll(node_t **head) {
	node_t *previous = NULL;
	node_t *current = *head;
	node_t *next = NULL;

	while (current) {
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
		*head = previous;
	}
}

int main() {
	node_t *head = NULL;
	add_node(&head, 1);
	add_node(&head, 2);
	add_node(&head, 3);
	add_node(&head, 4);
	add_node(&head, 5);

	print_ll(head);
	reverse_ll(&head);
	print_ll(head);
	return 0;
}

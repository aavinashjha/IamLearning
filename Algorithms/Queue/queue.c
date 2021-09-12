#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct node {
	int key;
	struct node *next;
} node;

typedef struct queue {
	node *head;
	node *tail;
} queue;

queue *makeQueue() {
	queue *q = (queue *)malloc(sizeof(queue));
	q->head = NULL;
	q->tail = NULL;
}

node *makeNode(int key) {
	node *n = (node *)malloc(sizeof(node));
	n->key = key;
	n->next = NULL;
	return n;
}

void enqueue(queue *q, int key) {
	node *n = makeNode(key);
	if (!q->head) {
		q->head = n;
		q->tail = n;
	} else {
		q->tail->next = n;
		q->tail = n;
	}
}

int dequeue(queue *q) {
	if (!q->head) {
		printf("Empty queue\n");
		return -1;
	}
	node* n = q->head;
	int val = n->key;
	if (n->next == NULL) {
		// Removed last element
		q->head = NULL;
		q->tail = NULL;
	} else {
		q->head = n->next;
	}
	//free(n);
	return val;
}

int empty(queue *q) {
	return q->head == NULL;
}

int main() {
	queue *q = makeQueue();
	assert(empty(q) == 1);
	enqueue(q, 1);
	enqueue(q, 2);
	enqueue(q, 3);
	assert(empty(q) == 0);
	assert(dequeue(q) == 1);
	assert(dequeue(q) == 2);
	assert(empty(q) == 0);
	assert(dequeue(q) == 3);
	assert(empty(q) == 1);

	return 0;
}

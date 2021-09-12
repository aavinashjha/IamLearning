/*
 * increment_address_one = (address+1) % length
 * decrement_address_one = (address+length -1) %length
 *
 * 0 1 2 3 4 5
 *
 * 5+1 % 6 = 0
 * 0+6-1 % 6 = 5 
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#define MAX_LENGTH 5

typedef struct queue {
	int read; // Tells us where the next dequeue operation should happen
	int write; // Tells us where the next enqueue operation should happen
	int store[MAX_LENGTH];
} queue;

queue *createQ() {
	queue *q = (queue *)malloc(sizeof(queue));
	q->read = 0;
	q->write = 0;
}

void push(queue *q, int e) {
	if (q->write+1 == q->read) {
		// When we increment write by 1 after this operation
		// We would not be clear if the stack is full or empty
		// Hence this case should be identified as full
		printf("ERROR: Stack is full, could not insert %d\n", e);
		return;
	}
	q->store[q->write] = e;
	q->write = (q->write+1) % MAX_LENGTH;
	printf("Pushed %d. Read [%d], Write [%d]\n", e, q->read, q->write);
}

int pop(queue *q) {
	int val = q->store[q->read];
	q->read = (q->read+MAX_LENGTH+1) % MAX_LENGTH;
	printf("Popped %d. Read [%d], Write [%d]\n", val, q->read, q->write);
	return val; 
}

int empty(queue *q) {
	return q->read == q->write;
}

int main() {
	// 10 11 12 13 14
	// 0  1  2  3  4
	queue *q = createQ();
	assert(empty(q) == 1);
	push(q, 10);
	push(q, 11);
	push(q, 12);
	assert(pop(q) == 10);
	assert(pop(q) == 11);
	push(q, 13);
	push(q, 14);
	push(q, 15);
	push(q, 16);
	assert(pop(q) == 12);
	assert(pop(q) == 13);
	assert(pop(q) == 14);
	assert(pop(q) == 15);
	push(q, 16);
	assert(pop(q) == 16);
}

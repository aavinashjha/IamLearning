#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef struct stack {
	int *store;
	int index;
} stack;

stack *createStack(int count) {
	stack *s = (stack *)malloc(sizeof(stack));
	s->store = (int *)malloc(sizeof(int)*count);
	s->index = -1;
}
void push(stack *s, int e) {
	s->index++;
	*(s->store+s->index) = e;
}

int pop(stack *s) {
	int e = *(s->store+s->index);
	*(s->store+s->index) = 0;
	s->index--;
	return e;
}

int top(stack *s) {
	return *(s->store+s->index);
}

int empty(stack *s) {
	return s->index == -1;
}

int main() {
	stack *s = createStack(10);
	assert(empty(s) == 1);
	push(s, 10);
	assert(top(s) == 10);
	push(s, 9);
	assert(top(s) == 9);
	pop(s);
	assert(top(s) == 10);
	assert(empty(s) == 0);
	pop(s);
	assert(empty(s) == 1);
}

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/*
 * size()
 * empty()
 * push_front()
 * pop_front()
 * top_front()
 */
typedef struct node_t {
        int key;
        struct node_t *next;
} node_t;

/* Allocates a node with key */
node_t* alloc_node(int key) {
        node_t* node = (node_t *)malloc(sizeof(node_t));
	node->key = key;
	node->next = NULL;
}

void print_list(node_t *head) {
	while (head) {
		printf("%d->", head->key);
		head = head->next;
	}
	printf("\n");
}

/* Is link list empty */
int empty(node_t *head) { 
	if (head == NULL) {
		return 1;
	}
	return 0;
}

/* Adds an item to the fornt of the list */
void push_front(int key, node_t **head) {
	node_t* node = alloc_node(key);
        if (*head != NULL) {
                node->next = *head;
        }
        *head = node;
}

/* Get front item */
node_t* top_front(node_t *head) {
	if (!empty(head)) {
		return head;
	}
	return NULL;
}

/* Removes front item and returns its value */
node_t* pop_front(node_t **head) {
	node_t *node = NULL;
	if (!empty(*head)) {
		node = *head;
		*head = node->next;
	}
	return node;
}

/* Returns value of nth item starting at index 0 */
node_t* value_at(int index, node_t *head) {
	int i = 0;
	if (!empty(head)) {
		while (i < index) {
			head = head->next;
			i++;
		}
		return head;
	}
	return NULL;
}

/* Adds an item at the end */
void push_back(int key, node_t **head) {
	node_t *mover = *head;
	node_t *node = alloc_node(key);
	if (empty(*head)) {
		*head = node;
		return;
	}
	while (mover->next) {
		mover = mover->next;
	}
	mover->next = node;
}

/* Removes end item and returns its value */
node_t* pop_back(node_t **head) {
	node_t *node = *head, *prev = NULL, *popped = NULL;

	if (!empty(node)) {
		if (!node->next) {
			*head = NULL;
			return node;
		}
		while (node->next->next) {
			node = node->next;
		}
		popped = node->next;
		node->next = NULL;
		return popped;
	}
	return NULL;
}

/* Add a node after the given node */
void add_after(node_t *node, int key) {
	node_t *new_node = NULL, *old_next = NULL;
	if (node) {
		new_node = alloc_node(key);
		old_next = node->next;
		node->next = new_node;
		new_node->next = old_next;
	}
}

/* Add a node before a particular given node */
void add_before(node_t *node, node_t **head, int key) {
	node_t *mover = *head, *old_next = NULL;
	node_t *new_node = alloc_node(key);
	if (empty(*head)) {
		*head = new_node;
		return;
	}
	if (mover == node) {
		// First node
		new_node->next = *head;
		*head = new_node;
		return;
	}

	while (mover->next != node) {
		mover = mover->next;
	}
	old_next = mover->next;
	mover->next = new_node;
	new_node->next = old_next;
}

/* Add at a particular index */
void insert(int index, int key, node_t **head) {
	node_t *node = value_at(index, *head);
	add_before(node, head, key);
}

/* Removes node at given index */
void erase(int index, node_t **head) {
	node_t *mover = *head, *prev = NULL;
	int i = 0;

	if (empty(*head)) {
		return;
	}
	if (index == 0) {
		*head = mover->next;
		free(mover);
		return;
	}

	while (mover) {
		prev = mover;
		mover = mover->next;
		if (index == i) {
			break;
		}
		i++;
	}
	prev->next = mover->next;
	free(mover);
}
/* Returns value of node at nth position from the end of the list */
node_t *value_n_from_end(int n, node_t *head) {
	node_t *lp = head, *rp = head;
	// Maintain a distance between two pointyers of n steps
	while (n) {
		rp = rp->next;
		n--;
	}
	while (rp) {
		lp = lp->next;
		rp = rp->next;
	}
	return lp;
}

void reverse(node_t **head) {
	// Every next pointer has to connect its previous element
	node_t *curr = *head, *prev = NULL, *next = NULL;
	// Prev---> Curr---->Next
	while (curr) {
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;
}

void remove_value(int value, node_t **head) {
	node_t *node = *head, *prev = NULL;
	if (empty(*head)) {
		return;
	}
	while (node->key != value) {
		prev = node;
		node = node->next;
	}
	if (prev == NULL) {
		*head = node->next;
		free(node);
		return;
	}
	prev->next = node->next;
	free(node);
}

node_t *find(int key, node_t *head) {
	if (empty(head)) {
		return NULL;
	}

	while (head && head->key != key) {
		head = head->next;
	}
	return head;
}

int main() {
	node_t *head = NULL;
	push_front(1, &head);
	assert(top_front(head)->key == 1);
	assert(pop_front(&head)->key == 1);
	assert(top_front(head) == NULL);

	push_front(0, &head);
	push_front(1, &head);
	push_front(2, &head);
	push_front(3, &head);
	push_front(4, &head);
	assert(value_at(0, head)->key == 4);
	assert(value_at(1, head)->key == 3);
	assert(value_at(2, head)->key == 2);
	assert(pop_back(&head)->key == 0);
	assert(pop_back(&head)->key == 1);
	push_back(100, &head);
	assert(pop_back(&head)->key = 100);

	add_after(value_at(0, head), 10);
	assert(value_at(1, head)->key == 10);

	add_before(value_at(1, head), &head, 99);
	assert(value_at(1, head)->key == 99);

	add_before(value_at(0, head), &head, 999);
	assert(value_at(0, head)->key == 999);

	insert(0, 1000, &head);
	assert(value_at(0, head)->key == 1000);

	erase(0, &head);
	assert(value_at(0, head)->key == 999);

	push_front(50, &head);
	assert(value_at(1, head)->key == 999);

	print_list(head);

	assert(value_n_from_end(3, head)->key == 10);
	assert(value_n_from_end(6, head)->key == 999);
	assert(value_n_from_end(2, head)->key == 3);

	reverse(&head);
	print_list(head);

	remove_value(999, &head);
	print_list(head);

	assert(find(999, head) == NULL);
	assert(find(10, head)->key == 10);
        return 0;
}       


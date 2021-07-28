#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define MAX_VALUE 2^16
#define MIN_VALUE -(2^16-1)

typedef struct node {
	struct node *left;
	struct node *right;
	int data;
} NODE;

void inorder(NODE *node) {
	if (node == NULL) {
		return;
	}
	inorder(node->left);
	printf("%d\n", node->data);
	inorder(node->right);
}

void insert(NODE **root, int data) {
	NODE *node = NULL;
	if (*root == NULL) {
		node = (NODE *)malloc(sizeof(NODE));
		memset((void *)node, 0, sizeof(NODE));
		node->data = data;
		*root = node;
		return;
	}

	node = *root;
	if (data < node->data) {
		insert(&node->left, data);
	} else {
		insert(&node->right, data);
	}
}
int get_node_count(NODE *root) {
	if (root == NULL) {
		return 0;
	}
	return 1 + get_node_count(root->left) + get_node_count(root->right);
}

int search(NODE *root, int data) {
	if (root == NULL) {
		return 0;
	} else if (data == root->data) {
		return 1;
	} else if (data < root->data) {
		return search(root->left, data);
	}
	return search(root->right, data);
}

int max(NODE *root) {
	if (root == NULL) {
		return MIN_VALUE;
	}
	
	while (root->right) {
		root = root->right;
	}
	return root->data;
}

int min(NODE *root) {
	if (root == NULL) {
		return MAX_VALUE;
	}
	
	while (root->left) {
		root = root->left;
	}
	return root->data;
}
int height(NODE* root) {
	// Height: Number of edges in longest path from node to a leaf node
	// Depth: Distance from root to node
	int hl, hr;
	if (root == NULL) {
		return -1;
	}
	hl = height(root->left);
	hr = height(root->right);
	return 1+(hl ? hl > hr: hr);
}

int main() {
	/*
	 *     4
	 *    /
	 *   2 
	 *  / \
	 * 1   3
	 */
	NODE *root = NULL; // This root variable has name and is on stack
	insert(&root, 4);
	insert(&root, 2);
	insert(&root, 1);
	insert(&root, 3);
	printf("Node Count: %d\n", get_node_count(root));
	inorder(root);
	printf("Search: 6: %d\n", search(root, 6));
	printf("Search: 3: %d\n", search(root, 3));
	printf("Minimum: %d\n", min(root));
	printf("Maximum: %d\n", max(root));
	printf("Height: %d\n", height(root));
}


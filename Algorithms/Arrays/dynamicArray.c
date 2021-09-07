#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
// Vector(c++), ArrayList(java), List(python)

int size = 0;
int capacity = 0;
int *arr;

int *allocate() {
	 return (int *)malloc(sizeof(int) * capacity);
}

int get(int index) {
	if (index < 0 || index >= size) {
		printf("Index out of range: %d\n", index);
		return -1;
	}
	return *(arr+index);
}

void set(int index, int value) {
	*(arr+index) = value;
}

int size_arr() {
	return size;
}

void insert(int index, int value) {
	int *new_arr = NULL;
	int i = 0;
	if (size == capacity) {
		capacity += capacity;
		printf("Expanding array from %d to %d\n", size, capacity);
		new_arr = allocate();
		for (i=0; i<size; i++) {
			*(new_arr+i) = *(arr+i);
		}
		free(arr);
		arr = new_arr;
	}

	for (i=size; i>index; i--) {
		*(arr+i) = *(arr+i-1);
	}
	*(arr+index) = value;
	size += 1;
	printf("Written %d at %d index [Size: %d]\n", value, index, size_arr());
}

void delete(int index) {
	// We want to reduce array size to half if size reduces to half of capacity
	int i;
	size -= 1;
	int *new_arr = NULL;
	for (i=index; i < size; i++) {
		*(arr+i) = *(arr+i+1);
	}
	printf("Deleted index[%d]\n", index);
	if (size == capacity/4) {
		printf("Reducing capacity to half from [%d] to [%d]\n", capacity, size);
		new_arr = malloc(sizeof(int) * capacity/2);
		for (i=0; i < size; i++) {
			*(new_arr+i) = *(arr+i);
		}
		free(arr);
		arr = new_arr;
		capacity /= 2;
	}
}

int find(int value) {
	int i;
	for (i=0; i<size; i++) {
		if (*(arr+i) == value) {
			return i;
		}
	}
	return -1;
}


void remove_arr(int index) {
	int i = 0;
	// copy all elemnets after index to its previous location
	for (i=index+1; i<size; i++) {
		*(arr+i-1) = *(arr+i);
	}
	size -= 1;
	printf("Deleted element at index %d, size: %d\n", index, size);
}

void remove_element(int value) {
	int index;
	while (1) {
		index = find(value);
		if (index == -1) {
			break;
		}
		remove_arr(index);
	}
}
void prepend(int value) {
	insert(0, value);
}

void pushBack(int value) {
	insert(size_arr(), value);
}

int pop() {
	int val = *(arr+size-1);
	*(arr+size-1) = 0;
	size -= 1;
	return val;
}

void setup() {
	capacity = 1;
	arr = allocate();
}

int is_empty() {
	return size_arr() == 0;
}

int main() {
	printf("Dynamic array\n");
	setup();
	assert(is_empty() == 1);
	pushBack(1);	
	pushBack(2);	
	pushBack(3);	
	pushBack(4);	
	pushBack(5);	
	pushBack(6);	
	pushBack(7);	
	pushBack(8);	
	pushBack(9);

	assert(get(3) == 4); 
	assert(get(8) == 9);
	set(3, 21);
	assert(get(3) == 21);
	assert(get(8) == 9);
	//assert(get(8) == 10);

	// [1, 2, 21, 4, 5, 6, 7, 8, 9]
	// [0, 1, 2,  3, 4, 5, 6, 7, 8]
	assert(size_arr() == 9);
	pushBack(10);
	assert(size_arr() == 10);
	assert(get(9) == 10);
	remove_arr(7);
	// [1, 2, 21, 4, 5, 6, 8, 9]
	assert(size_arr() == 9);
	assert(get(7) == 9);
	assert(get(8) == 10);
	// Out of index
	assert(get(-1) == -1);
	assert(get(100) == -1);

	assert(pop() == 10);
	assert(size_arr() == 8);

	prepend(1100);
	assert(size_arr() == 9);
	assert(get(0) == 1100);
	assert(get(8) == 9); // shifted by 1 index

	delete(1);
	assert(size_arr() == 8);
	assert(get(7) == 9);

	delete(1);
	assert(size_arr() == 7);
	assert(get(6) == 9);

	delete(1);
	assert(size_arr() == 6);
	assert(get(5) == 9);

	delete(1);
	assert(size_arr() == 5);
	assert(get(4) == 9);

	delete(1);
	assert(size_arr() == 4);
	assert(get(3) == 9);

	pushBack(100);
	assert(size_arr() == 5);
	assert(get(4) == 100);

	assert(find(100) == 4);
	assert(find(101) == -1);

	pushBack(100);
	insert(4, 100);
	remove_element(100);
	assert(find(100) == -1);
	assert(size_arr() == 4);

	assert(is_empty() == 0);
	return 0;
}


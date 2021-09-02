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

void remove_arr(int index) {
	int i = 0;
	// copy all elemnets after index to its previous location
	for (i=index+1; i<size; i++) {
		*(arr+i-1) = *(arr+i);
	}
	size -= 1;
	printf("Deleted element at index %d, size: %d\n", index, size);
}

void pushBack(int value) {
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
	*(arr+size) = value;
	size += 1;
	printf("Written %d at %d index [Size: %d]\n", value, size-1, size_arr());
}

void setup() {
	capacity = 1;
	arr = allocate();
}

int main() {
	printf("Dynamic array\n");
	setup();
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

	return 0;
}


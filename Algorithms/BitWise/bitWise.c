#include <stdio.h>
#define CHAR_BIT 8

int sign(int v) {
	// CHAR_BIT: Number of bits in byte
	return v >> (sizeof(int)*CHAR_BIT-1);
}

int oppositeSign(int x, int y) {
	return (x^y) < 0;
}

int absolute(int v) {
	// Absolute value without branching
	// Sign is not important
	int mask = v >> (sizeof(int) * CHAR_BIT-1); // 1111..11 for negative numbers and 0000..00 for positive numbers
	//return (v + mask) ^ mask;
	return (v ^ mask) - mask;
}
int minimum(int x, int y) {
	// if x < y is false then y ^ 0 is y
	// if x < y is true -1 (all 1's) y ^ x ^ y is x
	return y ^ ((x ^ y) & -(x < y));
}
int maximum(int x, int y) {
	return y ^ ((x^y) & -(x > y));
}
int powerOfTwo(int x) {
	// Power of Two will have only 1 bit set
	// x-1 will have all bits set except that one
	return (x & (x-1)) == 0;
}
void swap(int x, int y) {
	printf("X: %d. Y: %d\n", x, y);
	x ^= y;
	y ^= x;
	x ^= y;
	printf("X: %d. Y: %d\n", x, y);
}

int main() {
	printf("Sign 10: %d\n", sign(10));
	printf("Sign -10: %d\n", sign(-10));
	printf("Opposite Sign (5, 15): %d\n", oppositeSign(5, 15));
	printf("Opposite Sign (-5, 15): %d\n", oppositeSign(-5, 15));
	printf("Absolute 10: %d\n", absolute(10));
	printf("Absolute -10: %d\n", absolute(-10));
	printf("Minimum: (5, 15): %d\n", minimum(5, 15));
	printf("Minimum: (-5, -15): %d\n", minimum(-5, -15));
	printf("Maximum: (5, 15): %d\n", maximum(5, 15));
	printf("Maximum: (-5, -15): %d\n", maximum(-5, -15));
	printf("Power of two: 64: %d\n", powerOfTwo(64));
	printf("Power of two: 63: %d\n", powerOfTwo(63));
	swap(5, 10);
	return 0;
}

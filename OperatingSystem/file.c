#include <stdio.h>

int main() {
	FILE *fp;
	int ret;
	printf("file operations\n");
	fp = fopen("file.md", "r+");
	ret = fclose(fp);
	printf("close: %d\n", ret);
}

#include <stdio.h>
#include <string.h>

int main() {
	FILE *fp;
	char* data;
	char cache[256];

	printf("Char....\n");
	fp = fopen("/tmp/text", "w+");

	while (1) {
		data = fgets(cache, 10, stdin);
		printf("%s", data);
		if (!data || strlen(data) == 0) break;
		if (fputs(data, fp) < 0) break;
	}
	fclose(fp);
}

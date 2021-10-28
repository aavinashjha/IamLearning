#include <stdio.h>
#include <signal.h>
#include <stdlib.h>

void signal_callback_handler(int signum) {
	printf("Got signal: %d\n", signum);
	exit(1);
}

int main() {
	signal(SIGINT, signal_callback_handler);
	while (1) {
	}
}

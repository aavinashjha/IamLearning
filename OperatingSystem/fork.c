#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
	pid_t pid;
	int status;
	printf("before fork: %d\n", getpid());
	pid = fork();
	if (pid == 0) {
		printf("this is a child process\n");
	} else if (pid > 0) {
		printf("this is a parent process. PID of child is %d\n", pid);
		pid = wait(&status);
		printf("Bye: %d, status: %d\n", pid, status);
	}
	printf("After fork: %d\n", getpid());
	return -1;
}

#define MAXREQ 256

void server(int consockFd) {
	int n;
	char reqbuf[MAXREQ];

	while(1) {
		memset(reqbuf, 0, MAXREQ);
		n = read(consockfd, reqbuf, MAXREQ);
		if (n <= 0) return;
		n = write(STDOUT_FILENO, reqbuf, strlen(reqbuf));
		n = write(consockfd, reqbuf, strlen(reqbuf));
	}
}

lstnsockfd = socket(AF_INET, SOCK_STREAM, 0)
bind(lstnsokfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

while (1) {
	listen(lstnsockfd, MAXQUEUE);
	consockfd = accept(lstnsockfd, (struct sockaddr *)&cli_addr, &clilen);

	cpid = fork();
	if (cpid == 0) {
		close(lstnsockfd);
		server(consockfd);
		close(consockfd);
		exit(EXIT_SUCCESS);
	} else if (cpid > 0) {
		close(consockfd);
		tcpid = wait(&status);
	}
}
close(lstnsockfd);

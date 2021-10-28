#define MAXIN 256
#define MAXOUT 256
char *hostname;
int sockfd, portno;
struct sockaddr_in serv_addr;
struct hostent *server;
server = buildServerAddr(&serv_addr, hostname, portno);
sockfd = socket(AF_INET, SOCK_STREAM, 0);

connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

client(sockfd);
close(sockfd);
char *getreq(char *inbuf, int len) {
	printf("REQ: ");
	memset(inbuf, 0, len);
	return fgets(inbuf, len, stdin);
}

void client(int sockfd) {
	int n;
	char sndbuf[MAXIN];
	char rcvbuf[MAXOUT];

	getreq(sndbuf, MAXIN);

	while (strlen(sndbuf) > 0) {
		write(sockfd, sndbuf, strlen(sndbuf));
		memset(rcvbuf, 0, MAXOUT);
		n = read(sockfd, rcvbuf, MAXOUT-1); //Keep room for NULL character
		write(STDOUT_FILENO, rcvbuf, n);
		getreq(sndbuf, MAXIN);
	}
}


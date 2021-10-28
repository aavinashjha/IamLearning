Sockets
An abstraction of a network I/O queue
- Mechanism for inter process communication
- Embodies one side of a communication channel
  > Same interface regardless of location of other end
  > Could be local machine (called UNIX Socket) or remote machine (called Network Socket)

Socket Creation and Connection
- File systems provide a collection of permanent objects in structured name space
  > Processes open, read/write, close them
  > Files exist independent of the processes
- Sockets provide a means for processes to communicate (transfer data) to other processes
- Creation and connection is more complex
- Form 2 way pipes between processes (possibly worlds away)

Nmaespaces for communication over IP
- Hostname
- IP Address [32/128 bits]
- Port Number
  > 0-1023 are well known or system ports
    [Superuser privileges to bind to one]
  > 1024-49151 are registered ports (registry)
    [Assigned by IANA for specific services]
  > 49152-65535 (2^15+2^14 to 2^16-1) are dynamic
    [Automatically allocated as ephemeral ports]

Socket Setup over TCP/IP

          Request Connection
socket-------------------------> server socket
  |                                 |       New socket
  <---------------------------->  socket  
         Bidirectional Connection
Client                            Server

Server Socket: Listens for new connections
 > Produces new sockets for each unique connection

Connection involves 5 values: [5-Tuple]
- Client Addr, Client Port, Server Addr, Server Port, Protocol
- Often Client Port randomly assigned
  > Done by OS during client socket setup
- Server port well known

Server
- Create server socket
- Bind it to an address(address: port)
- Listen for connection

Client:
- Create client socket
- Connect to server (host: port)

Server:
- Accept connection
- read request

Client:
- write request

Server:
- write response

Client:
- read response

close client socket
close connection socket

On forking:
- child closes listen socket
- parent closes conn socket

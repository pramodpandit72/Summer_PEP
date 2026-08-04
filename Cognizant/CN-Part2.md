# Computer Networks (Part 2 - Placement Notes)

# 1. ARP (Address Resolution Protocol)

## What is ARP?

ARP is used to find the **MAC Address** of a device when we already know its **IP Address**.

Simple Flow:

IP Address → ARP → MAC Address

Example:

Computer A wants to send data to Computer B.

Computer A knows:
IP = 192.168.1.20

But it does not know the MAC Address.

ARP asks:
"Who has IP 192.168.1.20?"

Computer B replies with its MAC Address.

Now communication starts.

---

## Interview Question

Q. What is the use of ARP?

Answer:

ARP converts an IP Address into a MAC Address inside a local network.

---

# 2. RARP (Reverse ARP)

## What is RARP?

RARP is the opposite of ARP.

It converts:

MAC Address → IP Address

It is rarely used today.

DHCP has replaced RARP.

---

# 3. NAT (Network Address Translation)

## What is NAT?

NAT allows multiple devices in a private network to use one public IP address.

Example:

Home Wi-Fi

Mobile
Laptop
TV

All use one Internet connection.

Router performs NAT.

---

## Why NAT is used?

- Saves Public IP addresses
- Adds security
- Allows many devices to access Internet

---

## Interview Question

Q. Why is NAT used?

Answer:

NAT allows many private devices to share one public IP address.

---

# 4. Firewall

## What is Firewall?

A Firewall is a security system.

It monitors incoming and outgoing network traffic.

It allows safe traffic.

It blocks harmful traffic.

Example:

Like a security guard checking everyone entering a building.

---

## Types

Software Firewall

Example:
Windows Firewall

Hardware Firewall

Installed in companies.

---

## Interview Question

Q. What is the main purpose of Firewall?

Answer:

To protect a network from unauthorized access.

---

# 5. Proxy Server

## What is Proxy Server?

A Proxy Server acts as a middleman between client and server.

Flow:

Client → Proxy → Internet

Advantages

- Security
- Privacy
- Faster access (Caching)

---

# 6. VPN (Virtual Private Network)

## What is VPN?

VPN creates a secure encrypted connection over the Internet.

Advantages

- Secure communication
- Hide IP Address
- Protect data

Example

Employees working from home connect to company servers using VPN.

---

## Interview Question

Q. Why is VPN used?

Answer:

VPN provides a secure connection over the Internet.

---

# 7. Bandwidth

## What is Bandwidth?

Bandwidth is the maximum amount of data that can be transferred per second.

Unit

bps
Kbps
Mbps
Gbps

More bandwidth = More data transfer

---

# 8. Latency

## What is Latency?

Latency is the time taken for data to travel from source to destination.

Unit

Milliseconds (ms)

Lower latency is better.

Example

Online Gaming

Video Calling

---

# Difference

Bandwidth = Amount of data

Latency = Time taken

---

# 9. Packet

A Packet is a small unit of data sent over a network.

Large files are divided into packets.

Packets are reassembled at the destination.

---

# 10. Packet Switching

Packet Switching means dividing data into packets before transmission.

Advantages

- Faster
- Efficient
- Reliable

Internet uses Packet Switching.

---

# 11. Circuit Switching

Circuit Switching creates a dedicated communication path before sending data.

Example

Traditional Telephone Network

---

# Packet Switching vs Circuit Switching

| Packet Switching | Circuit Switching |
|------------------|-------------------|
| No dedicated path | Dedicated path |
| Internet | Telephone |
| Efficient | Less efficient |

---

# 12. Cookies

## What are Cookies?

Cookies are small files stored in the browser.

Used to remember:

- Login
- Language
- Shopping Cart

Example

You login once.

Next time website remembers you.

---

# 13. Session

## What is Session?

A Session stores user information on the server.

Example

After login

Server remembers user until logout.

---

# Cookies vs Session

| Cookies | Session |
|-----------|----------|
| Browser | Server |
| Less secure | More secure |
| Stores small data | Stores user information |

---

# Interview Question

Q. Difference between Cookies and Session?

Answer

Cookies are stored in the browser.

Sessions are stored on the server.

Sessions are more secure.

---

# 14. Socket

## What is Socket?

A Socket is one endpoint of communication between two computers.

A socket is created using:

IP Address + Port Number

Example

192.168.1.10:80

---

# 15. Three-Way Handshake (TCP)

TCP establishes connection using Three-Way Handshake.

Step 1

Client → SYN

"I want to connect."

Step 2

Server → SYN + ACK

"I received your request."

Step 3

Client → ACK

"Connection established."

Now data transfer begins.

Remember

SYN

SYN + ACK

ACK

---

## Interview Question

Q. Why is Three-Way Handshake used?

Answer

It establishes a reliable TCP connection.

---

# 16. Four-Way Handshake

Used to close a TCP connection.

Sequence

FIN

ACK

FIN

ACK

---

# 17. Flow Control

Flow Control prevents a fast sender from overwhelming a slow receiver.

TCP provides Flow Control.

---

# 18. Congestion Control

Congestion occurs when too much traffic enters the network.

TCP uses Congestion Control to reduce traffic.

---

# Difference

Flow Control

Controls sender and receiver speed.

Congestion Control

Controls network traffic.

---

# 19. Unicast

One Sender → One Receiver

Example

Sending Email

---

# 20. Broadcast

One Sender → All Devices

Example

ARP Request

---

# 21. Multicast

One Sender → Selected Group

Example

Online Meeting

Video Streaming

---

# Difference

| Type | Communication |
|--------|--------------|
| Unicast | One to One |
| Broadcast | One to All |
| Multicast | One to Many |

---

# 22. DNS Resolution

How DNS Works

Step 1

User enters

www.google.com

Step 2

Browser asks DNS Server

Step 3

DNS returns IP Address

Step 4

Browser connects to server

Step 5

Website opens

---

# 23. Network Topologies

## Bus

Single cable

Cheap

Failure of cable affects network.

---

## Star

All devices connect to a central switch.

Most common topology.

---

## Ring

Devices connected in a circle.

---

## Mesh

Every device connects to every other device.

Highly reliable.

Expensive.

---

# Interview Question

Q. Which topology is most common?

Answer

Star Topology

---

# 24. Client-Server Model

Client requests service.

Server provides service.

Examples

Browser → Web Server

Mobile App → Backend Server

---

# 25. Peer-to-Peer (P2P)

All computers are equal.

Each computer can act as both client and server.

Example

Torrent

---

# Client-Server vs Peer-to-Peer

| Client-Server | Peer-to-Peer |
|----------------|-------------|
| Central server | No central server |
| More secure | Less secure |
| Easy management | Difficult management |

---

# Frequently Asked Interview Questions

## Q1. What is ARP?

Answer

ARP converts an IP Address into a MAC Address.

---

## Q2. What is NAT?

Answer

NAT allows multiple private devices to share one public IP.

---

## Q3. What is Firewall?

Answer

Firewall protects the network by allowing safe traffic and blocking harmful traffic.

---

## Q4. What is VPN?

Answer

VPN creates a secure encrypted connection over the Internet.

---

## Q5. Difference between Cookies and Session?

Answer

Cookies are stored in the browser.

Sessions are stored on the server.

Sessions are more secure.

---

## Q6. What is Socket?

Answer

A Socket is a combination of an IP Address and Port Number used for communication.

---

## Q7. What is Three-Way Handshake?

Answer

TCP establishes a connection using:

SYN

SYN + ACK

ACK

---

## Q8. Difference between Flow Control and Congestion Control?

Answer

Flow Control manages sender and receiver speed.

Congestion Control manages overall network traffic.

---

## Q9. Difference between Packet Switching and Circuit Switching?

Answer

Packet Switching sends data in packets.

Circuit Switching creates a dedicated path before sending data.

---

## Q10. Difference between Unicast, Broadcast and Multicast?

Answer

Unicast = One to One

Broadcast = One to All

Multicast = One to Many

---

# Cognizant Placement Quick Revision

✔ ARP

✔ NAT

✔ Firewall

✔ VPN

✔ Proxy Server

✔ Packet

✔ Packet Switching

✔ Circuit Switching

✔ Socket

✔ Cookies

✔ Session

✔ TCP Three-Way Handshake

✔ Four-Way Handshake

✔ Flow Control

✔ Congestion Control

✔ DNS Resolution

✔ Topologies

✔ Client-Server

✔ Peer-to-Peer

---

# Top 20 Viva Questions (Very Important)

1. What is a Computer Network?
2. Difference between LAN and WAN.
3. Difference between Hub, Switch and Router.
4. Explain the OSI Model.
5. Difference between TCP and UDP.
6. Difference between HTTP and HTTPS.
7. What is DNS?
8. What is DHCP?
9. What is ARP?
10. What is NAT?
11. What is Firewall?
12. What is VPN?
13. Difference between IP Address and MAC Address.
14. What is a Port Number?
15. What is Socket?
16. Explain TCP Three-Way Handshake.
17. Difference between Cookies and Session.
18. Difference between Flow Control and Congestion Control.
19. Difference between Packet Switching and Circuit Switching.
20. Explain Client-Server Architecture.
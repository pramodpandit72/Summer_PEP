# Computer Networks (Placement Notes)

# 1. What is Computer Network?

A Computer Network is a group of computers connected together to share data, resources, and services.

Example:
- Internet
- College Wi-Fi
- Office Network

Advantages:
- File sharing
- Resource sharing (Printer, Internet)
- Fast communication
- Data backup

---

# 2. Types of Network

## PAN (Personal Area Network)

- Smallest network
- Range: Around 10 meters
- Example:
  - Bluetooth
  - Mobile hotspot

---

## LAN (Local Area Network)

- Covers small area
- High speed
- Private network

Example:
- College lab
- Office
- Home Wi-Fi

Advantages:
- Fast
- Low cost
- Secure

---

## MAN (Metropolitan Area Network)

- Covers a city

Example:
- City cable network

---

## WAN (Wide Area Network)

- Covers large geographical area
- Connects multiple LANs

Example:
- Internet

---

# Important Interview Question

Q. Difference between LAN and WAN?

| LAN | WAN |
|------|------|
| Small area | Large area |
| High speed | Lower speed |
| Less delay | More delay |
| Private | Public/Private |
| Example: College | Internet |

---

# 3. Network Devices

## Hub

- Connects multiple devices
- Sends data to every device
- No intelligence

Disadvantage:
- More collisions
- Less secure

---

## Switch

- Connects devices in LAN
- Sends data only to the correct device
- Uses MAC Address

Advantages:
- Faster
- Secure
- Less collision

Interview Line:
Switch works at Data Link Layer (Layer 2).

---

## Router

- Connects different networks
- Uses IP Address
- Connects LAN to Internet

Interview Line:
Router works at Network Layer (Layer 3).

---

## Modem

Meaning:
Modulator + Demodulator

Work:
Converts Digital Signal ↔ Analog Signal

Used for Internet connection.

---

## Access Point (AP)

Provides Wi-Fi connection to wireless devices.

---

# Important Question

Q. Difference between Hub, Switch and Router?

| Hub | Switch | Router |
|------|----------|---------|
| Broadcasts data | Sends to correct device | Connects networks |
| No MAC table | Uses MAC Address | Uses IP Address |
| Layer 1 | Layer 2 | Layer 3 |

---

# 4. OSI Model

OSI = Open Systems Interconnection

It has 7 Layers.

Remember:

All People Seem To Need Data Processing

Application
Presentation
Session
Transport
Network
Data Link
Physical

---

## Layer 7 - Application

Provides services to user.

Examples:
- HTTP
- FTP
- SMTP
- DNS

---

## Layer 6 - Presentation

Responsible for:
- Encryption
- Decryption
- Compression

Example:
SSL/TLS

---

## Layer 5 - Session

Creates and manages communication sessions.

Example:
Video Call

---

## Layer 4 - Transport

Responsible for:
- End-to-end communication
- Reliability
- Error recovery
- Flow control

Protocols:
- TCP
- UDP

---

## Layer 3 - Network

Responsible for:
- Routing
- IP Address

Device:
Router

Protocol:
IP

---

## Layer 2 - Data Link

Responsible for:
- MAC Address
- Error detection

Device:
Switch

---

## Layer 1 - Physical

Responsible for:
- Transmission of bits

Device:
Hub
Cable

---

# Interview Question

Q. Which layer uses IP Address?

Answer:
Network Layer

---

Q. Which layer uses MAC Address?

Answer:
Data Link Layer

---

Q. Which layer does Router work on?

Answer:
Layer 3

---

Q. Which layer does Switch work on?

Answer:
Layer 2

---

Q. Which layer does Hub work on?

Answer:
Layer 1

---

# 5. TCP/IP Model

TCP/IP has 4 Layers.

Application

Transport

Internet

Network Access

Difference:

OSI = 7 Layers

TCP/IP = 4 Layers

TCP/IP is used in real Internet.

---

# 6. IP Address

IP Address is a unique address used to identify a device on a network.

Example:

192.168.1.10

Types:

IPv4

32 bits

Example:
192.168.1.1

IPv6

128 bits

Example:

2001:db8::1

Reason for IPv6:
IPv4 addresses are limited.

---

# Public IP vs Private IP

Public IP

- Used on Internet
- Unique globally

Private IP

- Used inside local network
- Cannot be accessed directly from Internet

Example:
192.168.x.x

---

# Static IP

- Fixed IP
- Does not change

Example:
Server

---

# Dynamic IP

- Assigned automatically
- Changes over time

Used in:
Home Internet

---

# 7. MAC Address

MAC Address is the physical address of a device.

Characteristics:
- Unique
- Assigned by manufacturer
- 48 bits

Example:

00:1A:2B:3C:4D:5E

Interview:

IP can change.

MAC usually does not change.

---

# Difference between IP and MAC

| IP Address | MAC Address |
|-------------|-------------|
| Logical Address | Physical Address |
| Can change | Usually fixed |
| Layer 3 | Layer 2 |

---

# 8. Port Number

A Port Number identifies a specific application running on a device.

Examples:

HTTP → 80

HTTPS → 443

FTP → 21

SSH → 22

SMTP → 25

DNS → 53

POP3 → 110

IMAP → 143

---

# Important Port Numbers

| Protocol | Port |
|-----------|------|
| HTTP | 80 |
| HTTPS | 443 |
| FTP | 21 |
| SSH | 22 |
| SMTP | 25 |
| DNS | 53 |

---

# 9. TCP

TCP = Transmission Control Protocol

Features:

- Connection-oriented
- Reliable
- Error checking
- Data arrives in order
- Slower

Examples:

- Email
- Banking
- File Transfer

---

# 10. UDP

UDP = User Datagram Protocol

Features:

- Connectionless
- Faster
- No guarantee of delivery
- No ordering

Examples:

- Online Games
- Live Streaming
- Video Calls

---

# TCP vs UDP

| TCP | UDP |
|------|------|
| Reliable | Not reliable |
| Slow | Fast |
| Connection-oriented | Connectionless |
| Ordered delivery | No ordering |

---

# 11. HTTP vs HTTPS

HTTP

- Not secure
- Port 80

HTTPS

- Secure
- Uses SSL/TLS
- Port 443

Interview Question

Which is more secure?

HTTPS

---

# 12. DNS

DNS = Domain Name System

Work:

Converts

www.google.com

into

IP Address

Without DNS, users would have to remember IP addresses.

---

# 13. DHCP

DHCP = Dynamic Host Configuration Protocol

Work:

Automatically assigns:
- IP Address
- Gateway
- DNS

Example:

When you connect to Wi-Fi, DHCP gives your device an IP.

---

# 14. FTP

FTP = File Transfer Protocol

Used to transfer files between client and server.

Default Port:
21

---

# 15. SMTP

SMTP = Simple Mail Transfer Protocol

Used for:
Sending Email

Port:
25

---

# 16. POP3

POP3

Used to receive emails.

Port:
110

---

# 17. IMAP

IMAP

Used to receive emails while keeping them on the mail server.

Port:
143

---

# Frequently Asked Interview Questions

## Q1. What is Computer Network?

Answer:
A computer network is a collection of connected computers that communicate and share data and resources.

---

## Q2. Difference between IP Address and MAC Address?

Answer:

IP Address:
- Logical address
- Can change
- Layer 3

MAC Address:
- Physical address
- Usually fixed
- Layer 2

---

## Q3. Difference between TCP and UDP?

Answer:

TCP is reliable and connection-oriented.

UDP is faster but does not guarantee delivery.

---

## Q4. Difference between HTTP and HTTPS?

Answer:

HTTP:
- Not secure
- Port 80

HTTPS:
- Secure
- Port 443

---

## Q5. What is DNS?

Answer:

DNS converts domain names into IP addresses.

---

## Q6. What is DHCP?

Answer:

DHCP automatically assigns IP addresses to devices.

---

## Q7. What is Router?

Answer:

A router connects different networks and forwards data using IP addresses.

---

## Q8. What is Switch?

Answer:

A switch connects devices inside a LAN and forwards data using MAC addresses.

---

## Q9. What is Hub?

Answer:

A hub sends incoming data to every connected device.

---

## Q10. What is the OSI Model?

Answer:

The OSI Model is a networking model with 7 layers that explains how data travels from one device to another.

---

# Placement Revision (Must Remember)

✓ LAN, MAN, WAN

✓ Hub, Switch, Router

✓ OSI Layers

✓ TCP/IP Model

✓ IPv4 vs IPv6

✓ IP vs MAC

✓ TCP vs UDP

✓ HTTP vs HTTPS

✓ DNS

✓ DHCP

✓ FTP

✓ SMTP

✓ POP3

✓ IMAP

✓ Important Port Numbers
# ☁️ Cloud Computing Notes for Cognizant (AWS Basics)

> **Target:** Cognizant GenC / GenC Next, TCS, Infosys, Accenture, Capgemini
>
> **Level:** Beginner to Interview Ready
>
> Since you already have a basic understanding of AWS, these notes focus on concepts and AWS services commonly asked in interviews.

---

# 1. What is Cloud Computing? ⭐⭐⭐⭐⭐

Cloud Computing is the delivery of computing services such as servers, storage, databases, networking, software, and analytics over the Internet ("the cloud") instead of using your own physical infrastructure.

### Traditional Computing

```
Application
↓
Operating System
↓
Physical Server
```

You buy and maintain everything.

### Cloud Computing

```
Application
↓
Cloud Provider (AWS, Azure, GCP)
↓
Internet
```

Resources are rented on demand.

---

# 2. Advantages of Cloud Computing

- Pay only for what you use
- No hardware maintenance
- High availability
- Scalability
- Flexibility
- Faster deployment
- Automatic backups
- Global access

---

# 3. Types of Cloud

## Public Cloud

Resources are owned by cloud providers.

Examples

- AWS
- Microsoft Azure
- Google Cloud

---

## Private Cloud

Cloud infrastructure is dedicated to one organization.

Example

A bank hosts its own cloud.

---

## Hybrid Cloud

Combination of Public and Private Cloud.

Example

Sensitive customer data stays on a private cloud while the website runs on AWS.

---

# 4. Cloud Service Models ⭐⭐⭐⭐⭐

## IaaS (Infrastructure as a Service)

Provides

- Virtual Machines
- Storage
- Networking

Example

- Amazon EC2
- Azure Virtual Machines

Customer manages

- OS
- Applications
- Runtime

---

## PaaS (Platform as a Service)

Provides

- Runtime
- Operating System
- Development Platform

Example

- AWS Elastic Beanstalk
- Google App Engine

---

## SaaS (Software as a Service)

Complete software delivered over the internet.

Examples

- Gmail
- Microsoft 365
- Salesforce
- Zoom

---

## Comparison

| Service | Provider Manages | User Manages |
|----------|------------------|--------------|
| IaaS | Hardware | OS & App |
| PaaS | Hardware + OS | Application |
| SaaS | Everything | Only Usage |

---

# 5. What is AWS?

AWS (Amazon Web Services) is Amazon's cloud computing platform offering 200+ cloud services.

Popular services include

- EC2
- S3
- RDS
- Lambda
- IAM
- VPC

---

# 6. AWS Global Infrastructure ⭐⭐⭐⭐⭐

## Region

A geographical location containing multiple data centers.

Examples

- Mumbai (ap-south-1)
- Singapore
- Virginia
- London

---

## Availability Zone (AZ)

An isolated data center within a region.

Example

```
Mumbai Region

AZ-A

AZ-B

AZ-C
```

Using multiple AZs improves fault tolerance.

---

# 7. Amazon EC2 ⭐⭐⭐⭐⭐

EC2 = Elastic Compute Cloud

Provides virtual machines in the cloud.

Uses

- Hosting websites
- Backend APIs
- Databases
- Applications

---

### Features

- Launch Linux or Windows VM
- Resize instance
- Start/Stop
- Elastic IP
- Security Groups

---

# 8. EC2 Instance Types

Examples

- t2.micro
- t3.micro
- m5.large
- c5.large
- r5.large

Memory optimized

Compute optimized

General purpose

---

# 9. Amazon S3 ⭐⭐⭐⭐⭐

S3 = Simple Storage Service

Object Storage

Stores

- Images
- Videos
- PDFs
- Backups
- Static websites

---

### Features

- Unlimited storage
- High durability (11 nines)
- Versioning
- Encryption
- Lifecycle Rules

---

# 10. S3 Storage Classes

- Standard
- Intelligent-Tiering
- Standard-IA
- One Zone-IA
- Glacier Instant Retrieval
- Glacier Flexible Retrieval
- Glacier Deep Archive

---

# 11. Amazon RDS ⭐⭐⭐⭐⭐

RDS = Relational Database Service

Supports

- MySQL
- PostgreSQL
- MariaDB
- SQL Server
- Oracle

Advantages

- Automatic Backup
- Automatic Updates
- Multi-AZ
- Easy Scaling

---

# 12. Amazon DynamoDB

NoSQL Database

Features

- Fast
- Fully Managed
- Serverless
- Key-Value Database

---

# 13. IAM ⭐⭐⭐⭐⭐

IAM = Identity and Access Management

Controls

- Authentication
- Authorization
- Permissions

Components

- Users
- Groups
- Roles
- Policies

---

### Principle of Least Privilege

Give users only the permissions they need.

---

# 14. VPC ⭐⭐⭐⭐⭐

VPC = Virtual Private Cloud

Your own private network inside AWS.

Contains

- Subnets
- Route Tables
- Internet Gateway
- NAT Gateway

---

# 15. Security Group

Acts as a virtual firewall for EC2 instances.

Controls

- Inbound Traffic
- Outbound Traffic

Stateful firewall.

---

# 16. NACL (Network ACL)

Works at subnet level.

Stateless firewall.

---

# Security Group vs NACL

| Security Group | NACL |
|----------------|------|
| Instance Level | Subnet Level |
| Stateful | Stateless |
| Allow Rules Only | Allow & Deny Rules |

---

# 17. Elastic Load Balancer (ELB)

Distributes incoming traffic across multiple EC2 instances.

Advantages

- High Availability
- Fault Tolerance
- Scalability

---

# 18. Auto Scaling

Automatically increases or decreases EC2 instances based on demand.

Benefits

- Cost Saving
- High Availability

---

# 19. Route 53

AWS DNS Service.

Functions

- Domain Registration
- DNS Routing
- Health Checks

---

# 20. CloudFront

Content Delivery Network (CDN).

Caches content at edge locations.

Benefits

- Faster Website
- Lower Latency

---

# 21. AWS Lambda ⭐⭐⭐⭐⭐

Serverless computing service.

Run code without managing servers.

Charged only for execution time.

Supported Languages

- Python
- Java
- Node.js
- C#
- Go

---

# 22. Serverless Computing

Developer only writes code.

Cloud provider manages

- Servers
- Scaling
- Maintenance

Examples

- AWS Lambda
- Azure Functions

---

# 23. CloudWatch

Monitoring service.

Monitors

- CPU
- Memory (custom metrics)
- Logs
- Network
- Alarms

---

# 24. CloudTrail

Records AWS API activity.

Used for

- Auditing
- Security
- Compliance

---

# 25. AWS SNS

Simple Notification Service.

Used for

- SMS
- Email
- Push Notifications

---

# 26. AWS SQS

Simple Queue Service.

Message queue for communication between applications.

---

# 27. EBS

Elastic Block Store

Provides block storage for EC2 instances.

Persistent storage.

---

# 28. EFS

Elastic File System

Shared file storage.

Multiple EC2 instances can access it.

---

# 29. Containers

Container packages

- Application
- Dependencies
- Libraries

Popular Tool

Docker

---

# 30. Kubernetes (EKS)

Container orchestration platform.

AWS version

Amazon EKS

Functions

- Deploy containers
- Scale containers
- Manage containers

---

# 31. Docker vs Virtual Machine

| Docker | VM |
|----------|----|
| Lightweight | Heavy |
| Shares OS Kernel | Separate OS |
| Faster Startup | Slower Startup |
| Less Memory | More Memory |

---

# 32. CI/CD

CI

Continuous Integration

CD

Continuous Delivery / Deployment

Benefits

- Faster Release
- Automated Testing
- Better Quality

---

# 33. Shared Responsibility Model ⭐⭐⭐⭐⭐

AWS is responsible for

- Physical Security
- Hardware
- Networking
- Data Centers

Customer is responsible for

- IAM Permissions
- Data
- Applications
- Operating System (EC2)
- Security Groups

---

# Frequently Asked Interview Questions

### Q1. What is Cloud Computing?

Cloud Computing is the on-demand delivery of computing services such as servers, storage, databases, and networking over the Internet with pay-as-you-go pricing.

---

### Q2. What are the service models?

- IaaS
- PaaS
- SaaS

---

### Q3. What is EC2?

Amazon EC2 is a service that provides scalable virtual servers in the cloud.

---

### Q4. What is S3?

Amazon S3 is an object storage service used to store files like images, videos, backups, and static website assets.

---

### Q5. Difference between S3 and EBS?

| S3 | EBS |
|----|-----|
| Object Storage | Block Storage |
| Unlimited | Attached to EC2 |
| Stores files | Stores disk volumes |

---

### Q6. What is IAM?

IAM manages users, roles, groups, and permissions for AWS resources.

---

### Q7. Difference between Security Group and NACL?

Security Groups are stateful and work at the instance level, while NACLs are stateless and work at the subnet level.

---

### Q8. What is Auto Scaling?

Automatically adjusts the number of EC2 instances based on workload.

---

### Q9. What is AWS Lambda?

AWS Lambda is a serverless service that runs code without provisioning or managing servers.

---

### Q10. What is the AWS Shared Responsibility Model?

AWS secures the cloud infrastructure, while customers are responsible for securing their data, applications, identities, and configurations.

---

# ⭐ Most Important Topics for Cognizant

- Cloud Computing Basics
- Public, Private & Hybrid Cloud
- IaaS, PaaS, SaaS
- AWS Global Infrastructure (Regions & Availability Zones)
- EC2
- S3
- RDS
- DynamoDB
- IAM
- VPC
- Security Groups vs NACL
- Elastic Load Balancer
- Auto Scaling
- Route 53
- CloudFront
- AWS Lambda
- CloudWatch
- CloudTrail
- SNS & SQS
- EBS vs EFS
- Docker Basics
- Kubernetes (EKS)
- CI/CD
- Shared Responsibility Model
```
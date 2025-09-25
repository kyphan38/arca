# application architecture

![img](./img/3.png)

Question 1: Compare vertical and horizontal scaling. In large-scale systems, why is horizontal scaling almost always the preferred strategy?

Question 2: What is the primary function of a load balancer, and why is it a non-negotiable component in a horizontally scaled architecture?

Question 3: Describe the three core components used to monitor a modern application (logging, metrics, alerting) and how they interrelate?

## The Basics: From Developer to Server

- Developers write code that needs to be run on a server
- A server is like a computer that handles requested from users
- Before code reaches the server, it often goes through a build and deployment process. This can happen on a developer's computer or, more commonly in professional settings, on a CI/CD server
- The server needs to store data, so it connects to an external, persistent storage system over a network. This could be a database or another type of storage, and it is assumed to be on a separate computer, maybe even in a different part of the world

## Handling Users and Traffic

- The server can respond with front-end code (like HTML and JavaScript) to load a webpage, or it can be a backend API that responds with data (like JSON)
- When a single server cannot handle all user requests, you need to scale the system. There are two main ways to do this
  - Vertical Scaling: This involves making a single server more powerful by upgrading its components, like its CPU, RAM, or disk. This is conceptually simple but has limits because even the best computer cannot handle infinite requests
  - Horizontal Scaling: This involves adding more copies of the server to run the same code. This allows the system to handle more simultaneous requests because user requests can be sent to different servers
- When using multiple servers (horizontal scaling), a load balancer is needed. The load balancer's job is to distribute incoming user requests evenly across all the servers to ensure no single server gets overwhelmed

## Developer Tools for Monitoring

- Servers can communicate with other external servers or APIs, for example, to handle payments through service like Stripe
- To understand what's happening inside the application, developers use several tools that users don't interact with directly
  - Logging Service: Servers send log statements to an external logging service. These logs record information about every user request, whether it was successful or not, helping developers understand how the code is working and debug issues
  - Metrics Service: This service collects data on how the servers are performing. It tracks things like CPU and RAM usage, whether requests are falling, and other application or resource metrics. Metrics are often displayed on charts over time to show trends. Some metrics can be created directly from logs, since logs have timestamps
  - Alerting Service: This service watches the metrics and automatically notifies developers when something goes wrong. Developers can set thresholds, for example, if the success rate of user requests drops below 95%. This allows developers to learn about problems immediately, rather than waiting for users to report them

## The Bigger Picture

- This entire system is a simplified view of a real-world application, which can be much more complex
- An important aspect not covered in detail is networking, which is how all these different components (servers, storage, services) communicate with each other, especially since they are often running on different computers in different locations

# basics

- [x] Done

## Basics

Approaches: There are two ways in which you can create and manage your infrastructure

- Manual approach
- Through automation

## Examples

Example 1: Database backup

- Requirement: I was assigned a task to take a database backup every day at 10 PM, and the backup had to be stored in Amazon S3 Storage with an appropriate timestamp
  - db-backup-01-01-2024.sql
  - db-backup-01-02-2024.sql
- Bad solution: Initially, due to a lack of time, I used to take a DB backup manually at 10 PM and upload it to S3
- Lesson
  - If a particular task has to be done in a repeatable manner, then it MUST be automated
  - Depending on the type of task, the tools for automation will change

Example 2: A single service

- A set of resources (Virtual Machine, Database, S3, AWS Users) must be created with the exact same configuration in Dev, Stage, and Production environments

![img](./img/2/1.png)

## Infrastructure as Code

Concepts

- Infrastructure as Code (IaC) is the management and provisioning of infrastructure through code instead of through manual processes

Benefits

- Speed of infrastructure management
- Low risk of human errors
- Version control
- Easy collaboration between teams

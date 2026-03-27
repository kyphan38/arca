# regional and global aws architecture

- [x] Done

## Global Architecture

Concept: Components handle traffic before it enters a region

- Global Service Discovery (DNS)
  - DNS points URL to IP address or endpoint
- Global Health Checks & Failover
  - System checks region health
  - Route 53 reroutes traffic on failure
  - Routes to nearest location for low latency
- Content Delivery Network (CDN)
  - CloudFront caches content globally near users
  - Users pull data from local cache

## Regional Architecture

Concept: Regional traffic is divided into functional tiers

- The web tier - Entry point
  - Acts as application front door
  - Hides backend infrastructure from users
  - Enables backend scaling and failover
  - Services: Application Load Balancer (ALB), API Gateway
- The compute tier - The brains
  - Provides application logic and processing
  - Web tier sends traffic for processing
  - Services: EC2, Lambda, ECS
- The storage tier - Files and media
  - Holds files and media for compute tier
  - CloudFront can pull media from S3
  - Services: EBS (Elastic Block Store), EFS (Elastic File System), S3
- The database tier - Structured data
  - Provides long-term data storage
  - Services: RDS & Aurora, DynamoDB, Redshift
- The caching tier - Speed layer
  - Sits before database to improve performance
  - Application checks cache first for speed
  - Database queried only on cache miss
  - Services: ElastiCache, DAX
- Application services tier - Messaging
  - Provides messaging and application decoupling
  - Services: SQS (Queues), SNS (Notifications), Kinesis

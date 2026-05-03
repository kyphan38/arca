# implementation

- [x] Progress: Done

## Overview

### Flow

![img](./img/03/01.png)

### Components

- Corporation
  ![img](./img/03/02.png)
- Service A
  ![img](./img/03/03.png)
- RabbitMQ
  ![img](./img/03/04.png)
- Service B
  ![img](./img/03/05.png)
- Core Banking
  ![img](./img/03/06.png)
- DLQ
  ![img](./img/03/07.png)
- Message
  ![img](./img/03/08.png)
- Idempotency
  ![img](./img/03/09.png)
- Consumers
  ![img](./img/03/10.png)

## Execution

### How it works

- Dashed arc at top represents ACK loop - invisible feedback driving system
- Service B sends ACK, broker deletes message, gives B next message
- ACK loop ensures overall system safety
- NACK arrow routes from broker down to DLQ instead of directly from Service B - because Service B instructs broker to NACK and broker performs routing
- Service B never accesses DLQ directly

### Best practices

- Diagram functions as checklist for implementation practice
- Checklist flow: Corp → Producer (declare topology, basic_publish, delivery_mode=2) → Broker (exchange, queue, DLQ binding, routing key match) → Consumer (prefetch=1, auto_ack=False, idempotency check, ACK/NACK) → Core Banking
- Build components in specified sequence to achieve production-safe payment queue

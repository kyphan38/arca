# ipv4 addressing 2

- [x] Progress: Done

## Maximum Hosts Per Network

### Concepts

- Maximum hosts per network = 2^n - 2
- n represents the number of host bits

### Examples

- 192.168.1.0/24 to 192.168.1.255/24
  - Host portion is 8 bits (2^8 = 256)
  - Maximum hosts per network is 256 - 2 = 254
  - First usable address is 192.168.1.1
  - Last usable address is 192.168.1.254
- 172.16.0.0/16 to 172.16.255.255/16
  - Host portion is 8 bits = 2^16 = 65,536
  - Maximum hosts per network is 65,536 - 2 = 65,534
  - First usable address is 172.16.0.1
  - Last usable address is 172.16.255.254
- 10.0.0.0/8 to 10.255.255.255/8
  - Host portion: 8 bits = 2^24 = 16,777,216
  - Maximum hosts per network is 16,777,216 - 2 = 16,777,214
  - First usable address is 10.0.0.1
  - Last usable address is 10.255.255.254

## Configure IP Addresses on Cisco Devices

### Concepts

- Administratively down means the interface has been disabled with the shutdown command
- This is the default status of Cisco router interfaces
- Cisco switch interfaces are not administratively down by default
- Status column refers to layer 1 status
- Protocol column refers to layer 2 status

![img](./img/08/01.png)

### Commands

- R1 configuration for 10.0.0.0/8 network

```txt
en
show ip interface brief
conf t
interface g0/0
description ## to SW1 ##
ip address 10.255.255.254 255.0.0.0
no shutdown
do show ip interface brief
```

- R1 configuration for 172.16.0.0/16 network

```txt
interface g0/1
description ## to SW2 ##
ip address 172.16.255.254 255.255.0.0
no shutdown
do show ip interface brief
```

- R1 configuration for 192.168.1.0/24 network

```txt
interface g0/2
description ## to SW3 ##
ip address 192.168.0.254 255.255.255.0
no shutdown
do show ip interface brief
```

- Other verification commands

```txt
show interfaces g0/0
show interfaces description
```

## Exercises

### Examples

- Example 1: PC1 has an IP address of 43.109.23.12/8
  - Network address is 43.0.0.0
  - Maximum number of hosts per network is 16,777,214
  - Broadcast address is 43.255.255.255
  - First usable address is 43.1.0.0
  - Last usable address is 43.255.255.254

- Example 2: PC4 has an IP address of 129.221.23.13/16
  - Network address is 129.221.0.0
  - Maximum number of hosts per network is 65,534
  - Broadcast address is 129.221.255.255
  - First usable address is 129.221.0.1
  - Last usable address is 129.221.255.254

## Review Questions

Q: What is the formula for calculating the maximum hosts per network?

- 2^n - 2 (where n is the number of host bits)

Q: What does the status "administratively down" indicate on a Cisco device?

- The interface has been disabled with the shutdown command

Q: What is the default status of Cisco router interfaces?

- Administratively down

Q: Are Cisco switch interfaces administratively down by default?

- No, Cisco switch interfaces are not administratively down by default

Q: What does the "Status" column refer to in the interface brief output?

- Layer 1 status

Q: What does the "Protocol" column refer to in the interface brief output?

- Layer 2 status

# networking

## Main Network Environment Components

The key components are

- Network devices
  - The virtual/physical interfaces that connect a computer to a network
  - Running `ip link list` or `ip a`
    - Loopback interface `lo`
    - Ethernet interfaces `eth0`
- Routing tables
  - A set of rules that tell the computer how to send traffic
  - Running `ip route list`
- Firewall rules
  - Security rules that control the incoming and outgoing network traffic
  - Act a barrier between the computer and outside world, allowing you to block or allow specific connections
  - Running `iptables --list-rules`

What is a loopback interface?

- A special, virtual network interface that does not connect to any external network or hardware
- It allows network applications on the machine to communicate with each other
- It is used for testing network application and running client/server appplications on the same machine without sending any traffic out onto the physical network

What is an Ethernet interface?

- The physical connection to your local network
- It represents the actual network card (Network Interface Card or NIC) that you plug an Ethernet cable into
- It allows the computer to communicate with other devices on your local network
- It is used for all communication that needs to leave the computer, like browse webistes, sending emails, etc. to the the local network
- When you type `gooogle.com` into your browser, the request leaves your computer via the Ethernet interface, hits the local network, and is sent to the router, which then forwards it to the internet

## Creating a Container With a Network Namespace

We give a container its own private network environment via Linux feature - network namespaces (or netns)

A network namespace is giving a process its own virtual network. This mean it has its own private

- Network interfaces (like lo and eth0)
- Routing table
- Firewall rules (iptables)

Imagine your host computer is a large apartment building

- A network namespace is like giving a tenant (a container) their own private apartment
- Inside their apartment, they have
  - Their own mailbox
  - Their own list of directions for getting around town
  - Their own front door lock
- They are all completely separate from the other tenants

Practice

- Create a new network namespace: `sudo ip netns add ns1`
- List all namespaces: `ip netns list`
- Inspect the interfaces inside ns1: `sudo ip netns exec ns1 ip link list`
- Bring the lo inteface up inside ns1: `sudo ip netns exec ns1 link set lo up`

Current problem

- The ns1 is still completely isolated
- It cannot talk to the host or the internet

## Connecting the Container to the Host

How do we connect our isolated ns1 to the outside world (the host machine)?

- Right now, it's like an apartment with no doors or windows
- We need to create a pathway
- We do this using a virtual Ethernet device pair, or `veth` pair

A veth pair

- A pair of connected virtual network interfaces
- Whatever network traffic goes into one end of the cable immediately comes out the other end
- The best analogy is a virtual Ethernet cable or a patch cable
- Establish a direct point-to-point link between the host and our ns1 container

Why do we need IP addresses for both side

- It allows the OS to identify exactly where to send the network traffic
- The veth interface is the physical path, and the IP address is the logical address
- Without addresses, the interfaces are connected but have no way to "talk" to each other

Practice

- Create the veth pair
  - `veth-host` to stay on the host
  - `veth-ns1` to go into the namespace
  - `sudo ip link add veth-host type veth peer name veth-ns1`
- Move veth-ns1 into the ns1 namespace: `sudo ip link set veth-ns1 netns ns1`
- Check the interfaces inside ns1: `sudo ip netns exec ns1 ip link list`
- Configure the host end of the cable
  - `sudo ip link set veth-host up`
  - `sudo ip addr add 172.18.0.1/24 dev veth-host`
- Configure the namespace end of the cable
  - `sudo ip netns exec ns1 ip link set veth-ns1 up`
  - `sudo ip netns exec ns1 ip addr add 172.18.0.2/24 dev veth-ns1`
- Test connection from the host: `ping -c 4 172.18.0.2`
- Test connection from the namespace: `sudo ip netns exec ns1 ping -c 4 172.18.0.1`

You can now ping between the host and the container. Do you think the container (ns1) can ping an external site like Google's DNS server (8.8.8.8) yet? Why or why not?

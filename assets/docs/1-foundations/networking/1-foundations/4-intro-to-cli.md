# intro to cli

- [x] Done

## Cli

Definitions

- Command-line interface
- The interface you use to configure Cisco devices

## Gui

Definition: Graphical User interface

## Cisco Device Connection

How to connect a Cisco device via the RJ-45 console port?

![img](./img/4/1.png)

## Mode

![img](./img/4/2.png)

### User Exec

Definitions

- User EXEC mode is very limited
- Users can look at some things, but cannot make any changes to the configuration
- Also called user mode

```txt
# Hostname of the device and user EXEC mode
Router>
```

### Privileged Exec

Definitions

- Provides complete access to view the device's configuration, restart the device, etc.
- Cannot change the configuration, but can change the time on the device, save the configuration file, etc.

```txt
Router>enable
Router#
```

### Global Configuration

```txt
Router#configure terminal
Router(config)#
```

## Config

Definitions

- There are two separate configuration files kept on the device at once
- Running-config is the current, active configuration file on the device. As you enter commands in the CLI, you edit the active configuration
- Startup-config is the configuration file that will be loaded upon restart of the device

Commands

```txt
show running-config
show startup-config

# Save the configuration
write
write memory
copy running-config startup-config
```

## Practice

Commands

```txt
enable password ?
enable password CCNA

# Encrypt the enable password (and other passwords)
service password-encryption

# Configure a more secure, always-encrypted enable password
enable secret password
do show running-config

# Execute a privileged-exec level command from global configuration mode
run <privileged-exec-level-command>

# Remove the command
no service password-encryption
```

Notes

- If you enable service password-encryption
  - Current passwords will be encrypted
  - Future passwords will be encrypted
  - The enable secret will not be effected
- If you disable service password-encryption
  - Current passwords will not be encrypted
  - Future passwords will not be encrypted
  - The enable secret will not be effected
# links

- [ ] Progress: Draft

## Concepts

- **Hard link** - second directory entry pointing to the same inode as an existing file
  - No new inode, new data, or copying occurs
  - Example - `ln report.txt backup.txt`
  - Filenames `report.txt` and `backup.txt` map to the same inode number (example: 84213)
  - Increments the inode link count from 1 to 2
- **Symbolic link** (symlink) - separate file containing a path string pointing to another file
  - Has its own inode, size (path length), and permissions
  - Example - `ln -s report.txt shortcut.txt`
  - Allocates a new inode (example: 90517) of type symlink
  - Inode data stores the target path string `report.txt`
  - Creates a new directory entry mapping `shortcut.txt` to the new inode
  - Original file remains untouched and unaware of the symlink

## How it works

- Inode link count tracks directory entries pointing to it (visible via `ls -l` or `stat`)
- Hard links are robust because data resides in the inode

File deletion process via `rm`

- Kernel invokes `unlink()` to remove the directory entry
- Kernel decrements the inode link count
- Filesystem frees the inode and data blocks when the link count reaches zero

Symbolic link resolution process (example: `cat shortcut.txt`)

- Kernel looks up `shortcut.txt` to find inode 90517
- Kernel detects inode type is symlink and reads target path `report.txt`
- Kernel restarts path lookup using the target path `report.txt`
- Kernel resolves `report.txt` to target inode 84213
- Kernel reads target inode data blocks

## Comparison

| Feature | Hard Links | Symbolic Links |
| :--- | :--- | :--- |
| **Target Type** | Files only | Files and directories |
| **Scope** | Single filesystem only | Cross-filesystem support |
| **Inode usage** | Share the same inode | Allocate a new inode |
| **Visual representation** | Same as standard file | Distinguishable (example: `l` permission flag) |
| **Dangling vulnerability** | Resilient to target deletion | Breaks if target moves or is deleted |
| **Silent stale risk** | No | Yes (if target is replaced) |

- Symlinks can use absolute or relative paths
  - Example absolute - `ln -s /etc/nginx/sites-available/blog enabled-blog`
  - Example relative - `ln -s ../sites-available/blog enabled-blog`
- Dangling symlink - link pointing to a non-existent path (typically highlighted in red by `ls -l`)

## Use Cases

- Incremental backups
  - Tools like `rsnapshot` or Apple Time Machine use hard links for unchanged files

```txt
backups/2026-05-28/home/alex/report.txt   (inode 84213)
backups/2026-05-29/home/alex/report.txt   (inode 84213)  ← unchanged, hard-linked
backups/2026-05-30/home/alex/report.txt   (inode 92841)  ← modified, new copy
```

- File deduplication
  - Replaces identical files with hard links to reclaim disk space
- Content-addressed package managers
  - `pnpm` hard-links package files from a global store into `node_modules`
- Git local clone optimization
  - `git clone /path/to/local/repo` hard-links object files instead of copying
- Versioned software redirection
  - Repointing a symlink enables fast software upgrades or rollbacks
  - Tools like `nvm` or `pyenv` use this pattern internally

```txt
/opt/node-18.17.0/
/opt/node-20.10.0/
/opt/node-current  →  /opt/node-20.10.0
```
  
- Shared library version chains

```txt
libssl.so       →  libssl.so.3
libssl.so.3     →  libssl.so.3.0.2
libssl.so.3.0.2    (the actual file)
```

- Dotfile management

```txt
~/.bashrc      →  ~/dotfiles/bashrc
~/.vimrc       →  ~/dotfiles/vimrc
~/.gitconfig   →  ~/dotfiles/gitconfig
```

- Service activation (Debian-style)
  - Link creation enables the service without modifying the original configuration file
  - `systemd` uses the same pattern inside `.wants` directories

```txt
/etc/nginx/sites-available/   ← all configs live here
/etc/nginx/sites-enabled/     ← symlinks to the active ones
```

- Cross-filesystem references
  - Moving directories (example: `/var/log`) to separate disks while retaining original paths
- System kernel interfaces
  - Special symlinks like `/proc/self` resolve to active calling process information
- Executable version selection
  - Debian `update-alternatives` system routes paths through intermediate symlinks

```txt
/usr/bin/python  →  /etc/alternatives/python  →  /usr/bin/python3.11
```

- Directory path shortening

```txt
ln -s /mnt/storage/clients/2026/acme-corp/engineering ~/work
```

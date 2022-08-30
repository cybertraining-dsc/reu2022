# Cloudmesh Project Ramdisk

---

![](images/learning.png) **Learning Objectives**

* Learn how to set up a RAM disk
* Learn how to use a DAM disk

---

THis is an easy assignment to develop a cloudmesh command that sets up a 
RAMDISK in various operating systems. To facilitate this task we provide the 
first initial information.

The command should look similar to 

```bash
$ cms ramdisk --... --size=SIZE
```

We recommend that you use python humanize to make it easier to read file sizes 
such as 1GB (without humanize, the number of bytes is displayed instead of 
GB, making it hard to comprehend).

You could enhance the program to also integrate it into the OS so it starts up 
immediately after reboot. However for now a simple on demand program to start 
and stop the ramdisk is sufficient.

Advanced integration could include 

* dynamic ramdisk no reboot needed, but if reboot, ramdisk needs to
  be set up new
* ramdisk integrated in fstab with reboot
* backup and load ramdisk


On macOS a RAM disk with 512MB space can be created with the following
command:

```
n = 512 * 2048
os.system('diskutil eraseVolume HFS+ "RAMDisk" `hdiutil attach -nomount ram://{n}`')
```

## Ubuntu

On Ubuntu, a RAM disk and its read-only shadow can be created by:

```
mount -t tmpfs -o size=512m tmpfs /mnt/ramdisk
mount -t aufs -o br:/mnt/ramdisk=ro none /mnt/readonly
```

```
# mkdir /tmp/ramdisk; chmod 777 /tmp/ramdisk
# mount -t tmpfs -o size=256M tmpfs /tmp/ramdisk/
```

Links that could be useful include, but are not limited to

* Information about using /dev/shm is available at <http://ubuntuguide.
  net/ubuntu-using-ramdisk-for-better-performance-and-fast-response>
* Various methods (in german) are documented at 
<https://wiki.ubuntuusers.de/RAM-Disk_erstellen>
* ramfs is an older file system type and is replaced in mostly by tmpfs.
* Windows <https://forums.guru3d.com/threads/guide-using-imdisk-to-set-up-ram-disk-s-in-windows-with-no-limit-on-disk-size.356046/>

Assignment:


Provide processes with their own system view
Cgroups = limits how much resources we you can use; 
namespaces = limits what you can see

A Linux namespace is an abstraction over resources in the operating system.



# what it is, why is it required, how is it useful
Namespaces:-
1. PID namespace
2. Net namespace
3. Uts namespace
4. user namespace
5. mnt namespace
6. IPC
7. cgroups
## 1. PID namespace (Process isolation):-
    what it is?
    why is it required?
    how is it useful?

    Processes within a PID namespace only see processes in the same PID namespace
    Each PID namespace has its own numbering
    starting from 1
    If PID 1 goes away, whole namespace is killed
    Those namespaces can be nested
    A process ends up having multiple PIDs
    one per namespace in which its nested

## 2. Net namespace(ip-netns):-
    
* It provides a network isolation
* Network namespace creates acompletely new network stack including :
network interfaces (includinglo) routing   tables
iptables rules
sockets (ss, netstat)
* You can move a network interface across different net namespaces

```
ip netns add <new namespace name>

ip netns list # lists all net namespaces

ip link add veth0 type veth peer name veth1 # Create virtual link

ip link set veth1 netns blue #assign interfaces to namespace


```

## 3. UTS namespace(Unix Timesharing System)

    It isolates the system's host and domain name within a uts namespace. 

    why is it required?
    It is used to provide usernames and hostnames in a docker to executables
    
    The names are set using the sethostname() and setdomainname() system calls.

    Can be retrieved using uname(2), gethostname(2), and getdomainname(2). 

    The hostname and domain of
       the new UTS namespace are copied from the corresponding values in
       the caller's UTS namespace.

    UTS namespace provides a way to get information about the system with commands like uname or hostname.


## 4. User namespace:-
    User namespaces is a feature of Linux, that is used to separate the user IDs and group IDs between the host and containers

    can run containers using privileged and non-privileged users both.

    User namespaces allow a process to use unique user and group IDs within and outside a namespace. This means that a process can use privileged user and group IDs (zero) within a user namespace and continue with non-zero user and group IDs outside the namespace.
    

## 5. mnt namespace:-

    Mount and Unmount operations can change the filesystem view as seen by all processes in the system

    Mount namespaces provide isolation of the list of mount points seen by the processes in each namespace 

    Processes can have their own root fs

    Mounts can be totally private, or shared

    New mount namespace is a copy of the mount points from the parent namespace

    new mnt namespace can be created by:
    
    unshare -m

    The views provided by the /proc/[pid]/mounts,
       /proc/[pid]/mountinfo, and /proc/[pid]/mountstats files (all
       described in proc(5)) correspond to the mount namespace in which
       the process with the PID [pid] resides.

    A new mount namespace is created using either clone(2) or
       unshare(2)

    

## 6. Interprocess Communication(ipc_namespaces)

    IPCs handle the communication between processes by using shared memory areas, message queues, and semaphores

    These demarcate processes from using System V and POSIX message queues. This prevents one process from an ipc namespace accessing the resources of another.

    Allows a process (or group of processes)to have own:
        IPC semaphores
        IPC message queues
        IPC shared memory
        (without risk of conflict with other instances)

## 7. cgroups:-

    CGroups are a mechanism for controlling system resources.

    When a CGroup is active, it can control the amount of CPU, RAM, block I/O, and some other resources which a process consumes

    CGroups are created in the virtual filesystem /sys/fs/cgroup
    
    Processes inside a cgroup namespace are only able to view paths relative to their namespace root.

    types of cgroups:-
        memory

        keeps track of pages which pages are assignes to which group to keep a track of memory usage

        we can set limits to groups (optional)
        soft and hard

        cpu (cores , time)
        i/o(blocked use)
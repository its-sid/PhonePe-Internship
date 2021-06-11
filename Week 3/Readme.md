# Week 3 Tasks
Establish BGP Sessions between below pairs:
1. vm-1 <-> vm-router
2. vm-2 <-> vm-router
3. vm-3 <-> vm-router

Apply Bgp filters as follows
1. vm-router orginates and sends default route to vm-1 , vm-2 and vm-3
2. Each of the vms ( vm1, 2, 3 ) will accept only default route from its bgp peer ( vm-router) and advertise their own loopback(IP on its lo interface ) to vm-router
3. vm-router to accept /32 IPs that belong to subnet (10.1.1.0/24) and reject all other routes

Test case:
1. On vm1, ping 10.1.1.3 and 10.1.4 should work
2. On vm2, ping 10.1.1.2 and 10.1.1.4 should work
3. On vm3, ping 10.1.1.2 and 10.1.1.3 should work

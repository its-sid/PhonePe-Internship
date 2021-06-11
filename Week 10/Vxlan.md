### BGP configuration between R1,R2,R3,R4 on cumulus:-

+ Configuration

    Host | Interface | IP/mask
    :--: | :--: | :--:
    R1 | lo<br>swp1| 1.1.1.1/32<br>172.10.0.2/30
    R2 | lo<br>swp1 | 2.2.2.2/32<br>172.10.0.6/30
    R3 | lo<br>swp1 | 3.3.3.3/32<br>172.10.0.10/30
    R4 | lo<br>swp1<br>swp2<br>swp3 | 4.4.4.4/32<br>172.10.0.1/30 <br> 172.10.0.5/30<br>172.10.0.9/30

To Configure interfaces on all Vms we will use:
```
net add loopback lo ip address <ip/subnet>      # For loopback interface
net add interface swp1 ip address <ip/subnet>   # For regular interface
net pending                                   # Show what changes will be made
net commit                                    # To apply the changes
```

We will use R4 as router in this network:-

+ All the router are connected to each other as mensioned below:-
    R4 interface | Router | Interface | Network
    :--: | :--: | :--: | :--:
    swp1| R1 | swp1 | 172.10.0.0/30
    swp2| R2 | swp1 | 172.10.0.4/30
    swp3| R2 | swp1 | 172.10.0.8/30

Bgp for R4:-
```
net add bgp autonomous-system 4
# Neighbors
net add bgp neighbor 172.10.0.2 remote-as 1
net add bgp neighbor 172.10.0.6 remote-as 2
net add bgp neighbor 172.10.0.10 remote-as 3
# Advertise the loopbacks
net add bgp ipv4 unicast network 4.4.4.4/32
net pending
net commit
```

Bgp for other Vms:-
```
net add bgp autonomous-system 1
net add bgp neighbor 172.10.0.1 remote-as 4
net add bgp ipv4 unicast network 172.10.0.0/30
net add bgp network 1.1.1.1/32
net pending
net commit
```
We will follow same steps on other vms(Change IP address acc to Vms).

We have established bgp session

We will now set up l2vpn bgp connectivity:

```
#R1
net add bgp l2vpn evpn neighbor 172.10.0.1 activate
net commit
#R2
net add bgp l2vpn evpn neighbor 172.10.0.5 activate
net commit
#R3
net add bgp l2vpn evpn neighbor 172.10.0.9 activate
net commit
#R4
net add bgp l2vpn evpn neighbor 172.10.0.2 activate
net add bgp l2vpn evpn neighbor 172.10.0.6 activate
net add bgp l2vpn evpn neighbor 172.10.0.10 activate
net commit
```
Make vxlan , vlan and attach the interfaces to it

```
# adds VNID(123) to virtual interface(temp)

net add vxlan temp vxlan id 123 

# Adds VLAN 10 to temp		

net add vxlan temp bridge access 10		

# disables mac learning on temp

net add vxlan temp bridge learning off	

# specifies local source IP to be 1.1.1.1 for VXLAN packets    

net add vxlan temp vxlan local-tunnelip 1.1.1.1

# Add other interfaces to VLAN 10

net add interface swp1 bridge access 10
net add interface lo bridge access 10

#commit the changes

net commit

```


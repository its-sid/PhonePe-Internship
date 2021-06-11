# VM1 [Mesos master, Marathon, and Zookeeper] [172.0.0.2]
## 1. Mesos master:- 
+ Install jdk version 8 and 16 (dependencies)
	```
	sudo apt-get update
	sudo apt install openjdk-16-jre-headless
	sudo apt install openjdk-8-jre-headless
	```

+ Install messos(With java 16 as default)
	```
	update-alternatives --config java
	```
+ Get the env ready
	```
	sudo apt-get -y install build-essential python3-dev python3-six python3-virtualenv libcurl4-nss-dev libsasl2-dev 	libsasl2-modules maven libapr1-dev libsvn-dev zlib1g-dev iputils-ping
	sudo apt-get install libcurl4-openssl-dev
	```
+ Install mesos from .deb file
	```
	sudo dpkg -i mesos-1.9.0-0.1.20200901105608.deb
	```
	+ apt-cache policy mesos (to confirm the installation)

+ Set 1 in quorum file
	```
	sudo nano /etc/mesos-master/quorum
	```
+ Setup ip and hostname of mesos-master
	```
	sudo nano /etc/mesos-master/ip				# 172.0.0.2
	sudo nano /etc/mesos-master/hostname		# 172.0.0.2
	```

+ Configure ZooKeeper connection info to point to master servers:
	```
	sudo nano /etc/mesos/zk			# zk://172.0.0.2:2181/mesos
	```

+ We need to make sure that our master servers are only running the Mesos master process, and not running the slave process. We can ensure that the server doesn’t start the slave process at boot by creating an override file:

	```
	echo manual | sudo tee /etc/init/mesos-slave.override
	```

+ Start mesos-master
	```
	sudo service mesos-master restart
	```

## 2. Install zookeeper:-

+ Install using apt
	```
	sudo apt-get install zookeeper
	```

+ Give each master server a unique id from 1 to 255
	```
	sudo vi /etc/zookeeper/conf/myid  #1
	```

+ Specify all zookeeper server in the following file(server.1=171.0.0.2:2888:3888)
	```
	sudo vi /etc/zookeeper/conf/zoo.cfg
	```

+ Start zookeeper(java 11 or more)
	```
	cd /usr/share/zookeeper/bin
	./zkServer.sh status
	./zkServer.sh start
	```

## 3. Install Marathon

+ Setup deb repo
	```
	sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF
	DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]')
	CODENAME=xenial
	````
+ Add repo
	```
	echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" | sudo tee /etc/apt/sources.list.d/mesosphere.list
	sudo apt-get -y update
	```
+ Check version and install
	```
	apt-cache policy marathon
	sudo apt-get install marathon
	```

+ Marathon doesn’t read command line arguments from config file anymore so specify them in default file.
	```
	sudo vi /etc/default/marathon 
	```
	with conf

	```
	MARATHON_MESOS_USER=root
	MARATHON_MASTER="zk://172.0.0.2:2181/mesos"
	MARATHON_ZK="zk://172.0.0.2:2181/marathon"
	MARATHON_HOSTNAME="172.0.0.2"
	```
+ Start marathon (runs on java 8)
	```
	sudo service marathon restart
	```

MESOS INSTALLATION FROM .DEB
http://mesos.apache.org/documentation/latest/building/

CLUSTER SETUP 
https://www.bogotobogo.com/DevOps/DevOps_Mesos_Install.php

# VM2 [Mesos slave and Docker ]
## Mesos slave:-
+ Install jdk version 8 and 16 (dependencies)
	```
	sudo apt-get update
	sudo apt install openjdk-16-jre-headless
	sudo apt install openjdk-8-jre-headless
	```

+ Install messos(With java 16 as default)
	```
	update-alternatives --config java
	```
+ Get the env ready
	```
	sudo apt-get -y install build-essential python3-dev python3-six python3-virtualenv libcurl4-nss-dev libsasl2-dev 	libsasl2-modules maven libapr1-dev libsvn-dev zlib1g-dev iputils-ping
	sudo apt-get install libcurl4-openssl-dev
	```
+ Install mesos from .deb file
	```
	sudo dpkg -i mesos-1.9.0-0.1.20200901105608.deb
	```
	+ apt-cache policy mesos (to confirm the installation)

+ Make sure the mesos-master doesn't start on boot
	```
	echo manual | sudo tee /etc/init/mesos-master.override
	```
	```
+ Setup ip and hostname of mesos-slave
	```
	sudo nano /etc/mesos-slave/ip				# 172.0.0.6
	sudo nano /etc/mesos-slave/hostname		# 172.0.0.6
	```

+ Configure ZooKeeper connection info to point to master servers:
	```
	sudo nano /etc/mesos/zk			# zk://172.0.0.2:2181/mesos
	```


# Week 6 :
## RMQ
+ Install and configure 1 node RMQ cluster version 3.7.9
+ The RMQ cluster should be on TLS and have a username/password
+ Data should be persisted on disk
+ Add 2 more nodes to the cluster without restarting RMQ service on first one
+ Create a vhost and a user with read-write permissions to the vhost
+ Create 2 queues (DATA, DATA_SIDELINE) on the above created vhost
+ Create a publisher and consumer for the DATA queue, the messages which were not consumed by the consumer should move to the + DATA_SIDELINE queue after a specific time.
+ Stop the consumer
+ Publish 100 messages to DATA queue
+ The 100 messages should automatically get moved to DATA_SIDELINE queue
+ Stop the publisher
+ Take a dump of the messages in DATA_SIDELINE queue using RMQ API/curl
+ Delete the messages from the DATA_SIDELINE queue using RMQ API/curl
+ Push the messages to DATA queue using RMQ API/curl
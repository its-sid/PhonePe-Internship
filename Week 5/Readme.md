# Week 5 Tasks:
1. Introduction to Ansible:
    + Intent: Learn the fundamentals of Ansible 
    + Task: Run a shell command on 3 VMs from your local machine and save its output in a file locally.

2. Galera cluster setup using Ansible:
    + Intent: Explore different ansible modules. Design automation 
    + Tasks: Write a ansible playbook to automate the entire setup of a galera cluster. 
    + The playbook should include:
        + Setup of 3 node galera cluster
        + Demote the 3rd node to an async slave. 
        + Provisions to uninstall/destroy the cluster 
        + The playbook should be idempotent (i.e running the playbook multiple times shouldn't affect the setup)
        + The cluster once setup should have only 2 new users - one for you with read/write permissions and another called monitoring with only read permissions.
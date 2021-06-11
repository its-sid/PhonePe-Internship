1. On a standalone VM, install MariaDB 10.5.6 and create a user same as your laptop login user then, create database Nginx and restore the SQL file attached in the mail.
+ To install MariaDB we will use 10.5.6 version repository:
    ```
    sudo add-apt-repository 'deb [arch=amd64] https://archive.mariadb.org/mariadb-10.5.6/repo/ubuntu/ focal main'
    ```
+ After adding repo we can install mariaDB using:
    ```
        sudo apt install mariadb-server mariadb-client
    ```
+ To create a user we will use:
    ```
        CREATE USER 'newuser' IDENTIFIED BY 'password';
    ```
+ Give permission to a user(must be login from root user):
    ```
        GRANT ALL PRIVILEGES ON * . * TO 'newuser';
    ```
+ Login to a user:
    ```
        mysql -u newuser -p
    ```
+ To create a database Ngnix;
    ```
        CREATE DATABASE Nginx;
    ```
+ Restore data to a database from a file(On Command line):
    ```
         mysql db_name < backup-file.sql
    ```

2. On an another VM install MariaDB and configure it as the slave of the MariaDB installed in above step.

   + Install mariaDb and create user on slave VM (same as step 1)

   +  On master VM we have to configure /etc/mysql/mariadb.conf.d/50-server.cnf file
        ```
        set bind Address;
        set server-id
        and address of log_bin
        ```

Restart mariaDb using ``` systemctl restart mariadb ```

+ To grant the replication slave privilege to this user we can use(in root user):
```
    GRANT REPLICATION SLAVE ON *.* TO 'user_name';
```

+ Write the privileges using:
```
    FLUSH PRIVILEGES;
```

+ We can check the master status using
```
    show master status;
```

+ On slave VM we have to configure /etc/mysql/mariadb.conf.d/50-server.cnf file
```
    set bind Address;
    set server-id
    and address of log_bin
```

+ Restart mariaDb using systemctl restart mariadb
```
    Stop the existing slave to configure there master
```
+ Now we will assign master using command:
```
CHANGE MASTER TO MASTER_HOST = 'your-master-host-ip', MASTER_USER = 'user_name', MASTER_PASSWORD = 'your-password', MASTER_LOG_FILE = 'mysql-bin.000001', MASTER_LOG_POS = 313;
```

#log file and log position can be found in show master status in master VM
+ start the slave using :
```
    start slave;
```

+ Now we have master slave configuration we can check it using 
```
SHOW MASTER STATUS;
```

Convert this setup into Master Master replication b/w both the VMs.

To convert the master slave into master master we have to perform the same operations as in 3rd step :
    we have to grant repliction privilege to the VM WHich acted as slave before and assign master to the VM which acted as master

    For master master replication we will configure each VM to act as a master and slave both (steps to be followed are same in step 3 but shold be performed on both VMs)

# Queries:
+ summary for the day/week/month:<br />
    + highest requested host<br />
    + highest requested upstream_ip<br />
    + highest requested path (upto 2 subdirectories ex: /check/balance)<br />
    ```
    select t2.* from (
        select a, max(totalwins) as totalwins from (
            select STR_TO_DATE(time,'%d\/%b\/%Y') as a, host, count(*) as totalwins
            from ngnix_access_log t
            group by a, host
            ) s1 group by a) 
    w join
    (select STR_TO_DATE(time,'%d\/%b\/%Y') as a, host, count(*) as totalwins
        from ngnix_access_log t
        group by a, host
        ) t2 on t2.a = w.a and t2.totalwins = w.totalwins;
    ```
+ total requests per status code (Ex: count of requests returning 404/401/502/504/500/200)<br />
    ```
    SELECT statusCode, COUNT(statusCode) AS number FROM ngnix_access_log WHERE statusCode LIKE '404'; 
    SELECT statusCode, COUNT(statusCode) AS number FROM ngnix_access_log WHERE statusCode LIKE '401';
    SELECT statusCode, COUNT(statusCode) AS number FROM ngnix_access_log WHERE statusCode LIKE '502';
    SELECT statusCode, COUNT(statusCode) AS number FROM ngnix_access_log WHERE statusCode LIKE '504';
    SELECT statusCode, COUNT(statusCode) AS number FROM ngnix_access_log WHERE statusCode LIKE '500';
    SELECT statusCode, COUNT(statusCode) AS number FROM ngnix_access_log WHERE statusCode LIKE '200';
    ```

+ top 5 requests by upstream_ip<br />
    ```
    select upstream_ip_port, COUNT(upstream_ip_port) AS number FROM ngnix_access_log GROUP BY upstream_ip_port ORDER BY COUNT(upstream_ip_port) DESC LIMIT 5;
    ```
+ top 5 requests by host<br />
    ```
    select host, COUNT(host) AS number FROM ngnix_access_log GROUP BY host ORDER BY COUNT(host) DESC LIMIT 5;
    ```
+ top 5 requests by bodyBytesSent<br />
    ```
    select bodyBytesSent, COUNT(bodyBytesSent) AS number FROM ngnix_access_log GROUP BY bodyBytesSent ORDER BY COUNT(bodyBytesSent) DESC LIMIT 5;
    ```
+ top 5 requests by path (upto 2 subdirectories ex: /check/balance)<br />
    ```
    select substring_index(path,"/",3), count(*) from ngnix_access_log group by substring_index(path,"/",3) order by count(*) desc limit 5; 
    ```
+ top 5 requests with the highest response time<br />
    ```
    select host,ip,responseTime FROM ngnix_access_log GROUP BY responseTime ORDER BY responseTime DESC LIMIT 5;
    ```
+ get top 5 requests returning 200/5xx/4xx per host<br />
    ```
    select host,statusCode,count(*) from ngnix_access_log where statusCode like 200 or statusCode like "5%" or statusCode like "4%" group by host order by count(*) desc limit 10;
    ```
+ get all the requests taking more than 2/5/10 secs to respond.<br />
    ```
    select * from ngnix_access_log where responseTime>10;
    select * from ngnix_access_log where responseTime>5;
    select * from ngnix_access_log where responseTime>2;
    ```
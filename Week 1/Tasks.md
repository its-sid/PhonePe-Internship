T1 : Run Ubuntu Focal ISO on Virtual Box

    -> Download Virtual box.
         Link "https://www.virtualbox.org/wiki/Downloads"

    -> Download Ubuntu Server Iso 
        Link "https://releases.ubuntu.com/20.04/ubuntu-20.04.2-live-server-amd64.iso"

    -> Install Virtual box

    -> Create a new virtual machine in VB with configuration:
            > Name "ubuntu"
            > Type "Linux"
            > Ram size = 1024MB (Minimum required)
            > Create 4 Virtual hard drive 10GB each (In storage config)
            > Enable Bridged Connection in network tab (to communicate to host system)

    -> Start the Virtual Machine

    -> Give location on ubuntu server iso during machine startup

    -> Make a user with password


T2 : Create users and groups

    -> To create user commands used are:

            sudo adduser "username"
             
        # replace "username" with the name you want
        > provide root password
        > Enter details for new user(password,name,email)

    -> To create group commands used are:

            sudo addgroup "group_name"

        #replace "group_name" with the name you want

    ->To add user to a group commands used are:
 
            sudo usermod -a -G "group_name" "user_name"

         # replace "user_name" and group_name with the user and group you want
          -a is used to append 
          -G refers to secondary group
          -g can be used to change primary group

T3 : Create LVM , make a xfs filesystem and mount it on /data directory

    -> To create lvm we start with available virtual drives we added during configuration on VB

    -> To check the available disk we will use fdisk or lvmdiskscan
    
            sudo fdisk -l

                or

            sudo lvmdiskscan

        > it will list all available drives
        > most drives start with sd (sda,sdb,sdc)
        > usually sda has system partition
        > we will use sdb and sdc

    -> LVM consists of 3 main parts:
        > Physical Volumes (Basically disks)
        > Volume Groups (Basically a pool made of multiple physical volumes or single)
        > Logical Volumes (basicall a partition which takes the memory from volume group )

    -> Create Physical volumes for lvm:

        > command to create physical volume (pv):

            sudo pvcreate /dev/sdb /dev/sdc

        # sdb and sdc are disk we added

        > To verify physical volume is created we will use:

            sudo pvs
    
    -> Create Volume group(vg) using physical volumes:

        > command to create volume group:

            sudo vgcreate VolGrp_name /dev/sdb /dev/sdc

        # replace "VolGrp_name" with the name you want
        # size of volume group will be the sum of the disks

        > To verify physical volume are assigned to volume group we can use:

           sudo pvs

        > To check all volume groups we can use:

           sudo vgs

    -> Create logical volume from volume group:

        > command used are:

            sudo lvcreate -L 10G -n LogicalVol_name VolGrp_name

        # replace LogicalVol_name and VolGrp_name with appropriate logicalgroup name and volumegroup name
        # -L is used to specify the size
        # -l can be used to specify the size in extents

        > To check all logical volumes we can use:

            sudo lvs

        # logical devices are available in 2 places we can access them at:
        # "/dev/volumegrp_name/logicalvolume_name" and
        # "/dev/mapper/volume_group_name-logical_volume_name"
        
    -> Create xfs filesystem for our logical device:

        > commands used are:

            sudo mkfs.xfs /dev/VolGrp_name/LogicalVol_name

    -> Creating mount point at /data for logical volume:

        > commands used are:

            sudo mkdir -p /data/LogicalVol_name

    -> Mount logicalVol to /data:

        > commands used are:

            sudo mount /dev/LVMVolGroup/LogicalVol_name /data/LogicalVol_name

    -> To make mount persists across reboots we will append a line in file /etc/fstab which mounts all devices for system at startup

        /dev/LVMVolGroup/logicalVol_name /data/LogicalVol_name xfs defaults,nofail 0 0


    -> To extend lvm 
    
        > we need to assign a new physical volume

        > Use physical volume to expand volume group

            vgextend VolumeGrp_name -vg /dev/sdd

        > extend logical volume from volume group:

            lvextend -l+100%FREE /dev/VolGrp_name/logicalVol_name

        # -l+100%FREE is used to specify all free extents


T4 : Run a HTTP server. Make sure that the server starts automatically when the system starts.

    -> We will use Apache server

        > To install Apache server commands are:

            sudo apt update 
            suso apt install apache2

        # our server is in running state 

        > To confirm if its running we can  use:

            sudo systemctl status apache2

        > We can access our server by ip address on vB

        > To find the IP of virtual box we will use:

            hostname -I

        # Check if u have switched on your bridged connection in virtual box

        > To automatically start apache server :

            sudo update-rc.d apache2 defaults

        > We can ping and check if the server is active:

            ping ip_address


T5 :  Login via a private key and not a password.

    -> We 2 machines for ssh the server and the client so we will make another basic virtual machine and call it client

    -> we use client to generate private/public key pair

        ssh-keygen -t rsa

    -> by default private key will be saved in /home/user_client/.ssh/id_rsa and public key will be saved in /home/user_client/.ssh/id_rsa.pub

    ->On server machine make sure you have ssh installed ssh or we can install it using:

        sudo apt update
        sudo apt install openssh-server

    ->we need to transfer public key to server system in /home/user/.ssh/authorized_keys and set permission to 600 for file authorized_key and 700 to .shh dir

        > we can use:
            sudo chmod 700 /home/user/.shh

            and 

            sudo chmod 600 /home/user/.ssh/authorized_keys
    
    -> We can now login using ssh on remote machine

    -> we need to know the IP address of server machine , we can use hostname to know the IP:

        hostname -I

    ->to access the server machine using client machine we use commmand:

        ssh username@serverhost_ip

T6 : Mount /var/log on a separate mount point.

    -> To create a seperate mount point for /var/log we should remove the dir log which already exists in /var and copy the contents of log to the new mount point

    ->First create a new logical drive as mentioned in task t3(we assume the location of new logical drive is /dev/volumegrp_name/logicalvolume_name)

    -> Create a tmp mount point and mount the logical volume to the tmp mount point

        sudo mkdir -p /mnt/tmp
        sudo mount /dev/LVMVolGroup/LogicalVol_name /mnt/tmp

    -> Copy the contents of /var/log to new drive:

        cp -apx /var/* /mnt/tmp

    ->Before moving or removing from /var we need to stop the process which are using /var:

        service rsyslog stop

    -> remove/rename the log dir :

        mv /var /var.old

    -> make new dir /var:

        mkdir /var

    -> mount the drive to /var:

        sudo mount /dev/LVMVolGroup/LogicalVol_name /var

    -> Add entry to fstab to mount on boot:

        /dev/LVMVolGroup/logicalVol_name /var xfs defaults,nofail 0 0

    -> Start the log service :

        service rsyslog start





References :

https://www.guru99.com/file-permissions.html#:~:text=Linux%20divides%20the%20file%20permissions,ownership%20of%20a%20file%2Fdirectory.

https://www.digitalocean.com/community/tutorials/an-introduction-to-lvm-concepts-terminology-and-operations

https://www.tutorialspoint.com/how-to-increase-the-size-of-a-linux-lvm-by-adding-a-new-disk

https://linoxide.com/file-system/create-mount-extend-xfs-filesystem/

https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys

https://www.networkworld.com/article/3514607/setting-up-passwordless-linux-logins-using-publicprivate-keys.html

https://www.suse.com/support/kb/doc/?id=000018399


        
         

    

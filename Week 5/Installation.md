* Install ansible using homebrew for mac
    ```bash
    $ brew install ansible
    ```
* Test the Ansible's ssh connection through ping option
    ```bash
    $ ansible all -m ping
    ```
    and if this returns SUCCESS for each node or returns "ping": "pong" for each node, then the connection is successful.
* Run the ansible-playbook command
    ```bash
    ansible-playbook -u root pb.yml -k
    ```
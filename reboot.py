import paramiko
hosts = {"10.115.210.23": {
    "username": "cirros",
    "password": "gocubsgo"}}
port = 22

def rebootMachine(hostname, username, password=None):
    def sshexec(command):
        print("executing "+command)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        w, r, e = ssh.exec_command(command)
        if e:
            print(e)
    print("Rebooting machine")
    sshexec('sudo -i reboot')

def hostsReboot():
    for key, val in hosts.items():
        print("executing setup machine for " + key)
        rebootMachine(key, val['username'])


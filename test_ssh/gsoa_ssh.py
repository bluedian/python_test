#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Guos
import paramiko
import threading
import time
import requests
import json


class gsoa_ssh():
    def __init__(self):
        self.server_ip = ''
        self.server_port = 22
        self.server_user = 'root'
        self.server_pass = 'Guosong.1982'
        self.server_keys = 'tx_guosonggs02'
        pass

    def setServerIP(self, IP):
        pass

    def shell_cmd(self, ssh, commandstr):
        serverSSH = ssh
        stdin, stdout, stderr = serverSSH.exec_command(commandstr)
        stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
        # reRead = formatReadByte(stdout.read())
        reRead = stdout.read()
        return reRead

    def sshclient_execmd_pass(self, hostname, port=22, username='root', password='Guosong.1982'):
        paramiko.util.log_to_file("paramiko.log")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=hostname, port=port, username=username, password=password)

            stdin, stdout, stderr = ssh.exec_command('hostname')
            stdin.write("Y")
            reRead = formatReadByte(stdout.read())
            return ssh, reRead
        except:
            ssh.close()
            return False, 'False'

    def sshclient_execmd_key(self, hostname, port=22, username='root', pkey='tx_guosonggs02'):
        paramiko.util.log_to_file('paramiko.log')
        key = paramiko.RSAKey.from_private_key_file(pkey, password='******')  # 有解密密码时,
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.load_system_host_keys() #如通过known_hosts 方式进行认证可以用这个,如果known_hosts 文件未定义还需要定义 known_hosts
        try:
            ssh.connect(hostname=hostname, port=port, username=username, pkey=key)  # 这里要 pkey passwordkey 密钥文件
            stdin, stdout, stderr = ssh.exec_command('hostname')
            stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
            reRead = formatReadByte(stdout.read())
            return ssh, reRead
        except:
            ssh.close()
            return False, 'False'

    def ssh_connent_key(self, hostname, port=22, username='root', pkey='tx_guosonggs02'):
        paramiko.util.log_to_file('paramiko.log')
        key = paramiko.RSAKey.from_private_key_file(pkey, password='******')  # 有解密密码时,
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=hostname, port=port, username=username, pkey=key)
            if ssh:
                return ssh
            print('连接异常' + hostname)
            return
        except:
            return

    def ssh_connent_pass(self, hostname, port=22, username='root', password='Guosong.1982'):
        paramiko.util.log_to_file('paramiko.log')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=hostname, port=port, username=username, password=password)
            if ssh:
                return ssh
            print('连接异常' + hostname)
            return
        except:
            return

    def ssh_close(self, ssh):
        ssh.close()


def formatReadByte(b_byte):
    tostr1 = str(b_byte)
    # print("tostr and len:"+tostr1+str(len(tostr1)))
    if len(tostr1) == 3:
        return "nono"
    tostr2 = tostr1[2:-3]
    tostr3 = tostr2.replace('\\n', ',')
    return tostr3


if __name__ == '__main__':
    print('Start----')

    ssh_link = gsoa_ssh()
    ssha, sshb = ssh_link.sshclient_execmd_pass('192.168.1.123', username='pi', password='raspberry')
    print(ssha)
    print(sshb)

    comdrun = ssh_link.shell_cmd(ssha, 'ls -l')
    comdrun = str(comdrun)
    for item in comdrun.split('\\n'):
        print(item)

    ssh_link.ssh_close(ssha)

# from paramiko import SSHClient

# client = SSHClient()
# # client.load_system_host_keys()
# # client.load_host_keys('~/.ssh/known_hosts')
# # client.set_missing_host_key_policy(AutoAddPolicy())

# client.connect('192.168.0.106', username='bitthal', password='ladiwal0909')
# client.exec_command('ls')
# client.close()

import asyncssh
import asyncio
import getpass
async def execute_command(host, command = 'ls', username = 'bitthal', password = 'ladiwal0909'):
    async with asyncssh.connect(host, username = username, password= password) as connection:
        connection
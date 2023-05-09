from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '172.16.7.1',
    'username': 'admin',
    'password': 'cisco123',
    'port' : 22,          # optional, defaults to 22
}

net_connect = ConnectHandler(**cisco_881)

output = net_connect.send_command('show running-config')
print(output)


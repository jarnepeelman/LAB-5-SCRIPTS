from netmiko import ConnectHandler

# Apparaat parameters
device = {
    "device_type": "cisco_ios",
    "ip": "172.16.7.1",
    "username": "admin",
    "password": "cisco123",
    "secret": "cisco",
}

# Maak een SSH-verbinding met het apparaat
ssh = ConnectHandler(**device)

ssh.enable() # Enable method
ssh.config_mode() # Global config mode

config_commands = [
    'interface GigabitEthernet0/1',
    'Description Verbinding met het internet',
    'no shutdown',
    'interface GigabitEthernet0/0',
    'Description Verbinding met sw03',
    'no shutdown'
]

output = ssh.send_config_set(config_commands)
print(output)

print('Closing Connection')
ssh.disconnect()


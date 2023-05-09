from netmiko import ConnectHandler

# Apparaat parameters
device = {
    "device_type": "cisco_ios",
    "ip": "172.16.7.1",
    "username": "admin",
    "password": "cisco123",
}

# Maak een SSH-verbinding met het apparaat
ssh = ConnectHandler(**device)

# Voer meerdere show commands uit
output1 = ssh.send_command("show running-config")
output2 = ssh.send_command("show interfaces")
output3 = ssh.send_command("show version")

# Print de uitvoer van alle show commands
print(output1)
print(output2)
print(output3)

# Sluit de SSH-verbinding
ssh.disconnect()


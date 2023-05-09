from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip": "172.16.7.1",
    "username": "admin",
    "password": "cisco123",
}

# Establish SSH connection
ssh = ConnectHandler(**device)

# Send show command and save output to a file
command = "show interfaces"
output = ssh.send_command(command)
with open("output.txt", "w") as file:
    file.write(output)

# Close SSH connection
ssh.disconnect()


from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "172.16.7.1",
        "username": "admin",
        "password": "cisco123",
        "secret": "cisco"
    },
    {
        "device_type": "cisco_ios",
        "ip": "172.16.7.7",
        "username": "admin",
        "password": "administrator",
	"secret" : "cisco"
    }
]

config_commands = [
    'interface GigabitEthernet0/1',
    'description Dit is een poort'
]

for device in devices:
    print(f"Connecting to {device['ip']}...")
    ssh = ConnectHandler(**device)
    output = ssh.send_command("show interfaces")
    print(output)
    ssh.disconnect()
    print(f"Disconnected from {device['ip']}")

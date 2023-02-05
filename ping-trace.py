import subprocess

ip_address = input("Enter an IP address: ")

ping = subprocess.Popen(["ping", "-c", "3", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ping_output = ping.communicate()[0].decode("utf-8")

tracert = subprocess.Popen(["tracert", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
tracert_output = tracert.communicate()[0].decode("utf-8")

print("Ping output:\n" + ping_output)
print("Tracert output:\n" + tracert_output)

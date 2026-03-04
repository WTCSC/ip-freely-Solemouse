import sys
from pythonping import ping

def gethosts(ip_given):
    splitip = ip_given.split('/')
    ip = splitip[0].split('.')
    mask = int(splitip[1])
    hosts = []

    if mask == 32:
        return [splitip[0]]
    elif mask >= 24:
        part1 = ip[0]
        part2 = ip[1]
        part3 = ip[2]
        part4_base = int(ip[3]) + 1
        for part4 in range(part4_base, 256):
            hosts.append(f"{part1}.{part2}.{part3}.{part4}")
    elif mask >= 16:
        part1 = ip[0]
        part2 = ip[1]
        part3_base = int(ip[2])
        for part3 in range(part3_base, 256):
            for part4 in range(1, 255):
                hosts.append(f"{part1}.{part2}.{part3}.{part4}")
    elif mask >= 8:
        part1 = ip[0]
        part2_base = int(ip[1])
        for part2 in range(part2_base, 256):
            for part3 in range(1, 255):
                for part4 in range(1, 255):
                    hosts.append(f"{part1}.{part2}.{part3}.{part4}")
    else:
        part1_base = int(ip[0])
        for part1 in range(part1_base, 256):
            for part2 in range(1, 255):
                for part3 in range(1, 255):
                    for part4 in range(1, 255):
                        hosts.append(f"{part1}.{part2}.{part3}.{part4}")
    return hosts

subnet = sys.argv[1]
hosts = gethosts(subnet)

for host in hosts:
    try:
        response_list = ping(host, count=4)
        if response_list.success():
            print(f'{host} is up, Response: {response_list.avg_rtt} ms')
        else:
            print(f'{host} did not respond')
    except Exception as e:
        print(f"Error: {e}")

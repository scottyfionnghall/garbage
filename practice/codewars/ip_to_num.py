def ip_to_num(ip):
    num = ip.split('.')
    num = ['{:08b}'.format(int(i)) for i in num]
    num = ''.join(num)
    return int(num,2)

def num_to_ip(num):
    ip = '{:032b}'.format(int(num))
    ip = str(ip)
    result = []
    for i in range(0,31,8):
        result.append(ip[i:i+8])
    result = [int(i,2) for i in result]
    result = [str(i) for i in result]
    return('.'.join(result))
print(num_to_ip(3232235777))
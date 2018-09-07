
def get_block_size(cidr):
    return 2 ** (abs(8 - (cidr % 8)))


def fix_output(array):
    # .join needs strings, we had ints for math, easily converts it
    return [str(x) for x in array]


def check_octets(octets):
    # input validation for octets so shit doesn't break
    ret = []  # return values
    if len(octets) != 4:
        raise ValueError(f"octet data incorrect length -- {len(octets)}")
    for index in range(len(octets)):
        octet_value = octets[index]
        if not type(octet_value) == int:
            if octet_value.isnumeric():
                octet_value = int(octet_value)
            else:
                raise TypeError(f"octet data in octet {index + 1} incorrect -- {type(octet_value)}")
        if octet_value not in range(225) or octet_value == 127:
            print(type(octet_value))
            raise ValueError(f"octet data value at index {index} out of scope -- {octet_value}")
        ret.append(octet_value)

    return ret


def check_cidr(cidr):
    # input validation for cidr so shit doesn't break
    if not type(cidr) == int:
        raise TypeError(f"cidr type incorrect -- {type(cidr)}")
    if cidr < 8 or cidr > 32:
        raise ValueError(f"cidr out of range -- {cidr}")


def check_classful(class_, cidr):
    # making sure the cidr is in the right range for the class
    if class_ == 'a' and cidr not in range(8, 17):
        raise ValueError(f"cidr out of range for class {class_} -- {cidr}")
    elif class_ == 'b' and cidr not in range(16, 25):
        raise ValueError(f"cidr out of range for class {class_} -- {cidr}")
    elif class_ == 'c' and cidr not in range(24, 33):
        raise ValueError(f"cidr out of range for class {class_} -- {cidr}")


def main():
    # take the ip address as input
    ipaddress = input("Enter the IP address you'd like to subnet: ")

    # get the octets and cidr
    if "/" in ipaddress:
        defaulted = False
        cidr = int(ipaddress.split('/')[1])
        octets = ipaddress.split('/')[0]
    else:
        cidr = 0
        defaulted = True
        octets = ipaddress

    octets = check_octets(octets.split('.'))
    octet1, octet2, octet3, octet4 = octets

    # class and (maybe) default cidrs
    if octet1 in range(0, 127):
        class_ = 'a'
        cidr = 8 if defaulted else cidr  # if defaulted, cidr = 8, else it stays the same
    elif octet1 in range(128, 192):
        class_ = 'b'
        cidr = 16 if defaulted else cidr
    elif octet1 in range(192, 225):
        class_ = 'c'
        cidr = 24 if defaulted else cidr

    # cidr input validation
    check_cidr(cidr)

    # checks for cidr outside of classful range (I have good words)
    check_classful(class_, cidr)

    # block size
    block_size = get_block_size(cidr)

    # ternary operators to avoid taking seven lines to do this, which i then use to comment to explain ternary operators
    # if class is c, default cidr is 24
    # python really needs switch cases
    dcidr = 24 if class_ == 'c' else 16 if class_ == 'b' else 8 if class_ == 'a' else 0
    
    if class_ == 'c':
        dcidr = 24
    elif class_ == 'b':
        dcidr = 16
    elif class_ == 'a':
        dcidr = 8
    else:
        dcidr = 0

    # hosts, nets
    nets = (2 ** (cidr - dcidr))
    hosts = (2 ** (32 - cidr) - 2)

    # network id
    net_octet1, net_octet2, net_octet3, net_octet4 = octets

    if class_ == 'a':
        net_octet2 = block_size * (net_octet2 // block_size)
        net_octet3 = 0
        net_octet4 = 0
    elif class_ == 'b':
        net_octet3 = block_size * (net_octet3 // block_size)
        net_octet4 = 0
    elif class_ == 'c':
        net_octet4 = block_size * (net_octet4 // block_size)

    net_id = net_octet1, net_octet2, net_octet3, net_octet4

    # broadcast id

    bcst_octet1, bcst_octet2, bcst_octet3, bcst_octet4 = octets

    if class_ == 'a':
        bcst_octet2 = block_size * ((bcst_octet2 // block_size) + 1) - 1
        bcst_octet3 = 255
        bcst_octet4 = 255
    elif class_ == 'b':
        bcst_octet3 = block_size * ((bcst_octet3 // block_size) + 1) - 1
        bcst_octet4 = 255
    elif class_ == 'c':
        bcst_octet4 = block_size * ((bcst_octet4 // block_size) + 1) - 1

    broadcast_id = bcst_octet1, bcst_octet2, bcst_octet3, bcst_octet4

    # return the info

    octets = fix_output(octets)
    net_id = fix_output(net_id)
    broadcast_id = fix_output(broadcast_id)

    print(f"original IP: {'.'.join(octets)}")
    print(f"network ID: {'.'.join(net_id)}")
    print(f"broadcast ID: {'.'.join(broadcast_id)}")
    print(f"CIDR: {cidr} \nBlock size: {block_size}\nClass: {class_.upper()}")
    print(f"Hosts: {hosts} \nNetworks: {nets}")
# end of main

if __name__ == '__main__':
    main()

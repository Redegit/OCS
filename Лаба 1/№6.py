def ip_convert(ip):
    ip_list = ip.split('.')
    new_ip = []
    if len(ip_list) != 4:
        raise Exception("IP-адрес введён некорректно")
    elif min(len(i) == 8 for i in ip_list):
        for i in ip_list:
            try:
                new_ip.append(str(int(i, 2)))
            except ValueError:
                raise Exception("Неверное значение для бинарного числа")
        return '.'.join(new_ip)
    elif min([1 <= len(i) <= 3 for i in ip_list]):
        try:
            if int(max(ip_list)) > 255:
                raise Exception("Превышено максимальное значение по крайней мере одного октета")
        except ValueError:
            raise Exception("Неверное значение для десятичного числа")
        for i in ip_list:
            new_ip.append(f"{str(bin(int(i)))[2:]:0>8}")
        return '.'.join(new_ip)
    else:
        raise Exception("IP-адрес введён некорректно")


def ip_info(ip):
    try:
        o1 = int(ip.split('.')[0])
    except ValueError:
        raise Exception("Ошибка в IP-адресе")
    if 0 <= o1 <= 127:
        return {"network_class": "A", "start": "0.0.0.0", "end": "127.255.255.255", "mask": "255.0.0.0"}
    elif 128 <= o1 <= 191:
        return {"network_class": "B", "start": "128.0.0.0", "end": "191.255.255.255", "mask": "255.255.0.0"}
    elif 192 <= o1 <= 223:
        return {"network_class": "C", "start": "192.0.0.0", "end": "223.255.255.255", "mask": "255.255.225.0"}
    elif 224 <= o1 <= 239:
        raise Exception("IP-адрес принадлежит классу D")
    elif 240 <= o1 <= 255:
        raise Exception("IP-адрес принадлежит классу E")
    else:
        raise Exception("Ошибка в IP-адресе")


def add_points_bin(bin):
    new_bin = ''
    for e, j in enumerate(bin, 1):
        new_bin += j + '.' if e % 8 == 0 else j
    return new_bin.rstrip('.')


network_bit = {"A": 8, "B": 16, "C": 24}

ip = input("IP-адрес: ")
subnetworks_number = int(input("Количество подсетей: "))
hosts_number = int(input("Количество хостов: "))
ip_inf = ip_info(ip)
# N + S + H = 32
N = network_bit[ip_inf["network_class"]]
S = 0
while True:
    if 2 ** S >= subnetworks_number:
        break
    else:
        S += 1
H = 0
while True:
    if 2 ** H - 2 >= hosts_number:
        break
    else:
        H += 1

print("---\nКласс: {}\nНачальный адрес: {}\nКонечный адрес: {}\nМаска класса: {}\n---".format(*ip_inf.values()))

bit_for_hosts = [_ for _ in range(H, 32 - N - S + 1)]
if not bit_for_hosts:
    raise SystemExit("Задача не имеет решения")
for i, h in enumerate(bit_for_hosts, 1):
    M = 32 - h  # количество единиц в маске
    mask = ''
    for _ in range(32):
        if M > 0:
            mask += '1'
        else:
            mask += '0'
        M -= 1
    mask = add_points_bin(mask)
    print(f"Маска{i if len(bit_for_hosts) != 1 else ''}: {ip_convert(mask.rstrip('.'))}")
    ip_number = 2**h
    print(f"IP-адресов в сети: {ip_number}\nДоступно IP-адресов: {ip_number - 2}")
    print(f"Стек первых{' 5' if ip_number >= 5 else ''} допустимых IP-адресов: ")
    _ip = ip_convert(ip).replace(".", "")
    for _ in range(5):
        if _ >= ip_number:
            break
        temp_ip = f"{_ip[:32 - h]}{int(bin(_)[2:]):0>{h}}"
        temp_ip = add_points_bin(temp_ip)
        print(ip_convert(temp_ip))
    print(f"Стек последних{' 5' if ip_number >= 5 else ''} допустимых IP-адресов: ")
    max_host = int('1' * h, 2)
    for _ in range(5):
        if _ >= ip_number:
            break
        temp_ip = f"{_ip[:32 - h]}{int(bin(max_host - _)[2:]):0>{h}}"
        temp_ip = add_points_bin(temp_ip)
        print(ip_convert(temp_ip))
    print("---")
ex = input("Нажмите ENTER, чтобы выйти: ")

def ip_convert():
    ip = str(input("Введите IP-адрес: "))
    if ip.lower() == "exit":
        return
    ip_list = ip.split('.')
    new_ip = []
    if len(ip_list) != 4:
        print("IP-адрес введён некорректно")
        return ip_convert()
    elif min(len(i) == 8 for i in ip_list):
        for i in ip_list:
            try:
                new_ip.append(str(int(i, 2)))
            except ValueError:
                print("Неверное значение для бинарного числа")
                return ip_convert()
        print('.'.join(new_ip))
    elif min([1 <= len(i) <= 3 for i in ip_list]):
        try:
            if int(max(ip_list)) > 255:
                print("Превышено максимальное значение по крайней мере одного октета")
                return ip_convert()
        except ValueError:
            print("Неверное значение для десятичного числа")
            return ip_convert()
        for i in ip_list:
            new_ip.append(f"{str(bin(int(i)))[2:]:0>8}")
        print('.'.join(new_ip))
    else:
        print("IP-адрес введён некорректно")
        return ip_convert()
    return ip_convert()


ip_convert()

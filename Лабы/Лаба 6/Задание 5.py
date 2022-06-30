from tabulate import tabulate


def find_shortest(lst, time):
    lst = sorted(lst, key=lambda p: p.time)
    for i in lst:
        if time >= i.enter_time and i.time != 0:
            return i


def sjf():
    while True:
        try:
            number_of_processes = int(input("Количество процессов: "))
            break
        except:
            print("Некорректный ввод\n")
    proc_list = []
    i = 0
    while True:
        try:
            choice = int(input("Алгоритм вытесняющий? (1/0) > "))
            assert 0 <= choice <= 1
            is_displacing = True if choice else False
        except:
            print("Некорректный ввод")
        else:
            break

    while i < number_of_processes:
        try:
            if is_displacing:
                enter_time = int(input(f"Время появления p{i}: "))
                time = int(input(f"Время исполнения p{i}: "))
            else:
                time = int(input(f"Время исполнения {i}-го процесса: "))
                enter_time = 0
            assert 1 <= time
            assert enter_time >= 0
            proc_list.append(Process(time, enter_time))
        except:
            print("Некорректный ввод")
        else:
            i += 1

    total_time = sum([i.time for i in proc_list]) + min([proc.enter_time for proc in proc_list])
    table = [[i for i in range(1, total_time+1)], *[[] for _ in range(number_of_processes)]]
    pointer = 0
    total_waiting = 0
    while pointer < total_time:
        proc = find_shortest(proc_list, pointer)
        for i in range(len(table)-1):
            if proc_list[i] == proc:
                table[i+1].append("И")
                proc.time -= 1
            elif proc_list[i].enter_time <= pointer and proc_list[i].time != 0:
                table[i+1].append("Г")
                total_waiting += 1
            else:
                table[i + 1].append("")
        pointer += 1
    table[0].insert(0, "Время")
    for i in range(1, len(table)):
        table[i].insert(0, f"p{i-1}")
    print()
    print(tabulate(table, tablefmt='pipe'))
    print(f"Среднее время ожидания: {((total_waiting) / number_of_processes)}")
    return


class Process:
    def __init__(self, time, enter_time=0):
        self.time = time
        self.enter_time = enter_time
 

sjf()

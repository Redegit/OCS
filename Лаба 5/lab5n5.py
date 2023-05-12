from tabulate import tabulate


def roundrobin():
    while True:
        try:
            number_of_processes = int(input("Количество процессов: "))
            time_quantum = int(input("Квант времени: "))
            break
        except:
            print("Некорректный ввод\n")
    global proc_list
    proc_list = []
    i = 0
    while i < number_of_processes:
        try:
            time = int(input(f"p{i} >> "))
            assert 1 <= time
            proc_list.append(Process(time, i))
        except:
            print("Некорректный ввод")
            i -= 1
        i += 1
    total_time = sum([i.time for i in proc_list])
    table = [[i for i in range(1, total_time+1)], *[[] for i in range(number_of_processes)]]
    start = 0
    total_waiting = 0
    total_processing = 0
    while start < total_time:
        for proc in proc_list:
            for t in range(time_quantum):
                if proc.time > 0:
                    proc.time -= 1
                    table[proc.i+1].extend(["Г" for i in range(proc.pointer, start)])
                    table[proc.i+1].append("И")
                    total_processing += 1
                    total_waiting += start-proc.pointer
                    start += 1
                    proc.pointer = start
    table[0].insert(0, "Время")
    for i in range(1, len(table)):
        table[i].insert(0, f"p{i-1}")
    print(tabulate(table, tablefmt="grid"))
    print(f"Среднее время ожидания: {((total_waiting) / number_of_processes):.2f}")
    print(f"Среднее полное время выполнения: {(total_processing+total_waiting)/number_of_processes:.2f}")
    return


class Process:
    def __init__(self, time, i):
        self.i = i
        self.time = time
        self.ar = []
        self.pointer = 0


if __name__ == "__main__":
    try:
        roundrobin()
    except:
        print("Что-то пошло не так")
    input()

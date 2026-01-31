import multiprocessing

def process_file(file_path, result_queue):
    """

    Функция process_file(file_path, result_queue)
    принимает путь к файлу и очередь для передачи результатов.
    Функция должна:
    o Открыть файл и посчитать количество строк.
    o Поместить результат в очередь.

    """

    try:
        count = 0
        with open(file_path, 'r', encoding='utf-8') as f:

            #счетчик строк. Используется ручной счетчик, а не len,
            #так как len дает излишнюю нагрузку на память.
            for _ in f:
                count += 1

        result_queue.put(count)

        print(f'в файле {file_path} количество строк {count}')

    except FileNotFoundError as err:
        print(f"Файл {file_path} не найден. Ошибка: {err}")

    except Exception as e:
        print(f"Непредвиденная ошибка {e}")

def main():

    file_paths = [
        "file1.txt",
        "file2.txt",
        "file3.txt"]

    result_queue = multiprocessing.Queue() #очередь для мультипроцесса

    processes = []

    #чтение файла
    for file_path in file_paths:
        p = multiprocessing.Process(target=process_file, args=(file_path, result_queue))
        processes.append(p)
        p.start()
        p.join()

if __name__ == '__main__':
    main()



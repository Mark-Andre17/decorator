import datetime
import os


def decorate_log(file_path, file_name):
    file_place = os.path.join(file_path, file_name)

    def decorate_log_save(func):
        def save_file(*args, **kwargs):
            date = datetime.datetime.now()
            name_func = func.__name__
            result = func(*args, **kwargs)
            with open(f'{file_name}', 'w', encoding='utf-8') as file:
                file.write(
                    f'Дата и время:{date}\nИмя функции:{name_func}\nАргументы функции:{args, kwargs}\nРезудьтат '
                    f'функции:{result}\nПуть к файлу:{file_place}')
            return result

        return save_file

    return decorate_log_save


@decorate_log('pythonProject1', 'logger.txt')
def count_numbers(a, b):
    return a + b


if __name__ == '__main__':
    count_numbers(3, 5)

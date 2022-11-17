import requests
import validators


HTTP_METHODS = {
    'GET': requests.get,
    'HEAD': requests.head,
    'POST': requests.post,
    'PUT': requests.put,
    'DELETE': requests.delete,
    'OPTIONS': requests.options,
}


result = {}


def exc_input(text):
    try:
        num = int(input(text))
        return num
    except ValueError:
        print('Вы ввели не целое число! Повторите ввод')
        return exc_input(text)


def get_http_method(link):
    result[link] = {}
    for method, req_meth in HTTP_METHODS.items():
        if req_meth(link).status_code != 405:
            result[link].update({method: req_meth(link).status_code})


def iter_string(strings):
    for string in strings:
        if validators.url(string):
            get_http_method(string)
        else:
            print(f'Строка "{string}" не является ссылкой')
            continue


def main():
    strings = set()
    num = exc_input('Введите количество строк(целое число): ')
    while num > 0:
        string = input()
        if string == '+':
            num += exc_input(
                'Введите количество дополнительных строк(целое число): '
            )
            continue
        elif string == '-':
            num -= exc_input(
                'Введите количество удаляемых строк(целое число): '
            )
            continue
        else:
            strings.add(string)
        num -= 1
    iter_string(strings)


if __name__ == '__main__':
    main()
    print(result if result else 'В введенных строках ссылок не было.')

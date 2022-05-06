def print_loading(message: str):
    print(f'\033[1;33m[ LOADING ]\033[m \033[1;37m{message}\033[m')


def print_sucess(message: str):
    print(f'\033[1;32m[ SUCESS  ]\033[m \033[1;37m{message}\033[m')


def print_error(message: str):
    print(f'\033[1;31m[ ERROR   ]\033[m \033[1;37m{message}\033[m')


def print_path(path: str, message: str):
    print(f'\033[1;32m[{message}]\033[m {path}')


if __name__ == '__main__':
    print_loading('Loading wordlist')
    print_sucess('Wordlist loaded')
    print_error('Error to load wordlist')

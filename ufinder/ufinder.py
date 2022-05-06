import lprint
from argeasy import ArgEasy

from threading import Thread
import requests

WORDLIST_PATH = './wordlist.txt'
NUM_THREADS = 4


def main():
    wordlist_path = WORDLIST_PATH
    num_threads = NUM_THREADS

    parser = ArgEasy(
        project_name='UFinder',
        description='ufinder does a path search on the site using a wordlist. Showing all paths found.',
        version='1.0.0'
    )

    parser.add_argument('search', 'Search URL paths')
    parser.add_flag('--wordlist', 'Set the path of a custom wordlist')
    parser.add_flag('--threads', 'Set the number of threads')

    args = parser.get_args()

    # if available getting custom wordlist
    if args.wordlist:
        wordlist_path = args.wordlist

    # if available getting custom number of threads
    if args.threads:
        num_threads = int(args.threads)

    if args.search:
        url = args.search

        wordlist = _load_wordlist(wordlist_path)
        if wordlist is False: exit(0)

        threads_wordlist = _split_list(wordlist, num_threads)

        lprint.print_loading('Initializing threads...')
        _start_threads(num_threads, threads_wordlist, url)


def _split_list(_list: list, parts: int):
    list_len = len(_list)
    last_index = 0

    splited_list = []
    list_parts = int(list_len / parts)

    for __ in range(parts):
        splited_list.append(_list[last_index: list_parts + last_index])
        last_index += list_parts

    return splited_list


def _start_threads(num_threads: int, wordlist: list, url: str):
    print()

    for i in range(num_threads):
        thread_wordlist = wordlist[i]
        tr = Thread(target=_search_path, args=(thread_wordlist, url))
        tr.start()


def _search_path(wordlist: list, url: str):
    for path in wordlist:
        path = path.replace('\n', '')
        full_url = f'{url}/{path}'

        try:
            request = requests.get(full_url, timeout=5)
        except requests.exceptions.ReadTimeout:
            lprint.print_path(full_url, 'TIMEOUT')
        except:
            continue

        if request.status_code != 404:
            lprint.print_path(full_url, request.status_code)


def _load_wordlist(path: str):
    lprint.print_loading('Loading worldlist...')

    try:
        with open(path, 'r') as reader:
            wordlist = reader.readlines()
    except FileNotFoundError:
        lprint.print_error('Wordlist path not found')
        return False
    except UnicodeDecodeError:
        lprint.print_error('The wordlist content must be in text')
        return False

    if len(wordlist) == 0:
        lprint.print_error('The wordlist is empty (the paths must be separated by a line)')
        return False

    lprint.print_sucess('Wordlist loaded with sucess')
    return wordlist    

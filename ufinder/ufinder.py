import lprint
from argeasy import ArgEasy

from threading import Thread
import requests

WORDLIST_PATH = './wordlist.txt'
NUM_THREADS = 4

all_found_paths = []


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
        url_path = args.search


def split_list(_list: list, parts: int):
    list_len = len(_list)
    last_part = 0
    splited_list = []

    for __ in range(int(list_len / parts)):
        splited_list.append(_list[last_part: last_part + parts])
        last_part += parts

    return splited_list


def _start_thread(num_threads: int, wordlist: list, url: str):
    for i in num_threads:
        thread_wordlist = wordlist[i]
        tr = Thread(target=_search_thread, args=(thread_wordlist, url))
        tr.start()


def _search_thread(wordlist: list, url: str):
    found_paths = []

    for path in wordlist:
        full_url = f'{url}/{path}'
        request = requests.get(full_url, timeout=5)

        if request.status_code != 404:
            found_paths.append((full_url, request.status_code))

    all_found_paths.append(found_paths)


def load_wordlist(path: str):
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


main()

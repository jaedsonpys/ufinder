import lprint
from argeasy import ArgEasy

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
        url_path = args.search


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

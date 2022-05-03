import lprint
from argeasy import ArgEasy


def main():
    parser = ArgEasy(
        project_name='UFinder',
        description='ufinder does a path search on the site using a wordlist. Showing all paths found.',
        version='1.0.0'
    )

    parser.add_argument('search', 'Search URL paths')
    parser.add_flag('--wordlist', 'Set the path of a custom wordlist')

    args = parser.get_args()


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

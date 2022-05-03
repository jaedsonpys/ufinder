import lprint


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

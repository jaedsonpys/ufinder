# UFinder - URL path search

UFinder performs a search for paths (routes or directories) at the given URL, showing all those available on the site.

## Links

- [UFinder - URL path search](#ufinder---url-path-search)
  - [Links](#links)
- [Installation](#installation)
- [Using UFinder](#using-ufinder)
- [License](#license)

# Installation

You can download UFinder using the PIP package manager:

```bash
pip install ufinder 
```

Or install manually:

```bash
git clone git@github.com:jaedsonpys/ufinder.git
cd ufinder
python3 setup.py install
```

# Using UFinder

Using UFinder is **very simple**, you can define which wordlist to use, and how many threads will be used to search that URL. First of all, you must put the `search` command:

```bash
ufinder search https://github.com --wordlist ./mywordlist.txt
```

With that, you can now perform a search on the site. The default number of threads is 4, you can change this using the `--threads` argument, putting the number of threads after it:

```bash
ufinder search https://github.com --wordlist ./mywordlist.txt --threads 2
```

Simple.

# License

This project uses the `MIT license`.
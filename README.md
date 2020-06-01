# brute

[![Build Status](https://img.shields.io/github/workflow/status/ex0dus-0x/brute/CI/master)](https://github.com/ex0dus-0x/brute/actions?query=workflow%3ACI)
[![PyPI Version](https://badge.fury.io/py/brute.svg)](https://badge.fury.io/py/brute)
[![Github Issues](https://img.shields.io/github/issues/ex0dus-0x/brute.svg)](https://github.com/ex0dus-0x/brute/issues)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://codemuch.tech/license.txt)


Crowd-sourced credential stuffing engine built for security professionals

## Introduction

__brute__ is a Python-based library framework and engine that enables security professionals to rapidly construct bruteforce / credential stuffing attacks. It features both a multi-purpose command-line application (`brute`), and a software library that can be used in tandem to quickly generate standalone module scripts for attack.

You can use __brute__ to:

* Quickly launch an attack with the `brute` CLI with an included module (ie. SMTP server, or a Twitter account)
* Use the CLI to generate a module, which you can then run as a standalone script, or incorporate as part of your local module registry
* Use community modules from the global registry to "crowdsource" your attacks (NOTE: global registry is WIP)

### What can you do with it?

* Rapidly test publicly leaked credential corpora against multiple services.
* Construct PoC scripts quickly to test rate-limiting for authentication systems.
* Launch an active credential reuse campaign as part of an OSINT profile.

## Features

* __Functional__ - works out-of-the-box with 7 default modules for attacks on both network protocols and web-based services
* __Simple to use__ - launch an attack or implement an attack module in minutes and fewer lines of code!
* __Plugin manager__ - implement your own attack modules, and upload them to the local and global registry, or pull others from the community.
* __Logging facilities__ - incorporate dumped logs into a logging pipeline / SIEM.

## Usage

`brute` is built for Python 3.7+, and should work with any platform, preferably macOS/Linux.

To use `brute`, you can either install through `pip`:

```
$ pip install brute --user
```

or build locally:

```
$ git clone https://github.com/ex0dus-0x/brute
$ cd brute/
$ python3 setup.py install
```

### CLI Usage

```
usage: brute [-h] [--list_modules] [--add_module ADD_MODULE] [--new_module NEW_MODULE] [-m MODULE] [-u USERNAME] [-w WORDLIST]
             [-a ADDRESS] [-p PORT] [-d DELAY]

crowd-sourced credential stuffing engine

optional arguments:
  -h, --help            show this help message and exit

Module Management:
  --list_modules        List out the currently available modules in the local registry.
  --add_module ADD_MODULE
                        Add a new module to the local registry.
  --new_module NEW_MODULE
                        Given a specifier (type/name), initialize a new module plugin.

Launching an Attack:
  -m MODULE, --module MODULE
                        Provide a valid module to be executed.
  -c COMBO_LIST, --combo_list COMBO_LIST
                        Path or valid URL to combination list (--username and --wordlist will be ignored).
  -u USERNAME, --username USERNAME
                        Provide a valid username/identifier for module being executed. Can either be a single
                        username, comma-seperated list of users, or a file.
  -w WORDLIST, --wordlist WORDLIST
                        Provide a file path, directory of files, or a HTTP URL to a wordlist.
  -a ADDRESS, --address ADDRESS
                        Provide host address for specified service. Required for certain protocols.
  -p PORT, --port PORT  Provide port for host address for specified service, otherwise default will be used.
  -d DELAY, --delay DELAY
                        Provide the number of seconds the program delays as each password is tried.
  -t TIMEOUT, --timeout TIMEOUT
                        Number of seconds to stop bruteforce execution on currently executing user.
```

To interact with the modules in your local registry, you can do the following:

```
# show all modules in registry
$ brute --list_modules

# create a new plugin script
$ brute --new_module web/mysite

# .. edit it with functionality
$ vim mysite.py

# now you can run it normally ...
$ python3 mysite.py --username test --wordlist wordlist.txt

# .. or add it to the registry and use it with the cli
$ brute --add_module mysite.py
$ brute -m mysite --username test --wordlist wordlist.txt
```

You can specify different credential inputs in different formats.

First, you can use multiple usernames, either in a comma-seperated list or a file path. Be
sure to set a timeout with `-t/--timeout` in order to stop an execution on a user after
a finite amount of time. You can also choose to use a URL with a wordlist as well.

```
# with multiple usernames and a URL wordlist, timeout per user of 5 seconds
$ brute -m mysite --username myname,othername,anothername, --wordlist https://example.com/leak.txt -t 5

# with username file and wordlist file, timeout per user of 3 seconds
$ brute -m mysite --username user.txt --wordlist pass.txt -t 3
```

To better automate credential stuffing campaigns, you can use `-c/--combo_list` instead
of the `--username` and `--wordlist` flags, with either a filepath or URL. Be sure that the file
contains a colon-seperated combo per line as so: `user:pass`.

```
# with a file
$ brute -m mysite --combo_list test.txt

# .. or a URL
$ brute -m mysite --combo_list http://example.com/leak.txt
```

### Library

(TODO)

## Contributing

If you have any proposed changes, please make a pull request or issue!

brute was designed as a pragmatic approach towards credential stuffing and reuse. In no way does it endorse malicious hacking. Please do not support the use of this code as a method of advancing black-hat activites.

## License

[MIT](https://codemuch.tech/license.txt)

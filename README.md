# brute

[![GitHub forks](https://img.shields.io/github/forks/ex0dus-0x/brute.svg)](https://github.com/ex0dus-0x/brut3k1t/network)
[![GitHub issues](https://img.shields.io/github/issues/ex0dus-0x/brute.svg)](https://github.com/ex0dus-0x/brut3k1t/issues)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/ex0dus-0x/brute/master/LICENSE)

__brute__ is a security-oriented tool for conducting bruteforce attacks against a multitude of protocols and services

> NOTE: this has been renamed to brute, and depreciated. No further support will be provided after the latest final commit.

## Introduction

__brute__ is a  bruteforce framework that supports dictionary attacks for several protocols and services.
The current protocols that are complete and in support are:

```
----------------
Protocols:
----------------
ssh
ftp
smtp
xmpp
telnet

----------------
Webbased Services
----------------
instagram
facebook
twitter

----------------
Hashcrack
----------------
md5
sha1
sha224
```

Libraries for connecting and authenticating to network protocols have existed as part of most programming languages' standard library, and brute abuses them in order to execute bruteforce attacks. As for web-based services and sites, by utilizing browser manipulation, brute relies on a bot to visit the webpage, hooking onto authentication input field elements, and sending the username / password.


## Installation

```
$ git clone https://github.com/ex0dus-0x/brute && cd brut3k1t/
$ python setup.py install
```

## Usage

```
usage: brute [-h] [-s] [-u USERNAME] [-w WORDLIST] [-a ADDRESS] [-p PORT]
            [-d DELAY]

Bruteforce framework written in Python

optional arguments:
  -h, --help            show this help message and exit
  -a ADDRESS, --address ADDRESS
                      Provide host address for specified service. Required
                      for certain protocols
  -p PORT, --port PORT  Provide port for host address for specified service.
                      If not specified, will be automatically set
  -d DELAY, --delay DELAY
                      Provide the number of seconds the program delays as
                      each password is tried

required arguments:
  -s , --service        Provide a service being attacked. The Protocols and
                      Services supported are SSH, FTP, SMTP, XMPP, TELNET,
                      INSTAGRAM, FACEBOOK, TWITTER, MD5, SHA1, SHA224
  -u USERNAME, --username USERNAME
                      Provide a valid username/hashstring for
                      service/protocol/hashcrack being executed
  -w WORDLIST, --wordlist WORDLIST
                      Provide a wordlist or directory to a wordlist
```

Note that with the new release of the hashcrack feature, the `--username` flag is used to supply the target hashstring for hash cracking!

## Examples:

Bruteforcing SSH server running on `192.168.1.3` using `root` and `wordlist.txt` as a wordlist.

```
$ brute -s ssh -a 192.168.1.3 -u root -w wordlist.txt
```

The program will automatically set the port to 22, but if it is different, specify with `-p` flag.

Cracking email `test@gmail.com` with `wordlist.txt` on port `25` with a 3 second delay. For email it is necessary to use the SMTP server's address. For e.g Gmail = `smtp.gmail.com`. You can research this using Google.

```
$ brute -s smtp -a smtp.gmail.com -u test@gmail.com -w wordlist.txt -p 25 -d 3
```

Cracking XMPP `test@creep.im` with `wordlist.txt` on default port `5222`. XMPP also is similar to SMTP, whereas you will need to provide the address of the XMPP server, in this case `creep.im`.

```
$ brute -s xmpp -a creep.im -u test -w wordlist.txt
```

Cracking Facebook requires either the username (preferable, in this case, `test`), email, phone number, or even ID.

```
$ brute -s facebook -u test -w wordlist.txt
```

Cracking Instagram with username `test` with wordlist `wordlist.txt` and a 5 second delay

```
$ brute -s instagram -u test -w wordlist.txt -d 5
```

Cracking Twitter with username `test` with wordlist `wordlist.txt`

```
$ brute -s twitter -u test -w wordlist.txt
```

Cracking a MD5 hash (where username is the hashstring) with wordlist `wordlist.txt`

```
$ brute -s md5 -u 86bd1db79525abdd576165c1427f9bf6 -w wordlist.txt
```

## Troubleshooting

1. `Can't load the profile. Profile Dir: /some/path`, or `'geckodriver' executable needs to be in PATH. `

`geckodriver` is not in the `PATH`. Make sure that you have run the installer before-hand, and that there is a `geckodriver` in your `PATH` (e.g `/usr/bin`). If not, you may have to manually put it there by downloading the executable [here](https://github.com/mozilla/geckodriver/releases/), and placing it in your `PATH`.

2. Twitter/Facebook/Instagram login page is not rendering / brute is not hooking onto page!

Web-based services often change their authentication page front-end. If this is the case and new extraneous elements are introduced (such as unnecessary "loading bars"), use a higher delay. This way, the program is able to wait until they go away, and then inject the username/password.

## Contributing

If you have any proposed changes, please make a pull request or issue!

brute was designed as a pragmatic approach towards testing bruteforce attacks on various platforms. In no way does it endorse malicious hacking. Please do not support the use of this code as a method of advancing black-hat activites.

## License

[GPL-3.0](https://opensource.org/licenses/GPL-3.0)

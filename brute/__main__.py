#!/usr/bin/env python3
"""
__main__.py

    Main CLI entry point to the `brute` application. Provides
    interface for selecting attack and specifying parameters.

"""
import time
import random
import sys
import os
import argparse

from brute import (
    colors,
    hashcrack,
    protocols,
    web
)

PROTOCOLS = ["ssh", "ftp", "smtp", "telnet", "xmpp"]
WEB = ["instagram", "twitter", "facebook"]
HASHCRACK = ["md5", "sha1", "sha224"]


def main():
    print("""
  _                _   _____
 | |__  _ __ _   _| |_|___ /
 | '_ \| '__| | | | __| |_ \
 | |_) | |  | |_| | |_ ___) |
 |_.__/|_|   \__,_|\__|____/
    security-oriented bruteforce tool.
""")

    parser = argparse.ArgumentParser(description='Bruteforce framework written in Python')
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--service', dest='service', help="Provide a service being attacked.\
                          The Protocols and Services supported are SSH, FTP, SMTP, XMPP, TELNET, INSTAGRAM, FACEBOOK, TWITTER, MD5, SHA1, SHA224",\
                          metavar='', choices=['ssh', 'ftp', 'smtp', 'xmpp', 'telnet', 'instagram', 'facebook', 'twitter', 'md5', 'sha1', 'sha224'])
    required.add_argument('-u', '--username', dest='username', help='Provide a valid username/hashstring for service/protocol/hashcrack being executed')
    required.add_argument('-w', '--wordlist', dest='wordlist', help='Provide a wordlist or directory to a wordlist')
    parser.add_argument('-a', '--address', dest='address', help='Provide host address for specified service. Required for certain protocols')
    parser.add_argument('-p', '--port', type=int, dest='port', help='Provide port for host address for specified service. If not specified, will be automatically set')
    parser.add_argument('-d', '--delay', type=int, dest='delay', help='Provide the number of seconds the program delays as each password is tried')

    args = parser.parse_args()

    # Specify mandatory options.
    man_options = ['username', 'wordlist']
    for m in man_options:
        if not args.__dict__[m]:
            parser.print_help()
            colors.error("[!] You have to specify a username AND a wordlist! [!]")
            exit(1)

    # Detect if service arg is provided
    if args.service is None:
        colors.error("[!] No service provided! [!]")
        exit(1)

    # Detect is wordlist path is correct
    if os.path.exists(args.wordlist) == False:
        colors.error("[!] Wordlist not found! [!]")
        exit(1)


    # Check if the service provided is for hashcracking.
    if args.service in HASHCRACK:
        colors.warn("[!] Hashcrack detected! [!]")
        colors.good("[*] Hashstring: {}".format(args.username))
    else:
        colors.good("[*] Username: {}".format(args.username))


    time.sleep(0.5)
    colors.good("[*] Wordlist: {}".format(args.wordlist))

    time.sleep(0.5)
    print(C + "[*] Service: {}".format(arg.service) + W)

    if args.delay is None:
        colors.warn("[?] Delay not set! Default to 1 [?]")
        args.delay = 1

    time.sleep(0.5)

    # main program execution
    if args.service in colors.PROTOCOLS:

        # perform protocol-based bruteforce
        p = protocols.ProtocolBruteforce(args.service, args.address, args.username, args.wordlist, args.port, args.delay)
        p.execute()

    elif args.service in colors.WEB:

        # Web services do not require addresses or ports
        if args.address or args.port:
            colors.error("[!] NOTE: You don't need to provide an address OR port [!]")
            exit(1)

        # perform web-based bruteforce
        w = web.WebBruteforce(args.service, args.username, args.wordlist, args.delay)
        w.execute()

    elif args.service in colors.HASHCRACK:

        # Hashcrack does not require address or port
        if args.address or args.port:
            colors.error("[!] NOTE: You don't need to provide an address OR port [!]")
            exit(1)

        # perform hashcracking
        h = hashcrack.HashCrack(args.service, args.username, args.wordlist, args.delay)
        h.execute()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        colors.error("\n[!] Keyboard Interrupt detected! Killing program... [!]")
        exit(1)

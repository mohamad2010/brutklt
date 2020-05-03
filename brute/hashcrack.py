"""
hashcrack.py

    Core module for vulnerable hash bruteforcing

    This module provides the methods for hashcracking vulnerable one-way
    functions. This is achieved by recursively checking each cleartext's hash
    against the current hashstring. Since Python's hashlib library provides
    extensive support for many hashing algorithms, here are those that are
    currently being supported:
    - md5
    - sha1
    - sha224
"""

import brute.colors

import time
import hashlib


class HashCrack:
    def __init__(self, service, targetHash, wordlist, delay):
        self.targetHash = targetHash
        self.wordlist = wordlist
        self.delay = delay

        if service == "md5":
            self.hashtype = hashlib.md5()
        elif service == "sha1":
            self.hashtype = hashlib.sha1()
        elif service == "sha224":
            self.hashtype = hashlib.sha224()

    def execute(self):
        wordlist = open(self.wordlist, 'r')
        for i in wordlist.readlines():
            password = i.strip("\n")
            self.hashtype.update(password.encode('utf-8'))
            checkedHash = self.hashtype.hexdigest()

            try:
                if checkedHash != self.targetHash:
                    colors.warn("[*] Target Hash: {} | [*] Current Hash: {} | [*] Cleartext: {} | Incorrect!".format(self.targetHash, checkedHash, password))
                    time.sleep(self.delay)
                elif checkedHash == self.targetHash:
                    colors.green("[*] Target Hash: {} | [*] Current Hash: {} | [*] Cleartext: {} | Found!".format(self.targetHash, checkedHash, password))
                    wordlist.close()
                    exit(0)
            except KeyboardInterrupt:
                wordlist.close()
                exit(1)

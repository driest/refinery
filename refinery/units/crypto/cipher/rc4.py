#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Crypto.Cipher import ARC4

from . import StandardCipherUnit

ARC4.key_size = range(1, 257)


class rc4(StandardCipherUnit):
    """
    RC4 encryption and decryption.
    """
    _cipher = ARC4
    _requires_iv = False
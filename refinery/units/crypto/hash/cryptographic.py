#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implements various cryptographic hashing algorithms.
"""
import hashlib

from . import HashUnit


class md5(HashUnit):
    """
    Returns the MD5 hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.md5(data).digest()


class sha1(HashUnit):
    """
    Returns the SHA1 Hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.sha1(data).digest()


class sha224(HashUnit):
    """
    Returns the SHA224 Hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.sha224(data).digest()


class sha256(HashUnit):
    """
    Returns the SHA256 Hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.sha256(data).digest()


class sha384(HashUnit):
    """
    Returns the SHA384 Hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.sha384(data).digest()


class sha512(HashUnit):
    """
    Returns the SHA512 Hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.sha512(data).digest()


class blk224(HashUnit):
    """
    Returns the BLK224 Hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.blake2b(data, digest_size=28)


class blk256(HashUnit):
    """
    Returns the BLK256 Hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.blake2b(data, digest_size=32)


class blk384(HashUnit):
    """
    Returns the BLK384 Hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.blake2b(data, digest_size=48)


class blk512(HashUnit):
    """
    Returns the BLK512 Hash of the input data.
    """
    @classmethod
    def _algorithm(cls, data): return hashlib.blake2b(data, digest_size=64)

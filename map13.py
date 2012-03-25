#!/usr/bin/python
#-*- coding: utf-8 -*-

def generate_map(alphabet_in, alphabet_out):
    """
    >>> rot13 = generate_map("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
    >>> rot13("THis is a trivial problem that should easily be finished within 30 minutes. Tops")
    'GUvf vf n gevivny ceboyrz gung fubhyq rnfvyl or svavfurq jvguva 30 zvahgrf. Gbcf'
    """
    mapping = make_mapping(alphabet_in, alphabet_out)
    def mapper(stringy):
        return ''.join((mapping[char] if char in mapping else char for char in stringy))
    return mapper

def make_mapping(alphabet_in, alphabet_out):
    """
    (alphabetin, alphabetout) -> dictionary_mapping
    """
    if len(alphabet_in) != len(alphabet_out):
        raise Exception("Input alphabet must be the same as output alphabet!")
    return dict(zip(list(alphabet_in), list(alphabet_out)))

def rot13(stringy):
    """
    The famous ROT13 algo
    """
    alphabet_in = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_ot = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    return generate_map(alphabet_in, alphabet_ot)(stringy)

def balrot(stringy):
    """
    The not-so-famous reverse alphabet algo
    """
    alphabet_in = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_ot = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
    return generate_map(alphabet_in, alphabet_ot)(stringy)

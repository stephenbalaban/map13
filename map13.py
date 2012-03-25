#!/usr/bin/python
#-*- coding: utf-8 -*-

def generate_map(mapping):
    def mapper(stringy):
        return ''.join((mapping[char] if char in mapping else char for char in stringy))
    return mapper

def make_mapping(alphabet_in, alphabet_out):
    if len(alphabet_in) != len(alphabet_out):
        raise Exception("Input alphabet must be the same as output alphabet!")
    return dict(zip(list(alphabet_in), list(alphabet_out)))

def rot13(stringy):
    alphabet_in = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_ot = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    return generate_map(make_mapping(alphabet_in, alphabet_ot))(stringy)

def balrot(stringy):
    alphabet_in = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_ot = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
    return generate_map(make_mapping(alphabet_in, alphabet_ot))(stringy)

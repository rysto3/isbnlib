#!/usr/bin/env python3
import sys
print(f"Python: {sys.version}")
import isbnlib
print(f"isbnlib version: {isbnlib.__version__}")
print(f"Test ISBN-13: {isbnlib.is_isbn13('9780439554930')}")
print(f"Test ISBN-10: {isbnlib.is_isbn10('0439554934')}")
print(f"Convert to ISBN-13: {isbnlib.to_isbn13('0439554934')}")
print(f"Convert to ISBN-10: {isbnlib.to_isbn10('9780439554930')}")
print(f"Mask: {isbnlib.mask('9780439554930')}")
print("SUCCESS!")


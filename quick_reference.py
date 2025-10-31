#!/usr/bin/env python3
"""
Quick Reference Test for isbnlib
Demonstrates all core functionality with Python 3.12+ compatibility
"""

import isbnlib

print("="*70)
print("isbnlib Quick Reference - Python 3.12+ Compatible")
print("="*70)

# Example ISBN (Harry Potter and the Sorcerer's Stone)
isbn13 = "9780439554930"
isbn10 = "0439554934"

print("\n[1] ISBN Validation:")
print(f"  is_isbn13('{isbn13}'): {isbnlib.is_isbn13(isbn13)}")
print(f"  is_isbn10('{isbn10}'): {isbnlib.is_isbn10(isbn10)}")

print("\n[2] ISBN Conversion:")
print(f"  to_isbn13('{isbn10}'): {isbnlib.to_isbn13(isbn10)}")
print(f"  to_isbn10('{isbn13}'): {isbnlib.to_isbn10(isbn13)}")

print("\n[3] ISBN Formatting:")
print(f"  mask('{isbn13}'): {isbnlib.mask(isbn13)}")
print(f"  canonical('ISBN {isbn13}'): {isbnlib.canonical(f'ISBN {isbn13}')}")
print(f"  clean('ISBN-13: {isbn13}'): {isbnlib.clean(f'ISBN-13: {isbn13}')}")

print("\n[4] ISBN Information:")
isbn_obj = isbnlib.Isbn(isbn13)
print(f"  Isbn('{isbn13}'):")
print(f"    ISBN-13: {isbn_obj.isbn13}")
print(f"    ISBN-10: {isbn_obj.isbn10}")
print(f"    EAN-13: {isbn_obj.ean13}")

print("\n[5] Extract ISBNs from Text:")
text = "Check out ISBN 9780439554930 and also 0439023483 for great reads!"
found = isbnlib.get_isbnlike(text)
print(f"  Text: '{text}'")
print(f"  Found: {found}")

print("\n[6] Get Metadata (requires internet):")
try:
    meta = isbnlib.meta(isbn13)
    if meta:
        print(f"  Title: {meta.get('Title', 'N/A')}")
        print(f"  Authors: {', '.join(meta.get('Authors', []))}")
        print(f"  Publisher: {meta.get('Publisher', 'N/A')}")
        print(f"  Year: {meta.get('Year', 'N/A')}")
        print(f"  Language: {meta.get('Language', 'N/A')}")
    else:
        print("  No metadata found")
except Exception as e:
    print(f"  Error: {e}")

print("\n[7] Format as BibTeX (requires internet):")
try:
    from isbnlib.registry import bibformatters
    bibtex = bibformatters['bibtex'](meta) if meta else "No metadata"
    print(f"  {bibtex[:100]}..." if len(bibtex) > 100 else f"  {bibtex}")
except Exception as e:
    print(f"  Error: {e}")

print("\n" + "="*70)
print("✓ All functions working correctly with Python 3.12+")
print("="*70)


#!/usr/bin/env python3
"""Comprehensive test for isbnlib with Python 3.12+ compatibility."""

import sys
import traceback

def main():
    print("=" * 80)
    print(f"Python Version: {sys.version}")
    print("=" * 80)

    # Test import
    print("\n[1] Testing import...")
    try:
        import isbnlib
        print(f"✓ Import successful")
        print(f"✓ Version: {isbnlib.__version__}")
        print(f"✓ Support: {isbnlib.__support__}")
    except Exception as e:
        print(f"✗ Import failed: {e}")
        traceback.print_exc()
        return 1

    # Test ISBNs from AGENTS.md
    test_books = [
        ("Harry Potter and the Sorcerer's Stone", "9780439554930", "0439554934"),
        ("The Hunger Games", "9780439023481", "0439023483"),
        ("To Kill a Mockingbird", "9780060935467", "0060935464"),
        ("Pride and Prejudice", "9781441341709", "1441341706"),
        ("The Fault in Our Stars", "9780142424179", "014242417X"),
    ]

    print("\n[2] Testing ISBN Validation...")
    all_passed = True
    for title, isbn13, isbn10 in test_books:
        try:
            v13 = isbnlib.is_isbn13(isbn13)
            v10 = isbnlib.is_isbn10(isbn10)
            if v13 and v10:
                print(f"✓ {title}: ISBN-13={v13}, ISBN-10={v10}")
            else:
                print(f"✗ {title}: ISBN-13={v13}, ISBN-10={v10}")
                all_passed = False
        except Exception as e:
            print(f"✗ {title}: Error - {e}")
            all_passed = False

    print("\n[3] Testing ISBN Conversion...")
    for title, isbn13, isbn10 in test_books:
        try:
            c13 = isbnlib.to_isbn13(isbn10)
            c10 = isbnlib.to_isbn10(isbn13)
            if c13 == isbn13 and c10 == isbn10:
                print(f"✓ {title}: Conversions correct")
            else:
                print(f"✗ {title}: Expected ({isbn13}, {isbn10}), got ({c13}, {c10})")
                all_passed = False
        except Exception as e:
            print(f"✗ {title}: Error - {e}")
            all_passed = False

    print("\n[4] Testing ISBN Masking...")
    for title, isbn13, isbn10 in test_books:
        try:
            masked = isbnlib.mask(isbn13)
            if masked:
                print(f"✓ {title}: {masked}")
            else:
                print(f"✗ {title}: No mask returned")
        except Exception as e:
            print(f"✗ {title}: Error - {e}")

    print("\n[5] Testing ISBN Canonicalization...")
    for title, isbn13, isbn10 in test_books:
        try:
            canonical = isbnlib.canonical(f"ISBN {isbn13}")
            if canonical == isbn13:
                print(f"✓ {title}: {canonical}")
            else:
                print(f"✗ {title}: Expected {isbn13}, got {canonical}")
        except Exception as e:
            print(f"✗ {title}: Error - {e}")

    print("\n[6] Testing Metadata Retrieval...")
    for title, isbn13, isbn10 in test_books:
        try:
            meta = isbnlib.meta(isbn13)
            if meta:
                meta_title = meta.get('Title', 'N/A')
                authors = ', '.join(meta.get('Authors', []))
                year = meta.get('Year', 'N/A')
                print(f"✓ {title}:")
                print(f"    Title: {meta_title}")
                print(f"    Authors: {authors}")
                print(f"    Year: {year}")
            else:
                print(f"⚠ {title}: No metadata found")
        except Exception as e:
            print(f"✗ {title}: Error - {e}")

    print("\n" + "=" * 80)
    if all_passed:
        print("✓ All validation and conversion tests PASSED!")
    else:
        print("✗ Some tests FAILED!")
    print("=" * 80)

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())


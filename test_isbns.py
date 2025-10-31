#!/usr/bin/env python3
"""Test all ISBNs from AGENTS.md"""

import isbnlib

# Test ISBNs from AGENTS.md
test_books = [
    ("Harry Potter and the Sorcerer's Stone", "9780439554930", "0439554934"),
    ("The Hunger Games", "9780439023481", "0439023483"),
    ("To Kill a Mockingbird", "9780060935467", "0060935464"),
    ("Pride and Prejudice", "9781441341709", "1441341706"),
    ("The Fault in Our Stars", "9780142424179", "014242417X"),
]

print("=" * 80)
print("Testing ISBN Validation and Conversion")
print("=" * 80)

all_passed = True

for title, isbn13, isbn10 in test_books:
    print(f"\n{title}:")
    print(f"  ISBN-13: {isbn13}")
    print(f"  ISBN-10: {isbn10}")

    # Validate ISBNs
    is_valid_13 = isbnlib.is_isbn13(isbn13)
    is_valid_10 = isbnlib.is_isbn10(isbn10)
    print(f"  ✓ ISBN-13 valid: {is_valid_13}")
    print(f"  ✓ ISBN-10 valid: {is_valid_10}")

    if not is_valid_13 or not is_valid_10:
        all_passed = False
        print("  ✗ VALIDATION FAILED")
        continue

    # Test conversions
    converted_13 = isbnlib.to_isbn13(isbn10)
    converted_10 = isbnlib.to_isbn10(isbn13)
    print(f"  ✓ ISBN-10 → ISBN-13: {isbn10} → {converted_13}")
    print(f"  ✓ ISBN-13 → ISBN-10: {isbn13} → {converted_10}")

    # Verify conversions are correct
    if converted_13 != isbn13:
        print(f"  ✗ Conversion failed: {converted_13} != {isbn13}")
        all_passed = False
        continue

    if converted_10 != isbn10:
        print(f"  ✗ Conversion failed: {converted_10} != {isbn10}")
        all_passed = False
        continue

    # Test masking
    masked = isbnlib.mask(isbn13)
    print(f"  ✓ Masked: {masked}")

    # Test canonical
    canonical = isbnlib.canonical(f"ISBN {isbn13}")
    print(f"  ✓ Canonical: {canonical}")

print("\n" + "=" * 80)
print("Testing Metadata Retrieval")
print("=" * 80)

for title, isbn13, isbn10 in test_books:
    print(f"\n{title} ({isbn13}):")
    try:
        meta = isbnlib.meta(isbn13)
        if meta:
            print(f"  ✓ Title: {meta.get('Title', 'N/A')}")
            print(f"  ✓ Authors: {', '.join(meta.get('Authors', []))}")
            print(f"  ✓ Publisher: {meta.get('Publisher', 'N/A')}")
            print(f"  ✓ Year: {meta.get('Year', 'N/A')}")
            print(f"  ✓ Language: {meta.get('Language', 'N/A')}")
        else:
            print("  ⚠ No metadata found")
    except Exception as e:
        print(f"  ✗ Error: {e}")

print("\n" + "=" * 80)
if all_passed:
    print("✓ All validation and conversion tests passed!")
else:
    print("✗ Some tests failed!")
print("=" * 80)


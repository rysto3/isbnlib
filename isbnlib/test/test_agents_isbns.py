# -*- coding: utf-8 -*-
"""Test core functions with ISBNs from AGENTS.md."""

from isbnlib import meta

# ISBNs from AGENTS.md
ISBN_LIST = [
    "9780439554930",
    "0439554934",
    "9780439023481",
    "0439023483",
    "9780060935467",
    "0060935464",
    "9781441341709",
    "1441341706",
    "9780142424179",
    "014242417X",
]

def test_agents_isbns():
    """Test that the meta function returns metadata for the given ISBNs."""
    for isbn in ISBN_LIST:
        metadata = meta(isbn)
        assert isinstance(metadata, dict)

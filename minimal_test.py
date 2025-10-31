#!/usr/bin/env python3
import isbnlib


def main():
    data = isbnlib.meta('9780140328721', service='openl')
    print("Data:", data)
    print("Type:", type(data))
    if data:
        print("Keys:", data.keys())
        if 'Authors' in data:
            print("Authors:", data['Authors'])
        else:
            print("No Authors key")


main()

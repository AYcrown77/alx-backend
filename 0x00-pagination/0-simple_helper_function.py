#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    takes two integer arguments page and page_size
    return a tuple of size two containing a start index and an end index
    """
    if page == 1:
        page = 0
    else:
        page = page_size * (page - 1)
    return (page, page + page_size)

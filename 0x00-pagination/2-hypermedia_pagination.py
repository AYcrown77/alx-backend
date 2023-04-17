#!/usr/bin/env python3
"""
Simple pagination"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    returns a tuple of size two that contains
    the start index and end index of current page
    first parameter: page number
    second parameter: page size
    """
    if page == 1:
        page = 0
    else:
        page = page_size * (page - 1)
    return (page, page + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        takes two integer arguments page with default value 1
        and page_size with default value 10.
        return the appropriate page of the dataset (i.e. the correct
        list of rows).
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        [start, end] = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        returns a dictionary containing the following key-value pairs
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        hyper: dict = {}

        hyper["page_size"] = len(data)
        hyper["page"] = page
        hyper["data"] = data
        hyper["next_page"] = page + 1 if page + 1 <= total_pages else none
        hyper["prev_page"] = page - 1 if page > 1 else None
        hyper["total_pages"] = total_pages

        return hyper

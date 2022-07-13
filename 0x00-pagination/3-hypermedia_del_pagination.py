#!/usr/bin/env python3
""" Simple helper function """
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    The function should return a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return in a list for
    those particular pagination parameters.

    Arguments:
    page: integer
    page_size: integer
    """
    start_index = (page * page_size) - page_size
    end_index = start_index + page_size
    return(start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        find the correct indexes to paginate the dataset correctly and
        return the appropriate page of the dataset in a dictionary

        Arguments:
        index: integer
        page_size: integer
        """
        dataset = self.__indexed_dataset
        assert index >= 0 and index < len(dataset) - 1
        page_data = []
        next_index = index
        last_index = page_size + index
        i = index
        while i < last_index:
            row = dataset.get(i)
            if not row:
                last_index += 1
            else:
                page_data.append(row)
            next_index += 1
            i += 1
        data = page_data
        return {
            "page_size": page_size,
            "data": data,
            "next_index": next_index,
            "index": index
        }

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        find the correct indexes to paginate the dataset correctly and
        return the appropriate page of the dataset

        Arguments:
        page: integer
        page_size: integer
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        index = index_range(page, page_size)
        start = index[0]
        end = index[1]
        data = self.dataset()
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        find the correct indexes to paginate the dataset correctly and
        return the appropriate page of the dataset in a dictionary

        Arguments:
        page: integer
        page_size: integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        pages = index_range(page, page_size)
        start, end = pages[0], pages[1]
        page_size = end - start
        next_page = page + 1
        if next_page > len(data):
            next_page = None
        prev_page = page - 1
        if prev_page < 1:
            prev_page = None
        page_size
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

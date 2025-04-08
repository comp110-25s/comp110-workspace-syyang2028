"""The Dictionary"""

__author__: str = "730746714"

"""Function Inverting Given Dictionary"""


def invert(dict_input: dict[str, str]) -> dict[str, str]:
    result_dictionary: dict[str, str] = {}
    for key in dict_input:
        if dict_input[key] in result_dictionary:
            raise KeyError("Silly Bubba")
        result_dictionary[dict_input[key]] = key
    return result_dictionary


"""Function Counting # of times a value Appears in List"""


def count(list_input: list[str]) -> dict[str, int]:
    count_dictionary: dict[str, int] = {}
    idx: int = 0
    while idx < len(list_input):
        if list_input[idx] in count_dictionary:
            count_dictionary[list_input[idx]] += 1
        else:
            count_dictionary[list_input[idx]] = 1
        idx += 1
    return count_dictionary


"""Function that returns most common color"""


def favorite_color(color_input: dict[str, str]) -> str:
    idx: int = 0
    peak_idx: int = 0
    dup_idx: int = 0
    storage_list: list[str] = []
    for key in color_input:
        storage_list.append(color_input[key])
        # print(storage_list)
    while idx < len(storage_list):
        if storage_list.count(storage_list[idx]) > storage_list.count(
            storage_list[peak_idx]
        ):
            peak_idx = idx
        idx += 1
    while dup_idx < len(storage_list):
        if storage_list.count(storage_list[dup_idx]) == storage_list.count(
            storage_list[peak_idx]
        ):
            return storage_list[dup_idx]
        else:
            dup_idx += 1
    return storage_list[peak_idx]


"""Function Binning Same Length Sequences in List to a Dictionary"""


def bin_len(list_input: list[str]) -> dict[int, set[str]]:
    idx: int = 0
    bin_dict: dict[int, set[str]] = {}
    storage_set: set[str] = set()
    while idx < len(list_input):
        storage_set = set()
        if len(list_input[idx]) in bin_dict:
            storage_set = bin_dict[len(list_input[idx])]
            storage_set.add(list_input[idx])
            bin_dict[len(list_input[idx])] = storage_set
        else:
            storage_set.add(list_input[idx])
            bin_dict[len(list_input[idx])] = storage_set
        idx += 1
    return bin_dict

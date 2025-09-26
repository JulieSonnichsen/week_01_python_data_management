from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt


def remove_capital_letters(name_list: list[str]) -> list[str]:
    name_list = [name.casefold() for name in name_list]

    return name_list

def remove_duplicates_from_list(name_list: list[str]) -> list[str]:
    name_list = list(set(name_list))

    return name_list

def sort_dict_by_keys(result_dict: dict[int], key=None) -> dict[int]:
    result_dict = OrderedDict(sorted(result_dict.items(), key=key))

    return result_dict

def load_name_list(path: str) -> list[str]:
    with open(path, 'r') as f:
        name_list = f.readlines()

    full_name_list = []

    for line in name_list:
        full_name_list += line.split(',')

    return full_name_list

def count_letters(name_list: list[str]) -> dict[int]:
    letter_dict = {}

    for name in name_list:
        for letter in name:
            if letter in letter_dict.keys():
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    
    return letter_dict

def print_alphabetically_sorted_names(name_list: list[str]) -> None:
    name_list.sort()

    print('Names sorted alphabetically:')

    for name in name_list:
        print(f'\t {name}')

    print('\n \n')

def print_length_sorted_names(name_list: list[str]) -> None:
    name_list.sort(key=len)

    print('Names sorted by length:')

    for name in name_list:
        print(f'\t {name}')

    print('\n \n')


def print_letter_count(letter_dict: dict[int]) -> None:
    for key in letter_dict.keys():
        print(f'{key}: {letter_dict[key]}')

def print_bar_chart_from_dict(result_dict: dict[int], xlabel: str, ylabel: str) -> None:
    x = np.array(list(result_dict.keys()))
    y = np.array(list(result_dict.values()))

    plt.grid(alpha=0.2)
    plt.bar(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def print_wordcloud_from_dict(result_dict: dict[int]) -> None:
    pass
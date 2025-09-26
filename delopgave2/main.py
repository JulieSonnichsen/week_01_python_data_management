import re
from collections import OrderedDict

def load_logs(path: str) -> list[str]:
    with open(path) as f:
        logs = f.readlines()

    return logs

def remove_timestamp(log: str) -> str:
    return re.search('(INFO|WARNING|ERROR|SUCCESS).*', log).group()


def sort_logs(logs: list[str], log_levels: list[str]) -> dict[list[str]]:
    return_dict = {}

    for log in logs:
        for level in log_levels:
            if level in log:
                if level in return_dict.keys():
                    return_dict[level].append(log)
                else:
                    return_dict[level] = [log]
    
    return return_dict


def count_instances_in_list(count_list: list[str]) -> dict[int]:
    return_dict = {}

    for instance in count_list:
        if instance in return_dict.keys():
            return_dict[instance] += 1
        else:
            return_dict[instance] = 1
    
    return return_dict

def sort_dict(dict_to_sort: dict[int], key=None, reverse=False) -> dict[int]:
    return OrderedDict(sorted(dict_to_sort.items(), key=key, reverse=reverse))


def save_logs(logs: list[str], save_path: str) -> None:
    with open(save_path, 'w') as f:
        for log in logs:
            f.write(f'{log}')


logs = load_logs('delopgave2/data/app_log (logfil analyse) - random.txt')

log_levels = ['INFO', 'WARNING', 'ERROR', 'SUCCESS']

sorted_logs = sort_logs(logs, log_levels)

for level in log_levels:
    save_logs(sorted_logs[level], f'delopgave2/logs/{level}.txt')


for level in log_levels:
    level_logs = sorted_logs[level]
    level_logs = [remove_timestamp(log) for log in level_logs]
    log_instances = count_instances_in_list(level_logs)
    log_instances = sort_dict(log_instances, lambda x : x[1], reverse=True)

    print(f'LOG LEVEL: {level}')

    for key in log_instances:
        print(f'\t {key}: {log_instances[key]}')

    print('\n \n')
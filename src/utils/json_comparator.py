

def sorting_dict(item):
    if isinstance(item, dict):
        return sorted((key, sorting_dict(values)) for key, values in item.items())
    if isinstance(item, list):
        return sorted(sorting_dict(x) for x in item)
    else:
        return item


def compare_two_json(inp_dict1, inp_dict2):
    return sorting_dict(inp_dict1) == sorting_dict(inp_dict2)

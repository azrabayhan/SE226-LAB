def remove_duplicates(data_list):
    cleaned = []
    for item in data_list:
        if item not in cleaned:
            cleaned.append(item)
    return cleaned


def strip_whitespaces(string_list):
    cleaned = []
    for item in string_list:
        cleaned.append(item.strip())
    return cleaned
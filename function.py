def _filter(value, data):
    return filter(lambda x: value in x, data)


def _map(value, data):
    return map(lambda x: x.split(' ')[value], data)


def _unique(data):
    return set(data)


def _sort(value, data):
    return sorted(data, reverse=value)


def _open_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line


def query(cmd, value, file_name, data):
    if data == "":
        file = _open_file(file_name)
    else:
        file = data

    if cmd == "map":
        value = int(value)
        result = _map(value, file)
    elif cmd == "filter":
        result = _filter(value, file)
    elif cmd == "unique":
        result = _unique(file)
    elif cmd == "sort":
        if value in ("desc", "asc"):
            reverse = value == "desc"
            result = _sort(reverse, file)
        else:
            raise ValueError
    else:
        raise ValueError

    return list(result)

def required(value, message):
    if not value:
        raise ValueError(message)
    return value


def matches(value, regex, message):
    if value and not regex.match(value):
        raise ValueError(message)
    return value

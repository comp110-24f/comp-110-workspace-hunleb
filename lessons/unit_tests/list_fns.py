def get_first(list: list[str]) -> str:
    """Return first element"""
    return list[0]


def remove_first(list: [str]) -> None:
    """Remove first element"""
    list.pop(0)


def get_and_remove_first(list: [str]) -> str:
    """Returns and removes first element"""
    first_elem: str = list[0]

    list.pop(0)

    return first_elem

def is_char(s: str) -> bool:
    return True if isinstance(s, str) and len(s) == 1 and s.isascii() else False

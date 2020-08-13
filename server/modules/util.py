import random
import string
from typing import Optional, Tuple


def none_or_str(text: str) -> Optional[str]:
    """ Returns None if string is empty and the string otherwise """
    if text == "":
        return None

    return text
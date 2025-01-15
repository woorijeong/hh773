from typing import Final 

vowels: Final = "aeiouAEIOU" # 의미상 상수, 실제 재할당을 막지 못한다. 

def reverse(s: str) -> str:
    return s[::-1]

def upper(s: str) -> str:
    return s.upper()

def remove_vowels(s: str) -> str:
    return "".join([char for char in s if char not in vowels])

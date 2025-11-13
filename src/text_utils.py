import subprocess

def reverse_string(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Функция run_shell_command полностью удалена как небезопасная
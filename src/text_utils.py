import subprocess

# Намеренно нет аннотаций типов
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

# Намеренно небезопасный вызов для bandit
def run_shell_command(command):
    # Bandit должен обнаружить эту уязвимость!
    return subprocess.call(command, shell=True)
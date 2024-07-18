# The script defines a function to run a command and check if a specified text is in the command's output.
# e.g. It runs the command cat /etc/os-release to check the OS details and looks for the text Ubuntu 22.04.1 LTS in the output.
# It prints True if the text is found and the command executes successfully, otherwise it prints False.

import subprocess


def check_output_text(command, target_text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    print(out)
    if result.returncode == 0 and target_text in result.stdout:
        return True
    else:
        return False


command = 'cat /etc/os-release'
target_text = 'Ubuntu 22.04.1 LTS'
is_text_found = check_output_text(command, target_text)

print(is_text_found)

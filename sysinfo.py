#!/usr/bin/env python3

import platform

# Gather system profile information
profile = {
    "Architecture": platform.architecture(),
    "Libc Version": platform.libc_ver(),
    "Mac Version": platform.mac_ver(),
    "Machine": platform.machine(),
    "Node": platform.node(),
    "Platform": platform.platform(),
    "Processor": platform.processor(),
    "Python Build": platform.python_build(),
    "Python Compiler": platform.python_compiler(),
    "Python Version": platform.python_version(),
    "System": platform.system(),
    "Uname": platform.uname(),
    "Version": platform.version(),
}

# Check for Linux distribution information, handling newer Python versions
try:
    profile["Linux Distribution"] = platform.freedesktop_os_release()
except AttributeError:
    try:
        profile["Linux Distribution"] = platform.linux_distribution()
    except AttributeError:
        profile["Linux Distribution"] = "N/A"

# Print system profile information
for key, value in profile.items():
    print(f"{key}: {value}")

if __name__ == "__main__":
    # Optional: Could move the above code inside this block if you want it to only run when executed as a script.
    pass

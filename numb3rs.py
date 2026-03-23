import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    match = re.search(r"^([1-9]\d*|0)\.([1-9]\d*|0)\.([1-9]\d*|0)\.([1-9]\d*|0)$", ip)

    if not match:
        return False

    for part in match.groups():
        if int(part) not in range(0, 256):
            return False

    return True

if __name__ == "__main__":
    main()

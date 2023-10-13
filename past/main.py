import string
from random import choices
import argparse


def create_password(length=8, upper=False, lower=False, digit=False, pun=False):
    pool = ''
    if upper:
        pool += string.ascii_uppercase
    if lower:
        pool += string.ascii_lowercase
    if digit:
        pool += string.digits

    if pun:
        pool += string.punctuation

    if not pool:
        pool += string.ascii_letters
    return ''.join(choices(pool, k=length))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="password creator")
    parser.add_argument('length', type=int, help="Length of password")
    parser.add_argument('-u', '--upper', help="Upper case",
                        action='store_true')
    parser.add_argument("-l", "--lower", help="lower Case",
                        action='store_true')
    parser.add_argument("-d", "--digit", help="digit case",
                        action='store_true')
    args = parser.parse_args()
    print(create_password(args.length, args.upper, args.lower, args.digit))

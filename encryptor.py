#!/usr/bin/env python

"""
            DOOM-Encryptor-CLI
    For easy password encryption and storing
"""


import cryptocode as crypt
import argparse, sys, os, getpass


cli = argparse.ArgumentParser(usage='%(prog)s [option] [input] ...', description='--DOOM--\nSimple encryption command line interface')

# Method Argument, for encrypting or decrypting
cli.add_argument('-m', metavar='--method', help='Method to be used, encrypt, decrypt', required=True)

# Input file path for either text to be encrypted or decrypted
cli.add_argument('-i', metavar='--input', help='Input to be used for method, can be string or file location (must be absolute)', required=True)

# Output from method into file
cli.add_argument('-o', metavar='--output', help='Outputs into file / directory, if file is new include absolute path and filename')

# To check the input, acts as bool and way to read file and return it.
def checkin(input):
    if os.path.isfile(input):
            with open(input, 'r') as inputl:
                return inputl.read()
    else:
        return False
     
# writes the given strings to the output file, and checks it empty or filled.
def checkout(output, string):
    if os.path.isfile(output):
        with open(output, 'w') as output:
            output.write(f'\n{string}')
        return
    elif not os.path.isfile(output):
        with open(output, 'w') as output:
            output.write(f'{string}')
        return

def encrypt(string, outputl=None):
    if checkin(string):
        string = checkin(string)
    # Get Passwords
    pw = getpass.getpass("Enter Password: ")
    confirm = getpass.getpass("Confirm Password: ")
    # Do a password confirm, until the initial input and confirm input match.
    while pw != confirm:
        print('Passwords do not match. Try Again.')
        pw = getpass.getpass("Enter Password: ")
        confirm = getpass.getpass("Confirm Password: ")
    encryption = crypt.encrypt(string, pw)
    if outputl:
        checkout(outputl, encryption)
        return
    else:
        return print(f'{encryption}')

def decrypt(string, outputl=None):
    if checkin(string):
        string = checkin(string)
    pw = getpass.getpass("Enter Password: ")
    decryption = crypt.decrypt(string, pw)
    if decryption is False:
            return print('That passphrase doesn\'t decrypt that string')
        # If the decryption was successful check for a file path output, then write to that file or create a new one.
    else:
        if outputl == None:
            # If there is no output location just print the decrypted string.
            return print(f'{decryption}')
        elif outputl != None:
            checkout(outputl, decryption)
            return
            
args = cli.parse_args()

if args.m:
    if args.m.lower() == 'encrypt':
        if args.o:
            encrypt(args.i, args.o)
        if not args.o:
            encrypt(args.i)
    elif args.m.lower() == 'decrypt':
        if args.o:
            decrypt(args.i, args.o)
        if not args.o:
            decrypt(args.i)
    elif args.m.lower() != 'encrypt' or args.m.lower() != 'decrypt':
        print('Not a proper method. Please use encryptor --help for more information.')
        sys.exit()

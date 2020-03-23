#!/usr/bin/env python

import sys, random

# subprogram encodes checkerboard encodes text to numbers
def encode(text):
    checkerboard = { 'A': 0, 'T': 1, 'O': 3, 'N': 4, 'E': 5, 'S': 7, 'I': 8, 
            'R': 9, 'B': 20, 'C': 21, 'D': 22, 'F': 23, 'G': 24, 'H': 25, 
            'J': 26, 'K': 27, 'L': 28, 'M': 29, 'P': 60, 'Q': 61, 'U': 62, 
            'V': 63, 'W': 64, 'X': 65, 'Y': 66, 'Z': 67, '.': 68 }
    figures = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    numbers = []
    i = 0
    while i < len(text):
        ch = text[i]
        if (ch in checkerboard):
            numbers.append(checkerboard[ch])
        elif (ch in figures):
            numbers.append(69)
            while (ch in figures):
                numbers.append(int(ch))
                numbers.append(int(ch))
                numbers.append(int(ch))
                i = i + 1
                ch = text[i]
            numbers.append(69)
            numbers.append(checkerboard[ch])
        i = i + 1

    return numbers

# subprogram encrypts number encoded plaintext
def encrypt(plaintext):
    numbers = [ int(i) for i in plaintext ]
    pad = [ random.randint(0, 9) for i in range (len(numbers)) ]
    ciphertext = [ (x - y) % 10 for x, y in zip(numbers, pad) ]
    outfile = open('pad.dat', 'w')
    outfile.write( ''.join(str(n) for n in pad) )
    outfile.close()
    return ciphertext

# subprogram decrypts number encoded ciphertext
def decrypt(ciphertext):
    infile = open('pad.dat', 'r')
    pad = infile.read()
    infile.close()
    pad = [ int(i) for i in pad ]
    numbers = [ int(i) for i in ciphertext ]
    plaintext = [ (x + y) % 10 for x, y in zip(numbers, pad) ]
    return plaintext

# subprogram decodes number encoded plaintext
def decode(digits):
    checkerboard = { 0: 'A', 1: 'T', 3: 'O', 4: 'N', 5: 'E', 7: 'S', 8: 'I', 
            9: 'R', 20: 'B', 21: 'C', 22: 'D', 23: 'F', 24: 'G', 25: 'H', 
            26: 'J', 27: 'K', 28: 'L', 29: 'M', 60: 'P', 61: 'Q', 62: 'U', 
            63: 'V', 64: 'W', 65: 'X', 66: 'Y', 67: 'Z', 68: '.' }
    
    numbers = []
    n = 0;
    while n < len(digits):
        ch = digits[n]
        if ch == '2' or ch == '6':
            tmp = int(digits[n] + digits[n+1])
            numbers.append( tmp )
            n += 2
            #if n >= len(digits): break
            if tmp == 69:
                while digits[n] == digits[n+1] == digits[n+2]:
                    numbers.append(int(digits[n]))
                    numbers.append(int(digits[n]))
                    numbers.append(int(digits[n]))
                    n += 3
                numbers.append(69)
                n += 1
        else:
            numbers.append( int(digits[n]) )
            n += 1

    text = []
    n = 0
    while n < len(numbers):
        # print checkerboard[numbers[n]],
        if numbers[n] == 69:
            n += 1
            while numbers[n] != 69:
                text.append(str(numbers[n]))
                n += 3
            n += 1
        else:
            text.append(checkerboard[numbers[n]])
        n += 1
    
    return text

# subprogram prints numbers by groups
def print_groups(numbers):
    digits = ''.join(map(str, numbers))
    for n in range(0, len(digits), 5):
        print digits[n:n+5],
        if (n + 5) % 25 == 0: print

# main program
# check no. of command line arguments
if (len(sys.argv) < 3):
    print "Usage: " + sys.argv[0] + " filename encode|encypt|decrypt|decode"
    sys.exit(1)
infile = sys.argv[1]
flag = sys.argv[2]

# check flag validity
if (flag != 'encode' and flag != 'encrypt' and flag != 'decrypt' and flag != 'decode'):
    print "Usage: " + sys.argv[0] + " encode|encypt|decrypt|decode"
    sys.exit(1)    

# read file
text = []
filehandle = open(infile, 'r')
while True:
    ch = filehandle.read(1)
    if not ch: break
    if ch.isupper() or ch.isdigit() or ch == '.': text.append(ch)
    elif ch.islower(): text.append(ch.upper())
filehandle.close()

# main processing block
if flag == 'encode':
    print_groups(encode(text))
elif flag == 'encrypt':
    print_groups(encrypt(text))
elif flag == 'decrypt':
    print_groups(decrypt(text))
elif flag == 'decode':
    print_groups(decode(text))

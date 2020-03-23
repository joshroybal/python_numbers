@echo on
otp.py %1 encode > plaintext.dat
otp.py plaintext.dat encrypt > ciphertext.dat
otp.py ciphertext.dat decrypt > plaintext.dat
otp.py plaintext.dat decode > plaintext.txt

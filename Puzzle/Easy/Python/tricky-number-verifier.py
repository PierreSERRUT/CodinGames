#tricky-number-verifier
#python

import sys
import math

def check_date(date):
    month_31=[1,3,5,7,8,10,12]
    month_30=[4,6,9,11]

    d=int(date[:2])
    m=int(date[2:4])
    bisex=int(date[4:])%4

    if d == 0:      return 1
    if m == 2: 
        if (d > 28 and bisex != 0) or d > 29: 
                    return 1
    elif m in month_31:
        if d > 31:  return 1 
    elif m in month_30:
        if d > 30:  return 1 
    else:           return 1
    return 0

n = int(input())
incorrect = ['0']*n
identifier = []
check_digit = []
birthday = []

for i in range(n):
    number = input()
    try:
        identifier.append(number[:3])
        check_digit.append(number[3:4])
        birthday.append(number[4:])
    except:
        if len(identifier)!=i+1: identifier.append(0)
        if len(check_digit)!=i+1: check_digit.append(0)
        if len(birthday)!=i+1: birthday.append(0)

    if len(number) != 10 or not number.isnumeric() or identifier[i][0]=='0': 
        incorrect[i] = 'S'

for i in range(n):
    if incorrect[i] == '0':
        if check_date(birthday[i]):
            incorrect[i] = 'D'
    
    if incorrect[i] == '0':
        b = birthday[i]
        test_digit = 10

        while test_digit == 10:
            ide = identifier[i]
            test_digit = int(ide[0])*3+int(ide[1])*7+int(ide[2])*9+int(b[0])*5+int(b[1])*8+int(b[2])*4+int(b[3])*2+int(b[4])+int(b[5])*6
            test_digit = test_digit % 11
            
            if test_digit == 10: 
                identifier[i] = str(int(identifier[i])+1)
                incorrect[i] = 'M'
            
            elif int(check_digit[i]) != test_digit:
                check_digit[i]=str(test_digit)
                incorrect[i] = 'M'

    if incorrect[i] == '0':
        print('OK')
    elif incorrect[i] == 'S':
        print('INVALID SYNTAX')
    elif incorrect[i] == 'D':
        print('INVALID DATE')
    elif incorrect[i] == 'M':
        print(identifier[i]+check_digit[i]+birthday[i])
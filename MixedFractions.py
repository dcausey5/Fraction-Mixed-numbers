# Damariel Causey

'''Program will ask user for numerator and denominator then will run and find if proper or improper

The the program will decided if the fraction is mixed and if it can be reduced

'''
import math

numerator = int(input('Enter a postive number for numerator:'))
while numerator <= 0:
    numerator = int(input('Invaild score. Re-enter a postive number for numerator:'))
denominator = int(input('Enter a postive number for denominator:'))
while denominator <= 0:
    denominator = int(input('Invaild score. Re-enter a postive number for denominator:'))

c = numerator // denominator
f = numerator % denominator

if denominator > numerator:
    print('{}/{} Proper Fraction'.format(numerator, denominator))
    num_denominator = denominator
    b = numerator
    p = math.gcd(num_denominator, b)
    numerator = numerator // p
    denominator = denominator // p

    print('{}/{} Proper Fraction'.format(numerator, denominator))

else:
    print('improper fraction')
    if numerator < denominator:
        num_denominator = denominator
        b = numerator
        p = math.gcd(num_denominator, b)
        numerator = numerator // p
        denominator = denominator // p
        print('{}/{} improper Fraction'.format(numerator, denominator))
    else:
        print('cannot be reduced')

        if numerator > denominator:
            num_denominator = denominator
            b = numerator
            p = math.gcd(num_denominator, b)
            numerator = numerator // p
            denominator = denominator // p
            print('The mixed number is {} and {}/{}'.format(c, f, denominator))
        else:
            print('cannot be reduced')

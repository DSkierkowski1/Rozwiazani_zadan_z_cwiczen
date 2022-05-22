#ćwiczenia 1
# from math import *
# #zad4 napisz skrypt liczący i wyświetlający poszczególne wyrażenia
# a = exp(10)
#
# print(a)
# sinus = sin(8)**2
# logarytm = log(5 + sinus) ** (1/6)
# # b = pow(logarytm, 1/6)
# print(logarytm)
#
# c = floor(3.55)
# print(c)
# d = ceil(4.8)
# print(d)
# #zad5
# imie = "RADOSŁAW"
# nazwisko = "CYBULSKI"
# print(imie.capitalize() + " " + nazwisko.capitalize())
# #Zad6
# napis = "la la la la"
# print(napis.count("la"))
# #Zad7
# napis1 = "teskst do sprawdzenie"
# print(napis1[1], napis1[len(napis1)-1])
# #Zad8
# print(napis.split())
# #Zad9
# napis2 = "Jest dziś czwartek"
# print("Jaki mamy dziś dzień? %s " % napis2)
# liczba = 5.677
# print("twoja liczba to: %(z1).2f" % {'z1': liczba})
# liczba_szesnastkowo = 0xf351
# print(liczba_szesnastkowo)
# print("%x" % liczba_szesnastkowo)
#ćwiczenia 2

# import sys
# import math

# zad1
# sporty = ['piłka nożna', 'siatkówka', 'skoki narciarskie']
# print(sporty)
# sporty.reverse()
# sporty.append('koszykówka')
# print(sporty)
# # zas2, 3
# skroty = {'np': 'na przykład', 'pt': 'pod tytułem'}
# print(skroty)
# print(len(skroty))
#
# #zad4
# zdanie = input('wpisz komunikat: ')
# print(zdanie.count('a'))
#
# # zad5
# sys.stdout.write('podaj a: ')
# a = sys.stdin.readline()
# sys.stdout.write('podaj b: ')
# b = sys.stdin.readline()
# sys.stdout.write('podaj c: ')
# c = sys.stdin.readline()
# a = int(a)
# b = int(b)
# c = int(c)
# sys.stdout.write(str(math.pow(a, b) + c))
#
# # zad6
# a = input("Wprowadź liczbę a: ")
# b = input("Wprowadź liczbę b: ")
# c = input("Wprowadź liczbę c: ")
#
# a = int(a)
# b = int(b)
# c = int(c)
# if a == b == c:
#     print("wprowadziłeś trzy takie same liczby")
# elif a >= b:
#     if a > c:
#         print("liczba",a,"jest największa")
#     else:
#         print("liczba",c, "jest największa")
# elif b > a:
#     if b > c:
#         print("liczba",b,"jest największa")
#     else:
#         print("liczba",c, "jest największa")
#
# # zad7
# lista = [5, 4, 2.6, 8, 4.1, 3]
# for a in lista:
#     print(a**2)
#
# # zad8
# licznik = 0
# liczby_pazyste = []
# while licznik < 10:
#     try:
#         liczba = input('wprowadź liczbę: ')
#         if float(liczba):
#             liczba = float(liczba)
#             if liczba % 2 == 0:
#                 liczby_pazyste.append(liczba)
#                 licznik += 1
#     except ValueError:
#         print('nie wczytano liczby')
# print(liczby_pazyste)
# print(len(liczby_pazyste))

# zad9
# a = input('podaj liczbę: ')
# try:
#     a = int(a)
#     pierwiastek = math.sqrt(a)
#     print(pierwiastek)
# except ValueError:
#     if type(a) != int:
#         print('nie wczytano liczby')
#     elif a < 0:
#         print('liczba a nie może być mniejsza od 0')
##ćwiczenia 3
import random
from math import *

# import ciagi.arytmetyczny
# from ciagi import *

# lab3
# zad1
# a = [1-x for x in range(1, 11)]
# b = [4**x for x in range(0, 8)]
# c = [x for x in b if x % 2 == 0]
# print(a)
# print(b)
# print(c)
# zad2
# lista1 = []
# licznik = 0
# while licznik != 10:
#     a = random.randint(0, 100)
#     lista1.append(a)
#     licznik += 1
# print(lista1)
# nowa_lista = [x for x in lista1 if x % 2 == 0]
# print(nowa_lista)
# zad3
# slownik = {'mleko': 'sztuki', 'ziemiaki': 'kg', 'jogurt': 'sztuki'}
# lista = [key for key in slownik.keys() if slownik[key] == 'sztuki']
# print(lista)
# zad4
# def trojkat_prostokatny(a, b, c):
#     if a**2 + b**2 == c**2:
#         return 'trójtkąt prostokątny'
#     else:
#         return 'trójkąt nie jest prostokątny'
# print(trojkat_prostokatny(3, 4, 5))
# zad5
# def pole_trapezu(a=6,b=3,h=5):
#     return (a+b)*h/2
# print(pole_trapezu())
# # zad6
# def iloczyn(a=1, b=4, ile=10):
#     licznik = 0
#     while licznik != ile:
#         a *= b
#         licznik += 1
#     return a
# print(iloczyn())
# #zad7
# def iloczyn2(*liczby, b):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn_liczb = liczby[0] * b
#         for a in range(1, len(liczby), 1):
#             iloczyn_liczb *= b
#         return iloczyn_liczb
# print(iloczyn2(1,2,3,4,5,6,7,8,9,10,b=4))
# zad8
# def lista_zakupow(** rzeczy):
#     koszt_zakupow = 0
#     for koszt in rzeczy:
#         koszt_zakupow += rzeczy[koszt]
#     return len(rzeczy), round(koszt_zakupow,2)
# print(lista_zakupow(mleko=2.78, czekolada=5.40, kawa=22.99))
# zad9
##suma ciągu geometrycznego
#def n_ty_wyraz(a1, q, n):
#     return a1 * q**(n-1)
#
#
# def suma(a1, n, q):
#     if q == 1:
#         return a1*n
#     else:
#         return a1 * (1-q**n)/(1-q)
#suma ciągu arytmetycznego
# def n_ty_wyraz(a1, n, r):
#     return a1 + (n-1)*r
#
#
# def suma_ciagu(a1, an, n):
#     return (a1+an)/2*
# print(arytmetyczny.n_ty_wyraz(6, 6, 2))
# print(arytmetyczny.suma_ciagu(6, 16, 6))
# print(geometryczny.n_ty_wyraz(1, 4, 11))
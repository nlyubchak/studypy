#!/usr/bin/python3
# -*- coding: utf-8 -*-

Format  = 'N = {0:04d}, K = {1}' # в {} записывется то над чем работают
                                 # 0:04d - десятичн и 4 цифры после зап.
Format2 = 'N - {N}, K = {K}' # . - вываодим вещ. часть числа

Str  = Format.format( 12, 12.0 ) # разбирается по местам..
Str2 = Format2.format ( N=1, K=0+5j ) # данные соспоставляются по именам

N = 6
K = 10
Str3 = Format2.format( **locals() ) # Возвращает ссылку на словарь данного контекста (модуль для)

print(Str )
print(Str2 )
print(Str3 )

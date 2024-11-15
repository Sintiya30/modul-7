#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:02:39 2024

@author: adesintia
"""

# Fungsi untuk memeriksa apakah suatu bilangan prima
def is_prime(n):
    if n <= 1:
        return False  # Bilangan kurang dari atau sama dengan 1 bukan prima
    for i in range(2, int(n**0.5) + 1):  # Cek dari 2 hingga akar dari n
        if n % i == 0:
            return False  # Jika ada faktor lain selain 1 dan n, maka bukan prima
    return True  # Jika tidak ada faktor, maka bilangan prima

# Fungsi untuk memeriksa dan mencetak hasil
def check_prime(number):
    if is_prime(number):
        print(f"{number} adalah bilangan prima.")
    else:
        print(f"{number} bukan bilangan prima.")

# Contoh penggunaan
number = int(input("Masukkan sebuah bilangan: "))
check_prime(number)

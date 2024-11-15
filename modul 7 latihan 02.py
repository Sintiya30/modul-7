#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:08:57 2024

@author: adesintia
"""

def convert_to_ordinal(number):
    if 11 <= number <= 13:
        return f"{number}th"
    
    last_digit = number % 10
    if last_digit == 1:
        return f"{number}st"
    elif last_digit == 2:
        return f"{number}nd"
    elif last_digit == 3:
        return f"{number}rd"
    else:
        return f"{number}th"

def main():
    try:
        while True:
            user_input = int(input("Masukkan angka (0 untuk keluar): "))
            
            if user_input == 0:
                print("Program selesai")
                break
            
            ordinal_form = convert_to_ordinal(user_input)
            print(f"Angka: {user_input}")
            print(f"{ordinal_form} //output")
            
    except ValueError:
        print("Masukkan angka yang valid!")

if __name__ == "__main__":
    main()
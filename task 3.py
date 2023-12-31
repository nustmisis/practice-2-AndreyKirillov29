# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:05:53 2023

@author: workk



Упражнение 61. Действительный номерной знак машины?
(Решено. 28 строк)
Допустим, в  нашей стране старый формат номерных знаков автомобилей состоял из трех заглавных букв, следом за которыми шли три цифры. 
После того как все возможные номера были использованы, формат был 
изменен на четыре цифры, предшествующие трем заглавным буквам.
Напишите программу, запрашивающую у пользователя номерной знак 
машины и оповещающую о том, для какого формата подходит данная последовательность символов: для старого или нового. Если введенная последовательность не соответствует ни одному из двух форматов, укажите 
это в сообщении
"""
import re
number_plate = input("Введите номерной знак машины: ")
old_format_pattern = r"^[A-Z]{3}\d{3}$"
if re.match(old_format_pattern, number_plate):
    print("Введенный номерной знак соответствует старому формату.")
    exit()
new_format_pattern = r"^\d{4}[A-Z]{3}$"
if re.match(new_format_pattern, number_plate):
    print("Введенный номерной знак соответствует новому формату.")
    exit()
print("Введенный номерной знак не соответствует ни одному из форматов.")
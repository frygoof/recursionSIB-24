# def print_numbers_from_1_to_n(n):
#     if n < 1:
#         return
#     else:
#         print(n, end=' ')
#         print_numbers_from_1_to_n(n - 1)
# n = int(input("Введите натуральное число: "))
# print_numbers_from_1_to_n(n)
#
#
#
# def ackermann(m, n):
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return ackermann(m - 1, 1)
#     elif m > 0 and n > 0:
#         return ackermann(m - 1, ackermann(m, n - 1))
# m = int(input("Введите значение m: "))
# n = int(input("Введите значение n: "))
# result = ackermann(m, n)
# print(f'Результат функции Аккермана для m = {m} и n = {n} равен {result}')
#
#
#
# def print_numbers_in_range(A, B):
#     if A == B:
#         print(A)
#     elif A < B:
#         print(A)
#         print_numbers_in_range(A + 1, B)
#     else:
#         print(A)
#         print_numbers_in_range(A - 1, B)
# A = int(input("Введите число A: "))
# B = int(input("Введите число B: "))
# print_numbers_in_range(A, B)
#
#
#
# def is_power_of_two(N):
#     if N == 1:
#         return "YES"
#     elif N % 2 == 0 and N > 1:
#         return is_power_of_two(N // 2)
#     else:
#         return "NO"
# N = int(input("Введите натуральное число N: "))
# result = is_power_of_two(N)
# print(result)
#
#
#
# def sum_of_digits(N):
#     if N == 0:
#         return 0
#     else:
#         return N % 10 + sum_of_digits(N // 10)
# N = int(input("Введите натуральное число N: "))
# result = sum_of_digits(N)
# print("Сумма цифр числа N:", result)
#
#
#
# def sum_of_digits(N):
#     if N == 0:
#         return 0
#     else:
#         return N % 10 + sum_of_digits(N // 10)
# N = int(input("Введите натуральное число N: "))
# result = sum_of_digits(N)
# print("Сумма цифр числа N:", result)
#
#
#
# def print_digits_reversed(N):
#     if N < 10:
#         print(N)
#     else:
#         last_digit = N % 10
#         print(last_digit)
#         print_digits_reversed(N // 10)
# N = int(input("Введите натуральное число N: "))
# print("Цифры числа N в обратном порядке:")
# print_digits_reversed(N)
#
#
#
# def print_digits(N):
#     if N >= 10:
#         print_digits(N // 10)
#     print(N % 10)
#
# N = int(input("Введите натуральное число N: "))
# print("Цифры числа N в обычном порядке:")
# print_digits(N)
#
#
#
# import math
# def is_prime(n, divisor=2):
#     if n < 2:
#         return "NO"
#     if n == 2:
#         return "YES"
#     if n % divisor == 0:
#         return "NO"
#     if divisor * divisor > n:
#         return "YES"
#     return is_prime(n, divisor + 1)
# n = int(input("Введите натуральное число n (>1): "))
# result = is_prime(n)
# print(result)
#
#
#
# import math
# def prime_factors(n):
#     while n % 2 == 0:
#         print(2)
#         n = n // 2
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         while n % i == 0:
#             print(i)
#             n = n // i
#     if n > 1:
#         print(n)
# n = int(input("Введите натуральное число n (>1): "))
# print("Простые делители числа n:")
# prime_factors(n)
#
#
#
# def is_palindrome(word):
#     word = word.lower()
#     if len(word) <= 1:
#         return "YES"
#     if word[0] != word[-1]:
#         return "NO"
#     return is_palindrome(word[1:-1])
# word = input("Введите слово: ")
# result = is_palindrome(word)
# print(result)
#
#
#
# def print_odd_numbers():
#     n = int(input())
#     if n == 0:
#         return
#     if n % 2 == 1:
#         print(n)
#     print_odd_numbers()
# print("Введите последовательность натуральных чисел (0 для завершения):")
# print_odd_numbers()
#
#
#
# def print_alternate_numbers(is_odd=True):
#     n = int(input())
#     if n == 0:
#         return
#     if is_odd:
#         print(n)
#     print_alternate_numbers(not is_odd)
# print("Введите последовательность натуральных чисел (0 для завершения):")
# print_alternate_numbers()
#
#
#
# def find_max():
#     n = int(input())
#     if n == 0:
#         return 0
#     else:
#         max_rest = find_max()
#         return max(n, max_rest)
# print("Введите последовательность натуральных чисел (0 для завершения):")
# result = find_max()
# print("Наибольшее значение в последовательности:", result)
#
#
#
# def calculate_average():
#     n = int(input())
#     if n == 0:
#         return (0, 0)
#     else:
#         count, total = calculate_average()
#         return (count + 1, total + n)
# print("Введите последовательность натуральных чисел (0 для завершения):")
# count, total = calculate_average()
# if count > 0:
#     average = total / count
#     print("Среднее значение элементов:", average)
# else:
#     print("Последовательность не содержит чисел, кроме нуля.")
#
#
#
#     def count_max_element():
#         n = int(input())
#         if n == 0:
#             return (0, 0)
#         else:
#             count, max_val = count_max_element()
#             if n > max_val:
#                 return (1, n)
#             elif n == max_val:
#                 return (count + 1, max_val)
#             else:
#                 return (count, max_val)
#     print("Введите последовательность натуральных чисел (0 для завершения):")
#     count, max_val = count_max_element()
#     print("Количество элементов, равных наибольшему:", count)
#
#
#
#     def count_ones():
#         n = int(input())
#         if n == 0:
#             return 0
#         if n == 1:
#             count = count_ones()
#             return count + 1
#         return count_ones()
#     print("Введите последовательность натуральных чисел (два нуля для завершения):")
#     count = count_ones()
#     print("Число 1 встречается", count, "раз.")
#
#
#
#     n = int(input("Введите n: "))
#     current_number = 1
#     count = 0
#     for i in range(1, n + 1):
#         for j in range(i):
#             if count >= n:
#                 break
#             print(current_number, end=" ")
#             count += 1
#         current_number += 1
#
#
#
# def count_numbers(k, s, current_sum=0, current_number=0, position=0):
#     if position == k:
#         if current_sum == s:
#             return 1
#         else:
#             return 0
#     count = 0
#     start_digit = 1 if position == 0 else 0
#     for digit in range(start_digit, 10):
#         new_sum = current_sum + digit
#         if new_sum <= s:
#             new_number = current_number * 10 + digit
#             count += count_numbers(k, s, new_sum, new_number, position + 1)
#     return count
# k = int(input("Введите k: "))
# s = int(input("Введите s: "))
# result = count_numbers(k, s)
# print("Количество", k, "-значных натуральных чисел с суммой цифр", s, "равно", result)
#
#
#
# def count_sequences(a, b):
#     if a == 0 or b == 0:
#         return 1
#     else:
#         return count_sequences(a - 1, b) + count_sequences(a, b - 1)
# a = int(input("Введите количество нулей (a): "))
# b = int(input("Введите количество единиц (b): "))
# result = count_sequences(a, b)
# print("Количество последовательностей:", result)
#
#
#
# def reverse_number(n, reversed_n=0):
#     if n == 0:
#         return reversed_n
#     else:
#         last_digit = n % 10
#         reversed_n = reversed_n * 10 + last_digit
#         return reverse_number(n // 10, reversed_n)
# n = int(input("Введите число: "))
# reversed_n = reverse_number(n)
# print("Число в обратном порядке:", reversed_n)


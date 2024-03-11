#Игорь составляет таблицу кодовых слов для передачи сообщений, 
#каждому сообщению соответствует своё кодовое слово. В качестве кодовых слов Игорь использует трёхбуквенные слова, 
#в которых могут быть только буквы Ш, К, О, Л, А, причём буква К появляется ровно 1 раз. 
#Каждая из других допустимых букв может встречаться в кодовом слове любое количество раз или не встречаться совсем.
#Сколько различных кодовых слов может использовать Игорь?

from itertools import product

def count_code_words():
    valid_letters = ['Ш', 'К', 'О', 'Л', 'А']
    count = 0

    for p in product(valid_letters, repeat=3):
        if p.count('К') == 1:
            count += 1

    return count

# Используем функцию для подсчета различных кодовых слов
total_code_words = count_code_words()
print(f"Игорь может использовать {total_code_words} кодовых слов.")
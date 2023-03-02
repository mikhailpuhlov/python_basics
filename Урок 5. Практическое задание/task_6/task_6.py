"""
6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re

subjects_dict = {}
with open('less5_t6_diction.txt', 'r', encoding='UTF-8') as df:
    text = df.read()
    df.seek(0)
    for i in df:
        r_types = i.split(': ')
        hours = re.findall(r"\d+", r_types[1])
        subjects_dict.update({r_types[0]: sum([int(i) for i in hours])})
print(f'Словарь:\n {subjects_dict}')
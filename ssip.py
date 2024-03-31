#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import sys

def create_directory_structure(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    group_name = lines[0].strip()
    num_practices = int(lines[1].strip())

    # Директория группы
    group_directory = os.path.join(os.getcwd(), group_name)
    os.makedirs(group_directory, exist_ok=True)

    common_directories = ['практика', 'контрольная_работа', 'курсовая_работа', 'сессия', 'билеты']
    for directory in common_directories:
        os.makedirs(os.path.join(group_directory, directory), exist_ok=True)

    # Информация о студентах
    student_info = lines[2:]
    
    for info in student_info:
        # Проходим по каждому студентику
        info = info.strip().split()
        surname = info[0]
        student_directory = os.path.join(group_directory, surname)
        os.makedirs(student_directory, exist_ok=True)

        with open(os.path.join(student_directory, 'README.TXT'), 'w') as readme_file:
            readme_file.write(" ".join(info))

        # Директории практик
        for i in range(1, num_practices+1):
            practice_directory = os.path.join(student_directory, f'практика{i:02}')
            os.makedirs(practice_directory, exist_ok=True)

        # Ну и остальные директории
        other_directories = ['Контрольная_работа', 'Курсовая_работа', 'Сессия']
        for directory in other_directories:
            os.makedirs(os.path.join(student_directory, directory), exist_ok=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # 2 аргумента поскольку пример ввода выглядит так:
        # python script.py input_file.txt
        print("Пример ввода: python script.py input_file.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    create_directory_structure(input_file)


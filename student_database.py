from student_database import save_db, load_db, get_student, add_student, put_rating
# from teacher import add_student, put_rating
# from student import see_rating

def controller():
    load_db()
    print('Выберите режим работы : ')
    print('1. Учитель\n2. Ученик\n0. Выход')
    mode = int(input('Введите пункт меню: '))
    while mode == 1:
        print('Что хотите сделать?\n\n1 - записать ученика\n2 - выставить оценку\n0 - выйти из программы')
        act = int(input('Выберите пункт меню: '))
        if act == 1:
            add_student()
        elif act == 2:
            put_rating()
        elif act == 0:
            mode = 0
    else:
        save_db()  

    while mode == 2:
        last_name = input('Введите фамилию ученика или 0 для выхода\nВовд: ')
        if last_name == '0':
            mode = 0
        else:
            get_student(last_name)
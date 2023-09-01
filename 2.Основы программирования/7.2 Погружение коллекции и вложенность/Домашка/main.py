from functions import load_students, load_professions, get_student_by_pk, get_profession_by_title, check_fitness

user_name = int(input("Введите номер студента\n"))

if user_name == get_student_by_pk(user_name):
   print(get_student_by_pk(user_name))

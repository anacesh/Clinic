from Clinic import Clinic, Doctor

print ('Работа с новой поликлиникой. \n'
       'Введите название: ', end='')
name = input()
TClinic = Clinic(name)

while True:
    print('\n'
          '1. Добавить врача.\n'
          '2. Изменить ищформацию о враче.\n'
          '3. Вывод всей информации.\n'
          '4. Выход.\n')
    try:
        choice = int(input('Введите команду: '))
        if choice == 1:
            TClinic.AddDoctor()
        if choice == 2:
            TClinic.ChangeDoctorInfo()
        if choice == 3:
            TClinic.PrintInfo()
        if choice == 4:
            break
    except:
        print ('Ошибка ввода. ')
        break
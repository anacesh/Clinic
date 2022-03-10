class Clinic():
    def __init__(self, name): # создание контейнера поликлиника
        self.name = name
        self.doctors = []

    def AddDoctor(self):
        name = input('Введите фамилию нового доктора: ')
        TDoctor = Doctor(name)
        self.doctors.append(TDoctor)

    def ChangeDoctorInfo(self):
        name = input('Введите фамилию доктора, информацию о котором хотите заменить: ')
        Flag = False
        for a in self.doctors:
            if a.name == name:
                print ('Доктор',name,'найден.')
                DoctorFind = a
                Flag = True


        if Flag == False:
            print ('Доктор',name,'не найден. \n')
            return

        DoctorFind.change_info()

    def PrintInfo(self):

        sum_patients = 0
        average_patients = 0

        for a in self.doctors:
            a.print_information()
            sum_patients += sum(a.day_patients)
            average_patients += (sum(a.day_patients)/len(a.day_patients))

        print ('Общее количество пациентов:', sum_patients, '\nСреднее количество пациентов по клинике:', average_patients)


class Doctor():
    def __init__(self, name):   # инициалихация объекта с передачей имени
        self.name = name
        self.day_patients = []      # в дальнейшем будет содержать кол-во пациентов по дням

    def change_info(self):
        while True:
            choice = int(input('\n1. Добавить информацию о пациентах.\n'
                               '2. Изменить информацию о пациентах.\n'
                               '3. Вывести всю информацию о докторе.\n'
                               '4. Выход.\n'
                               'Введите команду: '))
            if choice == 1:
                self.add_patients()
            elif choice == 2:
                self.change_patient()
            elif choice == 3:
                self.print_information()
            else:
                break

    def add_patients(self):
        print('\nДля выхода в меню введите -1.')
        while True:
            print ('Добавление количества пациентов в', len(self.day_patients)+1,'день: ', end='')

            # небольшая обработка ошибок с добавлением возможности выхода в меню
            try:
                new_patients = int(input())
                if new_patients == -1:
                    return
                self.day_patients.append(new_patients)
            except:
                print ('Некорректный ввод, ожидалось число.')

    def change_patient(self):
        print ('Введено информации о', len(self.day_patients), 'днях. \nВведите номер дня для изменения: ', end='')

        try:
            day_num = int(input())
            if day_num > len(self.day_patients):
                print ('Некорректный ввод.')
                return
            if day_num == -1:
                return

            try:
                new_info = int(input('Введите новое значение: '))
                self.day_patients[day_num-1] = new_info
            except:
                print ('Некорректный ввод. Введите число пациентов.')

        except:
            print ('Некорректный ввод. Введите номер дня.')

    def print_information(self):
        print ('\n', self.name, self.day_patients)
        if len(self.day_patients) == 0:
            print ('Нет информации о пациентах.')
        else:
            print ('Суммарно пациентов:', sum(self.day_patients),
                   '\nПациентов в среднем по дням:',sum(self.day_patients)/len(self.day_patients)), '.4f'
def ask_for_id():
    global isikukood
    while True:
        idcode = input('Please enter your national id or "stop" to exit: ')
        if idcode == 'stop':
            quit()
        if idcode.isdecimal():
            if len(idcode) != 11:
                if len(idcode) < 11:
                    print('ID you entered is too short.')
                    continue
                else:
                    print('ID you entered is too long.')
                    continue
            else:
                isikukood = idcode
                break
        else:
            print('ID you entered is not numeric!')
            continue


def get_gender():
    n = isikukood[0]
    if n not in '09':
        if int(n) % 2 == 0:
            print('you are female')
        else:
            print('you are male')
    else:
        print('something wrong with your id')


def get_date_of_birth():
    day = isikukood[5:7]
    month = isikukood[3:5]
    year = isikukood[1:3]
    bcent = ''

    n = isikukood[0]
    if n not in '09':
        if n in '12':
            bcent= '18'
        elif n in '34':
            bcent = '19'
        elif n in '56':
            bcent = '20'
        elif n in '78':
            bcent = '21'
        print(f'{day}.{month}.{bcent}{year}')

    else:
        print('something wrong with your id')




# idcode = '38803160272'

def menu():
    ask_for_id()
    # if ask_for_id == '0':
    while True:
        user_choice = input('Please choose: \n'
                            '1. Gender\n'
                            '2. Date of birth\n'
                            '3. birth region\n'
                            '4. Validation\n'
                            '5. change ID\n'
                            '0. Exit\n'
                            '-->')
        if user_choice == '1':
            get_gender()
        elif user_choice == '2':
            get_date_of_birth()
        elif user_choice == '3':
            print(3,isikukood)
        elif user_choice == '4':
            print(4,isikukood)
        elif user_choice == '5':
            ask_for_id()
        elif user_choice == '0' or user_choice == 'stop':
            break
        else:
            print('Choice out of range')

isikukood = ''
menu()
import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()


def wyswietlenie(studentList):
    for students in studentList:
        print(f'{students}')


def wczytaj():
    student_List = []
    filepath = "students0.txt"
    with open(filepath, 'r') as file_object:
        for line in file_object:
            x = line.rstrip().split(',')
            if len(x) == 4:
                student_List.append(getStudent(x[0], x[1], x[2], x[3], '', ''))
            elif len(x) == 5:
                student_List.append(getStudent(x[0], x[1], x[2], x[3], x[4], ''))
            else:
                student_List.append(getStudent(x[0], x[1], x[2], x[3], x[4], x[5]))
    file_object.close()
    return student_List


def zapisz(student_List):
    filepath = "students0.txt"
    with open(filepath, 'w') as file_object:
        for students in student_List:
            if students["ocena"] is None:
                students["ocena"] = ''
            if students["status"] is None:
                students["status"] = ''
            line = f'{students["email"]},{students["imie"]},{students["nazwisko"]},{students["punkty"]},{students["ocena"]},{students["status"]}\n'
            file_object.write(line)
    file_object.close()


def autoOcena(student):
    value = int(student["punkty"])
    if value <= 50:
        return 2
    elif value <= 60:
        return 3
    elif value <= 70:
        return 3.5
    elif value <= 80:
        return 4
    elif value <= 90:
        return 4.5
    elif value > 91:
        return 5


def addStudent(studentList):
    line = input("Podaj studenta w nastepujacy sposob: email,imie,nazwisko,punkty,(opcjonalne)ocena,(opcjonalne)status")
    line = line.rstrip().split(',')
    if line[0] in [students['email'] for students in studentList]:
        print("Jest taki email, powrot do opcji wyboru")
    if len(line) < 4:
        print("Podano za malo informacji, powrot do opcji wyboru")
        return studentList
    elif len(line) == 4:
        studentList.append(getStudent(line[0], line[1], line[2], line[3], '', ''))
        print("Pomyslnie dodano studenta")
        return studentList
    elif len(line) == 5:
        studentList.append(getStudent(line[0], line[1], line[2], line[3], line[4], ''))
        print("Pomyslnie dodano studenta")
        return studentList
    else:
        studentList.append(getStudent(line[0], line[1], line[2], line[3], line[4], line[5]))
        print("Pomyslnie dodano studenta")
        return studentList


def deleteStudent(studentList):
    line = input("Podaj email studenta")
    for i, students in enumerate(studentList):
        if line == students["email"]:
            print("Usunieto pomyslnie studenta ", studentList.pop(i))
            return studentList
    print("Nie ma studenta o takim emailu. Powrot do okna wyboru.")
    return studentList


def getStudent(v1, v2, v3, v4, v5, v6):
    students = {"email": v1, "imie": v2, "nazwisko": v3, "punkty": v4, "ocena": v5, "status": v6}
    return students


decision = 'T'
i = 0
student_List = wczytaj()
while decision == 'T':
    decision2 = input("Wybierz nastepujace opcje:\n1: Wyswietl informacje o studentach\n2: Automatycznie wystaw "
                      "oceny\n3: Dodaj/Usun studenta\n4: Wyslij maila\n5: Zakoncz dzialanie programu")
    if decision2 == '1':
        wyswietlenie(student_List)
    elif decision2 == '2':
        for student in student_List:
            if student["status"] != 'GRADED' or student["status"] != 'MAILED':
                student["ocena"] = autoOcena(student)
                student["status"] = 'GRADED'
        zapisz(student_List)
    elif decision2 == '3':
        decision3 = input("D - dodanie, U - usuniecie")
        if decision3 == 'D':
            student_List = addStudent(student_List)
        elif decision3 == 'U':
            student_List = deleteStudent(student_List)
        else:
            print("Nie wybrano wlasciwej opcji, powort do glownego menu")
        zapisz(student_List)
    elif decision2 == '4':
        for student in student_List:
            if student['status'] != 'MAILED':
                send_email("Ocena", student["ocena"], student["email"], "przykladowyEmail@gmail.com", "hasloMaslo")
                print("Wyslano maila do",student['imie'],student['nazwisko'])
    elif decision2 == '5':
        decision = 'N'
        print("Program zakonczyl sie")
    else:
        print("Wybrano zla opcje, prosze dokonac ponownego wyboru")

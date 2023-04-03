import smtplib
def wyswietlenie(studentList):
    for students in studentList:
        print(f'{students}')

def ocena(student):
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


def student(v1, v2, v3, v4, v5):
    students = {"email": v1, "imie": v2, "nazwisko": v3, "punkty": v4, "status": v5}
    return students


decision = 'T'
i = 0
student_List = []
filepath = "students.txt"
with open(filepath) as file_object:
    for line in file_object:
        x = line.rstrip().split(',')
        if len(x) <= 4:
            student_List.append(student(x[0], x[1], x[2], x[3], ''))
        else:
            student_List.append(student(x[0], x[1], x[2], x[3], x[4]))
print(wyswietlenie(student_List))

for line in student_List:
    if line["status"].upper() != 'GRADED' and line["status"].upper() != 'MAILED':
        print(ocena(line))
decision2 = ''
print("Czy chcesz dodac/usunac uzytkownika")
while decision == 'T':
    if decision == 'T':
        print("D - dodanie, U - usuniecie")
        decision2 = input()
        if decision2 == 'D':
            print("Podaj w nastepujacy sposob: email,imie,nazwisko,punkty")
            line = input("")
            line = line.rstrip().split(',')
            if line[0] in [students['email'] for students in student_List]:
                raise ValueError(f'Isnieje taki student')
            else:
                if len(line) <= 4:
                    student_List.append(student(line[0], line[1], line[2], line[3], ''))
                else:
                    student_List.append(student(line[0], line[1], line[2], line[3], line[4]))
        elif decision2 == 'U':
            print("Podaj email")
            line = input()
            if line in [students['email'] for students in student_List]:
                student_List.remove(__contains__(line))
        else:
            print("Bledna odpowiedz")

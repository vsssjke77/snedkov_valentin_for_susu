first = input("Имя, Фамилия, Отчество, Год рождения,Заболевание(по образцу)")
second = input("Имя, Фамилия, Отчество, Год рождения,Заболевание")
third = input("Имя, Фамилия, Отчество, Год рождения,Заболевание")
fourth =  input("Имя, Фамилия, Отчество, Год рождения,Заболевание")
fifth = input("Имя, Фамилия, Отчество, Год рождения,Заболевание")
base = {}
base['first'] = first
base['second'] = second
base['third'] = third
base['fourth'] = fourth
base['fifth'] = fifth
print(base['first'].replace(',',' | '))
print(base['second'].replace(',',' | '))
print(base['third'].replace(',',' | '))
print(base['fourth'].replace(',',' | '))
print(base['fifth'].replace(',',' | '))
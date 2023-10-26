a = float(input("Dme la nota de tu examen: "))
b = float(input("Dime el número de clases a las que has asistido: "))
c = float(input("Dime el número de clases que tienes: "))

if a>=70 and b/c>=0.8 :
    print("Ha aprobado el curso")
else:
    print("Ha suspendido el curso")
grade = ( a/100 + b/c ) / 2 * 100
print(grade)
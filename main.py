#1. Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел. Результат вычислений вывести на экран.
#n1= int(input("Number 1:"))
#n2= int(input("Number 2:"))
#n3=int(input("Number 3:"))
#print(n1+n2+n3)
#print(n1*n2*n3)

#2. Напишите программу, вычисляющую площадь ромба. Пользователь с клавиатуры вводит длину двух его диагоналей.

#a=int(input("length1:"))
#b=int(input("length2:"))
#print((a*b)/2)



#3. Пользователь вводит с клавиатуры число, состоящее из четырех цифр. Требуется найти произведение цифр.
#s=int(input("the number"))
#v=s
#a=v%10
#v=v//10
#b=v%10
#c=v%10
#d=v%100
#p=a*b*c*d
#print(p)
#print(a,b,c,d)

#and-
#or-

hours= int(input("enter hours"))

if 12 < hours <= 24:
    print("pm")
elif hours >=0 and hours <=12:
    print("AM")
else:
    print("incorrent")





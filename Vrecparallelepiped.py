# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

from math import sqrt
import turtle
import math

print("Побудуйте прямокутний паралелепіпед, розрахуйте його об'єм та площу")
print("Введіть розміри :")
a = float(input("Введіть довжину ? = "))
b = float(input("Введіть висоту ? = "))
c = float(input("Введіть ширину ?  = "))
v = a*b*c
s = 2*(a*b+a*c+b*c)
print("V Обєм = %0.2f" %v)
print("S Площа = %0.2f" %s)
print ("Поки Ви звіряєте свій розв'язок із розв'язком даної програми, черепашка намалювала Вам ваш паралелепіпед. Знайдіть його у себе на моніторі.")
# будуємо екран
tut = turtle.Screen() 
  
# колір фону
tut.bgcolor("grey") 
  
# черепашка
tut.title("Turtle") 
my_pen = turtle.Turtle() 
  
# колір креслення 
my_pen.color("black") 
tut=turtle.Screen()            
  
# передній прямокутник
for i in range(2): 
    my_pen.forward(a*37) 
    my_pen.left(90) 
    my_pen.forward(b*37) 
    my_pen.left(90) 
  
# в глибину
my_pen.left(45)
my_pen.forward(c*37)
my_pen.right(45)
  
 # дальній прямокутник
for i in range(2): 
   my_pen.forward(a*37) 
   my_pen.left(90) 
   my_pen.forward(b*37) 
   my_pen.left(90)
  
# решта
my_pen.forward(a*37)
my_pen.right(135)
my_pen.forward(c*37)
my_pen.right(135)
my_pen.forward(b*37)
my_pen.right(45)
my_pen.forward(c*37)
my_pen.left(135)
my_pen.forward(a*37)
my_pen.left(45)
my_pen.forward(c*37)



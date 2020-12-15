import turtle
from random import randrange
from time import sleep

t=turtle.Turtle()
while True:
  t.reset()
  angulo = randrange(10,80)
  t.speed(50000)
  t.width(randrange(1,10))
  
  for i in range(500):
    vermelho = randrange(0,255)
    azul = randrange(0,255)
    verde = randrange(0,255)
    t.color(vermelho,azul,verde)
    t.forward(i)
    t.right(angulo)

  sleep(2)

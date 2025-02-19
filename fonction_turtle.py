from turtle import *

##exemple du résultat de la fonction 6-9
##li_naissances_cycle_lune = [7,6,5,5,5,8,7,8,9,6,3,3,5,6,6,8,8,7,7,9,8,8,9,6,4,5,5,4,2, '.']
##li_naissances_cycle_lune_fille = [8,6,5,5,5,8,7,8,9,6,3,3,5,6,6,8,8,7,7,9,8,8,9,6,4,5,5,4,2, '.']
##li_naissances_cycle_lune_garcon = [9,6,5,5,5,8,7,8,9,6,3,3,5,6,6,8,8,7,7,9,8,8,9,6,4,5,5,4,2, '.']
##à la place il faudra implanter les fonction, genre : fonction_6(li_dates)



def turtle(li_naissances_cycle_lune, li_naissances_cycle_lune_fille, li_naissances_cycle_lune_garcon):
##a mettre en full screen

speed(30)
penup()
forward(-620)
left(90)
forward(300)
right(90)

pendown()
color('black', 'white')
begin_fill()
circle(15)
end_fill()
write(li_naissances_cycle_lune[0])
penup()
forward(40)

for i in range(14):
    pendown()
    color('black', 'gray')
    begin_fill()
    circle(15)
    end_fill()
    write(li_naissances_cycle_lune[i+1])
    penup()
    forward(40)

pendown()
color('black', 'black')
begin_fill()
circle(15)
end_fill()
pencolor('white')
write(li_naissances_cycle_lune[i+14])
pencolor('black')
penup()
forward(40)

for i in range(14):
    pendown()
    color('black', 'gray')
    begin_fill()
    circle(15)
    end_fill()
    write(li_naissances_cycle_lune[i+16])
    penup()
    forward(40)

left(180)
home()
forward(-620)
pendown()
color('black', 'white')
begin_fill()
circle(15)
end_fill()
write(li_naissances_cycle_lune_fille[0])
penup()
forward(40)

for i in range(14):
    pendown()
    color('black', 'gray')
    begin_fill()
    circle(15)
    end_fill()
    write(li_naissances_cycle_lune_fille[i+1])
    penup()
    forward(40)

pendown()
color('black', 'black')
begin_fill()
circle(15)
end_fill()
pencolor('white')
write(li_naissances_cycle_lune_fille[i+14])
pencolor('black')
penup()
forward(40)

for i in range(14):
    pendown()
    color('black', 'gray')
    begin_fill()
    circle(15)
    end_fill()
    write(li_naissances_cycle_lune_fille[i+16])
    penup()
    forward(40)

home()
forward(-620)
right(90)
forward(300)
left(90)
pendown()
color('black', 'white')
begin_fill()
circle(15)
end_fill()
write(li_naissances_cycle_lune_garcon[0])
penup()
forward(40)

for i in range(14):
    pendown()
    color('black', 'gray')
    begin_fill()
    circle(15)
    end_fill()
    write(li_naissances_cycle_lune_garcon[i+1])
    penup()
    forward(40)

pendown()
color('black', 'black')
begin_fill()
circle(15)
end_fill()
pencolor('white')
write(li_naissances_cycle_lune_garcon[i+14])
pencolor('black')
penup()
forward(40)

for i in range(14):
    pendown()
    color('black', 'gray')
    begin_fill()
    circle(15)
    end_fill()
    write(li_naissances_cycle_lune_garcon[i+16])
    penup()
    forward(40)

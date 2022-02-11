
import numbers
import random 
import  tkinter as tk
from tkinter import END, font


window = tk.Tk()
window.title("Угадай число")
window.geometry("600x600")
   

def click_button(): 
    global number
    number=int(random.randint(0 ,30))
    btn_text.set("Поехали!\n Чтобы загадать новое число,\n нажми еще раз")
    lbl_text.set("Введите число")
    print(number)
    
def clear():
    ent2.delete(0, END)
    global guesses_made 
    guesses_made=1
    
def clear_number():
    ent.delete(0, END)


btn_text = tk.StringVar() 
btn_text.set("Я загадал \nцелое число от 0 до 30.\nЕсли хочешь отгадать?\nНажми")
lbl_text= tk.StringVar()    
lbl_text.set("___________")
btn=tk.Button(
    textvariable=btn_text,
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    font=("Verdana", "20", "bold"),
    command=lambda:[click_button(), clear()]
)
lbl=tk.Label(
    textvariable=lbl_text,
    font=("Verdana", "20", "bold")

)

ent=tk.Entry(
    width=10,
    bg="red",
    fg="yellow",
    font=("Verdana", "15", "bold")
)

def gues():   
    global guesses_made 
    guesses_made +=1
    ent2.delete(0, END)
    ent2.insert(0, guesses_made)

guesses_made=1    


def play():
           
    numbers_user=int(ent.get())
    
    if numbers_user == number:
        lbl2_text.set('Ух ты! Ты угадал мое число, \nиспользовав {0} попыток!'.format(guesses_made))

    if numbers_user < number:
        lbl2_text.set('Твое число меньше того, \nчто я загадал.')

    if numbers_user > number:
        lbl2_text.set('Твое число больше \nзагаданного мной.')
    if numbers_user <0 or numbers_user>30:
        lbl2_text.set("Внимательней - от 0 до 30!!!!!")
    
    # else:
        # print ('Не угадал! Я загадал число {0}'.format(number))
   

btn2=tk.Button(
    text=("Проверить"),
    command=lambda:[play(),gues(), clear_number()],
    # width=10,
    # height=5,
    bg="yellow",
    fg="blue",
    font=("Verdana", "20", "bold")
)
lbl2_text= tk.StringVar()    
lbl2_text.set("___________")
lbl2=tk.Label(
    textvariable=lbl2_text,
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    font=("Verdana", "20", "bold"),

)
lbl3=tk.Label(
    text="Счетчик попыток",
    font=("Verdana", "10", "bold")
)

ent2=tk.Entry(window,
    font=("Verdana", "10", "bold")
    )
btn.pack()
lbl.pack()
ent.pack()
btn2.pack()
lbl2.pack()
lbl3.pack()
ent2.pack()
window.mainloop()


import json, pyaudio
from multiprocessing.connection import answer_challenge
from vosk import Model, KaldiRecognizer
import sys
import webbrowser
import random
import datetime
import os
import speech_recognition as sr
import wikipedia
import pyscreenshot
import  pytesseract
from PIL import Image
import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox
import ctypes
import re
import os
import datetime
import pyglet
from time import sleep
def lll():
   print('привет я камилла голосовой помошник\nменя создавал камиль ему 15 лет\nя создавалась обсалютно без вдожений\nесли вы хотите мемя поддержать вот мой крипто кошелек\n0x18c232a8b0f160d89e22f3afd2dc38c83553f43f')
#ответы на не сложные диологи,в exe
def rgb(rgb):
    return "#%02x%02x%02x" % rgb
FILE_NAME = tkinter.NONE
root = Tk()
root.geometry('700x500')
root.title('Редактор кода')
previousText = ''
normal = rgb((234, 234, 234))
keywords = rgb((234, 95, 95))
comments = rgb((95, 234, 165))
string = rgb((234, 162, 95))
function = rgb((95, 211, 234))
background = rgb((42, 42, 42))
font = 'Consolas 15'
editArea = Text(
    root, background=background, foreground=normal, insertbackground=normal, relief=FLAT, borderwidth=30, font=font
    )
repl = [
     ['(^| )(False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield)($| )', keywords],
     ['".*?"', string],
     ['\'.*?\'', string],
     ['#.*?$', comments],
     ]
ur2 = 'https://www.youtube.com/'
url = 'https://www.youtube.com/'
url3 = 'https://www.google.com/search?q=курс+'
now = datetime.datetime.now()
anekdot = ["чем негр похож на вилосепед оба не могут работать без цепи", 
"Здравствуйте, нужен проверенный электрик, можете кого-нибудь посоветовать? Конечно могу! Любой живой электрик автоматически считается проверенным.", 
"Что должна была сделать настоящая, уважающая себя женщина 14 февраля? Правильно, выводы.", 
"Фрезеровщик Фёдор знал, что семь это счастливое число, но семь пальцев на руках не вселяли в него оптимизма.", 
"Халяльных ресторанов мало, а халявных нет вообще...", 
"У Буратино была кожаная куртка, из бересты",
"Погружаться в полную анархию и дикий хаос нужно под чьим-нибудь чутким руководством."]
chetati= ["Люди-идиоты плюс алкоголь — вот вам рецепт любой потасовки",
"Тем, кого вдохновляют мои герои, не помешало бы лишний раз подумать","Женщины у вас потрясающие! Безусловно. В России встречаются просто убойные красотки",
"Люди, считающие, что деньги способны сделать все, сами способны все сделать за деньги",
"Я полагаю, что европейцы опасны и волосаты",
"Превосходство — это когда есть на что насрать, и есть чем",
"Есть такая штука как «Двигаться дальше». Попробуйте, поможет",]
kak_dela = ["хорошо у вас?","превасходно","супер","отлично","все хорошо вот жду вашей команды",]
chto_delaech = ["ничего жду вашей команды","жду вашей команды","ничего особенного просто анализирую ваши последние запросы","ничего особенного","да так жду вашей команды",]
privet = ["салют","алоха","салам","приветик","hi",]
#a = input('введите путь к тесеракту') 
model = Model ('vosk-model-small-ru-0.4')
rec = KaldiRecognizer (model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input= True, frames_per_buffer=8000)
stream.start_stream()
wikipedia.set_lang("ru")


ctypes.windll.shcore.SetProcessDpiAwareness(True)

def fdg():
    editArea.pack(fill=BOTH, expand=1)

    editArea.insert('1.0', """from random import randint

    print([randint(1, 20) for i in range(10)]) 
    что бы запустить нажмите ctrl + r
    """)

    editArea.bind('<KeyRelease>', changes)

    root.bind('<Control-r>', execute)

    changes()
    root.mainloop()
def execute(event=None):
    with open('run.py', 'w', encoding='utf-8') as f:
        f.write(editArea.get('1.0', END))

    os.system('start cmd /K "python run.py"')


def changes(event=None):
    global previousText

    if editArea.get('1.0', END) == previousText:
        return

    for tag in editArea.tag_names():
        editArea.tag_remove(tag, "1.0", "end")

    i = 0
    for pattern, color in repl:
        for start, end in search_re(pattern, editArea.get('1.0', END)):
            editArea.tag_add(f'{i}', start, end)
            editArea.tag_config(f'{i}', foreground=color)

            i += 1

    previousText = editArea.get('1.0', END)


def search_re(pattern, text):
    matches = []
    text = text.splitlines()

    for i, line in enumerate(text):
        for match in re.finditer(pattern, line):

            matches.append(
                (f"{i + 1}.{match.start()}", f"{i + 1}.{match.end()}")
            )

    return matches


def new_file():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete('1.0', tkinter.END)

def save_file():
	data = text.get('1.0', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()

def save_as():
	out = asksaveasfile(mode='w', defaultextension='txt')
	data = text.get('1.0', tkinter.END)
	try:
		out.write(data.rstrip())
	except Exception:
		showerror(title="Error", message="Saving file error")

def open_file():
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)

def info():
	messagebox.showinfo("Information", "new redaktor for me\n")
def rrr():
 root = tkinter.Tk()
 root.title("заметки")

 root.minsize(width=500, height=500)
 root.maxsize(width=500, height=500)

 text = tkinter.Text(root, width=400, height=400, wrap="word")
 scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
 scrollb.pack(side="right", fill="y")
 text.configure(yscrollcommand=scrollb.set)

 text.pack()
 menuBar = tkinter.Menu(root)
 fileMenu = tkinter.Menu(menuBar)
 fileMenu.add_command(label="New", command=new_file)
 fileMenu.add_command(label="Open", command=open_file)
 fileMenu.add_command(label="Save", command=save_file)
 fileMenu.add_command(label="Save as", command=save_as)

 menuBar.add_cascade(label="File", menu=fileMenu)
 menuBar.add_cascade(label="Info", command=info)
 menuBar.add_cascade(label="Exit", command=root.quit)
 root.config(menu=menuBar)
 root.mainloop()

def ddd():
    if text == "что здесь написанно":
       image = pyscreenshot.grab()
       image.save('sss.png')
       img = Image.open('sss.png')
       pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Камильчик\Documents\ntcthfrn\tesseract.exe'#a
       texty = pytesseract.image_to_string(img)
       print(texty)
def command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Говорите")
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(source, duration=1)
		audio = r.listen(source)
	try: 
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		print("Вы сказали: " + zadanie)
	except sr.UnknownValueError:
		print("Я вас не поняла")
		zadanie = command()
	return zadanie


def my_fun():
    if text == 'камилла открыткрой ' :
            webbrowser.open(url)
    if text == 'камилла расскажи анекдот':
        random_index = random.randint(0, len(anekdot) - 1)
        print(anekdot[random_index])
    if text == 'камилла расскажи цитату':
        random_index = random.randint(0, len(chetati) - 1)
        print(chetati[random_index])
    if text == 'привет':
        random_index = random.randint(0, len(privet) - 1)
        print(privet[random_index])
    if text == 'как дела':
        random_index = random.randint(0, len(kak_dela) - 1)
        print(kak_dela[random_index])
    if text == 'что делаешь':
        random_index = random.randint(0, len(chto_delaech ) - 1)
        print(chto_delaech [random_index])
    if text == 'расскажи о себе':
        lll()
    if text == 'у меня тоже':
        print("отлично")
def het(): 
 music = pyglet.resource.media('music.mp3')
 time_now = datetime.datetime.now()
 print('Час')
 hour = str(input())
 print('Минуты')
 minutes = str(input())
 

 if len(hour) == 1:
    hour = '0' + hour
 if len(minutes) == 1:
    minutes = '0' + minutes
 while True:
    time_now = datetime.datetime.now()
    if str(time_now.hour) == hour and str(time_now.minute) == minutes:
        music.play()
        break
    sleep(1)
 pyglet.app.run()


def ggg():
    url1 = 'https://music.yandex.ru/search?text='
    
    if text == 'камилла давай послушаем':
        print('что')
        webbrowser.open(url1 + command())
    if text.count("камилла что такое") > 0:
            result = wikipedia.summary(text.replace("что такое", ""))
            print(result)
    if text == 'камилла включи ютуб':
        print('хорошо')
        webbrowser.open(ur2)
    if text == 'камилла курс валют':
        print('какой валюты')
        webbrowser.open(url3 + command())
    if text == 'камилла заметки':
        rrr()
    if text == 'открой редактор кода':
        print('хорошо')
        fdg()
    if text == 'будильник':
        het()


def listen():
  while True:
   data = stream.read(4000, exception_on_overflow= False)
   if (rec.AcceptWaveform(data)) and (len(data) > 0 ):
    answer = json.loads(rec.Result())
    if answer ['text']:
        yield answer['text']
        my_fun()
        ggg()
        ddd()
for text in listen():
         print(text)
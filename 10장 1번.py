from tkinter import Tk, Label, Button    # 창,레이블,버튼을 소환함

def greet():
 print("파이썬에 오신 것을 환영합니다. ")   # 만든 버튼중 환영합니다 버튼을 누르면 터미널에 뜨게함 

window = Tk()
label = Label(window, text="간단한 GUI 프로그램!")  # 레이블 설정 
label.pack()

greet_button = Button(window, text="환영합니다.", command=greet)  # 환영합니다. 버튼 생성
greet_button.pack()

close_button = Button(window, text="종료", command=window.quit)   # 종료 버튼 생성
close_button.pack()

window.mainloop()
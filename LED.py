# coding: utf-8

# GPIO
Import RPi.GPIO as GPIO

# Tkinter
Import tkinter as tk # Python3
# import Tkinter as tk # Python2

# 핀번호
GPIO.setmode(GPIO.BOARD)

# 핀 번호 할당
LED = 11

# 출력 핀 설정
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

# LED 켜고 끄기
def func():

   # 입력값 반전 출력
   # GPIO.output(LED, not GPIO.input(LED))

# root 작성
root = tk.Tk()

# 레이블 정의 및 배치
label = tk.Label(root, text=’LED 켜고 끄기’)
label.pack()

# 버튼 삽입
button = tk.Button(root, command=func)

# 버튼 배치
Button.pack()

#GPIO 개방
GPIO.cleanup()

import cv2
from idle import *
import tkinter as tk
import sys
import time

entrys = []
def pegar():
    entrys.append(e1.get())
    entrys.append(e2.get())

master = tk.Tk()
tk.Label(master, text="Endereço do vídeo:").grid(row=0)
tk.Label(master, text="Tempo de espera em minutos:").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, 
          text='Enter', 
          command=lambda:[pegar(),master.destroy()]).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)

tk.Button(master, 
          text='Exit', command=sys.exit).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
tk.mainloop()

#print(entrys)

file_name = (r"a.mp4")
cap = cv2.VideoCapture(file_name)
def video():
    file_name = (str(entrys[0]))
    window_name = "ss"
    interframe_wait_ms = 30



    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cap = cv2.VideoCapture(file_name)
    if not cap.isOpened():
        print("Error: Não foi possível abrir o vídeo.")
        exit()
    while (True):
        ret, frame = cap.read()
        if not ret or LASTINPUTINFO.get_idle_duration() == 0:
            cap = cv2.VideoCapture(file_name)
            break

        cv2.imshow(window_name, frame)
        if cv2.waitKey(interframe_wait_ms) & 0x7F == ord('q'):
            c = 1
            exit()

mano = 0
while True:
    time.sleep(0.001)
    mano = LASTINPUTINFO.get_idle_duration()+0.001
    #print(mano)
    if mano > float(entrys[1])*60:
        video()
    else:
       cap.release()
       cv2.destroyAllWindows()
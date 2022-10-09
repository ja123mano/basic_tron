from playsound import playsound 
import threading

class Hilos(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        playsound('tron.wav')

hilo = Hilos()
x = "go"
while x != "exit":
    x = input("Ingresa comando: ")
    if x == "stop":
        hilo.stop()
    elif x == "go":
        hilo.start()


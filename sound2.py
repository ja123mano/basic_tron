import winsound
winsound.PlaySound('tron.wav', winsound.SND_ASYNC)
x = input("Hola")
winsound.PlaySound(None, winsound.SND_PURGE)
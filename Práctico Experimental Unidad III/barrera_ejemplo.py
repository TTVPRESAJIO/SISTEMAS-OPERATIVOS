import threading

barrera = threading.Barrier(2)

def tarea():
    print("Hilo iniciado")
    barrera.wait()
    print("Hilo continuando")

hilo1 = threading.Thread(target=tarea)
hilo2 = threading.Thread(target=tarea)

hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

print("Programa terminado")

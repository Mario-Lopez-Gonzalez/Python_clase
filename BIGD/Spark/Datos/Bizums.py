import os
import shutil
import shutil, os
from random import randint, uniform,random

import time

ruta = os.getcwd() + os.sep

#bizum = input('Bizum: ')

i = 1
while i <= 20:
	num_aleatorio = randint(0,15)
	origen = ruta + 'Sin_llegar' + os.sep + 'Bizum' +str(num_aleatorio) + '.csv'
	destino = ruta + 'recibidos' + os.sep + 'Bizum' +str(num_aleatorio) + '.csv'
	try:
	    shutil.copyfile(origen, destino)
	    print("Bizum recibido")
	    i=i+1
	except:
		print("Error al enviar bizum")
		i=i+1
	time.sleep(10)
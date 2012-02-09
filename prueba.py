import os
so = os.name

if so == "posix":
	comando = "clear"
elif so == "nt":
	comando = "cls"

os.system( comando )
#!------ Declaracion de funciones -------
def menu(opc, complaint='Tienes que elegir alguna opcion del menu'):
	opc = raw_input(opc)
	for opc in('repositorios', 'repositorio'): actualizarRep(opc)

#!--------------------------@--------------------------------
def actualizarRep(ans, complaint='tienes que elegir si o no!'):
	print 'Bienvenido al actualizador, quieres actualizar?[S/N]	eleccion: '
	ans = raw_input(ans)
	if ans in ( 's', 'si', 'SI', 'S', 'sip' ): os.system('brew update')
	if ans in ('n'): return 1

#!--------------------------@---------------------------------
def salida(prompt, retries=4, complaint='Si o no, por favor!'):
	while 1:
		ok = raw_input( prompt )
		if ok in ( 's', 'si', 'SI', 'S', 'sip' ): return 1
		if ok in ( 'n', 'no', 'nop', 'nope'  ): os.system('python salir.py')
		retries = retries - 1
		if retries < 0: raise IOError, 'refusenik user'
		print complaint
#!--------------------------@-----------------------------------
#!------ Fin declaracion de funciones ----------
print "Instalador GNU/Linux de gonzo"
print "======"
print "Escoge una opcion por favor"
print "Actualizar repositorios [repositorios]"
print "Actualizar distribucion [distribucion]"

#!------- Llamada a la funcion menu -----------
menu ('Eleccion: ')
#!------- Llamada a la funcion salida -----------
salida ('Quieres salir?[S/N] eleccion: ')
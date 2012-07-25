################################################################
#                                                              #
#	MacApacheVHostKudeatzailea.py                              #
#	v0.1                                                       #
#                                                              #
#                                                              #
#	Script to update /etc/hosts and /etc/apache2 and           #
#	/etc/apache2/extra/httpd-vhosts.conf for setting           #
#   apache virtual host quickly                                #
#	Author: Iker Ibarguren (http://www.ikerib.com), 2012       #
#                                                              #
################################################################

LOCAL_HOSTS='/etc/hosts'
APACHE_VHOST='/etc/apache2/extra/httpd-vhosts.conf'
SCRIPT_IDENTIFIKATZAILEA = '############# MAC_APACHE_VHOST_KUDEATZAILEA ################'
HOSTS_IDENTIFIKATZAILEA = '### MAC_APACHE_VHOST_KUDEATZAILEA HOSTS :'
VHOST_IDENTIFIKATZAILEA = '### MAC_APACHE_VHOST_KUDEATZAILEA VHOST :'

import os, sys
so = os.name

if so == "posix":
	comando = "clear"
elif so == "nt":
	comando = "cls"

os.system( comando )


def menu(opc, complaint='Aukeratu zer egin nahi duzun'):
	opc = raw_input(opc)
	if opc in('1', '2', '3'):
		vApache( opc )
	else:
		menu ('Aukera okerra. Saiatu berriz: ')

def vApache(ans, complaint='Aukeratu ezazu bat!!'):
	if ans == '3' : sys.exit('Agur!')
	vhost = raw_input('Host berriaren izena: ')
	if ans == '1':
		gehitu(vhost)
	elif ans == '2':
		vHost(vhost)


def gehitu(vhost, complaint="Ez duzu izenik sartu!!"):

	if not os.access(LOCAL_HOSTS, os.W_OK):
		sys.exit('Ez dut idazteko baimenik '+LOCAL_HOSTS+' artxiboan, root gisa exekutatu' )

	vhost = vhost + ".local"
	print '\n' + vhost + ' sortuko da.'
	HOSTS_BERRIA = '127.0.0.1	' + vhost + '\n\r'

	# copy old hosts to new file, excluding any configs copied by this script
	reader = open(LOCAL_HOSTS, 'r')
	writer = open(LOCAL_HOSTS +'.tmp','w')
	lehen_aldia = True
	badago = False
	for row in reader:
		if row.strip('\n\r') == SCRIPT_IDENTIFIKATZAILEA:
			lehen_aldia = False

		if row.strip('\n\r') == HOSTS_IDENTIFIKATZAILEA + vhost:
			badago = True

		writer.write(row)

	reader.close()


	# if this is the first time we add the content, add script identifier and also add an empty line
	if lehen_aldia == True:
		writer.write('\n' + SCRIPT_IDENTIFIKATZAILEA + '\n\n')
	else:
		writer.write('\n')

	if badago == False:
		nirevhost = HOSTS_IDENTIFIKATZAILEA + vhost + '\n'
		writer.write(nirevhost)
		writer.write(HOSTS_BERRIA)

	writer.close()

	# remove new hosts file
	os.remove(LOCAL_HOSTS)

	# replace old hosts file with new version
	os.system('mv -f ' + LOCAL_HOSTS + '.tmp ' + LOCAL_HOSTS)

	print 'Operazioa zuzen burutu da. Gogoratu apache berriz abiarazi behar duzula: sudo /usr/sbin/apachectl restart'
	amaiera = raw_input('Sakatu tekla bat jarraitzeko.')
	print '\n'
	print "Apache Virtual Host kudeatzailea"
	print "======"
	print "Aukeratu eragiketa"
	print "1-. VHost bat gehitu."
	print "2-. Idatzi VHost berria"
	print "3-. Irten."
	print ""
	menu ('Aukeraketa: ')

def vHost(vhost, complaint="Ez duzu izenik sartu!!"):
	print 'Vhost berria sortzen...'
	if not os.access(APACHE_VHOST, os.W_OK):
		sys.exit('Ez dut idazteko baimenik ' + APACHE_VHOST + ' artxiboan, root gisa exekutatu')

	print vhost + ' sortuko da.'
	miHost = """<VirtualHost *:80>
    DocumentRoot "/Users/gitek/www/""" + vhost + """/web"
    DirectoryIndex app.php
    ServerName """ + vhost + """.local

    <Directory "/Users/gitek/www/""" + vhost + """/web">
        AllowOverride All
        Allow from All
    </Directory>

</VirtualHost>"""

	# copy old hosts to new file, excluding any configs copied by this script
	reader = open(APACHE_VHOST, 'r')
	writer = open(APACHE_VHOST +'.tmp','w')
	lehen_aldia = True
	badago = False
	for row in reader:
		if row.strip('\n\r') == SCRIPT_IDENTIFIKATZAILEA:
			lehen_aldia = False

		if row.strip('\n\r') == VHOST_IDENTIFIKATZAILEA + vhost:
			badago = True

		writer.write(row)

	reader.close()

	# if this is the first time we add the content, add script identifier and also add an empty line
	if lehen_aldia == True:
		writer.write('\n' + SCRIPT_IDENTIFIKATZAILEA + '\n')
	else:
		writer.write('\n')

	if badago == False:
		nirevhost = VHOST_IDENTIFIKATZAILEA + vhost + '\n'
		writer.write(nirevhost)
		writer.write(miHost)

	writer.close()

	# remove new hosts file
	os.remove(APACHE_VHOST)

	# replace old hosts file with new version
	os.system('mv -f ' + APACHE_VHOST + '.tmp ' + APACHE_VHOST)

	amaiera = raw_input('Operazioa zuzen burutu da. Sakatu tekla bat jarraitzeko. ')

	print '\n'
	print "Apache Virtual Host kudeatzailea"
	print "======"
	print "Aukeratu eragiketa"
	print "1-. VHost bat gehitu."
	print "2-. Idatzi VHost berria"
	print "3-. Irten."
	print ""
	menu ('Aukeraketa: ')

print "Apache Virtual Host kudeatzailea"
print "======"
print "Aukeratu eragiketa"
print "1-. VHost bat gehitu."
print "2-. Idatzi VHost berria"
print "3-. Irten."
print ""

menu ('Aukeraketa: ')
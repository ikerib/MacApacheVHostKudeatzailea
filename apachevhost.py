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
SCRIPT_IDENTIFIKATZAILEA = '############# MAC_APACHE_VHOST_KUDEATZAILEA ################'

import os, sys
so = os.name

if so == "posix":
	comando = "clear"
elif so == "nt":
	comando = "cls"

os.system( comando )


def menu(opc, complaint='Aukeratu zer egin nahi duzun'):
	opc = raw_input(opc)
	for opc in('1', '2', '3'): vApache(opc)

def vApache(ans, complaint='Aukeratu ezazu bat!!'):
	# ans = raw_input(ans)
	if ans in ( '1'): 
		vhost = raw_input('Host berriaren izena: ')
		gehitu(vhost)
	

def gehitu(vhost, complaint="Ez duzu izenik sartu!!"):

	if not os.access(LOCAL_HOSTS, os.W_OK):
		sys.exit('Ez dut idazteko baimenik '+LOCAL_HOSTS+' artxiboan, root gisa exekutatu' )

	print vhost + ' sortuko da.'
	HOSTS_BERRIA = '127.0.0.1	' + vhost + '\n\r'
	
	# copy old hosts to new file, excluding any configs copied by this script
	reader = open(LOCAL_HOSTS, 'r')
	writer = open(LOCAL_HOSTS +'.tmp','w')
	lehen_aldia = True
	for row in reader:
		if row.strip('\n\r') == SCRIPT_IDENTIFIKATZAILEA:
			writer.write(row)
			lehen_aldia = False
			break
		else:
			writer.write(row)
	reader.close()


	# if this is the first time we add the content, add script identifier and also add an empty line
	if lehen_aldia == True:
		writer.write('\n' + SCRIPT_IDENTIFIKATZAILEA + '\n\n')
	else:
		writer.write('\n')
	
	writer.write(HOSTS_BERRIA)	

	writer.close()

	# remove new hosts file
	os.remove(LOCAL_HOSTS)

	# replace old hosts file with new version
	os.system('mv -f ' + LOCAL_HOSTS + '.tmp ' + LOCAL_HOSTS)




print "Apache Virtual Host kudeatzailea"
print "======"
print "Aukeratu eragiketa"
print "1-. VHost bat gehitu."
print "2-. Irten."
print ""

menu ('Aukeraketa: ')
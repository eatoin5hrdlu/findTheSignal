#!/usr/bin/python

import smtplib, os, sys, time
from email.mime.image      import MIMEImage
from email.mime.multipart  import MIMEMultipart
from email.mime.text       import MIMEText
COMMASPACE = ', '

import subprocess
wgetip = "bash -c \"ipconfig | grep -Eo 'IPv4.*: ?([0-9]*\.){3}[0-9]*' | sed -E \\\"s/IPv4[^0-9]*(([0-9]+\.){3}[0-9]*).*/\\\\1/\\\""
getip = ['hostname','-I']


proc = subprocess.Popen(getip, stdout=subprocess.PIPE)
myip = "   ".join(proc.stdout.read().strip().split())
print myip
os.chdir('/'.join(sys.argv[0].split('/')[:-1]))
secrets = eval(open('secrets.py').read())
print str(secrets)

# fake it
# secrets = { 'login':'8wan5hrdlu', 'password': '<passwd>' }

carriers = { 'a' : '@mms.att.net',
             't' : '@tmomail.net',
             'v' : '@vtext.com',
             'vt': '@vtext.com',  #text
             'vp': '@vzwpix.com',  #pictures
             'n' : '@messaging.nextel.com',
             's' : '@messaging.sprintpcs.com',
             'Alltel' : '@message.alltel.com',
'Ampd Mobile' : '@vtext.com',
'Cingular' : '@mobile.mycingular.com',
'SunCom' : '@tms.suncom.com',
'VoiceStream' : '@voicestream.net',
'US Cellulart' : '@email.uscc.net', # text
'US Cellularp' : '@mms.uscc.net', #pictures
'Cricket' : '@mms.mycricket.com',
'Virgin' : '@vmobl.com',
'Cingular' : '@cingularme.com', #not sure
'Boost Mobile' : '@myboostmobile.com',
'Einstein PCS' : '@einsteinmms.com' }

car = 'vp'
num = '9194525098'
mess = myip + " FindTheSignal(pi)IP(s)\n"

if (len(sys.argv) == 3) :
    car = sys.argv[1]
    num = sys.argv[2]
else :
    print 'smstext [atvs] NNNNNNNNNN';
    print 'e.g. for [v]erizon use:   smstext v 9198675309'
    print '     for [a]tt use:      smstext a 9198675309'
    print '     for [t]mobile use: smstext t 9198675309'

# SMTP Port 25?
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( secrets['login'], secrets['password'] )
msg = MIMEText(mess,'plain')
msg['Subject'] = 'FindTheSignal IP'
msg['From'] = 'peterr@ncmls.org'
msg['To'] = num + carriers[car]

print "server.sendmail( 'phagestat@gmail.com', "+num+carriers[car]+", "+msg.as_string()+" )"

server.sendmail('phagestat@gmail.com', num+carriers[car], msg.as_string())
server.quit()
exit(0)



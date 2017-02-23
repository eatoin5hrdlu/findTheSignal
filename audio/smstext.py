#!/usr/bin/python

import smtplib, os, sys, time
from email.mime.image      import MIMEImage
from email.mime.multipart  import MIMEMultipart
from email.mime.text       import MIMEText
COMMASPACE = ', '

import subprocess
location = '/'.join(sys.argv[0].split('/')[:-1])
os.chdir(location)

if ( subprocess.call(location+'/newip.py') == 0 ) :
    sys.exit(0)

myip = open(location+'/lastIP','r').read()
print "Ready to send new IP [" + myip+ "]"

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
num = '9192208708'  # Richard the Mill Ward
mess = myip + " FindTheSignal(pi)IP(s)\n"

if (len(sys.argv) == 3) :
    print "yes there are three args, but zero is "+str(sys.argv[0])
    car = sys.argv[1]
    num = sys.argv[2]
else :
    print 'smstext [a t vp s] NNNNNNNNNN';
    print 'e.g. for [v]erizon use:   smstext v 9198675309'
    print '     for [a]tt use:      smstext a 9198675309'
    print '     for [t]mobile use: smstext t 9198675309'
    print '     for [v]picture use: smstext vp 9198675309'

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
print "I'm done"
sys.exit(0)



import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from config import *

 
username = 'ConSpeciFix@gmail.com'
password = 'helloW0rldHowAreYou'

fromaddr = 'ConSpeciFix@gmail.com'
toaddr  = getEmail()
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Update on your Exploration! id:'+ getTimeStamp()

res = '\n\n'
critInfoFD = open(PATH_TO_UPLOAD+'FinalResults.txt','r')
for l in critInfoFD:
	res += l
res+='\n'

body = "Hello!\n\nHere are the results of your exploration:"+res+"\n\nThanks,\nThe ConSpeciFix Team"
 
postMessage = "\n\n\nThis message is in regards to the file uploaded on "+str(datetime.datetime.fromtimestamp(int(getTimeStamp())/1000.0))

body = body + postMessage

msg.attach(MIMEText(body, 'plain'))

 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print msg.as_string()
print "all done. With everything!"



import imaplib
import email
from credentials import useName,passWord

imap_url ='imap.gmail.com'
my_mail = imaplib.IMAP4_SSL(imap_url)
my_mail.login(useName, passWord)

my_mail.select('Inbox')

data = my_mail.search(None, 'All')

mail_ids = data[1]  
id_list = mail_ids[0].split()   
first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])

for i in range(latest_email_id,first_email_id, -1):
     data = my_mail.fetch(str(i), '(RFC822)' )
     for response_part in data:
             arr = response_part[0]
             if isinstance(arr, tuple):
                 msg = email.message_from_string(str(arr[1],'utf-8'))
                 email_subject = msg['subject']
                 email_from = msg['from']
                 print('From : ' + email_from)
                 print('Subject : ' + email_subject + '\n')
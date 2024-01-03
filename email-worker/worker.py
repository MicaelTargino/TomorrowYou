import redis
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv('SUPABASE_URL', '')
SUPABASE_API_KEY = os.getenv('SUPABASE_API_KEY', '')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_API_KEY)
 
def send_mail(letter, receiver_email):            
        # try: 
            sender_email = os.getenv('SENDER_MAIL', '')
            password = os.getenv('SENDER_PASSWORD', '')
            print(sender_email)
            print(password)
                
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = "Letter from older you" #customize with subject
            body = letter #customize with email text
            message.attach(MIMEText(body, "plain"))

            server = smtplib.SMTP("smtp.gmail.com", 587) 
            server.starttls()
            server.login(sender_email, password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()

            return True
        # except: 
        #     return False

if __name__ == '__main__':
    r = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)
    print('Aguardando mensagens....')
    while True:
        mensagem = json.loads(r.blpop('email_queue')[1])

        #simulando envio de email 
        print('Mandando a mensagem para: ', mensagem['recipient_email'])
        res = send_mail(mensagem['message_body'], mensagem['recipient_email'])
        if res:
    
            data, count = supabase.table('api_mailmessage').update({'sent': True}).eq('id',mensagem['id']).execute()
            print('Mensagem para', mensagem['recipient_email'], 'enviada')
        else: print('Mensagem falha')
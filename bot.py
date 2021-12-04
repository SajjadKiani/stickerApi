from pyrogram import Client
import configparser
from App import WritePic

# api
conf = configparser.ConfigParser()
conf.read('config.ini')
api = conf['DEFAULT']


app = Client("my_account",api['api_id'],api['api_hash'])

print ('Start')

@app.on_message()
def my_handler(client, message):
    
    if  '/sticker' in str(message['text']) and 'Sjd0k' in str(message['from_user']['username']):
        print (message['reply_to_message']['from_user']['first_name']+ " : " +message['reply_to_message']['text'])
        
        # create picture
        WritePic(message['reply_to_message']['text'],message['reply_to_message']['from_user']['first_name']).write()
        
        app.send_sticker(message['chat']['id'],'files/res.webp')



app.run()


print ('End!')
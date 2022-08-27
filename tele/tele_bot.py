from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
import requests

updater = Updater(token='5634881507:AAEOo0fBST0VtiWkNFE2TGus-yA3yJmjO0w',use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

greeting= ["hello", "hi", "hey"]

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello world!')

def chatbotVideo(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='https://www.youtube.com/watch?v=38sL6pADCog')

def summary(update,context):
    response=requests.get('https://api.covid19api.com/summary')
    if response.status_code==200:
        data = response.json()
        # print(data)
        # print(data['Date'][:10])
        date=data['Date'][:10]

        ans = f'The summary of COVID-19 until {date} is:' + '\n'

        for attribute,value in data['Global'].items():
            if attribute not in ['NewRecovered', 'TotalRecovered', 'Date']:
                ans = ans + attribute + ' : '+str(value) + '\n'

        # print(f'The summary of COVID-19 until {date} is:')
        
        print(data['Countries'][77])

    context.bot.send_message(chat_id=update.effective_chat.id, text=ans)


summary_handler=CommandHandler('summary', summary)
dispatcher.add_handler(summary_handler)

hello_handler=CommandHandler(greeting, hello)
dispatcher.add_handler(hello_handler)

video_handler=CommandHandler('showvideo', chatbotVideo)
dispatcher.add_handler(video_handler)

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Sorry, I dont understand')

unknown_handler=MessageHandler(Filters.command,unknown)
dispatcher.add_handler(unknown_handler)

updater.idle()
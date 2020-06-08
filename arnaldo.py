import tweepy
import time
from threading import Thread
from time import sleep
import os
import keys

class IntervalRunner(Thread):
    def __init__(self, interval, function, *args, **kwargs):

        # super().__init__(self, IntervalRunner)

        Thread.__init__(self, target=IntervalRunner)

        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.executing = False

    def run(self):
        self.executing = True
        while self.executing:
            self.function(*self.args, **self.kwargs)
            time.sleep(self.interval)

    def stop(self):
        self.executing = False


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        stt = status.text.lower()
        if(stt == "pode isso arnaldo?" or stt == "pode isso, arnaldo?"):
            #msg = "@" + status.user.screen_name + " Diga lá, Tino!"
            # msg = "A regra é clara! Não pode!"
            # api.update_status(status = msg, in_reply_to_status_id = status.id, auto_populate_reply_metadata = True)
            # api.create_favorite(status.id)
            print("ok")
            print(stt)
            # print(msg)
            print("----------")

        else:
            usuarios = MyStreamListener.acao(self, stt)
            if usuarios:
                #msg = "@" + status.user.screen_name + " " + usuarios + " Diga lá, Tino!"
                # msg = "A regra é clara! Não pode!"
                print("ok2")
                print(stt)
                # print(msg)
                print("----------")
                # api.update_status(status = msg, in_reply_to_status_id = status.id, auto_populate_reply_metadata = True)
                # api.create_favorite(status.id)
                    
        
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
    def acao (self, t):
        t = t.lower()
        s = t.split(" ")
        tamanho = len(s)
        contador = 1
        us = []
        for n in s:
            if ("@" in n):
                contador = contador+1
                us.append(n)
                
        if (contador < tamanho):
            return False
        else:
            separador = " "
            usuario = separador.join(us)
            return (usuario)
        

API_KEY = keys.consumer_key
API_SECRET = keys.consumer_secret
ACCESS_TOKEN = keys.Acess_Token
ACCESS_TOKEN_SECRET = keys.Acess_Token_Secret


'''
API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
'''

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
myStreamListener = MyStreamListener()



def rodar():

    try:
        print('Bot rodando')
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
        myStream.filter(track=['pode isso Arnaldo?'])

    except Exception as inst:
        print(inst)

interval_monitor = IntervalRunner(1800, rodar)
interval_monitor.start()



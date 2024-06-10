import json
import pyaudio
from vosk import Model, KaldiRecognizer, SetLogLevel
###import  pyttsx3
import time
import keyboard
import os
import sys

    # FOR COMMA: TIMING CHECK
x=0
    # AUDIO-STREAM CHECK
streamIs = 0

    # FOR TALKER
###engine = pyttsx3.init()
###engine.setProperty('rate', 200)
###engine.setProperty('volume', 1)
class Helper():
    def __init__(self):
        SetLogLevel(-1)

            # GET ABSOLUTE WAY FOR PYINSTALLER BUILD
        def get_resource_path(relative_path):
            try:
                # PyInstaller creates a temporary _MEIPASS folder and saves files there
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)
        relative_model_path = "vosk-model-small-ru-0.22"
        absolute_model_path = get_resource_path(relative_model_path)
        model = Model(absolute_model_path)

        #print ("Model initiated")
        ###engine.say("распознавание голоса готово к работе")
        ###engine.runAndWait()

        self.rec = KaldiRecognizer(model, 16000)
        
        '''self.cmds = {
            ('время', 'сколько времени', 'какой час', 'сколько время') : self.get_time,
            ('спасибо', 'от души', 'сенк') : self.thx,
            ('прощай', 'пока', 'до свидания', 'гуд бай') : self.exit,
            ('привет', 'ку', 'приветствую', 'хелоу') : self.hello,
        }
    # Выход
    def exit(self):
        list_1 = ['Надеюсь мы скоро увидимся', 'Рада была помочь', 'Пока пока', 'Я отключаюсь']
        self.say(random.choice(list_1))
        self.engine.stop()
        os.system('cls')
        raise SystemExit(0)
    # Поиск
    def google(self, text):
        url = f'https://www.google.com/search?q={" ".join(text)}'
        self.say(f'Ищу в интернете: {" ".join(text)}')
        webbrowser.open(url)
    # Приветствие
    def hello(self):
        hello_list = ['привет', 'ку', 'приветствую', 'хелоу', 'дарова', 'здорово']
        self.say(random.choice(hello_list))
    # Открытие браузера
    def open_browser(self, task):
        links = {
            ('ютуб', 'ютюб'): 'https://youtube.com/',
            ('вк', 'вконтакте', 'контакт'): 'https:vk.com/feed',
            ('браузер', 'интернет', 'гугл'): 'https://google.com/',
            ('инстаграм', 'инста', 'инсту'): 'https://www.instagram.com/',
        }
        j = 0
        if 'и' in task:
            task = task.replace('и', '').replace('  ', ' ')
        double_task = task.split()
        if j != len(double_task):
            for i in range(len(double_task)):
                for vals in links:
                    for word in vals:
                        if fuzz.ratio(word, double_task[i]) > 75:
                            webbrowser.open(links[vals])
                            self.say('Открываю ' + double_task[i])
                            j += 1
                            os.system('cls')
                            print("Я вас слушаю...")
                            break
    # Получить время
    def get_time(self):
        now = datetime.datetime.now()
        self.engine.say("Сейчас " + str(now.hour)  + ":" + str(now.minute))
        self.engine.runAndWait()
    # Спасибо
    def thx(self):
        thx_list = ['На здоровье', 'Обращайся', 'Не за что', 'Не стоит благодарности', 'Это моя работа', 'Обращайтесь еще', 'Рад был помочь']
        self.say(random.choice(thx_list))
    #Talker
###    def say(self, text):
###        self.engine.say(text)
###        self.engine.runAndWait()'''


    def listen(self):
        global streamIs
            # Outputs  a sentence in yield
        while True:
                # ALt+WIN check
            while not (keyboard.is_pressed('alt') and keyboard.is_pressed('win')):
                
                if streamIs == 1:
                    while True:
                        try:
                            self.stream.stop_stream()
                            self.stream.close()
                            break
                        except Exception as e:
                            time.sleep(1)

                    streamIs = 0
                time.sleep(0.3)

            if streamIs == 0:        
                while True:
                    try:
                        self.stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1,rate=16000, input=True, frames_per_buffer=500)
                        self.stream.start_stream()
                        break
                    except Exception as e:
                        time.sleep(1)
                streamIs = 1
                
                ###engine.say("слушаю")
                ###engine.runAndWait()
                #print("Cлушаю")
                #time.sleep(2)
                #self.say("слушаю вас")
      
            data = self.stream.read(100, exception_on_overflow=False)
            if self.rec.AcceptWaveform(data) and len(data) > 0:
                answer = json.loads(self.rec.Result())
                if answer["text"]:
                    yield answer["text"]



    def recognize(self):
        global x
        collected_text = []
        first_fragment = True
        last_time = time.time() 

        for text in self.listen():

            '''if text.startswith(('открой', 'запусти', 'зайди', 'зайди на')):
                self.open_browser(text)
            elif text.startswith(('узнай', 'найди')):
                self.google(text.split()[1:])'''
            
            for word in text.split():
                current_time = time.time() 
                if not first_fragment and current_time - last_time >= 2 :  
                    ##print (f"current_time - last_time = {current_time - last_time}")
                    if not ((time.time()-x)>6 and x!=0):
                        collected_text.append(',')  
                collected_text.append(word) 
                last_time = current_time                      

            final_text = ' '.join(collected_text).replace(' ,', ',')
            collected_text = []
            if first_fragment == True or ((time.time()-x)>4 and x!=0) :
                final_text = final_text.capitalize() 
                first_fragment = False

            ##print (f"time.time()-x = {time.time()-x}")   
            x = time.time()
            ##print(final_text)
            keyboard.write(final_text)  

                    ##for keywords in self.cmds:
                    ##    if word in keywords:
                    ##        self.cmds[keywords]()
                    

if __name__ == '__main__':
    while True:
        try:
            Helper().recognize()
        except Exception as e:
            time.sleep(3)
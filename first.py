import vk_api 
from random import choice , randrange 
from vk_api.longpoll import Vk_LongPool, VkEventType 
TOKEN = '' 
Vk_session = vk_api.VkApi (token=TOKEN) 
longpoll =VkLongPoll(vk_session) 
vk = vk_session.get_api()
vars = ['камень', 'ножницы', ' бумага'] 
for event in longpoll.listen():  
    user = str(event.text).lower()
    if event.type ==VkEventType.MESSAGE_NEW and event.to_me and event.text in vars: 
        if event.from_user: 
            vk.messages.send(user_id=event.user_id, message=choice, random_id=randrange(1,100000000)) 
            out = None 
            bot = choice(vars)
            if bot == 'ножницы':  
                if user == 'ножницы' :
                  out = 'Ничья' 
                if bot == 'камень': 
                    if user == 'камень' :
                      out = 'Ничья'
                      if bot == 'бумага': 
                         if user == 'бумага': 
                          out = 'Ничья' 
                          if bot == 'камень': 
                             if user == 'ножницы':
                              out = 'Проигрыш' 
                              if bot == 'бумага': 
                                 if user == 'камень': 
                                    out = 'Проигрыш'
                                    if bot == 'ножницы': 
                                       if user == 'бумага': 
                                          out = 'Проигрыш' 
                                          if bot == 'камень' :
                                          if user == 'бумага': 
                                             out = 'Выигрыш'

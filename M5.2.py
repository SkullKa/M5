import json

t1 = ['Vesna', 'text2', 'Keny']
with open('m5.2.json', 'w') as f:
  json.dump(t1, f)
  
class Modul:
  def __init__(self, title, text, author):
    self.title = title
    self.text = text
    self.author = author
    print ('Заголовок {} Текст {} Автор {}'.format(self.title, self.text, self.author))
    


t = Modul('Zima', 'text6', 'Rokky')
print(t.__dict__)
t2 = (t.__dict__)
with open('m5.2.json', 'w+') as f:
  json.dump(t2, f)
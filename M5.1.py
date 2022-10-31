
class StringVar:

	def __init__(self):
		self.s = ''	

	def set(self, hello):
		self.s = 'Hello'
		print(self.s)
	def get(self):
		return self.s
	
s = StringVar()
print(s.set('alilua'))
print(s.get())



# class Point():

# 	def __init__(self, x, y):	
# 		self.x = x
# 		self.y = y
# 	def __add__(self, other):
# 		return Point(self.x + other.x,
# 		self.y + other.y)
# p1 = Point(1, 1)
# p2 = Point(2, 2)
# p3 = p1 + p2
# p3: (3, 3)
# x = input()
# y = input()


# class Point():


# 	def __init__(self,x ,y):
# 		self.x = x
# 		self.y = y

# 	def distance(self):
# 		return(x ** 2 + y ** 2) ** (1 / 2)


# p1 = Point(2, -2)
# p1.distance()
# x = input()
# y = input()


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** (1 / 2)


p1x = int(input("абсцисс1: "))
p1y = int(input("ординат1: "))

p2x = int(input("абсцисс2: "))
p2y = int(input("ординат2: "))

p1 = Point(p1x, p1y)
p2 = Point(p2x, p2y)

print(p1.dist(p2))




import random
 
class Warrer:
  def __init__(self, name, health=100):
    self.name = name
    self.health = health
    print ('Создан воин {} со здоровьем {}'.format(self.name, self.health))
 
  def strike(self, enemyWarrer):
    if True:
      print('Воин {} нанес урон -20 воину {}'.format(self.name, enemyWarrer.name))
      enemyWarrer.setHealth(enemyWarrer.getHealth() - 20)
    else:
      print('Некореектно заданно здоровье для воина {}'.format(enemyWarrer.name))
      print(type(enemyWarrer.getHealth()))
 
  def setHealth(self, health):
    self.health = health
    print('Установленно здоровье {} для воина {}'.format(self.health, self.name))
 
  def getHealth(self):
    try:
      return self.health
      print('Здоровье воина {} — {}'.format(self.name, self.health))
    except:
      return 'Здоровье не заданно'
      print('Здоровье для воина {} не заданно'.format(self.name))
 

one = Warrer('Поликарп', 100)
two = Warrer('Эфпидокл', 100)
 
while (one.health > 0) and (two.health > 0):
  round = random.randint(1, 2)
 
  if round == 1:
    one.strike(two)
  elif round == 2:
    two.strike(one)
 
if round == 1:
  name = one.name
  enemy_name = two.name
elif round == 2:
  name = two.name
  enemy_name = one.name
 
print('Поздравляем воина {}! Он одержал победу над воином {}'.format(name, enemy_name))



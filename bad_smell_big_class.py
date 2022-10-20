class Warrior:
  pass

class Healer:
  pass

class Tree:
  pass

class Trap:
  pass

class Skills:

  def attack(self):
    warrior = Warrior()
    trap = Trap()


  def defense(self):
    warrior = Warrior()
    healer = Healer()
    tree = Tree()


  def move(self):
    warrior = Warrior()
    healer = Healer()


  def heal(self):
    healer = Healer()


  def on_fire(self):
    tree = Tree()


if __name__ == '__main__':
    skills = Skills()
    skills.attack()
    skills.defense()

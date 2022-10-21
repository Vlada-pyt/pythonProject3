class Skills:

  def attack(self):
    pass


  def defense(self):
    pass


  def move(self):
    pass


  def heal(self):
    pass


  def on_fire(self):
    pass

class Warrior:
  def all_skills(self, skills: Skills):
    skills.attack()
    skills.defense()
    skills.move()

class Healer:
  def all_skills(self, skills: Skills):
    skills.heal()
    skills.defense()


class Tree:
  def all_skills(self, skills: Skills):
    skills.on_fire()
    skills.defense()


class Trap:
  def all_skills(self, skills: Skills):
    skills.attack()


if __name__ == '__main__':
    skills = Skills()
    warrior = Warrior()
    healer = Healer()

    warrior.all_skills(skills)
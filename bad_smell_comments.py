class Unit:

    """Функция реализует перемещение юнита по полю"""

    def __init__(self, position, field, speed=1):
        self.position = position
        self.field = field
        self.speed = speed


    def get_speed(self):
        if self.position == 'fly':
            return self.speed * 1.2
        elif self.position == 'crawl':
            return self.speed * 0.5

    def directions(self, direction):
        speed = self.get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

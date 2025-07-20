class Enemy():
    def __init__(self):
        self.hp = 10
        self.speed = 10.0
        self.alive = True
        self.damageable = True

    def delete(self):
        if self.alive == False:
            pass
class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        return f'{self.size} {self.color} ball, direction {self.direction}'

    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'
        elif self.direction == 'up':
            self.direction = 'down'
        else:
            print("Direction is not set correctly")


my_ball = Ball('red', 'small', 'down')
my_ball.color = 'green'

print("I just bounced the ball")
print("I am a", my_ball)
#"I am a <__main__.Ball object at 0x1024f6f90>"
print("Now I'm going to bounce the ball")
print()
my_ball.bounce()
print("Now the ball is going", my_ball.direction)

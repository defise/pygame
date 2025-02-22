class Camera:
    def __init__(self, width, height):
        self.dx = 0
        self.dy = 0
        self.width = width
        self.height = height

    def apply(self, sprite):
        sprite.rect.x += self.dx
        sprite.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.width // 2 - self.width // 2)
        self.dy = -(target.rect.y + target.rect.height // 2 - self.height // 2)

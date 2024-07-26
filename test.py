from scene import *
import random

# Define the Star class
class Star:
    def __init__(self, width, height):
        # Initialize a star with random position and speed
        self.x = random.uniform(0, width)
        self.y = random.uniform(0, height)
        self.z = random.uniform(0.1, width)
        self.width = width
        self.height = height

    def update(self):
        # Move the star closer to the viewer
        self.z -= 2
        if self.z <= 0:
            # Reset the star to the far distance
            self.x = random.uniform(0, self.width)
            self.y = random.uniform(0, self.height)
            self.z = self.width

    def draw(self):
        # Calculate the size of the star
        size = (self.width - self.z) / self.width * 5
        if size < 1:
            size = 1

        # Calculate the 2D position on the screen
        sx = (self.x - self.width / 2) * (self.width / self.z) + self.width / 2
        sy = (self.y - self.height / 2) * (self.width / self.z) + self.height / 2

        # Draw the star
        fill(1, 1, 1)
        ellipse(sx, sy, size, size)

# Define the Starfield class, inheriting from the Scene class
class Starfield(Scene):
    def setup(self):
        # Set up the scene
        self.stars = [Star(self.size.w, self.size.h) for _ in range(200)]

    def update(self):
        # Update each star and draw it on the screen
        background(0, 0, 0)
        for star in self.stars:
            star.update()
            star.draw()

# Run the scene
run(Starfield())

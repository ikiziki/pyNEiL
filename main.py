# main.py

from scene import *
from lib.manager import GameStateManager
from src.states.loading_state import LoadingState

class MyGame(Scene):
  def setup(self):
    self.state_manager = GameStateManager()
    self.state_manager.register_state('loading', LoadingState())
    self.state_manager.switch_state('loading')

  def update(self):
    self.state_manager.update(self.dt)

  def draw(self):
    self.state_manager.draw()

  def touch_began(self, touch):
    self.state_manager.touch_began(touch)

  def touch_moved(self, touch):
    self.state_manager.touch_moved(touch)

  def touch_ended(self, touch):
    self.state_manager.touch_ended(touch)

if __name__ == '__main__':
  run(MyGame())


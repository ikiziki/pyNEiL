# src/states/loading_state.py

from src.base_state import GameState
from src.states.menu_state import MenuState

class LoadingState(GameState):
  def enter(self, **params):
    self.manager.register_state('menu', MenuState())

  def exit(self):
    pass

  def update(self, dt):
    pass

  def draw(self):
    pass

  def touch_began(self, touch):
    pass

  def touch_moved(self, touch):
    pass

  def touch_ended(self, touch):
    self.manager.switch_state('menu')


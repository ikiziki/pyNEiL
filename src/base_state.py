# src/base_state.py

class GameState:
  def __init__(self):
    self.manager = None

  def enter(self, **params):
    pass

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
    pass

  def set_manager(self, manager):
    """Set the state manager for accessing the state manager's methods."""
    self.manager = manager


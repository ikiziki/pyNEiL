# lib/manager.py

class GameStateManager:
  def __init__(self):
    self.states = {}
    self.current_state = None

  def register_state(self, name, state):
    self.states[name] = state
    state.set_manager(self)

  def switch_state(self, name, **params):
    if self.current_state:
      self.current_state.exit()

    self.current_state = self.states.get(name)

    if self.current_state:
      self.current_state.enter(**params)

  def update(self, dt):
    if self.current_state:
      self.current_state.update(dt)

  def draw(self):
    if self.current_state:
      self.current_state.draw()

  def touch_began(self, touch):
    if self.current_state:
      self.current_state.touch_began(touch)

  def touch_moved(self,touch):
    if self.current_state:
      self.current_state.touch_moved(touch)

  def touch_ended(self, touch):
    if self.current_state:
      self.current_state.touch_ended(touch)


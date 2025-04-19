from pynput import keyboard
from core.app_global_state import AppGlobalState

class InputHandler:
  COMBINATION = {keyboard.Key.ctrl_r, keyboard.KeyCode(char='v')}

  def __init__(self, app_global_state: AppGlobalState):
    self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
    self.listener.start()
    self.current_keys = set()
    self.app_global_state = app_global_state

  def on_press(self, key):
    self.current_keys.add(key)

    if self.is_combination_pressed():
      self.app_global_state.set('is_recording', True)
      print("CTRL+V pressionado")

  def on_release(self, key):
    if self.any_key_pressed():
      self.app_global_state.set('is_recording', False)
      print(f'Liberando {key}')
      self.current_keys.clear()

  def is_combination_pressed(self):
    return all(k in self.current_keys for k in self.COMBINATION)

  def any_key_pressed(self):
    return any(k in self.current_keys for k in self.COMBINATION)
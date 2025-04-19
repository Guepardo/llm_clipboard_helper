import threading

class AppGlobalState:
  _instance = None
  _lock = threading.Lock()  # Lock para o singleton

  def __new__(cls):
      with cls._lock:
          if cls._instance is None:
              cls._instance = super(AppGlobalState, cls).__new__(cls)
              cls._instance._init_state()
          return cls._instance

  def _init_state(self):
    self._state_lock = threading.Lock()
    self._data = {}

  def set(self, key, value):
      print("setando", key, value)
      with self._state_lock:
          self._data[key] = value

  def get(self, key, default=None):
      print("pegando", key)
      with self._state_lock:
          return self._data.get(key, default)

  def clear(self):
      with self._state_lock:
          self._data.clear()
from pynput import keyboard
from core.app_global_state import AppGlobalState
from transcript.transcriber import Transcriber


class InputHandler:
    COMBINATION = {keyboard.Key.ctrl_r, keyboard.KeyCode(char='v')}

    def __init__(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        self.current_keys = set()
        self.transcriber = Transcriber()

    def on_press(self, key):
        self.current_keys.add(key)

        if self.is_combination_pressed():

            if not self.transcriber.is_transcribing:
                print("Listening...")
                self.transcriber.listen()
            else:
                print("Transcribing...")
                text = self.transcriber.stop_listen()
                print(text['text'])

    def on_release(self):
        if self.any_key_pressed():
            self.current_keys.clear()

    def is_combination_pressed(self):
        return all(k in self.current_keys for k in self.COMBINATION)

    def any_key_pressed(self):
        return any(k in self.current_keys for k in self.COMBINATION)

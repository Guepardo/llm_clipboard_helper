from pynput import keyboard
from core.app_global_state import AppGlobalState
from response.response_coordinator import ResponseCoordinator
from transcript.transcriber import Transcriber
from utils.helpers import beep

class InputHandler:
    COMBINATION = {keyboard.Key.ctrl, keyboard.KeyCode(char='m')}

    def __init__(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        self.current_keys = set()
        self.transcriber = Transcriber()
        self.response_coordinator = ResponseCoordinator()

    def on_press(self, key):
        self.current_keys.add(key)

        if self.is_combination_pressed():

            if not self.transcriber.is_transcribing:
                print("Listening...")
                beep()
                self.transcriber.listen()
            else:
                print("Transcribing...")
                beep()
                text = self.transcriber.stop_listen()
                self.response_coordinator.generate_response(text['text'])  # text['text']

    def on_release(self):
        if self.any_key_pressed():
            self.current_keys.clear()

    def is_combination_pressed(self):
        return all(k in self.current_keys for k in self.COMBINATION)

    def any_key_pressed(self):
        return any(k in self.current_keys for k in self.COMBINATION)

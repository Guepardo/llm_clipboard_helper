from cli.input_handler import InputHandler
from core.app_global_state import AppGlobalState
from time import sleep

def main():
  app_global_state = AppGlobalState()
  input_handler = InputHandler(app_global_state=app_global_state)

main()

sleep(912)
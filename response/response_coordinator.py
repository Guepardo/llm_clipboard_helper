from response.presenter.presenter import Presenter
from response.prompt_generator import PromptGenerator
from response.response_generator import ResponseGenerator


class ResponseCoordinator:
    def __init__(self):
        self.prompt_generator = PromptGenerator()
        self.response_generator = ResponseGenerator()
        self.response_presenter = Presenter()

    def generate_response(self, text):
        prompt = self.prompt_generator.generate_prompt(text)
        response = self.response_generator.generate_response(prompt)
        self.response_presenter.present(response)

import pyperclip


class PromptGenerator:
    PROMPT_TEMPLATE = """"
  Mantenha o texto resumido em poucas palavaras.
  Lembre-se que o local onde o texto será exibido é bem pequeno.
  Você é um programador experiente que ajuda pessoas com dúvidas de programação.

  Siga o prompt abaixo:
  #TEXT#

  Aqui estão dados adicionais que podem complementar a dúvida acima:
  #CLIP_BOARD#"
  """

    def generate_prompt(self, text):
        prompt = self._replace_text(text)
        print(prompt)
        return prompt

    def _replace_text(self, text):
        return self.PROMPT_TEMPLATE.replace("#TEXT#", text).replace(
            "#CLIP_BOARD#", pyperclip.paste())

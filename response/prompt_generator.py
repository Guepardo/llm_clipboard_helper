import pyperclip


class PromptGenerator:
    PROMPT_TEMPLATE = """
    Responda como um programador experiente, técnico e preciso, no estilo de Linus Torvalds.

    - Mantenha o texto direto, com frases curtas e linguagem clara.
    - Evite destaques com * ou _.
    - Seja detalhista e técnico, mesmo que às vezes se prolongue um pouco.
    - Não ultrapasse 1000 caracteres.

    Instrução principal:
    #TEXT#

    Informações adicionais que podem ajudar:
    #CLIP_BOARD#
    """

    def generate_prompt(self, text):
        prompt = self._replace_text(text)
        print(prompt)
        return prompt

    def _replace_text(self, text):
        return self.PROMPT_TEMPLATE.replace("#TEXT#", text).replace(
            "#CLIP_BOARD#", pyperclip.paste())

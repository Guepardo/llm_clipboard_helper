import re
from utils.helpers import in_groups_of

class Formatter:
    def format(self, response):
        phrases = re.split(r'(?<=[.!?])\s+', response)

        formatted_text_array = []

        for i, phrase in enumerate(phrases, 1):
            if i == 1:
                formatted_text_array.append(self.split_first_phrase(phrase))
            else:
                formatted_text_array.append(phrase)

        return "\n".join(formatted_text_array)

    def split_first_phrase(self, phrase):
        tmp = []
        for words in in_groups_of(phrase.split(" "), 10):
            tmp.append(" ".join(words))

        return "\n".join(tmp)


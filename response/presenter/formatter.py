import re

from utils.helpers import in_groups_of

import re

from utils.helpers import in_groups_of

class Formatter:
    def format(self, response):
        phrases = re.split(r'(?<=[.!?])\s+', response)

        to_read = []

        for i, phrase in enumerate(phrases, 1):
            if i == 1:
                to_read.append(self.split_first_phrase(phrase))
            else:
                to_read.append(phrase)

        return "\n".join(to_read)

    def split_first_phrase(self, phrase):
        tmp = []
        for words in in_groups_of(phrase.split(" "), 10):
            tmp.append(" ".join(words))

        return "\n".join(tmp)


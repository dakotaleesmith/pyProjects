### To add:
### - New attribute: theme
### - Make some attributes optional
### - Freeze attributes and re-run
### - Better read of attributes — not .py files, for example, but .txt (then use context manager)
### - Create GUI using Tkinter

import random
import characters
import settings
import situations
import genres

class Prompt:
    """Returns a random prompt for a short story"""
    def __init__(self):
        self.character = random.choice(characters.characters)
        self.setting = random.choice(settings.settings)
        self.situation = random.choice(situations.situations)
        self.genre = random.choice(genres.genres)

    def create_prompt(self):
        """Creates prompt from randomly selected story attributes"""
        prompt = f"{self.character} {self.situation.lower()} in {self.setting.lower()}. {self.genre.title()}."
        return prompt

if __name__ == "__main__":
    p = Prompt()
    print(p.create_prompt())

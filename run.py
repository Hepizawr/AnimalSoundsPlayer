import sys
from pathlib import Path
from playsound import playsound

from app.modules.backend.tools import get_animal_sound_file, get_animal_from_json
from config import ANIMAL_SOUNDS_DICT

animal = get_animal_from_json(json_file=Path("./app/source/jsons/file.json"))

animal_sound = ANIMAL_SOUNDS_DICT.get(animal)

if not (sound_file := get_animal_sound_file(animal_sound=animal_sound)):
    sys.exit()

# print(sound_file)
playsound(sound_file)

from pathlib import Path
import os

from app.modules.backend.schemas import JsonModel
from config import SOUNDS_DIR, SOUND_FORMATS, ANIMAL_SOUNDS_DICT


def get_animal_sound_path(animal: str) -> str | None:
    if animal_sound := ANIMAL_SOUNDS_DICT.get(animal):
        for sound_format in SOUND_FORMATS:
            sound_file = os.path.join(SOUNDS_DIR, (animal_sound + sound_format))
            if os.path.exists(sound_file):
                return sound_file
    return None


def get_animal_from_json(json_file: Path) -> str | None:
    try:
        json_data = Path(json_file).read_text()
        return JsonModel.model_validate_json(json_data).animal
    except:
        return None

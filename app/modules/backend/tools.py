from pathlib import Path

from app.modules.backend.schemas import JsonModel
from config import SOUNDS_DIR, SOUND_FORMATS


def get_animal_sound_file(animal_sound: str) -> Path | None:
    if animal_sound:
        for sound_format in SOUND_FORMATS:
            sound_file = Path(SOUNDS_DIR + animal_sound + sound_format)
            if sound_file.is_file():
                return sound_file
    return None


def get_animal_from_json(json_file: Path) -> str | None:
    try:
        json_data = Path(json_file).read_text()
        return JsonModel.model_validate_json(json_data).animal
    except:
        return None

import flet as ft

from app.modules.backend.tools import get_animal_from_json, get_animal_sound_path


class SoundApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.audio_playing = False
        self.volume_muted = False

        self.audio = ft.Audio(autoplay=False)
        self.file_picker = ft.FilePicker(on_result=self._on_file_picked)

        self.file_upload_button = ft.TextButton(
            text="Upload File",
            width=835,
            height=100,
            on_click=lambda _: self.file_picker.pick_files(allow_multiple=False, file_type=ft.FilePickerFileType.CUSTOM,
                                                           allowed_extensions=["json"])
        )

        self.play_button = ft.IconButton(
            icon=ft.icons.PLAY_ARROW,
            width=100,
            height=100,
        )

        file_handler_row = ft.Row(
            controls=[self.file_upload_button, self.play_button],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.volume_button = ft.IconButton(
            icon=ft.icons.VOLUME_UP,
            icon_size=25,
            on_click=self._toggle_volume
        )

        self.volume_slider = ft.Slider(
            min=0, max=1, value=1,
            width=745,
        )

        volume_handler_row = ft.Row(
            controls=[self.volume_button, self.volume_slider],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        )

        self.controls = [self.file_picker, file_handler_row, volume_handler_row]

    def _on_file_picked(self, e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            file_name = e.files[0].name

            if not (animal := get_animal_from_json(file_path)):
                self.page.open(ft.AlertDialog(
                    title=ft.Text("Invalid JSON"),
                    content=ft.Text("Json file does not have an “animal” field or it is empty "),
                ))
                return

            if not (animal_sound_path := get_animal_sound_path(animal)):
                self.page.open(ft.AlertDialog(
                    title=ft.Text("Sorry😢"),
                    content=ft.Text(f"We don't know what a {animal} sounds like"),
                ))

                return

            self.controls.append(self.audio)

            self.file_upload_button.text = file_name
            self.audio.src = animal_sound_path
            self.audio.volume = self.volume_slider.value
            self.play_button.on_click = self._toggle_audio_playback
            self.volume_slider.on_change = self._change_audio_volume

            self.update()

    def _change_audio_volume(self, e):
        self.audio.volume = e.control.value
        self.audio.update()

    def _toggle_audio_playback(self, e):
        if self.audio_playing:
            self.play_button.icon = ft.icons.PLAY_ARROW
            self.audio.pause()
        else:
            self.play_button.icon = ft.icons.STOP
            self.audio.play()

        self.audio_playing = not self.audio_playing
        self.update()

    def _toggle_volume(self, e):
        if self.volume_muted:
            self.volume_button.icon = ft.icons.VOLUME_UP
            self.volume_slider.disabled = False
            self.audio.volume = self.volume_slider.value
        else:
            self.volume_button.icon = ft.icons.VOLUME_MUTE
            self.volume_slider.disabled = True
            self.audio.volume = 0

        self.volume_muted = not self.volume_muted
        self.update()

import flet as ft


class Player(ft.Container):
    def __init__(self, audio_file, on_play_callback):
        super().__init__()

        self.audio_file = audio_file
        self.on_play_callback = on_play_callback

        # Создаем аудио компонент
        self.audio = ft.Audio(
            src=audio_file,
            autoplay=False,
            volume=1.0
        )

        # Полоса громкости
        self.volume_slider = ft.Slider(value=1, min=0, max=1, divisions=10, on_change=self.change_volume)

        # Иконка файла
        self.file_icon = ft.Icon(ft.icons.DESCRIPTION)

        # Название файла
        self.file_name = ft.Text(self.audio_file.split('/')[-1])

        # Кнопка Play
        self.play_button = ft.IconButton(
            icon=ft.icons.PLAY_ARROW,
            on_click=self.play_clicked
        )

        # Создаем строку с элементами (иконка файла, название и кнопка Play)
        self.display_view = ft.Row(
            controls=[
                self.file_icon,  # Иконка файла
                self.file_name,  # Название файла
                self.play_button  # Кнопка Play
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        # Основной контейнер с отображением аудиофайла и полосой громкости
        self.content = ft.Column(
            controls=[
                self.display_view,
                self.volume_slider  # Полоса громкости
            ]
        )

        self.controls = [self.content]

    # Метод для изменения громкости
    def change_volume(self, e):
        self.audio.volume = e.control.value

    # Метод для запуска аудио
    def play_clicked(self, e):
        self.on_play_callback(self)
        self.audio.play()


class PlayerApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.players = ft.Column()

        # Добавляем несколько примеров аудиофайлов для демонстрации
        self.audio_files = [
            "./app/source/sounds/meow.mp3",
        ]

        # Создаем плееры для каждого аудиофайла
        for audio_file in self.audio_files:
            player = Player(audio_file, self.play_audio)
            self.players.controls.append(player)

        # Добавляем все плееры в интерфейс
        self.controls = [
            ft.Text(value="Audio Player App", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
            self.players
        ]

    # Метод для запуска аудио
    def play_audio(self, player):
        # Останавливаем все остальные аудиофайлы
        for p in self.players.controls:
            if p != player:
                p.audio.pause()


def main(page: ft.Page):
    page.title = "Audio Player App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Добавляем приложение на страницу
    page.add(PlayerApp())


ft.app(target=main)

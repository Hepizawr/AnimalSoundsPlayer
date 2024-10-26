import flet as ft
from app.modules.frontend.SoundApp import SoundApp


def main(page: ft.Page):
    page.window.width = 1000
    page.window.height = 250
    page.window.resizable = False
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    sound_app = SoundApp()

    page.add(sound_app)


if __name__ == '__main__':
    ft.app(main)

from itertools import cycle
import os
import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300


class Window(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "FFmpeg sound demo")
        self.sounds = []
        for root, dirs, files in os.walk('sounds'):
            for file in files:
                if file.endswith(('.wav', '.ogg', '.mp3')):
                    sound = arcade.load_sound('sounds/' + file)
                    self.sounds.append((sound, file))
        self.sound_gen = cycle(self.sounds)

    def on_key_press(self, symbol, mod):
        sound, file = next(self.sound_gen)
        arcade.play_sound(sound)
        print(f"Playing {file}")


window = Window()
arcade.run()

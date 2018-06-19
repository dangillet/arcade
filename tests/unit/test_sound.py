import pytest
from pathlib import Path


def test_import(mock_window):
    import arcade
    assert 'load' in arcade.load_sound.__name__


@pytest.mark.not_ci
@pytest.mark.parametrize('sound_format', ('wav', 'mp3', 'ogg'))
def test_play_sound(mock_window, sound_format):
    import arcade
    import pyglet
    fn = Path(__file__).parent / f'laser1.{sound_format}'
    my_sound = arcade.load_sound(fn)
    player = arcade.play_sound(my_sound)
    player.on_player_eos = pyglet.app.exit
    arcade.run()

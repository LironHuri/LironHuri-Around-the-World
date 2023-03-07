from pygame import mixer


mixer.init()
def game_playing():
    mixer.music.load("sounds/background_music_game_playing.wav")
    mixer.music.play(-1)


def pause_game_playing():
    mixer.music.stop()
game_playing()



def main():
    print("classes & functions is ON")
    print(f"working from {__name__}")


if "__main__"==__name__:
    main()


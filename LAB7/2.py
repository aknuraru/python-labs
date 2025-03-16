import pygame
import os

pygame.init()

# Set up the screen and window caption
screen = pygame.display.set_mode((600, 200))
pygame.display.set_caption("Music Player")

# Set up the font for displaying instructions (Fixed path)
font_path = r"/Users/ryskulaknur/Desktop/python_labs/LAB7/Minecraft.ttf"
font = pygame.font.Font(font_path, 25)

text = [
    "'S' - Start playing music",
    "'Space' - Pause/Unpause music",
    "'P' - Play previous track",
    "'N' - Play next track"
]
instructions = [font.render(line, False, 'green') for line in text]

# Set up the playlist (Fixed paths)
MUSIC_DIR = r"/Users/ryskulaknur/Desktop/python_labs/LAB7/music/"
playlist = [
    os.path.join(MUSIC_DIR, "song1.mp3"),
    os.path.join(MUSIC_DIR, "song2.mp3"),
    os.path.join(MUSIC_DIR, "song3.mp3")
]

# Initialize the mixer
pygame.mixer.init()
current_song_index = 0

# Start the game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen
    y = 10
    for instruction in instructions:
        screen.blit(instruction, (10, y))
        y += 30
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Pause or unpause the current song
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_s:
                # Start playing the current song from the beginning
                pygame.mixer.music.load(playlist[current_song_index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_n:
                # Play the next song in the playlist
                current_song_index = (current_song_index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song_index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_p:
                # Play the previous song in the playlist
                current_song_index = (current_song_index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song_index])
                pygame.mixer.music.play()

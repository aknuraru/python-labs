'''
import pygame
import time

# Initialize pygame
pygame.init()

# Load clock and hand images
clock_img = pygame.image.load("/Users/ryskulaknur/Desktop/python_labs/LAB7/image/mickeyclock.jpeg")
minute_hand_img = pygame.image.load("/Users/ryskulaknur/Desktop/python_labs/LAB7/image/hand-1.png")
second_hand_img = pygame.image.load("/Users/ryskulaknur/Desktop/python_labs/LAB7/image/hand-2.png")


# Set window size and caption
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 750
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("MickeyClock")

# Create a clock object to control the FPS
clock = pygame.time.Clock()

# Set up the main game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the current time
    current_time = time.localtime()
    
    # Calculate angles for the minute and second hands
    minute_angle = (current_time.tm_min / 60) * 360
    second_angle = (current_time.tm_sec / 60) * 360
    
    # Rotate the hand images based on their angles
    minute_hand_rotated = pygame.transform.rotate(minute_hand_img, -minute_angle)
    second_hand_rotated = pygame.transform.rotate(second_hand_img, -second_angle)
    
    # Draw clock and hand images to the screen
    window.blit(clock_img, (0, 0))
    
    # Center the minute hand image on the screen
    minute_hand_x = WINDOW_WIDTH / 2 - minute_hand_rotated.get_width() / 2
    minute_hand_y = WINDOW_HEIGHT / 2 - minute_hand_rotated.get_height() / 2
    window.blit(minute_hand_rotated, (minute_hand_x, minute_hand_y))
    
    # Center the second hand image on the screen
    second_hand_x = WINDOW_WIDTH / 2 - second_hand_rotated.get_width() / 2
    second_hand_y = WINDOW_HEIGHT / 2 - second_hand_rotated.get_height() / 2
    window.blit(second_hand_rotated, (second_hand_x, second_hand_y))
    
    # Update the display
    pygame.display.update()
    
    # Limit the FPS to 60
    clock.tick(60)

# Quit pygame when the game loop is finished
pygame.quit()'
'''

import pygame
import time
import os

# Initialize pygame
pygame.init()

# Load images (ensure correct filenames)
IMAGE_PATH = "/Users/ryskulaknur/Desktop/python_labs/LAB7/image/"
clock_img = pygame.image.load(os.path.join(IMAGE_PATH, "mickeyclock.jpeg"))
minute_hand_img = pygame.image.load(os.path.join(IMAGE_PATH, "hand-1.png"))
second_hand_img = pygame.image.load(os.path.join(IMAGE_PATH, "hand-2.png"))

# Scale clock image if needed
clock_img = pygame.transform.scale(clock_img, (500, 500))

# Set window size and caption
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 750
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("MickeyClock")

# Clock center position
clock_center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Create a clock object to control the FPS
clock = pygame.time.Clock()

# Function to rotate hands correctly
def rotate_hand(image, angle, pivot):
    """ Rotates an image around a pivot point and returns the new rect """
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=pivot)  # Set new center
    return rotated_image, rotated_rect

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the current time
    current_time = time.localtime()
    
    # Calculate angles for the hands
    minute_angle = (current_time.tm_min / 60) * 360
    second_angle = (current_time.tm_sec / 60) * 360
    
    # Rotate the hands and reposition them to rotate from the clock center
    minute_hand_rotated, minute_hand_rect = rotate_hand(minute_hand_img, minute_angle, clock_center)
    second_hand_rotated, second_hand_rect = rotate_hand(second_hand_img, second_angle, clock_center)
    
    # Clear screen before drawing
    window.fill((255, 255, 255))
    
    # Draw clock image (centered)
    clock_rect = clock_img.get_rect(center=clock_center)
    window.blit(clock_img, clock_rect.topleft)
    
    # Draw hands
    window.blit(minute_hand_rotated, minute_hand_rect.topleft)
    window.blit(second_hand_rotated, second_hand_rect.topleft)
    
    # Update display
    pygame.display.update()
    
    # Limit FPS
    clock.tick(60)

# Quit pygame
pygame.quit()



# Import the Pygame library
import pygame

# Initialize Pygame
pygame.init()

# Set the window size
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Red Ball")

# Set the ball properties
ball_radius = 25
ball_x, ball_y = screen_width // 2, screen_height // 2
ball_color = (255, 0, 0)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        # Check if the user wants to quit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Check if the user pressed a key
        elif event.type == pygame.KEYDOWN:
            # Move the ball up if the user pressed the up arrow key
            if event.key == pygame.K_UP:
                ball_y = max(ball_y - 20, ball_radius)
            # Move the ball down if the user pressed the down arrow key
            elif event.key == pygame.K_DOWN:
                ball_y = min(ball_y + 20, screen_height - ball_radius)
            # Move the ball left if the user pressed the left arrow key
            elif event.key == pygame.K_LEFT:
                ball_x = max(ball_x - 20, ball_radius)
            # Move the ball right if the user pressed the right arrow key
            elif event.key == pygame.K_RIGHT:
                ball_x = min(ball_x + 20, screen_width - ball_radius)

    # Draw the background
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update the screen
    pygame.display.update()
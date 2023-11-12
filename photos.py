import os
import pygame
import pygame_gui
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 480  # Adjust to your screen's resolution
IMAGE_DIR = r"C:\Users\nicho\Documents\Coding\Python\Digital Photo Gallery\Photos"  # Replace with your images directory

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a UIManager for pygame_gui
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Define the fade-in and fade-out function
def fade_transition(old_image, new_image):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0,0,0))
    # Fade out
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(old_image, (0, 0))
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)
    # Fade in
    for alpha in range(300, 0, -1):
        fade.set_alpha(alpha)
        screen.blit(new_image, (0, 0))
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(2)

# Define the title screen function
def show_title_screen():
    screen.fill((0, 0, 0))  # Clear the screen
    font = pygame.font.Font(None, 50)  # Choose the font for the title
    text = font.render("Coding With the Doctors Photo Gallery", True, (255, 255, 255))  # Create the title text
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))  # Draw the title text
    pygame.display.flip()  # Update the display

# Function to handle touch events
def handle_event(event):
    if event.type == QUIT:
        pygame.quit()
    elif event.type == MOUSEBUTTONDOWN:
        if event.button == 1:  # Left click
            return 'next'
        elif event.button == 3:  # Right click
            return 'prev'

# Load images
images = []
for filename in os.listdir(IMAGE_DIR):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img = pygame.image.load(os.path.join(IMAGE_DIR, filename))
        img = pygame.transform.scale(img, (WIDTH, HEIGHT))
        images.append(img)

# Create a clock object
clock = pygame.time.Clock()

# Create a button for the title screen
button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH // 2 - 50, HEIGHT // - 100), (100, 50)),
                                      text='Start',
                                      manager=manager)

# Show the title screen
show_title_screen()

# Wait for the user to press the button
start_gallery = False  # Flag to indicate when to start the photo gallery
while not start_gallery:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    start_gallery = True
                    break

        manager.process_events(event)

    manager.update(time_delta)
    manager.draw_ui(screen)

    pygame.display.update()
    pygame.display.flip()  # Ensure the screen updates are displayed

# Main loop
index = 0
while True:
    old_image = images[index]
    image_changed = False
    for event in pygame.event.get():
        action = handle_event(event)
        if action == 'next':
            index = (index + 1) % len(images)
            image_changed = True
        elif action == 'prev':
            index = (index - 1 + len(images)) % len(images)
            image_changed = True

    if image_changed:
        fade_transition(old_image, images[index])

    screen.blit(images[index], (0, 0))
    pygame.display.flip()
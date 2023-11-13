import os
import pygame
import pygame_gui
import sys
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 480  # Adjust to your screen's resolution
IMAGE_DIR = "Photos"  # Replace with your images directory

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)

# Create a UIManager for pygame_gui
manager = pygame_gui.UIManager((WIDTH, HEIGHT))
# Buttons
top_secret_button = None
know_button = None
return_button = None
# Global variables
doomsday_running = False

def draw_main():
    global top_secret_button, know_button
    # Create the "TOP SECRET" button
    top_secret_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (150, 50)),
                                                 text='TOP SECRET',
                                                 manager=manager)
    # Create the "Get to know us!" button
    know_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH - 160, 10), (150, 50)),
                                                     text='Get to know us!',
                                                     manager=manager)


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

# Load images
images = []
for filename in os.listdir(IMAGE_DIR):
    if filename.endswith('.bmp') or filename.endswith('.png'):
        img = pygame.image.load(os.path.join(IMAGE_DIR, filename))
        img = pygame.transform.smoothscale(img, (WIDTH, HEIGHT))
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

# Define a theme dictionary
theme = {
    "dark": {
        "font": {
            "name": "fira_code",
            "size": 14,
            "bold": False,
            "italic": False
        },
        "colours": {
            "dark_bg": pygame.Color("#282828"),
            "normal_bg": pygame.Color("#3c3836"),
            "hovered_bg": pygame.Color("#504945"),
            "disabled_bg": pygame.Color("#282828"),
            "selected_bg": pygame.Color("#689d6a"),
            "active_bg": pygame.Color("#98971a"),
            "dark_text": pygame.Color("#a89984"),
            "normal_text": pygame.Color("#ebdbb2"),
            "hovered_text": pygame.Color("#ebdbb2"),
            "disabled_text": pygame.Color("#a89984"),
            "selected_text": pygame.Color("#ebdbb2"),
            "active_text": pygame.Color("#ebdbb2"),
            "dark_icon": pygame.Color("#a89984"),
            "normal_icon": pygame.Color("#ebdbb2"),
            "hovered_icon": pygame.Color("#ebdbb2"),
            "disabled_icon": pygame.Color("#a89984"),
            "selected_icon": pygame.Color("#ebdbb2"),
            "active_icon": pygame.Color("#ebdbb2"),
            "dark_outline": pygame.Color("#a89984"),
            "normal_outline": pygame.Color("#ebdbb2"),
            "hovered_outline": pygame.Color("#ebdbb2"),
            "disabled_outline": pygame.Color("#a89984"),
            "selected_outline": pygame.Color("#ebdbb2"),
            "active_outline": pygame.Color("#ebdbb2"),
        }
    }
}

# Create a UIManager with the theme
manager = pygame_gui.UIManager((WIDTH, HEIGHT), os.path.join(os.getcwd(), "theme.json"))
# Define the doomsday is running function
def doomsday_on():
    global doomsday_running
    doomsday_running = True
# Define the doomsday function
def doomsday():
    # Clear the screen
    screen.fill((0, 0, 0))

    # Kill the existing buttons
    top_secret_button.kill()
    know_button.kill()

    # Create a new loop that simulates a doomsday button
    doomsday = True
    countdown = 10

    # Create the "DO NOT TOUCH" button
    dont_touch_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH // 2 - 75, HEIGHT // 2 - 25), (150, 50)),
                                                     text='DO NOT TOUCH',
                                                     manager=manager)

    # Create the "RETURN" button
    global return_button
    return_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH - 160, 10), (150, 50)),
                                                 text='RETURN',
                                                 manager=manager)

    while doomsday:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == return_button:
                        # Kill the "DO NOT TOUCH" button
                        dont_touch_button.kill()
                        doomsday = False
                        break
                    elif event.ui_element == dont_touch_button:
                        # Kill the "DO NOT TOUCH" button
                        dont_touch_button.kill()
                        # Start the countdown
                        for i in range(countdown, 0, -1):
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    sys.exit()
                            screen.fill(theme["dark"]["colours"]["dark_bg"])
                            font = pygame.font.SysFont(theme["dark"]["font"]["name"], 100)
                            text = font.render(str(i), True, pygame.Color("red"))
                            text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
                            screen.blit(text, text_rect)
                            pygame.display.flip()
                            pygame.time.delay(1000)
                        # Display the "You died" message
                        screen.fill(theme["dark"]["colours"]["dark_bg"])
                        font = pygame.font.SysFont(theme["dark"]["font"]["name"], 100)
                        text = font.render("You died", True, pygame.Color("red"))
                        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
                        screen.blit(text, text_rect)
                        
                        # Display the "I told you so" message
                        font = pygame.font.SysFont(theme["dark"]["font"]["name"], 50)
                        text = font.render("I told you so >:)", True, pygame.Color("red"))
                        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2 + 75))
                        screen.blit(text, text_rect)
                        
                        pygame.display.flip()
                        pygame.time.delay(2000)

            # Move the process_events call inside the for loop
            manager.process_events(event)

        manager.update(time_delta)
        manager.draw_ui(screen)

        pygame.display.flip()

    # Destroy the "DO NOT TOUCH" and "RETURN" buttons
    return_button.kill()

    # Draw the main buttons
    draw_main()

    # Reset the doomsday_running flag
    doomsday_running = False

    # Blit an image onto the screen after returning from doomsday
    screen.blit(images[index], (0, 0))

    # Return to the slideshow
    start_gallery = True

def know():
        # Clear the screen
        screen.fill((0, 0, 0))

        # Kill the existing buttons
        top_secret_button.kill()
        know_button.kill()

        # Create the "RETURN" button
        global return_button
        return_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH - 160, 10), (150, 50)),
                                                     text='RETURN',
                                                     manager=manager)

        # Load images from the "Slides" folder
        slide_dir = "Slides"
        slide_images = []
        for filename in os.listdir(slide_dir):
            if filename.endswith('.bmp') or filename.endswith('.png') or filename.endswith('.tif'):
                img = pygame.image.load(os.path.join(slide_dir, filename))
                img = pygame.transform.smoothscale(img, (WIDTH, HEIGHT))
                slide_images.append(img)

        # Create arrow buttons
        arrow_left_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, HEIGHT // 2 - 25), (35, 25)),
                                                         text='<',
                                                         manager=manager)
        arrow_right_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH - 60, HEIGHT // 2 - 25), (35, 25)),
                                                          text='>',
                                                          manager=manager)

        # Display the first slide
        slide_index = 0
        screen.blit(slide_images[slide_index], (0, 0))

        # Loop until the user clicks the "RETURN" button
        while True:
            time_delta = clock.tick(60)/1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == return_button:
                            # Kill the arrow buttons and "RETURN" button
                            arrow_left_button.kill()
                            arrow_right_button.kill()
                            return_button.kill()

                            # Draw the main buttons
                            draw_main()

                            # Return to the slideshow
                            return

                        elif event.ui_element == arrow_left_button:
                            # Decrement the slide index
                            slide_index = (slide_index - 1) % len(slide_images)
                            screen.blit(slide_images[slide_index], (0, 0))

                        elif event.ui_element == arrow_right_button:
                            # Increment the slide index
                            slide_index = (slide_index + 1) % len(slide_images)
                            screen.blit(slide_images[slide_index], (0, 0))

                manager.process_events(event)

            manager.update(time_delta)
            manager.draw_ui(screen)

            pygame.display.flip()

# Confirm both buttons are drawn
draw_main()

# Main loop
index = 0
last_change_time = pygame.time.get_ticks()
change_interval = random.randint(3000, 4000) # 3-4 seconds
while True:
    old_image = images[index]
    image_changed = False
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Handle button trees
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == top_secret_button:
                    doomsday()
                elif event.ui_element == know_button:
                    know()

        manager.process_events(event)

    # Change the photo if the time interval has elapsed
    if pygame.time.get_ticks() - last_change_time > change_interval:
        index = (index + 1) % len(images)
        image_changed = True
        last_change_time = pygame.time.get_ticks()
        change_interval = random.randint(3000, 4000) # 3-4 seconds

    screen.blit(images[index], (0, 0))
    if image_changed and not doomsday_running:
        screen.blit(images[index], (0, 0))
    if image_changed and doomsday_running:
        screen.blit(images[index], (0, 0))

    # Draw the buttons after drawing the images
    manager.update(time_delta)
    manager.draw_ui(screen)

    pygame.display.flip()
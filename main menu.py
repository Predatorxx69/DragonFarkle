import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Load the background image
background_image = pygame.image.load('background_mainmenu.png')  # Replace 'background_image.jpg' with your image file
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Home Screen")

# Function to display text on the screen
def display_text(text, x, y):
    text_surface = FONT.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Main menu loop
def main_menu():
    while True:
        screen.blit(background_image, (0, 0))  # Draw the background image

        # Display options
        display_text("New Game", SCREEN_WIDTH // 2, 200)
        display_text("Rules", SCREEN_WIDTH // 2, 300)
        display_text("Credits", SCREEN_WIDTH // 2, 400)
        display_text("Exit", SCREEN_WIDTH // 2, 500)

        # Update the display
        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if the mouse click is within the bounds of an option
                if 300 <= mouse_pos[1] <= 350:  # New Game
                    print("Starting New Game")
                    # Add code to start a new game here
                elif 400 <= mouse_pos[1] <= 450:  # Rules
                    print("Showing Rules")
                    # Add code to display rules here
                elif 500 <= mouse_pos[1] <= 550:  # Credits
                    print("Showing Credits")
                    # Add code to display credits here
                elif 600 <= mouse_pos[1] <= 650:  # Exit
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main_menu()

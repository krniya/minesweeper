"""
button_module.py - Pygame Button Module

This module defines a Pygame Button class for creating interactive buttons.
Buttons can have text or images, and their appearance can change when hovered over.

Classes:
    - Button: Represents an interactive button in a Pygame environment.

Usage:
    To use this module, import the Button class and create instances of Button
    with the required parameters to display and handle user interaction with buttons.

"""


class Button:
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        """Initialize the Button.

        Args:
            image (pygame.Surface): The Pygame surface/image for the button (can be None for text-only).
            pos (Tuple[int, int]): The position of the button (x, y).
            text_input (str): The text displayed on the button.
            font (pygame.font.Font): The Pygame font for rendering text.
            base_color (Tuple[int, int, int]): The base color of the button.
            hovering_color (Tuple[int, int, int]): The color of the button when hovered over.
        """
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        """Update and render the button on the screen.

        Args:
            screen (pygame.Surface): The Pygame surface to render the button on.
        """
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        """Check if a given position is within the button area.

        Args:
            position (Tuple[int, int]): The position to check (x, y).

        Returns:
            bool: True if the position is within the button area, False otherwise.
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        """Change the button color based on whether the given position is over the button.

        Args:
            position (Tuple[int, int]): The position to check (x, y).
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[
            1
        ] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

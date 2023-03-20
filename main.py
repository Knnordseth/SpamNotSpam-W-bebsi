import re
import json
import pygame as pg

# Load the list of spam keywords from the JSON file and create a regular expression pattern
def load_spam_keywords():
    with open("SPAMKEYWORDS.json", 'r') as f:
        spam_keywords = json.load(f)['spam_keywords']
    pattern = '|'.join(spam_keywords)
    return spam_keywords, pattern

# Check if the input text is spam
def is_spam(text):
    spam_keywords, pattern = load_spam_keywords()
    match = re.search(pattern, text, re.IGNORECASE)
    return bool(match)

# Create the GUI window and input textbox
def create_input_box(x, y, w, h, font_size):
    font = pg.font.Font(None, font_size)
    input_box = pg.Rect(x, y, w, h)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    return font, input_box, color_inactive, color_active, color, active, text

# Draw the input textbox onto the screen
def draw_input_box(screen, font, text, input_box, color):
    # Render the current text
    txt_surface = font.render(text, True, color)
    # Resize the box if the text is too long
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    # Blit the text
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    # Blit the input_box rect
    pg.draw.rect(screen, color, input_box, 2)

# Check if the input text is spam and update the result label
def check_spam(text, result_label):
    if is_spam(text):
        result_label.config(text="The email is spam.")
    else:
        result_label.config(text="The email is not spam.")

# Main function to run the GUI
def main():
    pg.init()
    screen = pg.display.set_mode((640, 480))
    font_size = 32
    font, input_box, color_inactive, color_active, color, active, text = create_input_box(100, 100, 140, 32, font_size)
    result_label = pg.Label(text="")
    clock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable
                    active = not active
                else:
                    active = False
                # Change the current color of the input box
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        check_spam(text, result_label)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((251, 242, 199))
        draw_input_box(screen, font, text, input_box, color)
        result_label.draw(screen)
        pg.display.flip()
        clock.tick(30)

    pg.quit()

if __name__ == '__main__':
    main()

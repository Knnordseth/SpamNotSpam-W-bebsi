import re
import json
#fjerna tkinter
import pygame as pg #lagt til pygame

#prøv å ordne loada inn json script stuff
f = open('SPAMKEYWORDS.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

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

# Create a GUI window with an input textbox for checking spam emails
def check_spam_gui():
    spam_keywords, pattern = load_spam_keywords()
#sjekker tekstboksen inni GUI tekstfeltet med get() methoden som tar "1.0", "end-1c" for å velge alt av tekst i feltet
    def check_spam():
        text = input_box.get("1.0", "end-1c")
        if is_spam(text):
            result_label.config(text="The email is spam.")
        else:
            result_label.config(text="The email is not spam.")

    # GUI code goes here
    # Create the GUI window and input textbox



def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((251, 242, 199))

        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if rectangle_rect.collidepoint(mouse_pos):
                check_spam_gui()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()
            if rectangle_rect.collidepoint(mouse_pos):
                check_spam()

    # Draw the rectangle onto the screen
    screen.blit(rectangle_surface, rectangle_rect)

    # Update the display
    pg.display.update()


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()


# Start the GUI for checking spam emails
print("hello word, gui success!")
load_spam_keywords()





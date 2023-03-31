import re
import json 
import pygame
from pygame.rect import Rect

#prøv å ordne loada inn json script stuff
f = open('SPAMKEYWORDS.json')

# returns JSON object as 
# a dictionary
data = json.load(f)
# load keywords og pattern
def load_spam_keywords(text):
    with open("SPAMKEYWORDS.json", 'r') as f:
        spam_keywords = json.load(f)['spam_keywords']
    cleaned_keywords = [keyword.strip().lower() for keyword in spam_keywords]
    pattern = '|'.join(cleaned_keywords)
    pattern = re.compile(pattern, flags=re.IGNORECASE)
    return cleaned_keywords, pattern


def check_spam(text):
    if re.search(pattern, text):          
        text="The email is spam." #funke itj
        print("rød")
        global bg
        bg = (255, 0, 0)
        pygame.display.flip()
    else:
        print("grønn")
        text="The email is not spam."
        print(pattern)
        bg = (0, 245, 0)
        pygame.display.flip()
            # text = window.text.get("1.0", "end-1c") tror ikke den trengs. text variabel inneholder uansett teksten i think
           


pygame.init()
window = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
color = (0, 255, 0)
font = pygame.font.SysFont(None, 100)
text = ""
input_active = True
checked_active = False

bg = (0, 0, 0)

spam_keywords, pattern = load_spam_keywords(text)


run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN: #her når det trykkes enter aktiveres sjekkingen
                input_active = False
                print("du skreiv:" +text)
                #check_spam_gui() #flyttes ned
                check_spam(text)
                checked_active = True
                print(checked_active)
                #print fra check_spam_gui
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode
                
        window.fill(bg)
        text_surf = font.render(text, True, (0, 0, 255))
        window.blit(text_surf, text_surf.get_rect(center = window.get_rect().center))
        load_spam_keywords(text)
        pygame.display.flip()
 #sjekker funksjonen avansert
# while run:
#      clock.tick(60)
#      for event in pygame.event.get():
#          if event.type == pygame.KEYDOWN and checked_active == False and input_active == False:
#              if event.key == pygame.MOUSEWHEEL:
#                  print("unchecked, finna check")
#                  check_spam_gui()
#                  checked_active = True
#                  print("Checked")
pygame.quit()
exit()
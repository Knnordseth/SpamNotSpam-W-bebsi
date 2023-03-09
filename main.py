import re
import json
import tkinter as tk

#prøv å ordne loada inn json script stuff
f = open('SPAMKEYWORDS.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Load the list of spam keywords from the JSON file and create a regular expression pattern
def load_spam_keywords():
    with open("spam_keywords.json", 'r') as f:
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
    window = tk.Tk()
    window.title("Spam Checker")
    input_box = tk.Text(window, height=10, width=50)
    input_box.insert(tk.END, "Paste your email here to check for spam")
    input_box.pack()
    
    # Create a button to check for spam
    check_button = tk.Button(window, text="Check for spam", command=check_spam)
    check_button.pack()
    
    # Create a label to display the result
    result_label = tk.Label(window, text="Test label, line 52")
    result_label.pack()
    
    # Start the GUI event loop
    window.mainloop()

# Start the GUI for checking spam emails
print("hello word, gui success kanskje")
load_spam_keywords()



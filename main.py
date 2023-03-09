import re
import json
import tkinter as tk

#prøv å ordne loada inn json script stuff
f = open('SPAMKEYWORDS.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

def is_spam(text, SPAMKEYWORDS.json):
    # Load the list of spam keywords from the JSON file
    with open(SPAMKEYWORDS.json, 'r') as f:
        SPAMKEYWORDS.json = json.load(f)['spam_keywords']
    
    # Create a regular expression pattern to match the spam keywords
    pattern = '|'.join("spam_keywords")
    
    # Use regex to search for the pattern in the text input
    match = re.search(pattern, text, re.IGNORECASE)
    
    # Return True if a match is found (i.e., the text input is spam), False otherwise
    return bool(match)


# Create a GUI window with an input textbox for checking spam emails
def check_spam_gui():
    # Load the spam keywords from the JSON file
    SPAMKEYWORDS.JSON = "spam_keywords.json"
    with open(SPAMKEYWORDS.JSON, 'r') as f:
        spam_keywords = json.load(f)['spam_keywords']
    
    # Create a regex pattern to match the spam keywords
    pattern = '|'.join(spam_keywords)
    
    # Define a function to check if the input text is spam
    def check_spam():
        text = input_box.get("1.0", "end-1c")  # Get the text from the input textbox
        if is_spam(text, spam_keywords):
            result_label.config(text="The email is spam.")
        else:
            result_label.config(text="The email is not spam.")
    
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
    result_label = tk.Label(window, text="")
    result_label.pack()
    
    # Start the GUI event loop
    window.mainloop()

# Start the GUI for checking spam emails
check_spam_gui()


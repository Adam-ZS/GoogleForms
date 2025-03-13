# GoogleForm Auto Filler

This Python script automates the process of filling out and submitting a Google Form multiple times using the Selenium WebDriver with (( Firefox )). 

It operates in headless mode (no visible browser window) for faster execution. 
No TEXT QUESTIONS, only mcq's, checkboxes, ratings, ect..
Works with FIREFOX!

The automation does the following -
It loads the specified Google Form URL and waits for the form to be fully loaded. 
For each form question, it selects random answers (either radio buttons or checkboxes).
If a grid (Rate) question is detected, it randomly selects an option from the grid.
If any question is unanswered due to elements being stale or not interactable, the script retries those questions.
Once all questions are answered, the script submits the form and moves on to the next submission.
The process repeats for a specified number of submissions.

This script also ensures that it retries unanswered questions to avoid incomplete form submissions, handles element issues gracefully, and clears cookies after each submission for a clean slate on subsequent form submissions.

# Requirements


Python 3:

    sudo apt update
    sudo apt install python3 python3-pip

Selenium

    pip install selenium

GeckoDriver (for Firefox)
    
    pip install webdriver-manager

Firefox Browser

    sudo apt install firefox
# Get Started
    git clone https://github.com/Adam-ZS/GoogleForms.git
    cd GoogleForms

    
# Install Dependencies

Mostly you will need to use a virtual environment

    python -m venv myenv
    source myenv/bin/activate  # On Linux/macOS
    pip install selenium webdriver-manager

# Run it
        python form_fillerz.py


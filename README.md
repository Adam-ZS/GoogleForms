# GoogleForm Auto Filler, Auto Fill & Submit in Seconds!

This Python script automates the process of filling out randome choices and submitting a Google Form multiple times using the Selenium WebDriver with (( Firefox )). 

*Good For projects.*

It operates in headless mode (no visible browser window) for faster execution. 
No TEXT QUESTIONS, only mcq's, checkboxes, ratings, ect..
Works with FIREFOX!

# Features
✔ Headless Mode – Runs without opening a browser for faster execution.

✔ Random Answer Selection – Works with multiple-choice, checkboxes, and rating grids (⚠ No text-based answers).

✔ Error Handling – Retries unanswered questions to prevent skipping.

✔ Auto Form Submission – Clears cookies after each submission for fresh data.



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
# ⚠ If you get (error: externally-managed-environment), use a virtual environment

    python -m venv myenv  
    source myenv/bin/activate  
    pip install selenium webdriver-manager  


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

        
# Output / Results
![image](https://github.com/user-attachments/assets/f852cf29-6d36-4b78-bf00-707e83cd5f11)

![image](https://github.com/user-attachments/assets/bbac95f2-fcf0-43b5-aaf3-acf8f51503ac)


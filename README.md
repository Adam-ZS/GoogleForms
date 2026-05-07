# 🦜 Google Forms Auto Filler - Intelligent Auto Fill & Submit Bot

This Python script automates the process of filling out and submitting Google Forms multiple times using Selenium WebDriver with Firefox.

Perfect for:
- Testing Google Forms
- Survey simulations
- QA automation
- Research/demo environments

It runs in headless mode (no visible browser window) for maximum speed and efficiency.

---

# ✨ Features

✔ Headless Mode – Runs invisibly for faster execution.

✔ Random Answer Selection – Works with MCQs, checkboxes, grids, dropdowns, ratings, and more.

✔ Intelligent Text Handling – Automatically fills short answer & paragraph questions with randomized realistic responses.

✔ Smart Checkbox Handling – Selects 1-3 random checkboxes instead of all.

✔ Multi-page Form Support – Automatically navigates through sections.

✔ Error Recovery – Handles stale elements and retries unanswered questions.

✔ Auto Form Submission – Clears cookies after every submission for clean sessions.

✔ Smart Exclusions – Avoids options like "Other", "Medical", etc.

✔ Performance Stats – Displays total runtime and average speed per submission.

---

# 🚀 Supported Question Types

| Question Type | Supported |
|---|---|
| Multiple Choice | ✅ |
| Checkboxes | ✅ |
| Dropdowns | ✅ |
| Linear Scale | ✅ |
| Grid Questions | ✅ |
| Short Answer | ✅ |
| Paragraph | ✅ |
| Multi-page Forms | ✅ |

---

# 🧠 Intelligent Text Handling

The bot automatically fills text questions using randomized realistic answers.

```python
TEXT_RESPONSES = [
    "No",
    "None",
    "N/A",
    "Nothing to add",
    "Good",
    "Great",
    "Excellent",
    "Very good",
    "Satisfactory",
    "Acceptable",
    "Fine",
    "Okay",
    "Yes",
    "Agree",
    "I agree",
    "Strongly agree",
    "Noted",
    "Understood",
    "Thank you",
    "Appreciate it",
    "Looking forward",
    "All clear",
    "Perfect",
    "Sounds good",
    "Will do",
    "Confirmed",
    "Acknowledged"
]
```

Each submission gets different randomized text responses for more natural behavior.

---

# 📦 Requirements

## Python 3

```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## Selenium

```bash
pip install selenium
```

---

## GeckoDriver (Firefox)

```bash
pip install webdriver-manager
```

---

## Firefox Browser

```bash
sudo apt install firefox
```

---

# ⚠️ If you get `error: externally-managed-environment`

Use a virtual environment:

```bash
python -m venv myenv
source myenv/bin/activate
pip install selenium webdriver-manager
```

---

# 🚀 Get Started

## Clone Repository

```bash
git clone https://github.com/Adam-ZS/GoogleForms.git
cd GoogleForms
```

---

# 🔧 Install Dependencies

Recommended:

```bash
python -m venv myenv
source myenv/bin/activate  # Linux/macOS
pip install selenium webdriver-manager
```

Windows:

```bash
myenv\Scripts\activate
```

---

# ▶️ Run The Bot

```bash
python form_fillerz.py
```

---

# 📋 Usage

```text
📋 Enter Google Form URL:
🔢 How many submissions?
```

Example:

```text
📋 Enter Google Form URL: https://forms.gle/example
🔢 How many submissions? 100
```

---

# ⚡ Example Output

```text
                \       /
                 \ .--./
    ;;          - <o  o>  -            ;;;
                  | -- |              ;;;
    ``            |    |  
                  `----'    ````''
oO  oO  oO=====   //  \\    ====Oo  Oo  Oo
                 //    \\
                //      \\ 
               ||©Adam-ZS||
               ||  ~~~~  ||
             --`'--l---l---'`--

==================================================
Google Forms Auto Filler by Adam-ZS
==================================================

🚀 Starting 100 submissions...

📝 Submitting form 1/100...
✅ Submission 1 completed successfully!

📝 Submitting form 2/100...
✅ Submission 2 completed successfully!

...

==================================================
🎉 Finished: 100/100 successful submissions
⏱️ Total time: 210.54 seconds
⚡ Average: 2.10 seconds per submission
==================================================
```

---

# 📸 Output / Results

<img width="643" height="463" alt="image" src="https://github.com/user-attachments/assets/b4cb5909-36d4-460f-a868-9fd366ca1538" />

![image](https://github.com/user-attachments/assets/bbac95f2-fcf0-43b5-aaf3-acf8f51503ac)

---

# 🔧 Customization

## Add Your Own Text Responses

```python
TEXT_RESPONSES = [
    "Custom answer 1",
    "Custom answer 2",
    "Another response"
]
```

---

## Edit Excluded Options

```python
GLOBAL_EXCLUSIONS = [
    "medical",
    "other",
    "__other_option__",
    "اخرى",
    "other:",
    "أخرى:"
]
```

---

## Change Checkbox Selection Count

Default:

```python
num_to_select = random.randint(1, min(3, len(valid)))
```

Example (1-5 selections):

```python
num_to_select = random.randint(1, min(5, len(valid)))
```

---

## Disable Headless Mode

```python
# options.add_argument("--headless")
```

---

# 🐛 Troubleshooting

| Problem | Fix |
|---|---|
| GeckoDriver error | `pip install webdriver-manager` |
| Firefox missing | Install Firefox |
| Forms not submitting | Verify form URL |
| Slow execution | Check internet speed |
| Text inputs empty | Ensure `TEXT_RESPONSES` is not empty |

---

# 📝 Notes

- Works best on public Google Forms
- Supports almost all Google Forms question types
- Does not bypass CAPTCHA/security protections
- Designed for educational/testing purposes
- Use responsibly and with permission

---

# 👨‍💻 Author

**Adam-ZS**

GitHub: https://github.com/Adam-ZS

---

# 📄 License

MIT License

---

# ⭐ Support

If this project helped you:

⭐ Star the repository on GitHub.

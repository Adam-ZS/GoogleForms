from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import random
import time
parrot = r"""
                \       /
                 \ .--./
    ;;          - <o  o>  -            ;;;
                  | -- |              ;;;
    ``            |    |  
                  `----'    ````''
          =====   //  \\    ====Or no problem, you can use the original one I think its better 
                 //    \\
                //      \\ 
               ||©Adam-ZS||
               ||  ~~~~  ||
             --`'--l---l---'`--
"""
print(parrot)

def run_automation(form_url, submissions):
    # Configure Firefox for max speed
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Firefox(service=webdriver.FirefoxService(GeckoDriverManager().install()), options=options)
    driver.implicitly_wait(0.5)  # Faster execution

    for i in range(submissions):
        try:
            driver.get(form_url)

            # Wait for form to load
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='listitem']"))
            )

            # Select all questions
            questions = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")
            unanswered_questions = []

            for question in questions:
                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)

                    # Handle grid questions
                    grid_rows = question.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")
                    if grid_rows:
                        for row in grid_rows:
                            options = row.find_elements(By.CSS_SELECTOR, "div[role='radio']")
                            if options:
                                driver.execute_script("arguments[0].click();", random.choice(options))
                        continue  # Skip to next question

                    # Handle radio buttons & checkboxes
                    answers = question.find_elements(By.CSS_SELECTOR, "div[role='radio'], div[role='checkbox']")
                    if answers:
                        if "radio" in answers[0].get_attribute("role"):
                            driver.execute_script("arguments[0].click();", random.choice(answers))
                        else:
                            selected = random.sample(answers, random.randint(1, len(answers)))
                            for cb in selected:
                                driver.execute_script("arguments[0].click();", cb)

                    # Track unanswered questions for retries
                    unanswered_questions.append(question)
                    
                except StaleElementReferenceException:
                    print("  Element became stale. Refreshing and retrying...")
                    driver.refresh()
                    break  # Restart submission if needed

            # Retry unanswered questions to ensure nothing is skipped
            for retry_question in unanswered_questions:
                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", retry_question)
                    answers = retry_question.find_elements(By.CSS_SELECTOR, "div[role='radio'], div[role='checkbox']")
                    if answers:
                        if "radio" in answers[0].get_attribute("role"):
                            driver.execute_script("arguments[0].click();", random.choice(answers))
                        else:
                            selected = random.sample(answers, random.randint(1, len(answers)))
                            for cb in selected:
                                driver.execute_script("arguments[0].click();", cb)
                    print("  Retried unanswered question successfully.")
                except Exception as e:
                    print(f"  Failed to retry unanswered question: {e}")

            # Submit form
            submit_button = WebDriverWait(driver, 4).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'][aria-label='Submit']"))
            )
            driver.execute_script("arguments[0].click();", submit_button)

            # Confirm submission
            WebDriverWait(driver, 4).until(EC.url_contains("formResponse"))
            print(f"✅ Submission {i+1}/{submissions} successful!")

            driver.delete_all_cookies()

        except Exception as e:
            print(f"❌ Submission {i+1} failed: {e}")

    driver.quit()
    print("\nAll submissions completed! 🎉")

if __name__ == "__main__":
    form_url = input("Enter Google Form URL: ")
    submissions = int(input("How many times should we submit the form? "))
    run_automation(form_url, submissions)

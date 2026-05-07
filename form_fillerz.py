from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import StaleElementReferenceException
import random
import time

parrot = r"""
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
"""

# Configuration
GLOBAL_EXCLUSIONS = ["medical", "other", "__other_option__", "اخرى", "other:", "أخرى:"]

def fill_google_form(driver, form_url):
    """
    Fills and submits a Google Form with random selections.
    Handles checkboxes, radios, grids, and text inputs intelligently.
    """
    try:
        driver.get(form_url)
        finished_titles = set()
        processed_checkbox_groups = set()

        while True:
            time.sleep(0.3)
            q_blocks = driver.find_elements(By.CSS_SELECTOR, "div[role='listitem']")

            for q_block in q_blocks:
                if not q_block.is_displayed():
                    continue

                try:
                    # Get question title
                    try:
                        title = q_block.find_element(By.CSS_SELECTOR, "div[role='heading']").text
                    except:
                        title = q_block.text.split("\n")[0]

                    title = title.replace("*", "").strip().lower()
                    
                    if title in finished_titles:
                        continue

                    # ============================================
                    # CHECKBOXES (Handles grouped options properly)
                    # ============================================
                    checkboxes = q_block.find_elements(By.CSS_SELECTOR, "div[role='checkbox']")
                    if checkboxes:
                        if len(checkboxes) > 1:
                            if title in processed_checkbox_groups:
                                finished_titles.add(title)
                                continue
                            
                            already_checked = [cb for cb in checkboxes if cb.get_attribute("aria-checked") == "true"]
                            
                            if already_checked:
                                finished_titles.add(title)
                                processed_checkbox_groups.add(title)
                                continue

                            # Filter out excluded options
                            valid = [
                                cb for cb in checkboxes
                                if not any(ex in (cb.get_attribute("aria-label") or "").lower()
                                           for ex in GLOBAL_EXCLUSIONS)
                            ]
                            
                            if not valid:
                                finished_titles.add(title)
                                processed_checkbox_groups.add(title)
                                continue

                            # Randomly select 1-3 checkboxes
                            num_to_select = random.randint(1, min(3, len(valid)))
                            picks = random.sample(valid, num_to_select)
                            
                            for cb in picks:
                                driver.execute_script("arguments[0].click();", cb)
                                time.sleep(0.05)
                            
                            finished_titles.add(title)
                            processed_checkbox_groups.add(title)
                            time.sleep(0.2)
                        else:
                            finished_titles.add(title)
                        
                        continue

                    # ============================================
                    # RADIO BUTTONS
                    # ============================================
                    radios = q_block.find_elements(By.CSS_SELECTOR, "div[role='radio']")
                    if radios:
                        if any(r.get_attribute("aria-checked") == "true" for r in radios):
                            finished_titles.add(title)
                            continue

                        # Filter out excluded options
                        valid = [
                            r for r in radios
                            if not any(ex in (r.get_attribute("data-value") or "").lower()
                                       for ex in GLOBAL_EXCLUSIONS)
                        ]
                        
                        if not valid:
                            valid = radios

                        driver.execute_script("arguments[0].click();", random.choice(valid))
                        finished_titles.add(title)
                        continue

                    # ============================================
                    # TEXT INPUTS
                    # ============================================
                    text_inputs = q_block.find_elements(By.CSS_SELECTOR, "textarea, input[type='text']")
                    if text_inputs:
                        if not text_inputs[0].get_attribute("value"):
                            text_inputs[0].send_keys("N/A")
                        
                        finished_titles.add(title)
                        continue

                except StaleElementReferenceException:
                    break

            # ============================================
            # GRID RADIO SWEEPER (Matrix questions)
            # ============================================
            sweeper = False
            for row in driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']"):
                if not row.is_displayed():
                    continue
                radios = row.find_elements(By.CSS_SELECTOR, "div[role='radio']")
                if radios and not any(r.get_attribute("aria-checked") == "true" for r in radios):
                    driver.execute_script("arguments[0].click();", random.choice(radios))
                    sweeper = True
                    time.sleep(0.03)

            if sweeper:
                continue

            # ============================================
            # NAVIGATION (Next/Submit buttons)
            # ============================================
            submit = driver.find_elements(By.CSS_SELECTOR, "div[jsname='M2UYVd']")
            if submit and submit[0].is_displayed():
                driver.execute_script("arguments[0].click();", submit[0])
                return True

            next_btn = driver.find_elements(By.CSS_SELECTOR, "div[jsname='OCpkoe']")
            if next_btn and next_btn[0].is_displayed():
                driver.execute_script("arguments[0].click();", next_btn[0])
                finished_titles.clear()
                processed_checkbox_groups.clear()
                time.sleep(1.0)

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def run_automation():
    """Main automation runner with headless Firefox"""
    print(parrot)
    print("=" * 50)
    print("Google Forms Auto Filler by Adam-ZS")
    print("=" * 50)
    
    form_url = input("\n📋 Enter Google Form URL: ").strip()
    num_submissions = int(input("🔢 How many submissions? "))

    # Configure Firefox for headless mode
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1200,1000")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Firefox(
        service=webdriver.FirefoxService(GeckoDriverManager().install()),
        options=options
    )

    total = 0
    start_time = time.time()
    
    print(f"\n🚀 Starting {num_submissions} submissions...\n")
    
    for i in range(num_submissions):
        print(f"📝 Submitting form {i+1}/{num_submissions}...")
        
        if fill_google_form(driver, form_url):
            try:
                WebDriverWait(driver, 5).until(EC.url_contains("formResponse"))
                total += 1
                print(f"✅ Submission {i+1} completed successfully!")
            except:
                print(f"⚠️  Submission {i+1} may have failed")
        
        driver.delete_all_cookies()

    elapsed_time = time.time() - start_time
    driver.quit()
    
    print("\n" + "=" * 50)
    print(f"🎉 Finished: {total}/{num_submissions} successful submissions")
    print(f"⏱️  Total time: {elapsed_time:.2f} seconds")
    print(f"⚡ Average: {elapsed_time/num_submissions:.2f} seconds per submission")
    print("=" * 50)

if __name__ == "__main__":
    run_automation()

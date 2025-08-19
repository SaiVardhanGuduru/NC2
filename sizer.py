from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate_nutanix_login(email, password):
    """
    Automates the two-step login process for the Nutanix portal.
    
    Args:
        email (str): The user's email address.
        password (str): The user's password.
    """
    # Configure Chrome to run in headless mode for EC2
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver
    print("Starting the browser...")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20) # Increased wait time for stability

    # Navigate to the Nutanix login URL
    login_url = "https://my.nutanix.com/page/login"
    driver.get(login_url)
    print(f"Navigated to: {login_url}")

    try:
        # --- Page 1: Enter Email ---
        print("Finding email input field...")
        email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_field.send_keys(email)
        print("Email entered.")

        print("Finding and clicking the 'Next' button...")
        next_button = wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))
        next_button.click()
        print("'Next' button clicked.")

        # --- Page 2: Enter Password ---
        print("Finding password input field...")
        # The password field's ID is 'password' based on your provided HTML snippet.
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(password)
        print("Password entered.")
        
        # The 'Sign in' button on the second page often reuses an ID or has a new one.
        # Based on a common login flow, it's often the same 'Next' button or a new one.
        # Let's assume it's the same ID 'idp_next' for the example.
        print("Finding and clicking the 'Sign in' button...")
        signin_button = wait.until(EC.element_to_be_clickable((By.ID, "login-btn")))
        signin_button.click()
        print("'Sign in' button clicked.")

        # Confirm successful login by waiting for a new page URL
        wait.until(EC.url_contains("my.nutanix.com/page/accounts"))
        print("Successfully logged into the dashboard! 🎉")
        
        launch_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Launch Nutanix Sizer']")))
        launch_button.click()
        print("launch nutanix sizer button clicked")
        
        try:
            print("Waiting for the Nutanix Sizer tool to load...")
            # Replace 'scenario_title' with a unique locator on the new page
            scenario_header = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'New Scenario')]")))
            print("Nutanix Sizer page loaded successfully.")


        except Exception as e:
            print(f"Failed to load the Nutanix Sizer page: {e}")

        print("\n--- HTML Source of the Dashboard Page ---")
        page_source = driver.page_source
        print(page_source[:2000]) # Print the first 2000 characters for brevity
        print("\n--- End of HTML Source ---")
    except Exception as e:
        print(f"An error occurred during the login process: {e}")

    finally:
        # It's good practice to add a pause for observation before closing
        # time.sleep(5)
        print("Closing the browser...")
        driver.quit()

# --- Execution ---
if __name__ == "__main__":
    # **IMPORTANT**: Replace these with your actual credentials
    your_email = "kanchana.subramani@tcs.com" 
    your_password = "Avadi@2894"
    
    automate_nutanix_login(your_email, your_password)
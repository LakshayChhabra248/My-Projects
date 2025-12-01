import time
import urllib.parse
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class WhatsAppDriver:
    def __init__(self):
        self.driver = None
        self.wait = None

    def initialize_driver(self):
        """Initializes the Chrome driver."""
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless") # Cannot use headless for WhatsApp Web QR scan
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Persistent Profile
        profile_path = os.path.join(os.getcwd(), 'chrome_profile')
        options.add_argument(f"user-data-dir={profile_path}")
        
        # Initialize driver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 300) # Increased to 300 seconds (5 mins) for slow connections
        
        # Open WhatsApp Web
        self.driver.get("https://web.whatsapp.com")

    def wait_for_login(self):
        """
        Waits for the user to scan the QR code.
        Returns True if login is successful (detected by presence of chat list), False otherwise.
        """
        try:
            # Wait for the chat list side panel to appear, which indicates successful login
            # The side panel usually has an ID or class. 'side' ID was common, but classes change.
            # Looking for the search box or the chat list container is safer.
            # Using a generic wait for an element that exists only after login.
            print("Waiting for QR code scan (Timeout: 300s)...")
            # This xpath looks for the chat list pane
            self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
            return True
        except TimeoutException:
            return False

    def send_message(self, phone_number, message):
        """
        Sends a message to a specific phone number.
        Returns (True, None) if successful, (False, error_message) otherwise.
        """
        try:
            # Encode message for URL
            encoded_message = urllib.parse.quote(message)
            
            # Navigate to the send API URL
            # This triggers the chat to open for the specific number
            url = f"https://web.whatsapp.com/send?phone={phone_number}&text={encoded_message}"
            self.driver.get(url)
            
            # Wait for the chat to load and the send button to be clickable
            # The send button is usually an icon. 
            # We can look for the 'span[data-icon="send"]'
            
            # First, handle invalid number popup if it appears
            try:
                # Short wait for invalid number popup
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Phone number shared via url is invalid")]'))
                )
                return False, "Invalid Phone Number"
            except TimeoutException:
                pass # No popup, proceed

            # Wait for send button to appear and be clickable
            # We use multiple selectors to be robust against WhatsApp updates
            print(f"Waiting for Send button for {phone_number}...")
            send_button_xpath = '//span[@data-icon="send"] | //button[@aria-label="Send"]'
            
            send_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, send_button_xpath)))
            send_button.click()
            
            # Wait a bit for the message to actually leave (change to single tick)
            # This is a simple wait, could be improved by checking message status
            time.sleep(2) 
            
            return True, None
            
        except Exception as e:
            return False, str(e)

    def close(self):
        if self.driver:
            self.driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def setup_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (can help in some environments)

    # Disable WebGL if you don't need it
    chrome_options.add_argument("--disable-webgl")

    # Set a user-agent to mimic a real browser
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    )

    # Initialize and return the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    return driver

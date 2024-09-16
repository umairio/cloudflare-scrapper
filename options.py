from selenium import webdriver
# import undetected_chromedriver as uc
from fake_useragent import UserAgent

user_data_dir = r"C:\Users\umair\AppData\Local\Google\Chrome\User Data"
profile =r"C:\Users\umair\AppData\Local\Google\Chrome\User Data\Default"

options = webdriver.ChromeOptions()
# options = uc.ChromeOptions()


options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory=Default")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument('--excludeSwitches=enable-automation')
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--no-default-browser-check")
# options.add_argument("--no-first-run")
# options.add_argument(f"--user-agent={UserAgent().random}")
# options.add_argument('--guest')
# options.add_argument("--start-maximized")
# options.add_argument('--verbose')
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
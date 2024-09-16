from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
user_data_dir = r"C:\\Users\\umair\\AppData\\Local\\Google\\Chrome\\User Data"
profile = "Profile 2"  # Replace with the name of the profile you want to use
# options.add_argument(f"--user-agent={UserAgent().random}")
# options.add_argument("--start-maximized")
# options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile}")
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# options.add_experimental_option("useAutomationExtension", False)


driver = webdriver.Chrome(options=options)
BeautifulSoup(driver.page_source, 'html.parser')
stealth(
    driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)
time.sleep(5)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': """
Element.prototype._attachShadow = Element.prototype.attachShadow;
Element.prototype.attachShadow = function () {
    return this._attachShadow( { mode: "open" } );
};
"""})
time.sleep(5)
driver.get("https://cityofla.ezlinksgolf.com/")
time.sleep(5)
shadow_div = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div')
shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_div)
iframe = WebDriverWait(shadow_root, 30).until(EC.presence_of_element_located((By.ID, 'cf-chl-widget-hny23')))


# shadow_root.find_element(By.XPATH, '//*[@id="cf-chl-widget-mvcqa"]').click()
actions = ActionChains(driver)
actions.move_by_offset(410, 285).click().perform()
actions.move_by_offset(425, 278).click().perform()


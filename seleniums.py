import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from options import options
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

breakpoint()

service = Service(r'.\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=service)

url = "https://cityofla.ezlinksgolf.com/"
time.sleep(5)
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
time.sleep(5)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': """
Element.prototype._attachShadow = Element.prototype.attachShadow;
Element.prototype.attachShadow = function () {
    return this._attachShadow( { mode: "open" } );
};
"""})
time.sleep(5)

driver.get(url)
time.sleep(5)

shadow_div = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div')
shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_div)

time.sleep(2)
iframe = shadow_root.find_element(By.CSS_SELECTOR, "*")
driver.switch_to.frame(iframe)
print(driver.execute_script("return document.title"))


driver.execute_script("""
Element.prototype._attachShadow = Element.prototype.attachShadow;
Element.prototype.attachShadow = function () {
    return this._attachShadow({ mode: 'open' });
};
""")

driver.execute_script("document.body.focus();")

time.sleep(5)
shadow_body = driver.execute_script("return document.body;")

inner_shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_body)
if inner_shadow_root:
    # Interact with elements inside the inner shadow DOM (e.g., checkbox)
    checkbox = inner_shadow_root.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    checkbox.click()
else:
    print("Inner shadow root is None, unable to access")

driver.switch_to.default_content()
actions = ActionChains(driver)
actions.move_by_offset(410, 285).click().perform()
actions.move_by_offset(425, 278).click().perform()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome driver and diagrams.net URL
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://app.diagrams.net/")

# Wait for the page to load completely
time.sleep(5)

# Close the initial popup
driver.find_element(By.XPATH, "//button[contains(text(), 'Decide later')]").click()
time.sleep(1)

# Create a new diagram
driver.find_element(By.ID, 'newDiagram').click()
time.sleep(1)

# Select a default template and start editing
driver.find_element(By.XPATH, "//div[contains(text(), 'Create')]").click()
time.sleep(5)

# Add operations to draw your desired diagram
# Example: input text on the canvas
textarea = driver.find_element(By.CLASS_NAME, 'geDiagramContainer')
textarea.click()
textarea.send_keys('Hello, Draw.io!')

# Export to SVG
driver.find_element(By.ID, 'file').click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[contains(text(),'Export as')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[contains(text(),'SVG')]").click()
time.sleep(1)

# Set the file name and download path (may need to adjust based on your browser settings and OS)
# Download the file

# Cleanup and exit
driver.quit()

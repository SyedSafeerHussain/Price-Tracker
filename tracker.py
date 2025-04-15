from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
import time
driver=webdriver.Chrome()
url="https://coinmarketcap.com/"
driver.get(url)
time.sleep(20)
WebDriverWait(driver,30).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR,"table tbody tr"))
)
rows=driver.find_elements(By.CSS_SELECTOR,"table tbody tr")
with open("tracker.csv",'w')as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Price"])
    for row in rows:
        try:
            name=row.find_element(By.CSS_SELECTOR,"p.sc-65e7f566-0.iPbTJf.coin-item-name").text
            price=row.find_element(By.CSS_SELECTOR,"div.sc-142c02c-0.lmjbLF").text
            writer.writerow([name,price])
        except:
            continue
driver.quit()

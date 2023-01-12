from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

response = requests.get(
    "https://www.zoopla.co.uk/to-rent/property/manchester-city-centre/?price_frequency=per_month&q=Manchester%20City%20Centre%2C%20Greater%20Manchester&results_sort=newest_listings&search_source=to-rent",
    headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

all_link_elements = soup.select(".c-hhFiFN")
all_links = []
for link in all_link_elements[::2]:
    href = link["href"]
    print(href)
    all_links.append(f"https://www.zoopla.com{href}")

all_address_elements = soup.select(".c-eFZDwI")
all_addresses = [address.get_text() for address in all_address_elements]

all_price_elements = soup.select(".c-hBjSus")
all_prices = [price.get_text() for price in all_price_elements]

chrome_driver_path = "/Users/User101/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSceEinGzChsuiHLFWL8jMvFx5aaCI-vLCWspHQcJh5eZ0ihKw/viewform?usp=sf_link")

    time.sleep(2)
    address = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()
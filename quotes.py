from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)


with open("quotes.csv", "w") as csvfile:
  csv_writer = csv.writer(csvfile)
  csv_writer.writerow(["name", "quote"])

  driver.get("http://quotes.toscrape.com/")
  quotes = driver.find_elements_by_class_name("quote")
  for q in quotes:
    quote = q.find_element_by_class_name("text").text
    name = q.find_element_by_class_name("author").text
    print(name)
    print(quote)
    csv_writer.writerow([name, quote])

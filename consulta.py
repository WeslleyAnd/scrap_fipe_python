from xml.dom.minidom import Element
from selenium import webdriver
#from selenium.webdriver.options import options
from time import sleep

driver = webdriver.Chrome()
driver.get("https://veiculos.fipe.org.br/")

element = driver.find_element_by_css_selector('#front > div.content > div.tab.vertical.tab-veiculos > ul > li:nth-child(1)').click()
sleep(2)
element.send_keys(Keys.TAB, Keys.TAB, Keys.TAB)
element_date.send_keys('teste')
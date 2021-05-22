import time
import selenium
from selenium import  webdriver

print("가장 인기상품이 무엇인지 궁금한 상품 3개를 입력하시오(콤마로 구분할 것)")
print("ex: 과자, 악세사리, 필기구")
product_list_string=input(">> : ")
product_list=product_list_string.split(",")

URL= 'https://www.idus.com/'
driver=webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

for product in product_list:
    search_box=driver.find_element_by_id("header-search")
    search_box.send_keys(product)

    search_btn=driver.find_element_by_class_name("idus-icon-search")
    search_btn.click()

    title=driver.find_element_by_class_name("product-info__name").text

    print(product+" - "+title)

    time.sleep(3)
    search_box=driver.find_element_by_id("header-search")
    search_box.clear()

time.sleep(3)

driver.close()
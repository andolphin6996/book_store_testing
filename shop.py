import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
time.sleep(2)
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
login = driver.find_element_by_id("username")
login.send_keys("test123@mail.ru")
password1 = driver.find_element_by_id("password")
password1.send_keys("123456Sa#$%666")
log = driver.find_element_by_name("login")
log.click()
shop = driver.find_element_by_link_text("Shop")
shop.click()
book = driver.find_element_by_xpath("//*[@id='content']/ul/li[3]/a[1]/h3")
book.click()
element_log = WebDriverWait(driver, 10).until(
     EC.text_to_be_present_in_element((By.XPATH, "//*[@id='product-181']/div[2]/h1"), "HTML5 Forms"))
print(element_log)
driver.quit()


# 2количество товаров
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
time.sleep(2)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
login = driver.find_element_by_id("username")
login.send_keys("test123@mail.ru")
password1 = driver.find_element_by_id("password")
password1.send_keys("123456Sa#$%666")
log = driver.find_element_by_name("login")
log.click()
shop = driver.find_element_by_link_text("Shop")
shop.click()
html = driver.find_element_by_link_text("HTML")
html.click()
items = driver.find_elements_by_css_selector("h3")
if len(items) == 3:
    print("3 товара")
else:
    print("Ошибка")
driver.quit()

#3
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
login = driver.find_element_by_id("username")
login.send_keys("test123@mail.ru")
password1 = driver.find_element_by_id("password")
password1.send_keys("123456Sa#$%666")
log = driver.find_element_by_name("login")
log.click()
shop = driver.find_element_by_link_text("Shop")
shop.click()
default_sorting = driver.find_element_by_name("orderby")
sort_selected = default_sorting.get_attribute("value")
if sort_selected == "menu_order":
    print("Сортировка по умолчанию выбрана")
else:
    print("Сортировка НЕ выбрана")
select = Select(default_sorting)
select.select_by_value("price-desc")
default_sorting = driver.find_element_by_name("orderby")
low_sorting = default_sorting.get_attribute("value")
if low_sorting == "price-desc":
    print("Сортировка по убыванию выбрана")
else:
    print("Сортировка НЕ выбрана")
driver.quit()

#4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
login = driver.find_element_by_id("username")
login.send_keys("test123@mail.ru")
password1 = driver.find_element_by_id("password")
password1.send_keys("123456Sa#$%666")
log = driver.find_element_by_name("login")
log.click()
shop = driver.find_element_by_link_text("Shop")
shop.click()
book = driver.find_element_by_css_selector(".post-169 h3")
book.click()
price600 = driver.find_element_by_css_selector(".price > del > span")
price600_text = price600.text
price450 = driver.find_element_by_css_selector(".price > ins > span")
price450_text = price450.text
assert price600_text == "₹600.00"
assert price450_text == "₹450.00"
img = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a")))
img.click()
close = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
close.click()
driver.quit()

# 5 проверка цены в корзине
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop = driver.find_element_by_link_text("Shop")
shop.click()
book = driver.find_element_by_css_selector(".post-182 > a h3")
book.click()
add_cart = driver.find_element_by_css_selector(".single_add_to_cart_button")
add_cart.click()
time.sleep(5)
item_1_value = driver.find_element_by_css_selector(".wpmenucart-contents .cartcontents")
item_1_value_get_text = item_1_value.text
assert "1 Item" in item_1_value_get_text
price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
price_text = price.text
assert "₹180.00" in price_text
cart_btn = driver.find_element_by_class_name("wpmenucart-contents")
cart_btn.click()
subtotal = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00"))
total = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹183.60"))
driver.quit()

#6 работа в корзине
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(8)
shop = driver.find_element_by_link_text("Shop")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
add_cart_book1 = driver.find_element_by_css_selector("[data-product_id='182']")
add_cart_book1.click()
time.sleep(5)
add_cart_book2 = driver.find_element_by_css_selector("[data-product_id='180']")
add_cart_book2.click()
cart_btn = driver.find_element_by_class_name("wpmenucart-contents")
cart_btn.click()
time.sleep(5)
first_book = driver.find_element_by_class_name("remove")
first_book.click()
undo_btn = driver.find_element_by_link_text("Undo?")
undo_btn.click()
quantity = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
quantity.clear()
quantity.send_keys("3")
update_basket = driver.find_element_by_name("update_cart")
update_basket.click()
js_book = driver.find_element_by_css_selector("tbody > tr:nth-child(1) .product-quantity input")
js_book_1 = js_book.get_attribute("value")
assert js_book_1 == '3'
time.sleep(5)
apply_coup = driver.find_element_by_name("apply_coupon")
apply_coup.click()
error = driver.find_element_by_css_selector(".woocommerce-error")
error_text = error.text
assert error_text == 'Please enter a coupon code.'
driver.quit()

# 7 покупка товара
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(8)
shop = driver.find_element_by_link_text("Shop")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
add_cart_book1 = driver.find_element_by_css_selector("[data-product_id='182']")
add_cart_book1.click()
time.sleep(3)
cart_btn = driver.find_element_by_class_name("wpmenucart-contents")
cart_btn.click()
checkout_btn = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()
first_name = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Ann")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Smitt")
email = driver.find_element_by_id("billing_email")
email.send_keys("test123@mail.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89713456876")
contry = driver.find_element_by_id("s2id_billing_country")
contry.click()
search_country = driver.find_element_by_id("s2id_autogen1_search")
search_country.send_keys("Hong Kong")
contry_sel = driver.find_element_by_class_name("select2-match")
contry_sel.click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("street")
town = driver.find_element_by_id("billing_city")
town.send_keys("Bakercity")
region = driver.find_element_by_id("s2id_billing_state")
region.click()
search_reg = driver.find_element_by_id("s2id_autogen2_search")
search_reg.send_keys("Hong Kong Island")
reg_select = driver.find_element_by_class_name("select2-match")
reg_select.click()
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
pay = driver.find_element_by_id("payment_method_cheque")
pay.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
text = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
check_pay = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME,"method"), "Check Payments"))


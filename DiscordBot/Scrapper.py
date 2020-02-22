from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup

def search(msg):
    return getting_random_image(search_images(msg))


def search_reddit(msg):
    return search_images_reddit(msg)


def search_images(sBar: str) -> str:
    srappy = webdriver.PhantomJS()
    print('browser is ready')

    srappy.get("https://www.google.com/")
    time.sleep(1)

    s = srappy.find_element_by_class_name("gLFyf.gsfi")
    print("first item")
    s.clear()
    s.send_keys(sBar)
    s.send_keys(Keys.ENTER)

    img = WebDriverWait(srappy, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "q.qs"))
    )

    img.send_keys(Keys.ENTER)
    time.sleep(2)

    return srappy.page_source


def getting_random_image(source):
    soup = BeautifulSoup(source, 'html.parser')

    stipped = soup.get_text().split("\"")
    filtered = list(filter(lambda x: "http" in x and x.endswith(".jpg"), stipped))

    res = random.choice(filtered)

    return res


def search_images_reddit(sBar: str) -> str:
    srappy = webdriver.PhantomJS()
    print('browser is ready')

    srappy.get("https://www.reddit.com/")
    print('website gotten')
    search = srappy.find_element_by_class_name("_2xQx4j6lBnDGQ8QsRnJEJa")
    print('found first element')
    search.clear()
    search.send_keys(sBar)
    search.send_keys(Keys.ENTER)
    print('entered query')
    time.sleep(2)

    memes = srappy.find_elements_by_class_name("styled-outbound-link")
    print(memes)
    meme = random.choice(memes)
    print(meme)

    WebDriverWait(srappy, 20).until(EC.element_to_be_clickable(meme)).click()
    meme.send_keys(Keys.ENTER)
    # meme.click()

    time.sleep(2)
    print(srappy.window_handles)
    srappy.switch_to.window(list(filter(lambda x: "/search/" not in x, srappy.window_handles))[0])

    url = srappy.current_url

    srappy.quit()
    return url

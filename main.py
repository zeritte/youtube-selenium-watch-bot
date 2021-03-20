from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def main():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--headless")
        options.add_argument("--mute-audio")

        driver = webdriver.Chrome(options=options)
        driver.get("https://www.youtube.com/watch?v=_vO6ed5s6ik")

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "ytp-caption-window-container"))
        )

        player_button = driver.find_elements_by_css_selector(
            "#movie_player > div.ytp-cued-thumbnail-overlay > button"
        )
        player_button = player_button[0]

        player_button.click()

        time.sleep(10)
    except Exception as e:
        print(e)
        driver.close()


main()
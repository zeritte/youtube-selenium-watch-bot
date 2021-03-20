from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

video_list = [
    "https://www.youtube.com/watch?v=QEcSNmDPIEE",
    "https://www.youtube.com/watch?v=bgadhuBu4yw",
    "https://www.youtube.com/watch?v=vT5PawWveQM",
    "https://www.youtube.com/watch?v=2zw4nVVpcR8",
    "https://www.youtube.com/watch?v=Fk9rW4gYPWU",
    "https://www.youtube.com/watch?v=11rbvwjKuws",
    "https://www.youtube.com/watch?v=6MaaOjy1aGU",
    "https://www.youtube.com/watch?v=GGO-KGIPlPs",
    "https://www.youtube.com/watch?v=MpbtvRheXK4",
    "https://www.youtube.com/watch?v=KcCRMe7D5NY",
    "https://www.youtube.com/watch?v=_vO6ed5s6ik",
]
video_list.reverse()


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--mute-audio")

    player_button_css_selector = (
        "#movie_player > div.ytp-cued-thumbnail-overlay > button"
    )

    for i in range(0, 100000):
        print("=========", i, "th time watching ========")
        for video in video_list:
            try:
                driver = webdriver.Chrome(options=options)
                driver.get(video)
                print("opened the page", driver.title)

                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (By.ID, "ytp-caption-window-container")
                    )
                )
                print("found video container")

                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (
                            By.CSS_SELECTOR,
                            player_button_css_selector,
                        )
                    )
                )
                print("found play button")

                player_button = driver.find_elements_by_css_selector(
                    player_button_css_selector
                )
                player_button = player_button[0]
                print("got player button")

                player_button.click()
                print("clicked player button")

                time.sleep(10)
                print("waiting 10 seconds")

                driver.delete_all_cookies()
                driver.close()
                print("close the driver")
            except Exception as e:
                print(e)
                driver.close()


main()
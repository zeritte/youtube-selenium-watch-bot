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


def main():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--headless")
        options.add_argument("--mute-audio")

        driver = webdriver.Chrome(options=options)

        player_button_css_selector = (
            "#movie_player > div.ytp-cued-thumbnail-overlay > button"
        )

        for i in range(0, 100):
            for i in range(0, len(video_list)):
                driver.get(video_list[i])
                print("opened the page", driver.title)

                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(
                        (By.ID, "ytp-caption-window-container")
                    )
                )
                print("found video container")

                if i == 0:
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
                else:
                    print("video auto played")

                time.sleep(10)

    except Exception as e:
        print(e)
        driver.close()


main()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Pokretanje WebDrivera
web = 'https://rawg.io/'
driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()

def top_250_games():
    try:
        button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "250")]'))
        )
        button.click()
    except Exception as e:
        print(f"Gumb za top 250 igre nije pronađen! {e}")

def scroll_for_loading():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Povećajte vrijeme čekanja za sporije učitavanje
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            time.sleep(5)  # Dodajte dodatno vrijeme za svaki slučaj
            if new_height == driver.execute_script("return document.body.scrollHeight"):
                break
        last_height = new_height

def get_game_boxes():
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "game-card-medium"))
    )
    return driver.find_elements(By.CLASS_NAME, "game-card-medium")

def safe_find_element(driver, xpath):
    try:
        return driver.find_element(By.XPATH, xpath).text
    except Exception:
        return "N/A"

# Klik na "Top 250"
top_250_games()

# Skrolanje za učitavanje svih igara
scroll_for_loading()

# Dohvaćanje podataka o igrama
try:
    game_boxes = get_game_boxes()
    print(f"Ukupan broj pronađenih igara: {len(game_boxes)}")

    games = []
    for i, box in enumerate(game_boxes):
        try:
            # Koristi JavaScript za otvaranje linka, kako bi se izbjegli problemi s klikabilnošću
            title_element = box.find_element(By.XPATH, './/a[@class="game-card-medium__info__name"]')
            game_link = title_element.get_attribute('href')

            driver.execute_script("window.open(arguments[0]);", game_link)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(3)

            # Dohvaćanje podataka sa stranice igre
            game_title = safe_find_element(driver, '//h1[@class="heading heading_1 game__title"]')
            release_date = safe_find_element(driver, '//div[@class="game__meta-date"]')
            playtime = safe_find_element(driver, '//div[@class="game__meta-playtime"]')
            metascore = safe_find_element(driver, '/html/body/div[2]/div/div[3]/div[1]/div/main/div/div[2]/div[1]/div[8]/div[2]/div[2]/div')
            developer = safe_find_element(driver, '/html/body/div[2]/div/div[3]/div[1]/div/main/div/div[2]/div[1]/div[8]/div[5]/div[2]/a')
            publisher = safe_find_element(driver, '/html/body/div[2]/div/div[3]/div[1]/div/main/div/div[2]/div[1]/div[8]/div[6]/div[2]/a')
            age_rating = safe_find_element(driver, '/html/body/div[2]/div/div[3]/div[1]/div/main/div/div[2]/div[1]/div[8]/div[7]/div[2]')
            genre = safe_find_element(driver, '/html/body/div[2]/div/div[3]/div[1]/div/main/div/div[2]/div[1]/div[8]/div[3]/div[2]')
            platforms = safe_find_element(driver, '/html/body/div[2]/div/div[3]/div[1]/div/main/div/div[2]/div[1]/div[8]/div[1]')

            # Spremanje podataka
            games.append({
                "Title": game_title,
                "Release Date": release_date,
                "Playtime": playtime,
                "Metascore": metascore,
                "Developer": developer,
                "Publisher": publisher,
                "Age Rating": age_rating,
                "Genre": genre,
                "Platforms": platforms
            })

            print(f"Dohvaćeni podaci za igru: {game_title}")

            # Zatvaranje trenutne kartice i povratak na popis igara
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        except Exception as e:
            print(f"Greška kod obrade igre {i + 1}: {e}")
            continue

    # Spremanje podataka u CSV
    if games:
        df = pd.DataFrame(games)
        df.to_csv("rawg_top_250_detailed.csv", index=False)
        print("Podaci su spremljeni u 'rawg_top_250_detailed.csv'")

except Exception as e:
    print(f"Nisam pronašao igre! {e}")

# Zatvori preglednik
driver.quit()

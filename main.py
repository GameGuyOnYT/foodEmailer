import random, smtplib, email.mime.text
from selenium import webdriver
from selenium.webdriver.common.by import By


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('annemeyemekler@gmail.com', 'vznnfmkfbhwiypjr')

    mail = email.mime.text.MIMEText(finalRecipe, 'plain', 'utf-8')
    mail['From'] = 'annemeyemekler@gmail.com'
    mail['Subject'] = "Menü Geldi!!"
    mail['To'] = 'tuba@tahca.com'
    mail = mail.as_string()

    server.sendmail(
        'anneyeyemekler@gmail.com',
        'tuba@tahca.com',
        mail
    )


PATH = "C:\\Program Files (x86)\\chromedriver.exe"
listOfAddresses = ["https://nefisyemektarifleri.com/kategori/tarifler/aperatifler-tarifler", "https://www.nefisyemektarifleri.com/kategori/tarifler/hamurisi-tarifleri/", "https://www.nefisyemektarifleri.com/kategori/tarifler/et-yemekleri/", "https://www.nefisyemektarifleri.com/kategori/tarifler/hizli-yemekler/", "https://www.nefisyemektarifleri.com/kategori/tarifler/kahvaltilik-tarifleri/", "https://www.nefisyemektarifleri.com/kategori/tarifler/corba-tarifleri/", "https://www.nefisyemektarifleri.com/kategori/tarifler/salata-meze-kanepe/", "https://www.nefisyemektarifleri.com/kategori/tarifler/sebze-yemekleri/"]
recipeList = []
finalRecipe = ""

# opening the browser and finding title of the recipe
driver = webdriver.Chrome(PATH)
for i in listOfAddresses:
    driver.get(i)
    recipe = random.choice(driver.find_elements(By.CLASS_NAME, "recipe-info"))
    recipeList.append(recipe.text + "\n" + recipe.find_element(By.TAG_NAME, "a").get_attribute("href") + "\n\n")

for i in recipeList:
    finalRecipe += i

send_mail()
driver.quit()
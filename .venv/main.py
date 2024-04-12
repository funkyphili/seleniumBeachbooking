import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def book_slot(datum,day,timeslot,email):

    driver = webdriver.Chrome()
    driver.get("https://termine.moenchengladbach.de/select2?md=13")

    #locate correct website
    a = driver.find_element(By.ID,"header_concerns_accordion-27")
    driver.execute_script("arguments[0].click();", a)
    time.sleep(1)
    b = driver.find_element(By.ID,"cnc-155")
    driver.execute_script("arguments[0].click();", b)
    time.sleep(1)
    locations = driver.find_elements(By.NAME,"select_location")
    correct_loc = None
    for loc in locations:
        if  "Beachvolley" in loc.accessible_name:
            correct_loc = loc
    driver.execute_script("arguments[0].click();", correct_loc)
    time.sleep(1)
    filter = driver.find_element(By.ID,"ui-id-15")
    driver.execute_script("arguments[0].click();", filter)
    time.sleep(1)
    c = driver.find_element(By.ID,"ui-id-18")
    driver.execute_script("arguments[0].click();", c)
    time.sleep(1)
    d = driver.find_element(By.ID, "ui-id-17")
    driver.execute_script("arguments[0].click();", d)
    time.sleep(1)

#filter datum
    datum_pic = driver.find_element(By.ID,"suggest_date_wrap")
    von,bis = datum_pic.find_elements(By.XPATH, f"//input[contains(@name,'filter_date')]")
    driver.execute_script("arguments[0].setAttribute('value',arguments[1])", von, datum)
    driver.execute_script("arguments[0].setAttribute('value',arguments[1])", bis, datum)


#filter time
    zeit = driver.find_element(By.ID,"suggest_filter_timespan")
    time_str = timeslot[0:2] +" Uhr bis"
    cor_zeit = zeit.find_elements(By.XPATH,f"//div/div/label/span[contains(@title,'{time_str}')]")[0]
    driver.execute_script("arguments[0].click();", cor_zeit)

#filter day
    woche = driver.find_element(By.ID,"suggest_filter_weekday")
    wochentag = woche.find_element(By.ID,"panel_wochentag")
    tage = wochentag.find_elements(By.XPATH,"./child::*")
    for tag in tage:
        if tag.text=="Mittwoch" or tag.text=="Freitag":
            child = tag.find_element(By.XPATH,"./child::*")
            driver.execute_script("arguments[0].click();", child)


    filtern = driver.find_element(By.ID,"suggest_filter_form")
    filterbutton  = filtern.find_elements(By.XPATH,"./child::*")
    filter = [i for i in filterbutton if i.accessible_name == "Filtern"]
    driver.execute_script("arguments[0].click();", filter[0])
    time.sleep(3)

    detail_sum = driver.find_element(By.ID, "details_suggest_times")
    final_time = detail_sum.find_element(By.XPATH, f"//div/table/tbody/tr/td/form/button[@title='{timeslot}']")
    driver.execute_script("arguments[0].click();", final_time)

    time.sleep(1)

    confirm_popup = driver.find_element(By.ID, "TevisDialog")
    ja_popup = confirm_popup.find_elements(By.XPATH, f"//div/div/div[contains(@class,'modal-footer')]/button")[0]
    driver.execute_script("arguments[0].click();", ja_popup)

    time.sleep(2)
#fill out form

    anrede = driver.find_element(By.ID, "sexselect-button")
    driver.execute_script("arguments[0].click();", anrede)

    herr = driver.find_element(By.ID, "sexselect-option-2")
    herr_button = herr.find_element(By.XPATH, "./child::*")
    driver.execute_script("arguments[0].click();", herr_button)




    #driver.execute_script("arguments[0].innerText = 'Herr'", anrede)
    phone = driver.find_element(By.ID, "mobnr")
    phone.send_keys("015123333951")
    phone.send_keys(Keys.RETURN)

    vorname = driver.find_element(By.ID, "vorname")
    vorname.send_keys("Robin")

    nachname = driver.find_element(By.ID, "nachname")
    nachname.send_keys("Walter")

    email1 = driver.find_element(By.ID, "email")
    email1.send_keys(email)
    email2 = driver.find_element(By.ID, "emailwhlg")
    email2.send_keys(email)
    email2.send_keys(Keys.RETURN)


    datenschutz = driver.find_element(By.ID, "privacy_dialog")
    datenbox = driver.find_element(By.XPATH, f"//input[@title='Checkbox für Datenerhebung und -verarbeitung']")
    driver.execute_script("arguments[0].click();", datenbox)
    time.sleep(0.1)
    driver.execute_script("arguments[0].click();", datenbox)
    time.sleep(0.1)
    driver.execute_script("arguments[0].click();", datenbox)
    time.sleep(0.1)

    while True:
        pass

    final_confirm = driver.find_element(By.ID, "chooseTerminButton")
    driver.execute_script("arguments[0].click();", final_confirm)


    while True:
        pass


if __name__ == "__main__":
    book_slot("21.06.2024","Freitag","14:45","walter1357@gmx.de")

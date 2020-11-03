from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os
import shutil
import credentials

# Change these to your path
download_path = r"/Users/blackout/Downloads/"  # Path for downloads
athtech = r"/Users/blackout/Downloads/AthTech/Courses"  # Sorter function moves files in this directory
PATH = "/Users/blackout/Scraper/AthTechScraper/chromedriver"  # Path for chromedriver location
driver = webdriver.Chrome(PATH)
driver.get("http://ilearn.athtech.gr/login/index.php")

# Path for each folder
statistics = os.path.join(athtech, "Statistics")
comp_arch = os.path.join(athtech, "Computer Architecture")
management = os.path.join(athtech, "Management")
cont_math = os.path.join(athtech, "Continuous Math")

courses_list = [statistics, comp_arch, management, cont_math]  # Used to create or delete folders

# Creates/deletes folders
try:
    for x in range(len(courses_list)):
        shutil.rmtree(courses_list[x])
except FileNotFoundError:
    pass

try:
    for x in range(len(courses_list)):
        os.mkdir(courses_list[x])
except OSError:
    pass

# List of courses for bot to click
courses = ["/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[3]/a",
           "/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[5]/a",
           "/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[7]/a"]

list2 = [comp_arch, management, statistics]  # Sorter function loops through this list

# Credentials and Login
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys(credentials.username)  # Enter your username
password.send_keys(credentials.password)  # Enter your password
driver.find_element_by_id("loginbtn").click()


# Clicks on dropdown menu
def dropdown_menu():
    driver.find_element_by_xpath(
        "/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/a").click()


# Downloads files
def download():
    pdf = driver.find_elements_by_class_name("instancename")
    for x in range(len(pdf)):
        if pdf[x].is_displayed():
            pdf[x].click()


# Sorts files in folders
def sorter(folder):
    files = os.listdir(download_path)
    for f in files:
        src = download_path + f
        try:
            if "pdf" in f:
                shutil.move(src, folder)
        except shutil.Error:
            pass


# Downloads Math course
def download_math():
    dropdown_menu()
    driver.find_element_by_xpath("/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[4]/a").click()
    for x in range(2, 20): #Change the second value for weekly lessons
        for y in range(1, 5):
            driver.find_element_by_xpath(
                "/html/body/div[2]/section/div/div/div/section/div[2]/div/ul/li[" + str(x) + "]/div[3]/ul/li[" + str(
                    y) + "]/div/div/div[2]/div/a/span").click()


# Downloads Management, Statistics, Computer Architecture courses
for x in range(len(courses)):
    dropdown_menu()
    driver.find_element_by_xpath(courses[x]).click()
    download()
    time.sleep(2)
    sorter(list2[x])

# Downloads Math course
try:
    download_math()
except NoSuchElementException:
    pass

time.sleep(2)

sorter(cont_math)

time.sleep(2)
driver.quit()

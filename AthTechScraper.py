from selenium import webdriver
import time
import os
import shutil
import credentials

# Change these to your path
download_path = r"/Users/blackout/Downloads/"  # Path for downloads
athtech = r"/Users/blackout/Downloads/AthTech/Courses"

PATH = "/Users/blackout/Scraper/AthTechScraper/chromedriver"  # Path for chromedriver location

driver = webdriver.Chrome(PATH)
driver.get("http://ilearn.athtech.gr/login/index.php")

statistics = os.path.join(athtech, "Statistics")
comp_arch = os.path.join(athtech, "Computer Architecture")
management = os.path.join(athtech, "Management")


try:
    shutil.rmtree(statistics)
    shutil.rmtree(comp_arch)
    shutil.rmtree(management)
except FileNotFoundError:
    pass

try:
    os.mkdir(statistics)
    os.mkdir(comp_arch)
    os.mkdir(management)
except OSError:
    pass

# List of courses
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


for x in range(len(courses)):
    dropdown_menu()
    driver.find_element_by_xpath(courses[x]).click()
    download()
    time.sleep(2)
    sorter(list2[x])

# oop = "/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[2]/a"
# math = "/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[4]/a"
# paraskakis = "/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[6]/a"


time.sleep(2)
driver.quit()

from selenium import webdriver
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
math_exercises = os.path.join(cont_math, "Exercises")
math_solutions = os.path.join(cont_math, "Solutions")
pdf = os.path.join(download_path, "PDF")

courses_list = [statistics, comp_arch, management, cont_math]  # Used to create or delete folders

# Creates PDF folder and saves files already in downloads_folder
files = os.listdir(download_path)

try:
    os.mkdir(pdf)
except FileExistsError:
    pass

for f in files:
    src = download_path + f
    try:
        if "pdf" in f:
            shutil.move(src, pdf)
    except shutil.Error:
        pass

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

# Credentials and Login
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys(credentials.username)  # Enter your username
password.send_keys(credentials.password)  # Enter your password
driver.find_element_by_id("loginbtn").click()

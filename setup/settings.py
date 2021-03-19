from selenium import webdriver
import os
import shutil

from setup import credentials

answer = int(input('Choose Semester[1|2]: '))

# Change these to your path
download_path = r'/Users/blackout/Downloads/'  # Path for downloads
athtech = r'/Users/blackout/Downloads/AthTech/Courses'  # Sorter function moves files in this directory
PATH = '/Users/blackout/Scraper/AthTechScraper/chromedriver'  # Path for chromedriver location
driver = webdriver.Chrome(PATH)
driver.get('http://ilearn.athtech.gr/login/index.php')

# Path for each folder
pdf = os.path.join(download_path, 'PDF')

# First Semester filepaths
statistics = os.path.join(athtech, 'Semester1/Statistics')
comp_arch = os.path.join(athtech, 'Semester1/Computer Architecture')
management = os.path.join(athtech, 'Semester1/Management')
cont_math = os.path.join(athtech, 'Semester1/Continuous Math')
math_exercises = os.path.join(cont_math, 'Exercises')
math_solutions = os.path.join(cont_math, 'Solutions')

# Second Semester filepaths
networks = os.path.join(athtech, 'Semester2/Networks')
discrete_math = os.path.join(athtech, 'Semester2/Discrete Math')
probabilities = os.path.join(athtech, 'Semester2/Probabilities')

# Used to create or delete folders in filepaths
courses_list_semester1 = [statistics, comp_arch, management, cont_math]
courses_list_semester2 = [networks, discrete_math, probabilities]

# Don't Change
# Creates PDF folder and saves files already in downloads_folder
files = os.listdir(download_path)

try:
    os.mkdir(pdf)
except FileExistsError:
    pass

for f in files:
    src = download_path + f
    try:
        if 'pdf' in f:
            shutil.move(src, pdf)
    except shutil.Error:
        pass


# Creates/deletes folders in courses filepath
def create_delete_folders(folder_name):
    try:
        for x in range(len(folder_name)):
            shutil.rmtree(folder_name[x])
    except FileNotFoundError:
        pass

    try:
        for x in range(len(folder_name)):
            os.mkdir(folder_name[x])
    except OSError:
        pass


# Credentials and Login
username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
username.send_keys(credentials.username)  # Enter your username
password.send_keys(credentials.password)  # Enter your password
driver.find_element_by_id('loginbtn').click()

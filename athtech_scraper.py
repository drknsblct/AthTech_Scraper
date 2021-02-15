from selenium.common.exceptions import NoSuchElementException
import time
import os
import shutil
from setup import download_path, driver, pdf
from setup import statistics, comp_arch, management, cont_math, math_exercises, math_solutions

# Statistics and Management xpaths from dropdown menu
courses = ["/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[9]/a",
           "/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[12]/a"]

management_and_statistics = [management, statistics]  # Sorter function loops through this list


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
            if "pdf" in f or "pptx" in f:
                shutil.move(src, folder)
            elif "ipynb" in f or "xlsx" in f or "csv" in f:
                shutil.move(src, statistics)
            elif "sinx_cosx__plot.gif" in f or "sinx_cosx__table.jpg" in f:
                shutil.move(src, folder)
        except shutil.Error:
            pass


# Makes Exercises and Solutions folders inside Math folder
def math_sorter():
    files = os.listdir(cont_math)
    os.mkdir(math_exercises)
    os.mkdir(math_solutions)
    for f in files:
        src = cont_math + "/" + f
        try:
            if "Solutions" in f or "SOLUTIONS" in f:
                shutil.move(src, math_solutions)
            elif "Exercises" in f or "EXERCISES" in f or "Revision" in f:
                shutil.move(src, math_exercises)
            elif "printer friendly" in f or "printer_friendly" in f:
                os.remove(src)
        except FileNotFoundError:
            pass


# Downloads Math course
def download_math():
    dropdown_menu()
    driver.find_element_by_xpath("/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[7]/a").click()
    pdf = driver.find_elements_by_class_name("instancename")
    for x in range(len(pdf)):
        if x == 1:
            continue
        if pdf[x].is_displayed():
            pdf[x].click()


def download_comp_arch():
    dropdown_menu()
    driver.find_element_by_xpath("/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[6]/a").click()
    pdf = driver.find_elements_by_class_name("instancename")
    for x in range(len(pdf)):
        if x == 2 or x == 12 or x == 13 or x == 15:
            continue
        if pdf[x].is_displayed():
            pdf[x].click()


if __name__ == '__main__':
    download_comp_arch()  # downloads comp_arch course
    time.sleep(2)  # waits x seconds
    sorter(comp_arch)  # moves items to folder

    # Downloads Management, Statistics courses
    for x in range(len(courses)):
        dropdown_menu()
        driver.find_element_by_xpath(courses[x]).click()
        download()
        time.sleep(2)
        sorter(management_and_statistics[x])

    # Downloads Math course
    try:
        download_math()
    except NoSuchElementException:
        pass

    time.sleep(2)
    sorter(cont_math)
    math_sorter()

    # Deletes PDF folder if there weren't any pdf before program started
    if len(os.listdir(pdf)) == 0:
        shutil.rmtree(pdf)
    elif len(os.listdir(pdf)) == 1 and ".DS_Store" in os.listdir(pdf):
        shutil.rmtree(pdf)  # if only .DS_Store in folder then delete

    driver.quit()

# Clicks on dropdown menu
import os
import shutil
import time

from setup.settings import driver, download_path, statistics


def dropdown_menu():
    driver.find_element_by_xpath(
        '/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/a').click()


# Downloads files
def download():
    pdf = driver.find_elements_by_class_name('instancename')
    for x in range(len(pdf)):
        if pdf[x].is_displayed():
            pdf[x].click()


# Sorts files in folders
def sorter(folder):
    files = os.listdir(download_path)
    for f in files:
        src = download_path + f
        try:
            if 'pdf' in f or 'pptx' in f or 'ppsx' in f or 'docx' in f:
                shutil.move(src, folder)
            elif 'ipynb' in f or 'xlsx' in f or 'csv' in f:
                shutil.move(src, statistics)
            elif 'sinx_cosx__plot.gif' in f or 'sinx_cosx__table.jpg' in f:
                shutil.move(src, folder)
        except shutil.Error:
            pass


# Opens dropdown menu, downloads courses and sorts them
def download_and_sort(courses, courses_list):
    for x in range(len(courses)):
        dropdown_menu()
        driver.find_element_by_xpath(courses[x]).click()
        download()
        time.sleep(2)
        sorter(courses_list[x])

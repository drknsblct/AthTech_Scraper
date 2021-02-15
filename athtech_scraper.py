from selenium.common.exceptions import NoSuchElementException
import time
import os
import shutil
from setup.settings import driver, pdf, comp_arch, cont_math
from semesters.first_semester import download_comp_arch, sorter, courses, dropdown_menu, download, \
    management_and_statistics, download_math, math_sorter

answer = int(input('Choose 1/2 '))

if __name__ == '__main__':
    while True:
        if answer == 1:
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
            break
        # elif answer == 2:

    # Deletes PDF folder if there weren't any pdf before program started
    if len(os.listdir(pdf)) == 0:
        shutil.rmtree(pdf)
    elif len(os.listdir(pdf)) == 1 and '.DS_Store' in os.listdir(pdf):
        shutil.rmtree(pdf)  # if only .DS_Store in folder then delete

    driver.quit()

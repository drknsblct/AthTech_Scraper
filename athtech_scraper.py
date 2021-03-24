import os
import shutil
import time

from selenium.common.exceptions import NoSuchElementException

from semesters.first_semester import download_comp_arch, courses, management_and_statistics, download_math, math_sorter
from semesters.second_semester import download_probabilities, download_networks, courses2, discr_math
from semesters.semesters import sorter, download_and_sort
from setup.settings import answer, create_delete_folders, courses_list_semester1, comp_arch, cont_math, \
    courses_list_semester2, probabilities, networks, pdf, driver

if __name__ == '__main__':
    while True:
        if answer == 1:
            create_delete_folders(courses_list_semester1)

            download_comp_arch()  # downloads comp_arch course
            time.sleep(2)  # waits x seconds
            sorter(comp_arch)  # moves items to folder
            download_and_sort(courses, management_and_statistics)  # downloads course and sorts it

            # Downloads Math course
            try:
                download_math()
            except NoSuchElementException:
                pass

            time.sleep(2)
            sorter(cont_math)
            math_sorter()
            break

        elif answer == 2:
            create_delete_folders(courses_list_semester2)

            download_probabilities()
            time.sleep(2)
            sorter(probabilities)

            download_networks()
            time.sleep(2)
            sorter(networks)

            download_and_sort(courses2, discr_math)
            break

    # Deletes PDF folder if there weren't any pdf before program started
    if len(os.listdir(pdf)) == 0:
        shutil.rmtree(pdf)
    elif len(os.listdir(pdf)) == 1 and '.DS_Store' in os.listdir(pdf):
        shutil.rmtree(pdf)  # if only .DS_Store in folder then delete

    driver.quit()

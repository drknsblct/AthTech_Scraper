from semesters.first_semester import dropdown_menu
from setup.settings import discrete_math, driver

courses2 = ['/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[8]/a']

courses_list_semester2 = [discrete_math]

# Downloads Probabilities course
def download_probabilities():
    dropdown_menu()
    driver.find_element_by_xpath('/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[12]/a').click()
    pdf = driver.find_elements_by_class_name('instancename')
    for x in range(len(pdf)):
        if x == 3:
            break
        if pdf[x].is_displayed():
            pdf[x].click()

# Downloads Networks course
def download_networks():
    dropdown_menu()
    driver.find_element_by_xpath('/html/body/header/nav/div/div/div/div[1]/div/div[2]/ul/li/ul/li[9]/a').click()
    pdf = driver.find_elements_by_class_name('instancename')
    for x in range(len(pdf)):
        if x == 5 or x == 6:
            continue
        if pdf[x].is_displayed():
            pdf[x].click()

from selenium import webdriver
import csv

DRIVER_PATH = r'A:\Mohamed\Downloads(HDD)\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

URL = 'https://www.algoexpert.io/questions'

driver.get(URL)
question_columns = driver.find_elements_by_class_name("QuestionPage-questionsColumnContainer")

questions = []
for question_column in question_columns:
    question_containers = question_column.find_elements_by_css_selector("div[class*='js-question-band']")
    for question_container in question_containers:
        question_element = question_container.find_element_by_css_selector("div:nth-of-type(2)")
        questions.append(question_element.get_attribute("id"))

print(questions)


# print the questions to CSV
with open('algoexpert_questions.csv', mode='w', newline='', encoding="utf-8") as file:
    question_writer = csv.writer(file, 
                                 delimiter=',', 
                                 quotechar='"', 
                                 quoting=csv.QUOTE_MINIMAL)

    for question in questions:
        question_writer.writerow([question])
        


from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Be sure to have chrome driver installed, and update the path below to the location of the executable
DRIVER_PATH = r'PATH_TO_CHROME_DRIVER'
URL = 'https://www.algoexpert.io/questions'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

question_columns = driver.find_elements(By.CLASS_NAME, value="QuestionPage-questionsColumnContainer")

questions = []
for question_column in question_columns:
    question_containers = question_column.find_elements(By.CSS_SELECTOR, value="div[class*='js-question-band']")
    for question_container in question_containers:
        question_element = question_container.find_elements(By.CSS_SELECTOR, value="div:nth-of-type(2)")
        questions.append(question_element[0].text)

print(questions)

# print the questions to CSV
with open('algoexpert_questions.csv', mode='w', newline='', encoding="utf-8") as file:
    question_writer = csv.writer(file, 
                                 delimiter=',', 
                                 quotechar='"', 
                                 quoting=csv.QUOTE_MINIMAL)

    for question in questions:
        question_writer.writerow([question])
        

import requests
import names
from selenium import webdriver

# 1:
response = requests.get("https://api.github.com/users/avielb/repos")
count = 0
max_count = 5
for repo in response.json():
    if repo != '' and count != max_count:
        count = count + 1
    elif count == max_count:
        print("At least " + str(max_count) + " git repositories exists in the API")
        break

# 2:
check_amount = 3
min_age = 0
max_age = 120
for i in range(check_amount):
    name = names.get_first_name()
    response1 = requests.get("https://api.agify.io/?name="+name)
    if response1.json()["age"] > min_age and response1.json()["age"] < max_age:
        print(name + " age is OK, below " + str(max_age) + " and over " + str(min_age))
    else:
        print(name + " age is Not OK")


# 3:
response2 = requests.get("http://universities.hipolabs.com/search?country=Israel")
count = 0
max_count1 = 5
for repo in response2.json():
    if repo["country"] == "Israel" and count != max_count1:
        count = count + 1
    elif count == max_count1:
        print("At least " + str(max_count1) + " Universities in Israel")
        break


# 4:
def check_title(driver, expected_title):
    if expected_title == driver.title:
        print("The title is : " + expected_title)
    else:
        print("The title is NOT " + expected_title)


my_driver = webdriver.Chrome()
my_driver.get("https://www.ycombinator.com/")
check_title(my_driver, "Y Combinator")

# 5:
my_driver.get("https://hub.docker.com")
check_title(my_driver, "Docker Hub Container Image Library | App Containerization")

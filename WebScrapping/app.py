import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".js-post-summary")
# print(questions[0])
# the html element

# print(type(questions[0]))
# <class 'bs4.element.Tag'>

# attribute object of the div element like class and id , is store in attribute
# print(questions[0].attrs)
# {'id': 'question-summary-75345553', 'class': ['s-post-summary', 'js-post-summary'], 'data-post-id': '75345553', 'data-post-type-id': '1'}


# GET the id of the first div element
print(questions[0]["id"])
# or
print(questions[0].get("id", 0))
# question-summary-75345578

# select - return list of object(html)
print(questions[0].select(".s-link"))
# [<a class="s-link" href="/questions/75345578/svn-commit-shows-error-not-a-working-copy">Svn commit shows error 'not a working copy'</a>]

# select one - return one
print(questions[0].select_one(".s-link").getText())
# Using Abstract Class when declare variables in TypeScript

for question in questions:
    print(question.select_one(".s-link").getText())
    print(question.select_one(".s-post-summary--stats-item-number").getText())


# PROEJCT RUN THROUGH FIRST TEN PAGE question using the pagination button

# DOCUMENTATION
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

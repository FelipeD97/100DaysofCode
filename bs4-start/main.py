from bs4 import BeautifulSoup

with open("bs4-start/website.html") as file:
    contents = file.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)

# print(soup.prettify)

# print(soup.a)

all_anchor_tags = soup.find_all("a")

# for tag in all_anchor_tags:
#     # print(tag.get_text())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="#name")
# print(company_url.get_text())

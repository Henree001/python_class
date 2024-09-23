import requests
from bs4 import BeautifulSoup


url = "https://appclick.ng/portal/site/login"
response = requests.get(url)

# print(response.text)
courses = ["frontend-development", "backend-development"]

extracted_data = []
for course in courses:
    if course == "cybersecurity":
        appclick_url = ""
    else:
        appclick_url = f"https://www.appclick.ng/course-details-{course}.php"
    response = requests.get(appclick_url)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup.prettify())
    # title = soup.title.text
    # print(title)
    # div = soup.div.contents
    # print(div)
    # print(soup.link['href'])
    # print(soup.link['rel'])
    # print(soup.link['type'])
    # print(soup.div.name)
    h2 = soup.find('div', class_='breadcrumb-title').contents[1]
    duration_ul = soup.find('div', class_='course-details-widget').contents[1]
    duration_li_standard = duration_ul.contents[5]
    p_standard = duration_li_standard.contents[3]
    duration_li_adv = duration_ul.contents[7]
    p_adv = duration_li_adv.contents[3]

    course_outline = soup.find_all('ul', class_='course-details-list')
    # print(course_outline)
    # print(course_outline[0].find_all('li'))

    # LIST COMPREHENSION
    # numbers = [1, 2, 3, 4, 5]
    # new_list = []
    # for number in numbers:
    #     new_num = number ** 2
    #     new_list.append(new_num)
    # lists = [num**2 for num in numbers]
    # print(new_list)
    # print(lists)


    dic = {

        "course": h2.text,
        "duration(standard)": p_standard.text,
        "duration(advanced)": p_adv.text,
        "course_outline(standard))": [li.text for li in course_outline[0].find_all('li')],
        "course_outline(advanced)": [li.text for li in course_outline[1].find_all('li')],
    }

    extracted_data.append(dic)
print(extracted_data)
    
# [
#         "course": h2.text,
#         "duration(standard)": p.text,
#         "duration(advanced)": p.text,
#         "course_outline(standard))": [],
#         "course_outline(advanced)": [],
#     },
#     {
#         "course": h2.text,
#         "duration(standard)": p.text,
#         "duration(advanced)": p.text,
#         "co
#     {urse_outline(standard))": p.text,
#         "course_outline(advanced)": p.text,
#     },

# ]
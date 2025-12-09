from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

tag_object=soup.title
print("tag object:",tag_object)

print("tag object type:", type(tag_object))

tag_object = soup.h3
print("tag object:",tag_object)

tag_child = tag_object.b
print("Child:", tag_child)

parent_tag = tag_child.parent
print("Parent:", parent_tag)

sibling_1=tag_object.next_sibling
print("First Sibling:",sibling_1)

sibling_2 = sibling_1.next_sibling
print("Second Sibling:", sibling_2)

print(tag_child['id'])

print(tag_child.attrs)

print(tag_child.get('id'))

tag_string=tag_child.string
print(tag_string)

print(type(tag_string))

unicode_string = str(tag_string)
print(unicode_string)

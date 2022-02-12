content = """
<html>
<body>
<h1>Beautiful Soup Demo </h1>
<p id="p1">
This is first para
</p>
<p id="p2">This is second para </p>

<h2>Topics </h2>
Here are topics 
<ul>
  <li>How to install </li>
  <li>How to impprt </li>
  <li>How to navigate document </li>
</ul>
For more details, visit <a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/#'>
Beautiful Soup Documentation </a>

"""

from bs4 import BeautifulSoup

bs = BeautifulSoup(content, "html.parser")
print(bs.h1.text)
print(bs.p.text)

para2 = bs.find(id="p2")
print(type(para2))
print(para2.text)

# display list items
for li in bs.find_all('li'):
    print(li.text)

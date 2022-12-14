import re
import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()
# print(root.tag)
# print(root.attrib)

# for child in root:
#     print(child.tag, child.attrib)

x = [elem.tag for elem in root.iter()]

# for i in x:
#     print(i)
#
# for movie in root.iter('movie'):
#     print(movie.attrib)
#
# for desc in root.iter('description'):
#     print(desc.text)
#
# for movie in root.findall('./genre/decade/movie/[year="1992"]'):
#     print(movie.attrib)
#
# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']"):
#     print(movie.attrib)

# for movie in root.findall("./genre/decade/movie/format/[@multiple='Yes']..."):
#     print(movie.attrib)

# for movie in root.iter('movie'):
#     print(movie.attrib)

b2 = root.find("./genre/decade/movie[@title='Back 2 the Future']")
b2.attrib["title"] = "Back to the Future"
# print(b2.attrib)

for form in root.findall("./genre/decade/movie/format"):
    match = re.search(',', form.text)
    if match:
        form.set('multiple', 'Tak')
    else:
        form.set('multiple', 'Nie')

tree.write("filmy.xml")

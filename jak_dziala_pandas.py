import xml.etree.ElementTree
import pandas as pd

e = xml.etree.ElementTree.parse(open("./sroda/test.xml"))
f = pd.DataFrame([{a.get('name'): a.text for a in t} for t in e.findall("tuple")])
print(f)
# f.to_json('test2.json')


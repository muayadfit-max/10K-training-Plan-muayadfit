import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile('10K Beginner Training Plans.docx')
xml_content = z.read('word/document.xml')
tree = ET.XML(xml_content)
namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
text = '\n'.join([node.text for node in tree.findall('.//w:t', namespace) if node.text])

with open('plans_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)

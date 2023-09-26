

import pandas as pd
import json
import xml.etree.ElementTree as ET

#Read From CSV by creating method
def read_from_csv(filename):
    data = pd.read_csv(filename)
    return data

#Lets call now Json file
def read_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    return df


#Read from XML
def read_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    rows = []
    for child in root:
        row ={}
        for element in child:
            row[element.tag] = element.text

        rows.append(row)

    df = pd.DataFrame(rows)
    return df


#Using the functions
csv_data = read_from_csv('dataCsv.csv')
print(csv_data.head())

json_data = read_from_json('dataJson.json')
print("\n Json Data:")
print(json_data)

xml_data = read_from_xml('dataXml.xml')
print("\nXML Data:")
print(xml_data.head())

#So we created three different files lets run and see the output:

if __name__ == "__main__":
    #########################################
    #              Procedure 1              #
    #########################################
    # Add print statement here
    print("Hello world")
#
import xml.etree.ElementTree as ET
with open('xml_example.xml','r') as file1:
    mytree = ET.parse(file1)
myroot = mytree.getroot()
## Print the tags
print('Tags in the XML:')    
for element in myroot:
    print(element.tag)
#
# Print the value of id tag
print('user tag value:')
print(myroot.find('user').text)
#
#    print(type(data))
user = myroot.find('user')
print(user.find('name').text)
for role in user.findall('roles'):
    print(role.text)
#
user.find('location').find('city').text = 'Capracotta'
user.find('location').find('state').text = 'Molise'

with open('xml_example_edited.xml','w') as file2:
    mytree.write(file2, encoding='unicode')
    
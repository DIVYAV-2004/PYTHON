#converting the python object(like list, dict, etc.) into json string
#dumps() method is used to convertpython code to json string
import json

data={'name':'chitti','age':25,'city':'Hyderabad'}
json_string=json.dumps(data)
print(json_string)
print(type(json_string))
#optional parameters in dumps() method
print(json.dumps(data, indent=4))

#converting python object list to json string
data1=['chitti','divya','cryso']
json_str=json.dumps(data1)
print(json_str)
print(type(json_str))

#converting json string back to python object
#here loads method is used for converting json string to python object
json_str1='{"name":"divya","age":22,"city":"hyderabad"}'
python_obj=json.loads(json_str1)
print(python_obj)
print(type(python_obj))

#converting json string to python list
json_str2='["apple","banana","mango"]'
python_list=json.loads(json_str2)
print(python_list)
print(type(python_list))
#list operation
python_list.append('grapes')
print(python_list)

#real world student details example
json_data='{"students":[{"name":"divya","age":22},{"name":"chitti","age":25}]}'
#convert to python
python_data=json.loads(json_data)
print(python_data['students'][0]['name'])
#modify and convert back to json
python_data['students'].append({'name':'smiley','age':20})
updated_json=json.dumps(python_data, indent=4)
print(updated_json)

# #another example
# json_data1='{"students":[{"name":"dog","age":5},{"name":"cat","age":4}]}'
# python_data1=json.loads(json_data1)
# print(python_data1['students'][0]['age'])

# python_data1['students'].append({'name':"rat",'age':3})
# updated_json1=json.dumps(python_data1, indent=4)
# print(updated_json1)

#adding few names into the existing list in the file
json_str3='["apple","banana","carrot"]'
python_list3=json.loads(json_str3)
print(python_list3)
print(type(python_list3))
python_list3.append('grapes')
python_list3.append('jackfruit')
python_list3.append('mango')
print(python_list3)
print(type(python_list3))
updated_json3=json.dumps(python_list3)
print(updated_json3)
print(type(updated_json3))

#remove any name from the list
python_list3.remove('grapes')
print(python_list3)
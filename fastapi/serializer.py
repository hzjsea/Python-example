import json

test_dict = {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}

# 转换成字符串 dumps
test_string = json.dumps(test_dict)
print(type(test_string))

# 转换成字典
test_json = json.loads(test_string)
print(type(test_json))

# 将字典转换成字符串写入文件
file = open('1.json','w',encoding='utf-8')
json.dump(test_dict,file)

# 将文件中的字符串转换成字典输出
file = open('1.json','r',encoding='utf-8')
info = json.load(file)
print(info)
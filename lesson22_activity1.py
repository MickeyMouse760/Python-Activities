studentdata={'id1':
{'name':['James'],
'class': ['V'],
'subjects':['english, math, science']
},
'id2':
{'name': ['David'],
'class': ['V'],
'subjects': ['english, math, science']
},
'id3':
{'name' : ['Sarah'],
'class':['V'],
'subjects': ['english, math, science'],
},
'id4':
{'name': ['Chris'],
'class':['V'],
'subjects':['english, math, science']
},
}
result = {}
for key,value in studentdata.items():
    if value not in result.values():
        result[key]=value
print(result)
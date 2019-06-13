def group_by_owners(files):
    myDict = {}
    for k in files:
        value = files.get(k)
        myDict.setdefault(value,[]).append(k)  
    return myDict
   
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}  
print(group_by_owners(files))


print(files.get('Input.txt'))


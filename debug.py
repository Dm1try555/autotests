data1 =  ['Notes', 'React', 'Veu', 'Private', 'Downloads', 'Word File.doc', 'Excel File.doc']
data2 = ['notes', 'react', 'veu', 'private', 'downloads', 'wordFile', 'excelFile']

print(str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower())
print(data2)

data1 = str(data1).replace(' ', '').replace('doc', '').replace('.', '').lower()
data2 =str(data2).lower().replace(' ','')
assert data1 == data2


data3 = r"C:\Users\Dima\Downloads\Telegram Desktop\filetest150.txt"
data4 = r"C:\fakepath\filetest150.txt"

print(data3.split('\\')[-1])
print(data4.split('\\')[-1])

assert data3.split('\\')[-1] == data4.split('\\')[-1]
values = ['very high', 'high', 'medium', 'low', 'very low']

user_input = {
    'humidity' : 'very high',
    'temp' : 'high',
    'rainfall' : 'very high',
    'elevaion' : 'low'
}

keys = ['humidity', 'temp', 'rainfall', 'elevation']

data = {
    'tropical' : {
        'humidity' : 'very high',
        'temp' : 'high',
        'rainfall' : 'very high',
        'elevaion' : 'low'
        },
    'arid' : {
        'humidity' : 'low',
        'temp' : 'high',
        'rainfall' : 'very low',
        'elevaion' : 'high'
        }
}

grades = []

for i in data.keys():
    grade = 0
    for j in data[i].keys():
        print(values.index(data[i][j]),values.index(user_input[j]))
        if values.index(data[i][j])- values.index(user_input[j]) == 0:
            grade +=2
        else :
            grade -= abs(values.index(data[i][j]) -  values.index(user_input[j]))
    print('grade ' + str(grade))
    grades.append(grade)

print(list(data.keys())[grades.index(max(grades))])
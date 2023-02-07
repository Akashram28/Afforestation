from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
class ForestType(Resource):
    data = {
    'Moist tropical forest' : {
        'humidity' : 'very high',
        'temp' : 'high',
        'rainfall' : 'very high',
        'elevaion' : 'very low'
        },
    'Dry tropical forest' : {
        'humidity' : 'low',
        'temp' : 'very high',
        'rainfall' : 'low',
        'elevaion' : 'low'
        },
    'Montane temperte forest':{
        'humidity' : 'high',
        'temp' : 'medium',
        'rainfall' : 'high',
        'elevaion' : 'high'
        
    },
    'Montane sub tropical forest':{
        'humidity' : 'medium',
        'temp' : 'low',
        'rainfall' : 'medium',
        'elevaion' : 'medium'
    },    
    'Alpine forest':{
        'humidity' : 'very low',
        'temp' : 'very low',
        'rainfall' : 'very low',
        'elevaion' : 'very high'
        
    }
    }
    keys = ['humidity', 'temp', 'rainfall', 'elevation']
    values = ['very high', 'high', 'medium', 'low', 'very low']
    
  

    def get(self,humidity,temp,rainfall,elevation):
         user_input = {
            'humidity' : 'low',
            'temp' : 'high',
            'rainfall' : 'low',
            'elevaion' : 'very high'}
        
         grades = []

         for i in list(self.data.keys()):
            grade = 0
            for j in list(self.data[i].keys()):
                print(self.values.index(self.data[i][j]),self.values.index(user_input[j]))
                if self.values.index(self.data[i][j])- self.values.index(user_input[j]) == 0:
                    grade +=2
                else :
                    grade -= abs(self.values.index(self.data[i][j]) -  self.values.index(user_input[j]))
            print('grade ' + str(grade))
            grades.append(grade)
         print(max(grades))
         return {"ForestType":(list(self.data.keys())[grades.index(max(grades))])}
        
api.add_resource(ForestType,'/foresttype/<string:humidity>/<string:temp>/<string:rainfall>/<string:elevation>')
if __name__ == "__main__":
    app.run(debug=True)
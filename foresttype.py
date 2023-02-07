from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
class ForestType(Resource):
    climate={'Moist tropical forest':'Hot','Dry tropical forest':'Arid','Alpine forest':'Cold','Monatane temperte forest':'warm','Montaine sub tropical forest':'Cool'}
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
    solutions = {'Alpine Forest':'As alpine forests are mostly chopped to use their long straight wood. Selective logging is a method that can be used to meet the needs of both the forests and humans seeking economical resources. Selective logging is the removal of trees within a stand based on size limitations. This technique allows for forest regeneration to occur between and after the selective harvest cycles.',
                 'Dry Tropical forest':'Site water management also plays an essential role in site preparation in certain areas. If drainage is not considered in some low-lying afforestation lands, the afforestation will fail.Flooding is a treatment that use channel or dikes to guide the water from afforestation site with high moisture, like coastal and riparian lands, shrimp ponds, swamps. Flooding or irrigation also can reduce the salt and alkali content of saline soil . Irrigation is an essential way in improving site water conditions in water-deficient areas, such as the Middle East, South Africa, China, India, especially for the cultivation of timber forests ',
                 'Moist Tropical Forest':'Building blocks for tropical rainforest conservation include ecotourism and rehabilitation. Reforestation and restoration are common practices in certain areas to try to increase tropical rainforest density. By communicating with the local people living in, and around, the rainforest, conservationists can learn more about what might allow them to best focus their efforts.[1] Rainforests are globally important to sustainability and preservation of biodiversity. Although they may vary in location and inhabited species of plants and animals, they remain important worldwide for their abundance of natural resources and for the ecosystem services. It is important to take into consideration the differing species and the biodiversity that exists across different rainforest types in order to accurately implement methods of conservation',
                 'Montane tem forest':'Maintaining and restoring degraded forests: Montane temperate forests are often degraded due to human activities such as clear-cutting, overgrazing, and mining. Restoration and reforestation efforts can help to recover these degraded areas and improve the overall health of the forest ecosystem. Protecting key wildlife habitats: Montane temperate forests are home to many unique and threatened species, so its important to protect critical habitats, such as riparian areas, den sites, and nesting sites, in order to conserve biodiversity',
                 'Montane temperte forest':'Montane sub-tropical forests are often threatened due to the planting of non-native tree species, so promoting the use of native tree species can help to conserve the unique biodiversity of these forests. Improving fire management practices: Fire is an important ecological process in montane sub-tropical forests, but it can also have negative impacts when its not managed properly. Implementing fire management strategies that balance the need for fire with the need to protect human communities and assets can help to maintain the health of these forests.'}
    
  

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
         return {"ForestType":(list(self.data.keys())[grades.index(max(grades))]),"Solution":""}
        
api.add_resource(ForestType,'/foresttype/<string:humidity>/<string:temp>/<string:rainfall>/<string:elevation>')
if __name__ == "__main__":
    app.run(debug=True)
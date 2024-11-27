from utils.DataResponse import DataResponse
from config.Enviroment import Enviroment
from utils.RequestHTTP import RequestHTTP
from model.getter.Person import Person
from model.getter.Branch import Branch
from model.getter.Group import Group
from model.getter.Section import Section


class PersonData:

    def __init__(self):
        self.base_url=Enviroment().getAPIProtocol()+Enviroment().getAPIHost()
        self.api_token=Enviroment().getAPIToken()
        self.people="/api/personas"

    def callback(self,json_data):
        people=[]

        for obj in json_data['data']:

            branches=[]
            groups=[]
            sections=[]

            for branch in obj['sucursales']:
                branches.append(Branch( branch['id'], branch['codigo'], branch['nombre'],
                                        branch['direccion'], branch['telefono'], branch['descripcion'],
                                        branch['localidad'], branch['provincia'], branch['departamento'],
                                        branch['created_at'], branch['updated_at']))
                
            for group in obj['grupos']:
                groups.append(Group(group['id'], group['nombre'], group['descripcion'],
                                    group['localidad'], group['provincia'], group['departamento'],
                                    group['created_at'], group['updated_at']))
                
            for section in obj['secciones']:
                sections.append(Section(section['id'], section['nombre'], section['descripcion'],
                                        section['localidad'], section['provincia'], section['departamento'],
                                        section['created_at'], section['updated_at']))

            people.append(Person(  obj['id'], obj['codigo'], obj['numero_item'], 
                                    obj['nombres'], obj['apellidos'], obj['ci'], 
                                    obj['profesion'], obj['fecha_nacimiento'], 
                                    obj['sexo'], obj['cargo'], obj['direccion'], 
                                    obj['telefono'], obj['email'], obj['estado_civil'], 
                                    obj['haber_basico'], obj['talla_ropa'], obj['file_curriculum'], 
                                    obj['localidad'], obj['provincia'], obj['departamento'], 
                                    obj['numero_seguro'], obj['nacionalidad'], obj['estado'], 
                                    obj['otros'], obj['created_at'], obj['updated_at'],
                                    branches=branches, groups=groups, sections=sections))
            
        return people

    def getPersonFromAPI(self,database,page):
        request=RequestHTTP(base_url=self.base_url)
        dataResponse=request.GET(self.people, params={ "database" : database , "page" : page },
                    headers={ "token" : self.api_token , "Accept" : "application/json" },
                    callback=self.callback)
        return dataResponse
    

    def callbackTotalPages(self,json_data):
        return int(json_data['last_page'])

    def getTotalPagesFromAPI(self,database):
        request=RequestHTTP(base_url=self.base_url)
        dataResponse=request.GET(self.people, params={ "database" : database , "page" : "1" },
                    headers={ "token" : self.api_token , "Accept" : "application/json" },
                    callback=self.callbackTotalPages)
        return dataResponse
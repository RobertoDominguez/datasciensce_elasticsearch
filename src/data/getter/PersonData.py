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

            for obj in json_data['data']:
                branches.append(Branch( obj['id'], obj['codigo'], obj['nombre'],
                                    obj['direccion'], obj['telefono'], obj['descripcion'],
                                    obj['localidad'], obj['provincia'], obj['departamento'],
                                    obj['created_at'], obj['updated_at']))
            for obj in json_data['data']:
                groups.append(Group(    obj['id'], obj['nombre'], obj['descripcion'],
                                    obj['localidad'], obj['provincia'], obj['departamento'],
                                    obj['created_at'], obj['updated_at']))
            for obj in json_data['data']:
                sections.append(Section(    obj['id'], obj['nombre'], obj['descripcion'],
                                        obj['localidad'], obj['provincia'], obj['departamento'],
                                        obj['created_at'], obj['updated_at']))

            people.append(Person(  obj['id'], obj['codigo'], obj['numero_item'], 
                                    obj['nombres'], obj['apellidos'], obj['ci'], 
                                    obj['profesion'], obj['fecha_nacimiento'], 
                                    obj['sexo'], obj['cargo'], obj['direccion'], 
                                    obj['telefono'], obj['email'], obj['estado_civil'], 
                                    obj['haber_basico'], obj['talla_ropa'], obj['file_curriculum'], 
                                    obj['localidad'], obj['provincia'], obj['departamento'], 
                                    obj['numero_seguro'], obj['nacionalidad'], obj['estado'], 
                                    obj['otros'], obj['created_at'], obj['updated_at']))
            
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
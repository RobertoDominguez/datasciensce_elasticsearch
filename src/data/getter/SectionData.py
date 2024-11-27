from utils.DataResponse import DataResponse
from config.Enviroment import Enviroment
from utils.RequestHTTP import RequestHTTP
from model.getter.Section import Section

class SectionData:

    def __init__(self):
        self.base_url=Enviroment().getAPIProtocol()+Enviroment().getAPIHost()
        self.api_token=Enviroment().getAPIToken()
        self.sections="/api/secciones"

    def callback(self,json_data):
        sections=[]

        for obj in json_data['data']:
            sections.append(Section(    obj['id'], obj['nombre'], obj['descripcion'],
                                        obj['localidad'], obj['provincia'], obj['departamento'],
                                        obj['created_at'], obj['updated_at']))
            
        return sections

    def getSectionFromAPI(self,database,page):
        request=RequestHTTP(base_url=self.base_url)
        dataResponse=request.GET(self.sections, params={ "database" : database , "page" : page },
                    headers={ "token" : self.api_token , "Accept" : "application/json" },
                    callback=self.callback)
        return dataResponse
    

    def callbackTotalPages(self,json_data):
        return int(json_data['last_page'])

    def getTotalPagesFromAPI(self,database):
        request=RequestHTTP(base_url=self.base_url)
        dataResponse=request.GET(self.sections, params={ "database" : database , "page" : "1" },
                    headers={ "token" : self.api_token , "Accept" : "application/json" },
                    callback=self.callbackTotalPages)
        return dataResponse
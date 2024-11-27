from utils.DataResponse import DataResponse
from config.Enviroment import Enviroment
from utils.RequestHTTP import RequestHTTP
from model.getter.Attendance import Attendance

class AttendanceData:

    def __init__(self):
        self.base_url=Enviroment().getAPIProtocol()+Enviroment().getAPIHost()
        self.api_token=Enviroment().getAPIToken()
        self.attendances="/api/asistencias"

    def callback(self,json_data):
        attendances=[]

        for obj in json_data['data']:
            attendances.append(Attendance(  obj['id'], obj['codigo_aux'], obj['id_persona'],
                                            obj['fecha'], obj['codigo'], obj['nombre'],
                                            obj['sucursal'], obj['grupo'], obj['seccion'],
                                            obj['dia'], obj['ingreso_programado'],
                                            obj['salida_programado'], obj['min_programado'],
                                            obj['ingreso_real'], obj['salida_real'],
                                            obj['min_trabajados'], obj['diff_ingreso'],
                                            obj['diff_salida'], obj['min_aprobados'],
                                            obj['min_noaprobados'], obj['min_retrasos'],
                                            obj['min_retrasos_tolerancia'], obj['min_faltas'],
                                            obj['min_abandono'], obj['ingreso_sinfichada'],
                                            obj['salida_sinfichada'], obj['ingreso_auto'],
                                            obj['salida_auto'], obj['numeroturno'],
                                            obj['ingreso_programado_descanso'],obj['salida_programado_descanso'],
                                            obj['min_programado_descanso'], obj['ingreso_real_descanso'],
                                            obj['salida_real_descanso'], obj['min_real_descanso'], obj['diff_ingreso_descanso'],
                                            obj['diff_salida_descanso'], obj['ingreso_programado_permiso1'], obj['salida_programado_permiso1'],
                                            obj['min_programado_permiso1'], obj['ingresoreal_permiso1'], obj['salidareal_permiso1'],
                                            obj['min_real_permiso1'], obj['diff_ingreso_permiso1'], obj['diff_salida_permiso1'],
                                            obj['dia_completo_permiso1'], obj['descuento_permiso1'], obj['ingreso_programado_permiso2'],
                                            obj['salida_programado_permiso2'], obj['min_programado_permiso2'], obj['ingresoreal_permiso2'],
                                            obj['salidareal_permiso2'], obj['min_real_permiso2'], obj['diff_ingreso_permiso2'], obj['diff_salida_permiso2'],
                                            obj['dia_completo_permiso2'], obj['descuento_permiso2'], obj['min_extra_programado'], obj['min_extra_real'],
                                            obj['nocturno'], obj['feriado'], obj['vacacion'], obj['horas_jornada'], obj['horas_semana'], obj['observacion'],
                                            obj['create_at'], obj['update_at']))
            
        return attendances

    def getAttendanceFromAPI(self,database,page) -> DataResponse:
        request=RequestHTTP(base_url=self.base_url)
        dataResponse=request.GET(self.attendances, params={ "database" : database , "page" : page },
                    headers={ "token" : self.api_token , "Accept" : "application/json" },
                    callback=self.callback)
        return dataResponse
    

    def callbackTotalPages(self,json_data):
        return int(json_data['last_page'])

    def getTotalPagesFromAPI(self,database):
        request=RequestHTTP(base_url=self.base_url)
        dataResponse=request.GET(self.attendances, params={ "database" : database , "page" : "1" },
                    headers={ "token" : self.api_token , "Accept" : "application/json" },
                    callback=self.callbackTotalPages)
        return dataResponse
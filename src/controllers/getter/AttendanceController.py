from data.getter.AttendanceData import AttendanceData
from config.Enviroment import Enviroment
from utils.ElasticSearchPDO import ElasticSearchPDO
from model.getter.Attendance import Attendance

class AttendanceController:
    def migrate():
        databases = int(Enviroment().getAPIDatabases())
        nameDatabases = Enviroment().getDatabaseNames()
        
        indexAttendance = 'AttendanceFacts'
        ElasticSearchPDO().create_index(index_name=indexAttendance)

        for numberDB in range(databases):
            totalPages = AttendanceData().getTotalPagesFromAPI(database=numberDB)
            for pageAttendance in range(totalPages):
                attendancesDataResponse = AttendanceData().getAttendanceFromAPI(database=numberDB,page=pageAttendance)

                if (attendancesDataResponse.status == True ):
                    attendances = list[Attendance]( attendancesDataResponse.getData() )

                    for att in attendances:
                        ElasticSearchPDO().create_document(index_name=indexAttendance, document={
                            "person_id": att.person_id,
                            "name_person": "",
                            "branch_id": "5678",
                            "branch_name": "Oficina Central",
                            "group_name": "Administración",
                            "section_name": "Recursos Humanos",
                            "company_id": "1",
                            "company_name": "Empresa ABC",
                            "date": "2024-11-01",
                            "day_of_week": "miércoles",
                            "minutos_trabajados": 450,
                            "minutos_programados": 480,
                            "minutos_extras": 30,
                            "minutos_retraso": 10,
                            "faltas": 0,
                            "turno_tipo": "Diurno",
                            "actividad_tipo": "Asistencia"
                        })
                else:
                    print('Error loading Attendance from API')
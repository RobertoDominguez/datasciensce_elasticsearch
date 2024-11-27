from data.getter.AttendanceData import AttendanceData
from data.getter.PersonData import PersonData
from data.getter.BranchData import BranchData
from data.getter.GroupData import GroupData
from data.getter.SectionData import SectionData

from config.Enviroment import Enviroment
from utils.ElasticSearchPDO import ElasticSearchPDO
from model.getter.Attendance import Attendance
from model.getter.Person import Person
from model.getter.Branch import Branch
from model.getter.Group import Group
from model.getter.Section import Section



class GetterController:

    def __init__(self):
        self.databases=int(Enviroment().getAPIDatabases())
        self.nameDatabases=Enviroment().getDatabaseNames()

    def migrate(self):
        #Fact
        indexAttendance = 'attendance_facts'
        
        #Dimensions
        indexPerson = 'person_dim'
        indexBranch = 'branch_dim'
        indexGroup = 'group_dim'
        indexSection = 'section_dim'


        ElasticSearchPDO().create_index(index_name=indexPerson)
        ElasticSearchPDO().create_index(index_name=indexBranch)
        ElasticSearchPDO().create_index(index_name=indexGroup)
        ElasticSearchPDO().create_index(index_name=indexSection)

        for numberDB in range(1,self.databases+1):
        #=============================PERSON==========================================================================
            totalPagesDR = PersonData().getTotalPagesFromAPI(numberDB)
            if (not totalPagesDR.status):
                print("Error loading total Pages (Person)")
                return
            
            for pagePerson in range(1,int(totalPagesDR.getData())+1):
                peopleDataResponse = PersonData().getPersonFromAPI(database=numberDB, page=pagePerson)

                if (not peopleDataResponse.status):
                    print('Error loading Person from API')

                people = list[Person]( peopleDataResponse.getData() )

                for person in people:
                    ElasticSearchPDO().create_document(index_name=indexPerson, doc_id=str(numberDB)+'_'+str(person.id) ,document={
                        "code": person.code,
                        "first_name": person.first_name,
                        "last_name": person.last_name,
                        "ci": person.ci,
                        "position": person.position,
                        "gender": person.gender,
                        "birthdate": person.birth_date,
                        "address": person.address,
                        "phone": person.phone,
                        "email": person.email
                    })
                    print("(Person) Document created"+str(numberDB)+'_'+str(person.id))
                
        #=============================BRANCH==========================================================================
            totalPagesDR = BranchData().getTotalPagesFromAPI(numberDB)
            if (not totalPagesDR.status):
                print("Error loading total Pages (Branch)")
                return
            
            for pageBranch in range(1,int(totalPagesDR.getData())+1):
                branchesDataResponse = BranchData().getBranchFromAPI(database=numberDB, page=pageBranch)

                if (not branchesDataResponse.status):
                    print('Error loading Branch from API')

                branches = list[Branch]( branchesDataResponse.getData() )

                for branch in branches:
                    ElasticSearchPDO().create_document(index_name=indexBranch, doc_id=str(numberDB)+'_'+str(branch.id) ,document={
                        "code": branch.code,
                        "name": branch.name,
                        "locality": branch.locality,
                        "province": branch.province,
                        "departament": branch.department
                    })
                    print("(Branch) Document created"+str(numberDB)+'_'+str(person.id))

        #=============================GROUP==========================================================================
            totalPagesDR = GroupData().getTotalPagesFromAPI(numberDB)
            if (not totalPagesDR.status):
                print("Error loading total Pages (Group)")
                return
            
            for pageGroup in range(1,int(totalPagesDR.getData())+1):
                groupsDataResponse = GroupData().getGroupFromAPI(database=numberDB, page=pageGroup)

                if (not groupsDataResponse.status):
                    print('Error loading Group from API')

                groups = list[Group]( groupsDataResponse.getData() )

                for group in groups:
                    ElasticSearchPDO().create_document(index_name=indexGroup, doc_id=str(numberDB)+'_'+str(group.id) ,document={
                        "name": group.name,
                        "locality": group.locality,
                        "province": group.province,
                        "departament": group.department
                    })
                    print("(Group) Document created"+str(numberDB)+'_'+str(group.id))


        #=============================SECTION==========================================================================
            totalPagesDR = SectionData().getTotalPagesFromAPI(numberDB)
            if (not totalPagesDR.status):
                print("Error loading total Pages (Section)")
                return
            
            for pageSection in range(1,int(totalPagesDR.getData())+1):
                sectionsDataResponse = SectionData().getSectionFromAPI(database=numberDB, page=pageSection)

                if (not sectionsDataResponse.status):
                    print('Error loading Section from API')

                sections = list[Section]( sectionsDataResponse.getData() )

                for section in sections:
                    ElasticSearchPDO().create_document(index_name=indexSection, doc_id=str(numberDB)+'_'+str(section.id) ,document={
                        "name": section.name,
                        "locality": section.locality,
                        "province": section.province,
                        "departament": section.department
                    })
                    print("(Section) Document created"+str(numberDB)+'_'+str(section.id))



        # Migration Attendance Fact
        ElasticSearchPDO().create_index(index_name=indexAttendance)

        for numberDB in range(1,self.databases+1):
            totalPagesDR = AttendanceData().getTotalPagesFromAPI(database=numberDB)

            if (not totalPagesDR.status):
                print("Error loading total Pages (Attendance)")
                return

            for pageAttendance in range(1,int(totalPagesDR.getData())+1):
                attendancesDataResponse = AttendanceData().getAttendanceFromAPI(database=numberDB,page=pageAttendance)

                if (not attendancesDataResponse.status):
                    print('Error loading Attendance from API')
                    return
                
                attendances = list[Attendance]( attendancesDataResponse.getData() )

                for att in attendances:

                    personES=ElasticSearchPDO().get_document(index_name=indexPerson, doc_id=str(numberDB)+'_'+str(att.person_id))
                    branchES=ElasticSearchPDO().search(index_name=indexBranch, query={"match": {"name": str(att.branch)}})
                    groupES=ElasticSearchPDO().search(index_name=indexGroup, query={"match": {"name": str(att.group)}})
                    sectionES=ElasticSearchPDO().search(index_name=indexSection, query={"match": {"name": str(att.section)}})

                    documentAttendance=dict[str,any]({
                        #Attendance Data
                        "entry": att.actual_entry, #only time
                        "exit": att.actual_exit, #only time
                        "worked_minutes": att.worked_minutes,
                        "entry_difference": att.entry_difference,
                        "exit_difference": att.exit_difference,
                        "approved_minutes": att.approved_minutes,
                        "unapproved_minutes": att.unapproved_minutes,
                        "late_minutes": att.late_minutes,
                        "abandon_minutes": att.abandon_minutes,
                        "no_entry_stamp": att.no_entry_stamp,
                        "no_exit_stamp": att.no_exit_stamp,

                        #Schedule Data
                        "scheduled_entry": att.scheduled_entry,
                        "scheduled_exit": att.scheduled_exit,
                        "scheduled_minutes": att.scheduled_minutes,

                        #Company Data
                        "company_name": self.nameDatabases[str(numberDB)],

                        #Time Data
                        "date": att.date[:10],
                        "year": att.date[:4],
                        "month": att.date[5:7],
                        "day": att.date[8:10],
                        "day_of_week": att.day,
                        "is_holiday": att.holiday,
                        "is_weekend": 0,

                        #Event Data
                        "event_description": 'Work',

                        #Person Data
                        "code": personES['code'],
                        "first_name": personES['first_name'],
                        "last_name": personES['last_name'],
                        "ci": personES['ci'],
                        "position": personES['position'],
                        "gender": personES['gender'],
                        "birthdate": personES['birthdate'],
                        "address": personES['address'],
                        "phone": personES['phone'],
                        "email": personES['email']
                    })

                    if (int(branchES['hits']['total']['value'])==1):
                        documentAttendance.update({
                            "branch_code": branchES['hits']['hits'][0]['_source']['code'],
                            "branch_name": branchES['hits']['hits'][0]['_source']['name'],
                            "branch_locality": branchES['hits']['hits'][0]['_source']['locality'],
                            "branch_province": branchES['hits']['hits'][0]['_source']['province'],
                            "branch_departament": branchES['hits']['hits'][0]['_source']['departament']
                        })

                    if (int(groupES['hits']['total']['value'])==1):
                        documentAttendance.update({
                            "group_name": groupES['hits']['hits'][0]['_source']['name'],
                            "group_locality": groupES['hits']['hits'][0]['_source']['locality'],
                            "group_province": groupES['hits']['hits'][0]['_source']['province'],
                            "group_departament": groupES['hits']['hits'][0]['_source']['departament']
                        })

                    if (int(sectionES['hits']['total']['value'])==1):
                        documentAttendance.update({
                            "section_name": sectionES['hits']['hits'][0]['_source']['name'],
                            "section_locality": sectionES['hits']['hits'][0]['_source']['locality'],
                            "section_province": sectionES['hits']['hits'][0]['_source']['province'],
                            "section_departament": sectionES['hits']['hits'][0]['_source']['departament']
                        })

                    ElasticSearchPDO().create_document(index_name=indexAttendance, doc_id=str(numberDB)+'_'+str(att.id), document=documentAttendance)
                    print("(Attendance) Document created"+str(numberDB)+'_'+str(att.id))

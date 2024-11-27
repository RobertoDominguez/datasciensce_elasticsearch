from data.getter.AttendanceData import AttendanceData

# This file inserts the data obtained by the API Service to Elasticsearch

AttendanceData().getAttendanceFromAPI(1,1)
dr=AttendanceData().getTotalPagesAttendanceFromAPI(1)
print(dr.getData())
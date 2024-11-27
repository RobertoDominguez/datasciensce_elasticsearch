class DataResponse:
    def __init__(self, data, status, code, message, headers=None):
        self.data = data  # datos de la respuesta
        self.status = status  # estado de la petición ("success" o "error")
        self.code = code  # código de respuesta HTTP
        self.message=message
        self.headers = headers  # encabezados de la respuesta (opcional)

    def setStatus(self,_status):
        self.status=_status
    
    def getData(self):
        return self.data
    
    def setData(self,_data):
        self.data=_data
    
    def setMessage(self,_message):
        self.message=_message
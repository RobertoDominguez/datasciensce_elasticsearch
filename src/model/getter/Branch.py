# Sucursal
class Branch:
    def __init__(self, id, code, name, address, phone, description, locality, province, department, created_at, updated_at):
        self.id = id  # id
        self.code = code  # codigo
        self.name = name  # nombre
        self.address = address  # direccion
        self.phone = phone  # telefono
        self.description = description  # descripcion
        self.locality = locality  # localidad
        self.province = province  # provincia
        self.department = department  # departamento
        self.created_at = created_at  # created_at
        self.updated_at = updated_at  # updated_at

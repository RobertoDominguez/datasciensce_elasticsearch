# Grupo
class Group:
    def __init__(self, id, name, description, locality, province, department, created_at, updated_at):
        self.id = id  # id
        self.name = name  # nombre
        self.description = description  # descripcion
        self.locality = locality  # localidad
        self.province = province  # provincia
        self.department = department  # departamento
        self.created_at = created_at  # created_at
        self.updated_at = updated_at  # updated_at

# Persona
class Person:
    def __init__(self, id, code, item_number, first_name, last_name, ci, profession, birth_date,
                 gender, position, address, phone, email, marital_status, basic_salary, clothing_size,
                 resume_file, locality, province, department, insurance_number, nationality, status,
                 others, created_at, updated_at, branches, groups, sections):
        
        self.id = id  # id
        self.code = code  # codigo
        self.item_number = item_number  # numero_item
        self.first_name = first_name  # nombres
        self.last_name = last_name  # apellidos
        self.ci = ci  # ci
        self.profession = profession  # profesion
        self.birth_date = birth_date  # fecha_nacimiento
        self.gender = gender  # sexo
        self.position = position  # cargo
        self.address = address  # direccion
        self.phone = phone  # telefono
        self.email = email  # email
        self.marital_status = marital_status  # estado_civil
        self.basic_salary = basic_salary  # haber_basico
        self.clothing_size = clothing_size  # talla_ropa
        self.resume_file = resume_file  # file_curriculum
        self.locality = locality  # localidad
        self.province = province  # provincia
        self.department = department  # departamento
        self.insurance_number = insurance_number  # numero_seguro
        self.nationality = nationality  # nacionalidad
        self.status = status  # estado
        self.others = others  # otros
        self.created_at = created_at  # created_at
        self.updated_at = updated_at  # updated_at
        self.branches = branches  # sucursales
        self.groups = groups  # grupos
        self.sections = sections  # secciones

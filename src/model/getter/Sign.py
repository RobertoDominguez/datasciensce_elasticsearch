# Marcacion
class Sign:
    def __init__(self, id, branch_id, authorizer_id, code, date, event, hostname, ip, manual, used, created_at, updated_at):
        self.id = id  # id
        self.branch_id = branch_id  # id_sucursal
        self.authorizer_id = authorizer_id  # id_autoriza
        self.code = code  # codigo
        self.date = date  # fecha
        self.event = event  # evento
        self.hostname = hostname  # hostname
        self.ip = ip  # ip
        self.manual = manual  # manual
        self.used = used  # usado
        self.created_at = created_at  # created_at
        self.updated_at = updated_at  # updated_at

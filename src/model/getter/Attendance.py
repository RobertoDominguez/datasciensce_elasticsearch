# Asistencia
class Attendance:
    def __init__(self, id, aux_code, person_id, date, code, name, branch, group, section, day,
                 scheduled_entry, scheduled_exit, scheduled_minutes, actual_entry, actual_exit,
                 worked_minutes, entry_difference, exit_difference, approved_minutes, 
                 unapproved_minutes, late_minutes, tolerated_late_minutes, absent_minutes, 
                 abandon_minutes, no_entry_stamp, no_exit_stamp, auto_entry, auto_exit, 
                 shift_number, scheduled_break_entry, scheduled_break_exit, scheduled_break_minutes, 
                 actual_break_entry, actual_break_exit, actual_break_minutes, break_entry_difference, 
                 break_exit_difference, scheduled_leave_entry1, scheduled_leave_exit1, 
                 scheduled_leave_minutes1, actual_leave_entry1, actual_leave_exit1, 
                 actual_leave_minutes1, leave_entry_difference1, leave_exit_difference1, 
                 full_day_leave1, leave_discount1, scheduled_leave_entry2, scheduled_leave_exit2, 
                 scheduled_leave_minutes2, actual_leave_entry2, actual_leave_exit2, 
                 actual_leave_minutes2, leave_entry_difference2, leave_exit_difference2, 
                 full_day_leave2, leave_discount2, scheduled_extra_minutes, actual_extra_minutes, 
                 night_shift, holiday, vacation, work_hours_day, work_hours_week, 
                 observation, created_at, updated_at):
        
        self.id = id  # id
        self.aux_code = aux_code  # codigo_aux
        self.person_id = person_id  # id_persona
        self.date = date  # fecha
        self.code = code  # codigo
        self.name = name  # nombre
        self.branch = branch  # sucursal
        self.group = group  # grupo
        self.section = section  # seccion
        self.day = day  # dia
        self.scheduled_entry = scheduled_entry  # ingreso_programado
        self.scheduled_exit = scheduled_exit  # salida_programado
        self.scheduled_minutes = scheduled_minutes  # min_programado
        self.actual_entry = actual_entry  # ingreso_real
        self.actual_exit = actual_exit  # salida_real
        self.worked_minutes = worked_minutes  # min_trabajados
        self.entry_difference = entry_difference  # diff_ingreso
        self.exit_difference = exit_difference  # diff_salida
        self.approved_minutes = approved_minutes  # min_aprobados
        self.unapproved_minutes = unapproved_minutes  # min_noaprobados
        self.late_minutes = late_minutes  # min_retrasos
        self.tolerated_late_minutes = tolerated_late_minutes  # min_retrasos_tolerancia
        self.absent_minutes = absent_minutes  # min_faltas
        self.abandon_minutes = abandon_minutes  # min_abandono
        self.no_entry_stamp = no_entry_stamp  # ingreso_sinfichada
        self.no_exit_stamp = no_exit_stamp  # salida_sinfichada
        self.auto_entry = auto_entry  # ingreso_auto
        self.auto_exit = auto_exit  # salida_auto
        self.shift_number = shift_number  # numeroturno
        self.scheduled_break_entry = scheduled_break_entry  # ingreso_programado_descanso
        self.scheduled_break_exit = scheduled_break_exit  # salida_programado_descanso
        self.scheduled_break_minutes = scheduled_break_minutes  # min_programado_descanso
        self.actual_break_entry = actual_break_entry  # ingreso_real_descanso
        self.actual_break_exit = actual_break_exit  # salida_real_descanso
        self.actual_break_minutes = actual_break_minutes  # min_real_descanso
        self.break_entry_difference = break_entry_difference  # diff_ingreso_descanso
        self.break_exit_difference = break_exit_difference  # diff_salida_descanso
        self.scheduled_leave_entry1 = scheduled_leave_entry1  # ingreso_programado_permiso1
        self.scheduled_leave_exit1 = scheduled_leave_exit1  # salida_programado_permiso1
        self.scheduled_leave_minutes1 = scheduled_leave_minutes1  # min_programado_permiso1
        self.actual_leave_entry1 = actual_leave_entry1  # ingresoreal_permiso1
        self.actual_leave_exit1 = actual_leave_exit1  # salidareal_permiso1
        self.actual_leave_minutes1 = actual_leave_minutes1  # min_real_permiso1
        self.leave_entry_difference1 = leave_entry_difference1  # diff_ingreso_permiso1
        self.leave_exit_difference1 = leave_exit_difference1  # diff_salida_permiso1
        self.full_day_leave1 = full_day_leave1  # dia_completo_permiso1
        self.leave_discount1 = leave_discount1  # descuento_permiso1
        self.scheduled_leave_entry2 = scheduled_leave_entry2  # ingreso_programado_permiso2
        self.scheduled_leave_exit2 = scheduled_leave_exit2  # salida_programado_permiso2
        self.scheduled_leave_minutes2 = scheduled_leave_minutes2  # min_programado_permiso2
        self.actual_leave_entry2 = actual_leave_entry2  # ingresoreal_permiso2
        self.actual_leave_exit2 = actual_leave_exit2  # salidareal_permiso2
        self.actual_leave_minutes2 = actual_leave_minutes2  # min_real_permiso2
        self.leave_entry_difference2 = leave_entry_difference2  # diff_ingreso_permiso2
        self.leave_exit_difference2 = leave_exit_difference2  # diff_salida_permiso2
        self.full_day_leave2 = full_day_leave2  # dia_completo_permiso2
        self.leave_discount2 = leave_discount2  # descuento_permiso2
        self.scheduled_extra_minutes = scheduled_extra_minutes  # min_extra_programado
        self.actual_extra_minutes = actual_extra_minutes  # min_extra_real
        self.night_shift = night_shift  # nocturno
        self.holiday = holiday  # feriado
        self.vacation = vacation  # vacacion
        self.work_hours_day = work_hours_day  # horas_jornada
        self.work_hours_week = work_hours_week  # horas_semana
        self.observation = observation  # observacion
        self.created_at = created_at  # create_at
        self.updated_at = updated_at  # update_at

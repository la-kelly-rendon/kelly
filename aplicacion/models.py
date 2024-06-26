from django.db import models


class Alumno(models.Model):
    id_a = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=45, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    id_curso2 = models.ForeignKey('Curso', models.DO_NOTHING, db_column='id_curso2', blank=True, null=True)
    cod_mat = models.ForeignKey('Matricula', models.DO_NOTHING, db_column='cod_mat', blank=True, null=True)
    
    def __str__(self):
        return self.nom
    

    class Meta:
        managed = False
        db_table = 'alumno'


class Asignatura(models.Model):
    id_asig = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignatura'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Curso(models.Model):
    id_curso = models.IntegerField(primary_key=True)
    grado_curso = models.CharField(max_length=15, blank=True, null=True)
    num_aula = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curso'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HorarioDetalle(models.Model):
    hora_ini = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    dia = models.CharField(max_length=10, blank=True, null=True)
    id_curso1 = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso1', blank=True, null=True)
    id_asig1 = models.ForeignKey(Asignatura, models.DO_NOTHING, db_column='id_asig1', blank=True, null=True)
    cod_h = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'horario_detalle'


class Matricula(models.Model):
    cod_mat = models.IntegerField(primary_key=True)
    fecha_mat = models.DateField(blank=True, null=True)
    costo = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matricula'


class ProfeCurso(models.Model):
    id_curso3 = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso3', blank=True, null=True)
    id_profe2 = models.ForeignKey('Profesor', models.DO_NOTHING, db_column='id_profe2', blank=True, null=True)
    cod = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'profe_curso'


class Profesor(models.Model):
    id_profe = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    apellido = models.CharField(max_length=45, blank=True, null=True)
    profesion = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesor'
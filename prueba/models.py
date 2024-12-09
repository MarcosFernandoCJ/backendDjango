from django.db import models

# Create your models here.
class Careers(models.Model):
    department = models.ForeignKey('Departments', models.DO_NOTHING, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'careers'


class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Events(models.Model):
    max_participants_group = models.IntegerField()
    status_event = models.TextField()  # This field type is a guess.
    end_date = models.DateTimeField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    organizador = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    img_event = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class GroupEvents(models.Model):
    department = models.ForeignKey(Departments, models.DO_NOTHING)
    event = models.ForeignKey(Events, models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_events'


class Inscriptions(models.Model):
    event = models.ForeignKey(Events, models.DO_NOTHING, blank=True, null=True)
    fecha_inscripcion = models.DateTimeField(blank=True, null=True)
    group_event = models.ForeignKey(GroupEvents, models.DO_NOTHING, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscriptions'


class Jurys(models.Model):
    event = models.ForeignKey(Events, models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'jurys'


class Roles(models.Model):
    name = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'
        
    
    def __str__(self):
        return self.name
    


class Scores(models.Model):
    score = models.IntegerField()
    fecha_puntaje = models.DateTimeField(blank=True, null=True)
    group_event = models.ForeignKey(GroupEvents, models.DO_NOTHING)
    id = models.BigAutoField(primary_key=True)
    jury = models.ForeignKey(Jurys, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scores'


class UserRoles(models.Model):
    role = models.OneToOneField(Roles, models.DO_NOTHING, primary_key=True)  # The composite primary key (role_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_roles'
        unique_together = (('role', 'user'),)


class Users(models.Model):
    career = models.ForeignKey(Careers, models.DO_NOTHING, blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'users'
        
    def __str__(self):
        return self.username

    
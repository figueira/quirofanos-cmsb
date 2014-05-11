# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cuenta'
        db.create_table(u'quirofanos_cmsb_cuenta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('privilegio', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('clave_inicial', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Cuenta'])

        # Adding model 'Medico'
        db.create_table(u'quirofanos_cmsb_medico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cuenta', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quirofanos_cmsb.Cuenta'], unique=True, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cedula', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('especializacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Medico'])

        # Adding model 'Departamento'
        db.create_table(u'quirofanos_cmsb_departamento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cuenta', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quirofanos_cmsb.Cuenta'], unique=True, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Departamento'])

        # Adding model 'Quirofano'
        db.create_table(u'quirofanos_cmsb_quirofano', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Quirofano'])

        # Adding model 'MaterialQuirurgico'
        db.create_table(u'quirofanos_cmsb_materialquirurgico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['MaterialQuirurgico'])

        # Adding model 'ServicioOperatorio'
        db.create_table(u'quirofanos_cmsb_serviciooperatorio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['ServicioOperatorio'])

        # Adding model 'EquipoEspecial'
        db.create_table(u'quirofanos_cmsb_equipoespecial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['EquipoEspecial'])

        # Adding model 'SistemaCorporal'
        db.create_table(u'quirofanos_cmsb_sistemacorporal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_icd_10_pcs', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['SistemaCorporal'])

        # Adding model 'TipoProcedimientoQuirurgico'
        db.create_table(u'quirofanos_cmsb_tipoprocedimientoquirurgico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_icd_10_pcs', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['TipoProcedimientoQuirurgico'])

        # Adding model 'OrganoCorporal'
        db.create_table(u'quirofanos_cmsb_organocorporal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_icd_10_pcs', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('sistema_corporal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.SistemaCorporal'])),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['OrganoCorporal'])

        # Adding M2M table for field tipos_procedimientos_permitidos on 'OrganoCorporal'
        m2m_table_name = db.shorten_name(u'quirofanos_cmsb_organocorporal_tipos_procedimientos_permitidos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organocorporal', models.ForeignKey(orm[u'quirofanos_cmsb.organocorporal'], null=False)),
            ('tipoprocedimientoquirurgico', models.ForeignKey(orm[u'quirofanos_cmsb.tipoprocedimientoquirurgico'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organocorporal_id', 'tipoprocedimientoquirurgico_id'])

        # Adding model 'CompaniaAseguradora'
        db.create_table(u'quirofanos_cmsb_companiaaseguradora', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['CompaniaAseguradora'])

        # Adding model 'Paciente'
        db.create_table(u'quirofanos_cmsb_paciente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cedula', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('compania_aseguradora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.CompaniaAseguradora'], null=True, blank=True)),
            ('area_ingreso', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('numero_expediente', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('numero_habitacion', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('diagnostico_ingreso', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Paciente'])

        # Adding M2M table for field servicios_operatorios_requeridos on 'Paciente'
        m2m_table_name = db.shorten_name(u'quirofanos_cmsb_paciente_servicios_operatorios_requeridos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('paciente', models.ForeignKey(orm[u'quirofanos_cmsb.paciente'], null=False)),
            ('serviciooperatorio', models.ForeignKey(orm[u'quirofanos_cmsb.serviciooperatorio'], null=False))
        ))
        db.create_unique(m2m_table_name, ['paciente_id', 'serviciooperatorio_id'])

        # Adding model 'IntervencionQuirurgica'
        db.create_table(u'quirofanos_cmsb_intervencionquirurgica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_intervencion', self.gf('django.db.models.fields.DateField')()),
            ('hora_inicio', self.gf('django.db.models.fields.TimeField')()),
            ('hora_fin', self.gf('django.db.models.fields.TimeField')()),
            ('duracion', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=2)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('preferencia_anestesica', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('riesgo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('razon_riesgo', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('paciente', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quirofanos_cmsb.Paciente'], unique=True)),
            ('quirofano', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.Quirofano'])),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['IntervencionQuirurgica'])

        # Adding M2M table for field materiales_quirurgicos_requeridos on 'IntervencionQuirurgica'
        m2m_table_name = db.shorten_name(u'quirofanos_cmsb_intervencionquirurgica_materiales_quirurgicos_requeridos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('intervencionquirurgica', models.ForeignKey(orm[u'quirofanos_cmsb.intervencionquirurgica'], null=False)),
            ('materialquirurgico', models.ForeignKey(orm[u'quirofanos_cmsb.materialquirurgico'], null=False))
        ))
        db.create_unique(m2m_table_name, ['intervencionquirurgica_id', 'materialquirurgico_id'])

        # Adding M2M table for field equipos_especiales_requeridos on 'IntervencionQuirurgica'
        m2m_table_name = db.shorten_name(u'quirofanos_cmsb_intervencionquirurgica_equipos_especiales_requeridos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('intervencionquirurgica', models.ForeignKey(orm[u'quirofanos_cmsb.intervencionquirurgica'], null=False)),
            ('equipoespecial', models.ForeignKey(orm[u'quirofanos_cmsb.equipoespecial'], null=False))
        ))
        db.create_unique(m2m_table_name, ['intervencionquirurgica_id', 'equipoespecial_id'])

        # Adding model 'ProcedimientoQuirurgico'
        db.create_table(u'quirofanos_cmsb_procedimientoquirurgico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('intervencion_quirurgica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.IntervencionQuirurgica'], null=True, blank=True)),
            ('tipo_procedimiento_quirurgico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.TipoProcedimientoQuirurgico'])),
            ('organo_corporal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.OrganoCorporal'])),
            ('monto_honorarios_cirujano_principal', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['ProcedimientoQuirurgico'])

        # Adding model 'Participacion'
        db.create_table(u'quirofanos_cmsb_participacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('procedimiento_quirurgico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.ProcedimientoQuirurgico'])),
            ('medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.Medico'])),
            ('rol', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('monto_honorarios', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Participacion'])

        # Adding model 'Reservacion'
        db.create_table(u'quirofanos_cmsb_reservacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_reservacion', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(default='00000', unique=True, max_length=10)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('tipo_solicitud', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('dias_hospitalizacion', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.Medico'])),
            ('intervencion_quirurgica', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quirofanos_cmsb.IntervencionQuirurgica'], unique=True)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Reservacion'])


    def backwards(self, orm):
        # Deleting model 'Cuenta'
        db.delete_table(u'quirofanos_cmsb_cuenta')

        # Deleting model 'Medico'
        db.delete_table(u'quirofanos_cmsb_medico')

        # Deleting model 'Departamento'
        db.delete_table(u'quirofanos_cmsb_departamento')

        # Deleting model 'Quirofano'
        db.delete_table(u'quirofanos_cmsb_quirofano')

        # Deleting model 'MaterialQuirurgico'
        db.delete_table(u'quirofanos_cmsb_materialquirurgico')

        # Deleting model 'ServicioOperatorio'
        db.delete_table(u'quirofanos_cmsb_serviciooperatorio')

        # Deleting model 'EquipoEspecial'
        db.delete_table(u'quirofanos_cmsb_equipoespecial')

        # Deleting model 'SistemaCorporal'
        db.delete_table(u'quirofanos_cmsb_sistemacorporal')

        # Deleting model 'TipoProcedimientoQuirurgico'
        db.delete_table(u'quirofanos_cmsb_tipoprocedimientoquirurgico')

        # Deleting model 'OrganoCorporal'
        db.delete_table(u'quirofanos_cmsb_organocorporal')

        # Removing M2M table for field tipos_procedimientos_permitidos on 'OrganoCorporal'
        db.delete_table(db.shorten_name(u'quirofanos_cmsb_organocorporal_tipos_procedimientos_permitidos'))

        # Deleting model 'CompaniaAseguradora'
        db.delete_table(u'quirofanos_cmsb_companiaaseguradora')

        # Deleting model 'Paciente'
        db.delete_table(u'quirofanos_cmsb_paciente')

        # Removing M2M table for field servicios_operatorios_requeridos on 'Paciente'
        db.delete_table(db.shorten_name(u'quirofanos_cmsb_paciente_servicios_operatorios_requeridos'))

        # Deleting model 'IntervencionQuirurgica'
        db.delete_table(u'quirofanos_cmsb_intervencionquirurgica')

        # Removing M2M table for field materiales_quirurgicos_requeridos on 'IntervencionQuirurgica'
        db.delete_table(db.shorten_name(u'quirofanos_cmsb_intervencionquirurgica_materiales_quirurgicos_requeridos'))

        # Removing M2M table for field equipos_especiales_requeridos on 'IntervencionQuirurgica'
        db.delete_table(db.shorten_name(u'quirofanos_cmsb_intervencionquirurgica_equipos_especiales_requeridos'))

        # Deleting model 'ProcedimientoQuirurgico'
        db.delete_table(u'quirofanos_cmsb_procedimientoquirurgico')

        # Deleting model 'Participacion'
        db.delete_table(u'quirofanos_cmsb_participacion')

        # Deleting model 'Reservacion'
        db.delete_table(u'quirofanos_cmsb_reservacion')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quirofanos_cmsb.companiaaseguradora': {
            'Meta': {'object_name': 'CompaniaAseguradora'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quirofanos_cmsb.cuenta': {
            'Meta': {'object_name': 'Cuenta'},
            'clave_inicial': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'privilegio': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'quirofanos_cmsb.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'cuenta': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quirofanos_cmsb.Cuenta']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'})
        },
        u'quirofanos_cmsb.equipoespecial': {
            'Meta': {'object_name': 'EquipoEspecial'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quirofanos_cmsb.intervencionquirurgica': {
            'Meta': {'object_name': 'IntervencionQuirurgica'},
            'duracion': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '4', 'decimal_places': '2'}),
            'equipos_especiales_requeridos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['quirofanos_cmsb.EquipoEspecial']", 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_intervencion': ('django.db.models.fields.DateField', [], {}),
            'hora_fin': ('django.db.models.fields.TimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales_quirurgicos_requeridos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['quirofanos_cmsb.MaterialQuirurgico']", 'null': 'True', 'blank': 'True'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quirofanos_cmsb.Paciente']", 'unique': 'True'}),
            'preferencia_anestesica': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'quirofano': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.Quirofano']"}),
            'razon_riesgo': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'riesgo': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'quirofanos_cmsb.materialquirurgico': {
            'Meta': {'object_name': 'MaterialQuirurgico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quirofanos_cmsb.medico': {
            'Meta': {'object_name': 'Medico'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'cuenta': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quirofanos_cmsb.Cuenta']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'especializacion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'})
        },
        u'quirofanos_cmsb.organocorporal': {
            'Meta': {'object_name': 'OrganoCorporal'},
            'codigo_icd_10_pcs': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sistema_corporal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.SistemaCorporal']"}),
            'tipos_procedimientos_permitidos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quirofanos_cmsb.TipoProcedimientoQuirurgico']", 'symmetrical': 'False'})
        },
        u'quirofanos_cmsb.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'area_ingreso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'compania_aseguradora': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.CompaniaAseguradora']", 'null': 'True', 'blank': 'True'}),
            'diagnostico_ingreso': ('django.db.models.fields.TextField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numero_expediente': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'numero_habitacion': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'servicios_operatorios_requeridos': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['quirofanos_cmsb.ServicioOperatorio']", 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'quirofanos_cmsb.participacion': {
            'Meta': {'object_name': 'Participacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.Medico']"}),
            'monto_honorarios': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '15', 'decimal_places': '2'}),
            'procedimiento_quirurgico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.ProcedimientoQuirurgico']"}),
            'rol': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'quirofanos_cmsb.procedimientoquirurgico': {
            'Meta': {'object_name': 'ProcedimientoQuirurgico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervencion_quirurgica': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.IntervencionQuirurgica']", 'null': 'True', 'blank': 'True'}),
            'medicos_participantes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quirofanos_cmsb.Medico']", 'through': u"orm['quirofanos_cmsb.Participacion']", 'symmetrical': 'False'}),
            'monto_honorarios_cirujano_principal': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '2'}),
            'organo_corporal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.OrganoCorporal']"}),
            'tipo_procedimiento_quirurgico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.TipoProcedimientoQuirurgico']"})
        },
        u'quirofanos_cmsb.quirofano': {
            'Meta': {'object_name': 'Quirofano'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {})
        },
        u'quirofanos_cmsb.reservacion': {
            'Meta': {'object_name': 'Reservacion'},
            'codigo': ('django.db.models.fields.CharField', [], {'default': "'00000'", 'unique': 'True', 'max_length': '10'}),
            'dias_hospitalizacion': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_reservacion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervencion_quirurgica': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quirofanos_cmsb.IntervencionQuirurgica']", 'unique': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.Medico']"}),
            'tipo_solicitud': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'quirofanos_cmsb.serviciooperatorio': {
            'Meta': {'object_name': 'ServicioOperatorio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quirofanos_cmsb.sistemacorporal': {
            'Meta': {'object_name': 'SistemaCorporal'},
            'codigo_icd_10_pcs': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'quirofanos_cmsb.tipoprocedimientoquirurgico': {
            'Meta': {'object_name': 'TipoProcedimientoQuirurgico'},
            'codigo_icd_10_pcs': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['quirofanos_cmsb']
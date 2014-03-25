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
            ('nombre_usuario', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('contrasena', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('privilegio', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('fecha_creacion', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Cuenta'])

        # Adding model 'Especializacion'
        db.create_table(u'quirofanos_cmsb_especializacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Especializacion'])

        # Adding model 'Medico'
        db.create_table(u'quirofanos_cmsb_medico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cuenta', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quirofanos_cmsb.Cuenta'], unique=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cedula', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Medico'])

        # Adding M2M table for field especializaciones on 'Medico'
        m2m_table_name = db.shorten_name(u'quirofanos_cmsb_medico_especializaciones')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('medico', models.ForeignKey(orm[u'quirofanos_cmsb.medico'], null=False)),
            ('especializacion', models.ForeignKey(orm[u'quirofanos_cmsb.especializacion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['medico_id', 'especializacion_id'])

        # Adding model 'MedicoTratante'
        db.create_table(u'quirofanos_cmsb_medicotratante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('medico', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quirofanos_cmsb.Medico'], unique=True)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['MedicoTratante'])

        # Adding model 'Departamento'
        db.create_table(u'quirofanos_cmsb_departamento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cuenta', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quirofanos_cmsb.Cuenta'], unique=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Departamento'])

        # Adding model 'Quirofano'
        db.create_table(u'quirofanos_cmsb_quirofano', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.IntegerField')()),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Quirofano'])

        # Adding model 'MaterialQuirurgico'
        db.create_table(u'quirofanos_cmsb_materialquirurgico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['MaterialQuirurgico'])

        # Adding model 'ServicioOperatorio'
        db.create_table(u'quirofanos_cmsb_serviciooperatorio', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['ServicioOperatorio'])

        # Adding model 'EquipoEspecial'
        db.create_table(u'quirofanos_cmsb_equipoespecial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['EquipoEspecial'])

        # Adding model 'TipoIntervencionQuirurgica'
        db.create_table(u'quirofanos_cmsb_tipointervencionquirurgica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['TipoIntervencionQuirurgica'])

        # Adding model 'Paciente'
        db.create_table(u'quirofanos_cmsb_paciente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cedula', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('numero_expediente', self.gf('django.db.models.fields.IntegerField')(unique=True, max_length=5, blank=True)),
            ('numero_habitacion', self.gf('django.db.models.fields.CharField')(max_length=5, blank=True)),
            ('numero_inscripcion_medico', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10, blank=True)),
            ('diagnostico_ingreso', self.gf('django.db.models.fields.TextField')()),
            ('familiar_medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.Medico'], blank=True)),
            ('parentezco_familiar_medico', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
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
            ('duracion', self.gf('django.db.models.fields.DecimalField')(max_digits=2, decimal_places=2)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('preferencia_anestesica', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('observaciones', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('riesgo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('razon_riesgo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('paciente', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quirofanos_cmsb.Paciente'], unique=True)),
            ('tipo_intervencion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.TipoIntervencionQuirurgica'])),
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

        # Adding model 'Participacion'
        db.create_table(u'quirofanos_cmsb_participacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('intervencion_quirurgica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.IntervencionQuirurgica'])),
            ('medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.Medico'])),
            ('rol', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Participacion'])

        # Adding model 'Reservacion'
        db.create_table(u'quirofanos_cmsb_reservacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_reservacion', self.gf('django.db.models.fields.DateField')(auto_now=True, auto_now_add=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('tipo_solicitud', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('dias_hospitalizacion', self.gf('django.db.models.fields.IntegerField')()),
            ('medico', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quirofanos_cmsb.MedicoTratante'])),
            ('intervencion_quirurgica', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['quirofanos_cmsb.IntervencionQuirurgica'], unique=True)),
        ))
        db.send_create_signal(u'quirofanos_cmsb', ['Reservacion'])


    def backwards(self, orm):
        # Deleting model 'Cuenta'
        db.delete_table(u'quirofanos_cmsb_cuenta')

        # Deleting model 'Especializacion'
        db.delete_table(u'quirofanos_cmsb_especializacion')

        # Deleting model 'Medico'
        db.delete_table(u'quirofanos_cmsb_medico')

        # Removing M2M table for field especializaciones on 'Medico'
        db.delete_table(db.shorten_name(u'quirofanos_cmsb_medico_especializaciones'))

        # Deleting model 'MedicoTratante'
        db.delete_table(u'quirofanos_cmsb_medicotratante')

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

        # Deleting model 'TipoIntervencionQuirurgica'
        db.delete_table(u'quirofanos_cmsb_tipointervencionquirurgica')

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

        # Deleting model 'Participacion'
        db.delete_table(u'quirofanos_cmsb_participacion')

        # Deleting model 'Reservacion'
        db.delete_table(u'quirofanos_cmsb_reservacion')


    models = {
        u'quirofanos_cmsb.cuenta': {
            'Meta': {'object_name': 'Cuenta'},
            'contrasena': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_creacion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_usuario': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'privilegio': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'quirofanos_cmsb.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'cuenta': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quirofanos_cmsb.Cuenta']", 'unique': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'quirofanos_cmsb.equipoespecial': {
            'Meta': {'object_name': 'EquipoEspecial'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'quirofanos_cmsb.especializacion': {
            'Meta': {'object_name': 'Especializacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'quirofanos_cmsb.intervencionquirurgica': {
            'Meta': {'object_name': 'IntervencionQuirurgica'},
            'duracion': ('django.db.models.fields.DecimalField', [], {'max_digits': '2', 'decimal_places': '2'}),
            'equipos_especiales_requeridos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quirofanos_cmsb.EquipoEspecial']", 'symmetrical': 'False', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_intervencion': ('django.db.models.fields.DateField', [], {}),
            'hora_fin': ('django.db.models.fields.TimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materiales_quirurgicos_requeridos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quirofanos_cmsb.MaterialQuirurgico']", 'symmetrical': 'False', 'blank': 'True'}),
            'medicos_participantes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quirofanos_cmsb.Medico']", 'through': u"orm['quirofanos_cmsb.Participacion']", 'symmetrical': 'False'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'paciente': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quirofanos_cmsb.Paciente']", 'unique': 'True'}),
            'preferencia_anestesica': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'quirofano': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.Quirofano']"}),
            'razon_riesgo': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'riesgo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'tipo_intervencion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.TipoIntervencionQuirurgica']"})
        },
        u'quirofanos_cmsb.materialquirurgico': {
            'Meta': {'object_name': 'MaterialQuirurgico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'quirofanos_cmsb.medico': {
            'Meta': {'object_name': 'Medico'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'cuenta': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quirofanos_cmsb.Cuenta']", 'unique': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'especializaciones': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quirofanos_cmsb.Especializacion']", 'symmetrical': 'False'}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'quirofanos_cmsb.medicotratante': {
            'Meta': {'object_name': 'MedicoTratante'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medico': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quirofanos_cmsb.Medico']", 'unique': 'True'})
        },
        u'quirofanos_cmsb.paciente': {
            'Meta': {'object_name': 'Paciente'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'cedula': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'diagnostico_ingreso': ('django.db.models.fields.TextField', [], {}),
            'familiar_medico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.Medico']", 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'numero_expediente': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '5', 'blank': 'True'}),
            'numero_habitacion': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'numero_inscripcion_medico': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'blank': 'True'}),
            'parentezco_familiar_medico': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'servicios_operatorios_requeridos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['quirofanos_cmsb.ServicioOperatorio']", 'symmetrical': 'False', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'quirofanos_cmsb.participacion': {
            'Meta': {'object_name': 'Participacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervencion_quirurgica': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.IntervencionQuirurgica']"}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.Medico']"}),
            'rol': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'quirofanos_cmsb.quirofano': {
            'Meta': {'object_name': 'Quirofano'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.IntegerField', [], {})
        },
        u'quirofanos_cmsb.reservacion': {
            'Meta': {'object_name': 'Reservacion'},
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'dias_hospitalizacion': ('django.db.models.fields.IntegerField', [], {}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'fecha_reservacion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intervencion_quirurgica': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['quirofanos_cmsb.IntervencionQuirurgica']", 'unique': 'True'}),
            'medico': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quirofanos_cmsb.MedicoTratante']"}),
            'tipo_solicitud': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'quirofanos_cmsb.serviciooperatorio': {
            'Meta': {'object_name': 'ServicioOperatorio'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'quirofanos_cmsb.tipointervencionquirurgica': {
            'Meta': {'object_name': 'TipoIntervencionQuirurgica'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['quirofanos_cmsb']
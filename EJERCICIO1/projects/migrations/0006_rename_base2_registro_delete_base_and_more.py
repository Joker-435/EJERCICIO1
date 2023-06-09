# Generated by Django 4.2 on 2023-05-11 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_base2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Base2',
            new_name='Registro',
        ),
        migrations.DeleteModel(
            name='Base',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='acepto_notificaciones2',
            new_name='acepto_notificaciones',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='acepto_terminos2',
            new_name='acepto_terminos',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='ciudad_residencia2',
            new_name='ciudad_residencia',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='codigo_referido2',
            new_name='codigo_referido',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='contrasena2',
            new_name='contrasena',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='correo_electronico2',
            new_name='correo_electronico',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='departamento_residencia2',
            new_name='departamento_residencia',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='direccion2',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='fecha_expedicion2',
            new_name='fecha_expedicion',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='genero2',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='id_usuario2',
            new_name='id_usuario',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='nacionalidad2',
            new_name='nacionalidad',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='numero_documento2',
            new_name='numero_documento',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='primer_apellido2',
            new_name='primer_apellido',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='primer_nombre2',
            new_name='primer_nombre',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='segundo_apellido2',
            new_name='segundo_apellido',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='segundo_nombre2',
            new_name='segundo_nombre',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='telefono_movil2',
            new_name='telefono_movil',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='tipo_documento2',
            new_name='tipo_documento',
        ),
    ]

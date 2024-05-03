# Generated by Django 3.1.2 on 2021-04-14 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numero_espectros', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IngresoPaciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_Primera_Atencion', models.CharField(max_length=50)),
                ('Citologia', models.CharField(choices=[('ACG', 'ACG'), ('ASC - H', 'ASC - H'), ('ASC-US - VPH', 'ASC-US - VPH'), ('ASC-US', 'ASC-US'), ('Cambios atrofia', 'Cambios atrofia'), ('Cambios indeterminados', 'Cambios indeterminados'), ('Cambios reactivos', 'Cambios reactivos'), ('Carcinoma invasivo', 'Carcinoma invasivo'), ('Displasia cervical', 'Displasia cervical'), ('Inflamatoria', 'Inflamatoria'), ('Inflamacion severa', 'Inflamacion severa'), ('Negativo neoplasia', 'Negativo neoplasia'), ('Leiomioma', 'Leiomioma'), ('LEI AG', 'LEI AG'), ('LEI AG - VPH', 'LEI AG - VPH'), ('LEI BG', 'LEI BG'), ('LEI BG - VPH', 'LEI BG - VPH'), ('Tricomonas', 'Tricomonas'), ('VPH', 'VPH'), ('Sin reporte', 'Sin reporte'), ('Sin dato', 'Sin dato')], max_length=50)),
                ('Fecha_Citologia', models.CharField(max_length=50)),
                ('Colposcopia', models.CharField(choices=[('Insatisfactoria típica', 'Insatisfactoria típica'), ('Insatisfactoria atípica', 'Insatisfactoria atípica'), ('Satisfactoria típica', 'Satisfactoria típica'), ('Satisfactoria atípica', 'Satisfactoria atípica'), ('Sin dato', 'Sin dato')], max_length=200)),
                ('Control_citologico', models.CharField(choices=[('ASC - US', 'ASC - US'), ('Atrofia', 'Atrofia'), ('Carcinoma escamocelular', 'Carcinoma escamocelular'), ('LEI AG', 'LEI AG'), ('LEI BG', 'LEI BG'), ('LEI BG -VPH', 'LEI BG -VPH'), ('Lesion Paracervical Extirpada', 'Lesion Paracervical Extirpada'), ('Negativo para neoplasia', 'Negativo para neoplasia'), ('Sin dato', 'Sin dato')], max_length=50)),
                ('Control_colposcopico', models.CharField(choices=[('Insatisfactoria típica', 'Insatisfactoria típica'), ('Insatisfactoria atípica', 'Insatisfactoria atípica'), ('Satisfactoria típica', 'Satisfactoria típica'), ('Satisfactoria atípica', 'Satisfactoria atípica'), ('Sin dato', 'Sin dato')], max_length=50)),
                ('Biopsia', models.CharField(choices=[('Carcinoma infiltrante', 'Carcinoma infiltrante'), ('Carcinoma escamocelular no queratizante', 'Carcinoma escamocelular no queratizante'), ('Carcinoma escamocelular', 'Carcinoma escamocelular'), ('Cervicitis cronica - VPH', 'Cervicitis cronica - VPH'), ('Cervicitis cronica - Polipo endocervical', 'Cervicitis cronica - Polipo endocervical'), ('Coilocitosis - VPH', 'Coilocitosis - VPH'), ('Displasia cervical leve', 'Displasia cervical leve'), ('Displasia epitelial moderada', 'Displasia epitelial moderada'), ('Endocervicitis cronica', 'Endocervicitis cronica'), ('Histologicamente normal', 'Histologicamente normal'), ('Hiperplasia sin atipias', 'Hiperplasia sin atipias'), ('Negativo para neoplasia', 'Negativo para neoplasia'), ('NICI', 'NICI'), ('NICI - Coilocitosis', 'NICI - Coilocitosis'), ('NICI - Coilocitosis - VPH', 'NICI - Coilocitosis - VPH'), ('NICI - Polipo endocervical - VPH', 'NICI - Polipo endocervical - VPH'), ('NICI - VPH', 'NICI - VPH'), ('NICI - VPH - CC', 'NICI - VPH - CC'), ('NICII', 'NICII'), ('NICII - Coilocitosis', 'NICII - Coilocitosis'), ('NICII - Coilocitosis - VPH', 'NICII - Coilocitosis - VPH'), ('NICII - VPH', 'NICII - VPH'), ('NICIII', 'NICIII'), ('NICIII - Coilocitosis', 'NICIII - Coilocitosis'), ('NICIII - Coilocitosis - VPH', 'NICIII - Coilocitosis - VPH'), ('NICIII - VPH', 'NICIII - VPH'), ('Polipo endocervical', 'Polipo endocervical'), ('Polipo endocervical-cervicitis cronica', 'Polipo endocervical-cervicitis cronica'), ('Polipo edocervical - VPH', 'Polipo edocervical - VPH'), ('VPH', 'VPH'), ('VPH - Quiste de naboth', 'VPH - Quiste de naboth'), ('Sin dato', 'Sin dato'), ('Sin reporte', 'Sin reporte')], max_length=50)),
                ('Control_Histologico', models.CharField(choices=[('Carcinoma invasivo', 'Carcinoma invasivo'), ('Coilocitosis - VPH', 'Coilocitosis - VPH'), ('Compatible con cambios displasicos', 'Compatible con cambios displasicos'), ('Epitelio escamoso - coilocitosis', 'Epitelio escamoso - coilocitosis'), ('Material purulento cavidad uterina', 'Material purulento cavidad uterina'), ('Negativo para neoplasia', 'Negativo para neoplasia'), ('NICII', 'NICII'), ('NICII - Coilocitosis - VPH', 'NICII - Coilocitosis - VPH'), ('NICII - VPH', 'NICII - VPH'), ('NICI - VPH', 'NICI - VPH'), ('NICIII - VPH', 'NICIII - VPH'), ('Sin dato', 'Sin dato')], max_length=50)),
                ('Tratamiento', models.CharField(choices=[('Antibiotico', 'Antibiotico'), ('Baycuten', 'Baycuten'), ('Conizacion', 'Conizacion'), ('Clotrimazol', 'Clotrimazol'), ('Doxiciclina -metronidazol', 'Doxiciclina -metronidazol'), ('Fluconazol -gynoplus', 'Fluconazol -gynoplus'), ('Histerectomia', 'Histerectomia'), ('Hormonoterapia', 'Hormonoterapia'), ('Legrado endocervical', 'Legrado endocervical'), ('Metronidazol - Doxiciclina - Gentamicina', 'Metronidazol - Doxiciclina - Gentamicina'), ('Radioterapia', 'Radioterapia'), ('Topicacion con ATA', 'Topicacion con ATA'), ('Vaporizacion', 'Vaporizacion'), ('Vaporizacion -Levamisole', 'Vaporizacion -Levamisole'), ('No requiere', 'No requiere'), ('Sin dato', 'Sin dato')], max_length=50)),
                ('Fecha_tratamiento', models.CharField(max_length=100)),
                ('Fecha_Ultimocontrol', models.CharField(max_length=100)),
                ('Hallazgo_mama', models.CharField(max_length=300)),
                ('Departamento', models.CharField(max_length=50, null=True)),
                ('Municipio', models.CharField(max_length=50, null=True)),
                ('Zona', models.CharField(choices=[('Rural', 'Rural'), ('Urbana', 'Urbana')], max_length=50, null=True)),
                ('DocumentoIdentificacion', models.IntegerField(null=True)),
                ('Nombre', models.CharField(max_length=50, null=True)),
                ('Apellido', models.CharField(max_length=50, null=True)),
                ('EstadoCivil', models.CharField(choices=[('Soltera', 'Soltera'), ('Separada', 'Separada'), ('Unión Libre', 'Union Libre'), ('Viuda', 'Viuda')], max_length=50, null=True)),
                ('Edad', models.IntegerField(null=True)),
                ('FechaNacimiento', models.CharField(max_length=50, null=True)),
                ('Direccion', models.CharField(max_length=100, null=True)),
                ('Telefono', models.IntegerField(null=True)),
                ('Ocupacion', models.CharField(max_length=50, null=True)),
                ('Escolaridad', models.CharField(choices=[('Primaria', 'Primaria'), ('Secundaria', 'Secundaria'), ('Tecnico', 'Tecnico'), ('Tecnologo', 'Tecnologo'), ('Universitaria', 'Universitaria'), ('Otro', 'Otro')], max_length=50, null=True)),
                ('Seguridadsocial', models.CharField(choices=[('Contributivo', 'Contributivo'), ('Sunsidiado', 'Subsiciado'), ('No afiliado', 'No afiliado'), ('No especifica', 'No especifica')], max_length=50, null=True)),
                ('Partos', models.IntegerField(null=True)),
                ('Edadprimerparto', models.IntegerField(null=True)),
                ('Menarca', models.CharField(max_length=50, null=True)),
                ('EdadinicioRS', models.IntegerField(null=True)),
                ('Abortos', models.IntegerField(null=True)),
                ('Gravidex', models.CharField(max_length=50, null=True)),
                ('Paridad', models.CharField(max_length=50, null=True)),
                ('Vivos', models.CharField(max_length=50, null=True)),
                ('Metodo_Anticompceptivo', models.CharField(max_length=50, null=True)),
                ('Fecha_ultimaMenstura', models.CharField(max_length=50, null=True)),
                ('CirugiaGinecologica', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=50, null=True)),
                ('ETS', models.CharField(max_length=50, null=True)),
                ('AntecedenteFami', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=50, null=True)),
                ('Fuma', models.CharField(choices=[('NO', 'NO'), ('Poco', 'Poco'), ('Mucho', 'Mucho')], max_length=50, null=True)),
                ('ConsumoLicor', models.CharField(choices=[('NO', 'NO'), ('Poco', 'Poco'), ('Mucho', 'Mucho')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotasMedicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hallazgo_imagen', models.CharField(max_length=300)),
                ('Nota', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PCAgraf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image3', models.ImageField(upload_to='muestra')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('name3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba3.ingresopaciente')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba3.ingresopaciente')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='muestra')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('Nombre_Paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba3.ingresopaciente')),
            ],
        ),
    ]
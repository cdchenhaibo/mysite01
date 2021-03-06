# Generated by Django 3.0.6 on 2020-05-23 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pmareas',
            options={'ordering': ['prj_area']},
        ),
        migrations.AlterModelOptions(
            name='pmprojects',
            options={'verbose_name': '项目', 'verbose_name_plural': '项目规划库'},
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='access_system_proposal',
            field=models.CharField(max_length=300, verbose_name='接入系统方案'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='cable_len',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='电缆长度'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='capacity_size',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='容量大小'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='commissioning_date',
            field=models.DateField(verbose_name='投产时间'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.PMCountys', verbose_name='项目县级区域'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='dev_attr',
            field=models.CharField(choices=[('XJ', '新建'), ('KJ', '扩建'), ('GJ', '改建')], max_length=2, verbose_name='建设性质'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='info',
            field=models.CharField(max_length=300, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='is_country_grid',
            field=models.BooleanField(verbose_name='是否农网项目'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='line_len',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='架空线路长度'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='prj_attr',
            field=models.CharField(max_length=300, verbose_name='工程属性'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='start_date',
            field=models.DateField(verbose_name='开工时间'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='supply_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.PMAreas', verbose_name='供电区域'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='title',
            field=models.CharField(max_length=300, verbose_name='项目名称'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='total_investment',
            field=models.DecimalField(decimal_places=2, max_digits=12, verbose_name='总投资'),
        ),
        migrations.AlterField(
            model_name='pmprojects',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pm.PMYears', verbose_name='立项年度'),
        ),
        migrations.AlterField(
            model_name='pmyears',
            name='year',
            field=models.CharField(max_length=4, verbose_name='立项年度'),
        ),
    ]

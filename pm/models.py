from django.db import models
from uploader.models import FileInfo

# Create your models here.

class PMYears(models.Model):
    year = models.CharField(max_length=4, verbose_name="立项年度")

    def __str__(self):
        return self.year

    class Mate:
        ordering = ['-year']
        verbose_name = '立项年度'
        verbose_name_plural = '立项年度'


class PMAreas(models.Model):
    prj_area = models.CharField(max_length=4, verbose_name="供电区域")

    def __str__(self):
        return self.prj_area

    class Meta:
        ordering = ['prj_area']
        verbose_name = '供电区域'
        verbose_name_plural = '供电区域'


class PMCountys(models.Model):
    county_name = models.CharField(max_length=12, verbose_name='项目县级区域')

    def __str__(self):
        return self.county_name

    class Mate:
        ordering = ['county_name']
        verbose_name = '项目县级区域'
        verbose_name_plural = '项目县级区域'


class PMPrjTypes(models.Model):
    prj_type = models.CharField(max_length=24)

    def __str__(self):
        return self.prj_type


class PMProjects(models.Model):
    #项目名称
    title = models.CharField(max_length=300, verbose_name='项目名称')

    #项目立项年度
    year = models.ForeignKey(PMYears, on_delete=models.CASCADE, verbose_name='立项年度')

    #供电区域(农B/农C/农D)
    supply_area = models.ForeignKey(PMAreas, on_delete=models.CASCADE, verbose_name='供电区域')

    #建设性质(扩建/新建/改建)
    class DevAttrChoices(models.TextChoices):
        XJ = 'XJ', '新建'
        KJ = 'KJ', '扩建'
        GJ = 'GJ', '改建'
    dev_attr = models.CharField(max_length=2, choices=DevAttrChoices.choices, verbose_name='建设性质')

    #项目县级区域(鼎城/汉寿)
    county = models.ForeignKey(PMCountys, on_delete=models.CASCADE, verbose_name='项目县级区域')

    #架空线路长度
    line_len = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='架空线路长度')

    #电缆长度
    cable_len = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='电缆长度')

    #容量大小
    capacity_size = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='容量大小')

    #总投资
    total_investment = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='总投资')

    #是否农网项目(是/否)
    is_country_grid = models.BooleanField(verbose_name='是否农网项目')

    #开工时间
    start_date = models.DateField(verbose_name='开工时间')

    #投产时间
    commissioning_date = models.DateField(verbose_name='投产时间')

    #工程属性
    prj_attr = models.CharField(max_length=300, verbose_name='工程属性')

    #接入系统方案
    access_system_proposal = models.CharField(max_length=300, verbose_name='接入系统方案')

    #备注
    info = models.CharField(max_length=300, verbose_name='备注')

    #内审时间
    end_date = models.DateField(verbose_name='内审时间')


    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '1.项目规划库'

    def __str__(self):
        return self.title


class PMPrjPreFeasibility(models.Model):
    prj = models.ForeignKey(PMProjects, on_delete=models.CASCADE, verbose_name='项目')

    #架空线路长度
    line_len = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='架空线路长度', blank=True, null=True)

    #电缆长度
    cable_len = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='电缆长度', blank=True, null=True)

    #容量大小
    capacity_size = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='容量大小', blank=True, null=True)

    #总投资
    total_investment = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='总投资', blank=True, null=True)

    file_info = models.ForeignKey(FileInfo, on_delete=models.CASCADE, verbose_name='内审文件', blank=True, null=True)

    # 备注
    info = models.CharField(max_length=300, verbose_name='备注')

    def __str__(self):
        return self.prj.__str__()

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '2.项目可研库(内审)'


class PMPrjFeasibility(models.Model):
    prj = models.ForeignKey(PMProjects, on_delete=models.CASCADE, verbose_name='项目')

    # 备注
    info = models.CharField(max_length=300, verbose_name='备注')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '3.项目可研库(省公司)'

class PMPrjPreFirstFounded(models.Model):
    prj = models.ForeignKey(PMProjects, on_delete=models.CASCADE, verbose_name='项目')

    # 备注
    info = models.CharField(max_length=300, verbose_name='备注')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '4.项目初设库(内审)'

class PMPrjFirstFounded(models.Model):
    prj = models.ForeignKey(PMProjects, on_delete=models.CASCADE, verbose_name='项目')

    # 备注
    info = models.CharField(max_length=300, verbose_name='备注')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '5.项目初设库(省公司)'
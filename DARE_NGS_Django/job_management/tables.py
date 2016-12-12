# tutorial/tables.py
from django_tables2.utils import A
import django_tables2 as tables
from .models import Job
class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name
class JobTable(tables.Table):
    #delete_link = tables.LinkColumn('action', args=[A('pk')], verbose_name='delete',)
    Select = CheckBoxColumnWithName(verbose_name="Select", accessor="id")
    class Meta:
    	model = Job
        #amend = CheckBoxColumnWithName(verbose_name="Amend", accessor="pk")
        # add class="paleblue" to <table> tag
    	attrs = {"class": "paleblue"}

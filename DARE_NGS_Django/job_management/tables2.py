import django_tables2 as tables
from .models import Job
class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name   
class IbiomesTable(tables.Table):
    Select = CheckBoxColumnWithName(verbose_name="Select", accessor="pk")
    class Meta:
        model = Job
        amend = CheckBoxColumnWithName(verbose_name="Amend", accessor="pk")
        #fields = ('id','status','submitted_time','type','detail_status','dareprocess_id','userid')
        
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}

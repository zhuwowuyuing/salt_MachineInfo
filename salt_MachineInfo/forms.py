__author__ = 'liangnaihua'

from django import forms
from salt_MachineInfo.models import *

class serverinfo(forms.Form):
    hostname    = forms.CharField(label='主机名')
    status      = forms.CharField(label='状态')
    cpu_model   = forms.CharField(label='CPU 型号')
    num_cpus    = forms.IntegerField(label='CPU 数量')
    mem_total   = forms.IntegerField(label='内存')
    os          = forms.CharField(label='操作系统')
    productname = forms.CharField(label='服务器型号')
    manufacturer= forms.CharField(label='品牌')
    diskinfo    = forms.
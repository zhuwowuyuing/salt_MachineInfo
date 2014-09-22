__author__ = 'liangnaihua'

from models import *
from django.shortcuts import render
import json;

def machineinfo(request):
    info = {}
    # machineSet = BaseInfo.objects.all()
    for machine in BaseInfo.objects.all():
    # for machine in BaseInfo.objects.filter(hostname__contains='is13084905-068'):
        hostname            = machine.hostname
        status              = machine.status
        cpu_model           = machine.cpu_model
        num_cpus            = machine.num_cpus
        mem_total           = machine.mem_total
        os                  = machine.os
        productname         = machine.productname
        manufacturer        = machine.manufacturer
        disks               = machine.disks.all()
        interfaces          = machine.interfaces.all()

        if not info.has_key(hostname):
            info.setdefault(hostname, {})
            info[hostname].setdefault('status', status)
            info[hostname].setdefault('cpu_model', cpu_model)
            info[hostname].setdefault('num_cpus', num_cpus)
            info[hostname].setdefault('mem_total', mem_total)
            info[hostname].setdefault('os', os)
            info[hostname].setdefault('productname', productname)
            info[hostname].setdefault('manufacturer', manufacturer)
            info[hostname]['interfaces'] = {}
            for i in disks:
                info[hostname]['interfaces']

            for j in interfaces:
                info[hostname].setdefault('interface',j.interface)
                info[hostname].setdefault('mac',j.hwaddr)
                info[hostname].setdefault('ipaddr',j.ipaddr)
            # info[hostname].setdefault('interfaces', interfaces)

    encodedjson = json.dumps(info)
    info = json.loads(encodedjson)

    return render(request, 'names.html', locals())


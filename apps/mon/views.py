from apps.mon.models import Record

def mon_mon(request, pattern, *args, **kwargs):
    dates = {
        'year': None,
        'month': None,
        'day': None
    }
    valid_fields = Record.data_fields()
    fields = list()

    for p in pattern.split('/'):
        if p.isdigit():
            l = len(p)
            num = int(p)
            if l is 4:
                dates['year'] = num
            elif not dates['month'] and l < 13:
                dates['month'] = num
            else:
                dates['day'] = num
        else:
            dtype = p.lower()
            if dtype in valid_fields:
                fields.append(dtype)

    for k,v in dates.items():
        if not v:
            del dates[k]

    return "Success"

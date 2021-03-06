#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from workalendar.asia import China
from datetime import timedelta, date
import json
if __name__ == "__main__":
    cal = China()
    cur = date.today() - timedelta(days=3)
    res = {}
    for i in range(30):
        cur += timedelta(days=1)
        res[str(cur)] = cal.is_working_day(cur)
    with open('cn.json', 'w') as json_file:
        json.dump(res, json_file, indent=4, sort_keys=True)

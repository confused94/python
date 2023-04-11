# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 22:22:07 2023

@author: Ekrem Burak Onuş
"""

import calendar

takvim=calendar.TextCalendar(calendar.MONDAY)
ekranayaz=takvim.formatmonth(2023, 4)

print(ekranayaz)

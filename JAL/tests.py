from django.test import TestCase
from JAL import models
# Create your tests here.
class test:
    def __init__(self, xx):
        self.haha = xx
    def __str__(self):
        return '({})'.format(self.haha)
a = test('biubiu')

# print(a)

_asin_ = ['B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR']

print(_asin_.index('B09YLKWBMV'))

_nav_ = {
        'ME AND MR. LEO': 'index',
        'About': 'about',
        'Product': 'product',
        'ZMH': 'B09YLLXKDT',
        'YDJ': 'B09YLKWBMV',
        'DDL': 'B09KG4R3YR',
        'Login': 'login',
        'Sign Up': 'signUp',
    }
print(_nav_.keys())
print(_nav_['DDL'])
print(list(_nav_))
print(list(_nav_.values()).index('index'))
print(_nav_.keys())
print(list(_nav_.keys())[list(_nav_.values()).index('index')])

# for i in range(3):
#     for k in range(2):
#         print(k,i)
        # print(i)


xx = 'abc'
print(xx[0])

print(range(6))


from threading import Timer
def hello(): 
    print ("hello, world")
    # Timer(5.0, hello).start()
   
# t = Timer(5.0, hello)
# t.start()



import datetime, time, zoneinfo, pytz
'''
print('===========================')
print('|   Part: set timezone    |')
print('===========================')
'''
print('\n=== Eastern time zone ========================')
all_timezones = pytz.all_timezones
_format_ = '%Y-%m-%d %H:%M:%S %Z %z'
# _format_ = '%Y%m%d %H:%M:%S'
# _format_ = '%m/%d/%Y %H:%M:%S'
# print(all_timezones)
# current_time
local_time = datetime.datetime.now()
print('| BJS_time', local_time, ' |')
# BJS_time
_shanghai_ = pytz.timezone('Asia/Shanghai')
shanghai_time = datetime.datetime.now(tz=_shanghai_).strftime(_format_)
print('| SHA_time', shanghai_time, ' |')
# LON_time
# Greenwich_Mean_Time = timezone.now()
_lon_ = pytz.timezone('Europe/London')
lon_time = datetime.datetime.now(tz=_lon_).strftime(_format_)
print('| LON_time', lon_time, ' |')
# NYC_time
_nyc_ = pytz.timezone('America/New_York')
nyc_time = datetime.datetime.now(tz=_nyc_).strftime(_format_)
print('| NYC_time', nyc_time, ' |')
# LAX_time
_lax_ = pytz.timezone('America/Los_Angeles')
lax_time = datetime.datetime.now(tz=_lax_)

time_zone = lax_time
print('| LAX_time', lax_time, ' |')
print('=== Western time zone ========================\n')

print(type(lax_time.strftime('%H:%M')),lax_time.strftime('%H:%M:%S'),lax_time.strftime('%S'))

# while True:
#     if datetime.datetime.now(tz=_shanghai_).strftime('%S') == '00':
#         print(datetime.datetime.now(tz=_shanghai_).strftime('%H:%M:%S'))
#         time.sleep(55)

# while datetime.datetime.now(tz=_shanghai_).strftime('%H:%M') < '21:41':
#     print(datetime.datetime.now(tz=_shanghai_).strftime('%H:%M:%S'))
#     time.sleep(5)
# else:
#     email()
    


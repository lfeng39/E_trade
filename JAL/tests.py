from django.test import TestCase

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
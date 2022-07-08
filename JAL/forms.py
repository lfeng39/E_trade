
import pandas as pd
import os
from django import forms

class DataForm(forms.Form):
    def getAccountInfo(request):
        
        if request.method == 'POST':
            responseData = request.POST.get('passWord')
            aaa = request.POST.get('account')
            
        return responseData, aaa
    
    def accountVerify():
        pass



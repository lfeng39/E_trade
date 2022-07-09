
import pandas as pd
import os
from django import forms

class DataForm(forms.Form):
    def getAccountInfo(request):
        
        if request.method == 'POST':
            getAccount = request.POST.get('account')
            getPassWord = request.POST.get('passWord')
            
        return getAccount, getPassWord
    
    def accountVerify():
        pass




import pandas as pd
import os
from django import forms
from JAL import models


class DataForm(forms.Form):
    def getAccountInfo(request):
        
        if request.method == 'POST':
            getAccount = request.POST.get('account')
            getPassWord = request.POST.get('passWord')
            
        models.UserAccount.objects.create(
            email = getAccount,
            password = getPassWord,
            # country = '',
            # ctiy = '',
            # address = '',
            # first_name = 'Leo',
            # last_name = '',
        )

        return getAccount, getPassWord
    
    def accountVerify():
        pass



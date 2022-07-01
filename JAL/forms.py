
import pandas as pd
import os
from django import forms

class DataForm(forms.Form):
    def getData(request):
        
        if request.method == 'POST':
            responseData = request.POST.get('test')
            
        return responseData
    
    def accountVerify():
        pass



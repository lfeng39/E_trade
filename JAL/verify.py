print('>>> this is verify.py <<<')

from JAL import forms
from JAL import models


class VerifyAsin:
    def checkAsin():
        pass

    def addAsin():
        pass


class VerifyAccount:
    '''
    get account info from DB
    '''
    def accountDB():
        return models.UserAccount.objects.all().values('email','password')
    '''
    get account info from web POST
    '''
    def getAccountInfo(request):
        return forms.getAccountInfo(request)
    '''
    verify POST is valid
    '''
    def verifyValid(request):
        is_valid = forms.AccountDataForm(request.POST)
        if is_valid.is_valid():
            print('is valid', is_valid.cleaned_data, is_valid.errors)
            
        else:
            print('not valid', is_valid.cleaned_data,is_valid.errors)

    '''
    verify email, if exist, return True, if not, return False
    '''
    def verifyEmail(request):
        # if VerifyAccount.getAccountInfo(request)['email'] == 'Email' or VerifyAccount.getAccountInfo(request)['email'] == '':
        #     return False, 'Input email, please!'
        # elif VerifyAccount.getAccountInfo(request)['password'] == 'Password' or VerifyAccount.getAccountInfo(request)['password'] == '':
        #     return False, 'Input password, please!'
        # elif VerifyAccount.getAccountInfo(request)['email'] == 'Email' and VerifyAccount.getAccountInfo(request)['password'] == 'password':
        #     return False, 'Enter is not valid'
        # elif VerifyAccount.getAccountInfo(request)['email'] == '' and VerifyAccount.getAccountInfo(request)['password'] == '':
        #     return False, 'Enter can not null'
        # elif '@' not in VerifyAccount.getAccountInfo(request)['email']:
        #     return False, 'email error'
        '''
        check user_account from db, if in, return tips
        '''
        for index in range(len(VerifyAccount.accountDB())):
            if VerifyAccount.getAccountInfo(request)['email'] == VerifyAccount.accountDB()[index]['email']:
                return True, VerifyAccount.accountDB()[index]['email'], index
        '''
        user not in db, return created
        '''
        return False, VerifyAccount.getAccountInfo(request)['email']
    '''
    check password by index
    '''
    def verifyPassWord(request):
        if VerifyAccount.verifyEmail(request)[0]:
            if VerifyAccount.getAccountInfo(request)['password'] == VerifyAccount.accountDB()[VerifyAccount.verifyEmail(request)[2]]['password']:
                print('herepassword', VerifyAccount.verifyEmail(request)[2], VerifyAccount.accountDB()[VerifyAccount.verifyEmail(request)[2]])
                return True
            else:
                return False

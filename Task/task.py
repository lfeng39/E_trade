from django.shortcuts import render

# Create your views here.
import datetime, time, zoneinfo, pytz
from django.utils import timezone
from django.core.mail import send_mail, send_mass_mail, EmailMessage
from django.template.loader import render_to_string
from JAL import models, urls, spider, images, forms, verify, views


email = models.UserAccount.objects.all().values()[0]






def sendMail():
    '''
    send_mail()/send_mass_mail()
    '''
    subject = 'Coupon from ME AND MR.LEO Offical'
    body = 'Coupon Code: DJ923IR0DFJ92'
    from_email = 'sandianjiuke@163.com'
    to_email = [
        'lfeng39@163.com',
        '51630822@qq.com',
        'jessiezhu221@163.com',
    ]
    
    # html_message = """
    # <div>SHA_TIME: """ + str(datetime.datetime.now(tz=spider._shanghai_).strftime(spider._format_)) + """</div>
    # <div>SHA_WEATHER: """ + spider.cityWeather('Shanghai')['description'] + """</dvi>
    # """
    
    '''
    emailmessage()
    '''
    # data = {
    #     'key': 'values',
    #     }
    # html_message = render_to_string('msg.html', data)
    try:
        # send_mail(subject, '', from_email, to_email, fail_silently=False, html_message=views.htmlMsg())
        # datatuple = (
        #     (subject, views.htmlMsg(), from_email, to_email[0]),
        #     (subject, views.htmlMsg(), from_email, to_email[1]),
        #     (subject, views.htmlMsg(), from_email, to_email[2]),
        # )
        # send_mass_mail(datatuple)

        # message1 = (
        #     subject,
        #     '',
        #     from_email,
        #     ['lfeng39@163.com', '51630822@qq.com'],
        # )
        # message2 = (
        #     subject,
        #     '',
        #     from_email,
        #     ['lfeng39@163.com'],
        # )
        # send_mass_mail((message1, message2), fail_silently=False, html_message=views.htmlMsg())

        msg = EmailMessage(subject, views.htmlMsg(), from_email, to_email)
        msg.content_subtype = 'html'
        msg.send()
        timenow = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S %Z %z')
        print('Email sent successfully!')
        print(timenow)
    except Exception as e:
        print(f'Error: {e}', e)
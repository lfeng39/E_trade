// import base.js
function addScript(url){
	document.write("<script language='javascript' src='./base.js'></script>");
}

// account input control
if(page_id == 'login' || 'signUp')
{
    var get_input_email = document.getElementById('email')
    var get_input_password = document.getElementById('password')
    // var get_email_tips = document.getElementById('email_tips')
    var get_email_valid = document.getElementById('email_valid')
    var get_password_error = document.getElementById('password_error')
    console.log('account.js i get:',get_input_email.value)

    // verify email format valid
    function isEmail(email)
    {
        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return regex.test(email);
    }

    // verifyAccountInfo
    function verifyAccountInfo(type)
    {
        console.log('get_input_email.value:',get_input_email.value)
        // email input get foucse
        if(type == 'accountClick')
        {
            if(get_input_email.value == 'Email')
            {
                get_input_email.value = ''
                // get_email_tips.style = 'display:none'
                get_email_valid.style = 'display:none'
            }
            if(get_input_email.value !== '')
            {
                get_input_email.value = get_input_email.value
                get_email_valid.style = 'display:none'
            }
        }
        
        // email input lose foucse
        if(type == 'accountOnblur')
        {
            if(get_input_email.value == '')
            {
                get_input_email.value = 'Email'
            }
            else if(get_input_email.value !== '')
            {
                // if(get_input_email.value.includes('@'))
                if(isEmail(get_input_email.value))
                {
                    get_input_email.value = get_input_email.value
                    get_email_valid.style = 'display:none'
                }    
                else
                {
                    get_email_valid.style = ''
                }
            }

        }
        // paassword input get foucse
        if(type == 'passWordClick')
        {
            if(get_input_password.value == 'Password')
            {
                get_input_password.value = ''
                get_password_error.style = 'display:none'
                // activation verify email format
                if(isEmail(get_input_email.value))
                {
                    console.log('Valid email');
                }
                // if(get_input_email.value == 'Email')
                // {
                //     get_email_format.style = 'display:none'
                // }
                else
                {
                    get_email_valid.style = ''
                    console.log('Invalid email');
                }
            }
            else
            {
                get_input_password.value = get_input_password.value
            }
        }
        // paassword input lose foucse
        if(type == 'passWordOnblur')
        {
            if(get_input_password.value == '')
            {
                get_input_password.value = 'Password'
            }
            else
            {
                get_input_password.value = get_input_password.value
            }
        }

    }


    

    function account_email()
    {
        console.log('yes')
        // if(get_input_email.value != '')
        // {
        //     console.log('email yes')
        //     get_input_email.value = get_input_email.value
        // }
        // if(get_input_password.value != '')
        // {
        //     console.log('password yes')
        //     get_input_password.value = get_input_password.value
        // }
    }
}

// if(page_id == 'signUp')
// {
//     var get_input_email = document.getElementById('email')
//     var get_input_password = document.getElementById('passWord')
//     console.log('i get:',get_input_email.value)
//     // login input control
    
// }
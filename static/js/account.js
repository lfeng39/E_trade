// import base.js
function addScript(url){
	document.write("<script language='javascript' src='./base.js'></script>");
}

// account input control
if(page_id == 'login' || 'signUp')
{
    var get_input_email = document.getElementById('email')
    var get_input_password = document.getElementById('passWord')
    console.log('i get:',get_input_email.value)
    // login input control
    function loginControl(type)
    {
        if(type == 'accountClick')
        {
            if(get_input_email.value == 'EMAIL' || 'Your Email')
            {
                get_input_email.value = ''
            }
            else
            {
                get_input_email.value = get_input_email.value
            }
        }
        else if(type == 'accountOnblur')
        {
            if(get_input_email.value == '')
            {
                get_input_email.value = 'EMAIL'
            }
            else
            {
                get_input_email.value = get_input_email.value
            }
        }
        else if(type == 'passWordClick')
        {
            if(get_input_password.value == 'PASSWORD' || '123+ABC+!@#')
            {
                get_input_password.value = ''
            }
            else
            {
                get_input_password.value = get_input_password.value
            }
        }
        else if(type == 'passWordOnblur')
        {
            if(get_input_password.value == '')
            {
                get_input_password.value = 'PASSWORD'
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
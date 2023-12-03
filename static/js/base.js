// get page_id
var page_id = document.getElementsByTagName('body')[0].getAttribute('page_id')
console.log('base.js has get page_id:', page_id)


// 临时使用
var app_list = ['index', 'about', 'products', 'B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR', 'login', 'signUp']
var _nav_ = document.getElementById('app_list')
console.log('app_list_url:',_nav_.getElementsByTagName('a')[0].href)
console.log('app_list_conut:',_nav_.children.length)
// console.log('app_list_conut:',wrap_list)

// set nav
for(i=0; i<_nav_.children.length; i++)
{
    if(app_list[i+1] == page_id && page_id != 'B09YLLXKDT' && page_id != 'B09YLKWBMV')
    {
        _nav_.children[i].className = '-focus-'
    }
    if(page_id == app_list[2] || page_id == app_list[3] || page_id == app_list[4] || page_id == app_list[5])
    {
        _nav_.children[1].className = '-focus-'
    }
}

// set bodyHeight
var hei = document.getElementById('hei')
var clientHei = document.documentElement.clientHeight
var bodyHei = document.body.clientHeight
console.log('clientHei:', clientHei)
hei.textContent = 'clientHei: '+clientHei+' | '+'bodyHei: '+bodyHei
var footerTag = document.getElementsByTagName('footer')[0]
var footerHeight = window.getComputedStyle(footerTag,null).height
console.log('footerHeight:', footerHeight)

if(bodyHei < clientHei)
{
    hei.textContent = 'clientHei: '+clientHei+' | '+'bodyHei: '+bodyHei +' | '+'newHei: '+clientHei 
    document.body.style.height = clientHei +'px'
}

// set banner img
if(page_id == 'index')
{
    // set index banner
    var bodyWid = document.body.clientWidth
    var banner = document.getElementById('banner')
    var banner_asin = banner.getAttribute('name')
    var banner_img = banner.getAttribute('img_name')
    console.log('bannerTag:',banner)
    console.log('banner_asin:',banner_asin)
    console.log('banner_img:',banner_img)
    if(bodyWid > 1280)
    {
        banner_bg_style = "background: url('/static/image/show/" + banner_asin + "/" + banner_img + ".jpg') no-repeat; background-size: 100%; height:" + bodyWid * 0.5 + "px;"
        banner.style = banner_bg_style
        console.log('bodyWid > 1280, banner_wid:', bodyWid)
    }
    if(bodyWid < 1280)
    {
        banner_bg_style = "background: url('/static/image/show/" + banner_asin + "/" + banner_img + ".jpg') no-repeat 80%; background-size: auto 100%; height:" + bodyWid + "px;"
        document.getElementById('banner').style = banner_bg_style
        console.log('bodyWid < 1280, banner_wid:', bodyWid)
    }
    if(page_id == 'index')
    {
        // set resize
        function resizeFunction()
        {
            // 打印页面默认加载时的宽度
            console.log('bodyWid:', document.body.clientWidth)
            console.log('bodyHei:', document.body.clientHeight)

            var bodyWid = document.body.clientWidth
            var bodyHei = document.body.clientHeight
            var newHei = document.body.clientHeight
            console.log('new_banner:', newHei)
            if(bodyWid < 1280)
            {
                document.getElementById('banner').style.height = newHei
                console.log('new_banner:', newHei)
            }
            
        }

        // windows method listener
        window.addEventListener("resize", resizeFunction);

        // windows method onload()
        window.onload = function()
        {  
            resizeFunction()
        }
        
    }
}


//
function onClick()
{
    document.getElementById('side_bar').style = "width: 300px; height:100px; background: rgb(250,250,250); position: absolute; index: 1000; right: 2%; top: 10%; display: block;"
}
// function onClosed()
// {
//     document.getElementById('side_bar').style = "display: none;"
// }

var come_soon = document.getElementById('come_soon')
console.log('come_soon',come_soon)
come_soon.style = 'border: 3px solid #ff8800; height: '+(clientHei*0.6)+'px; text-align: center; line-height: '+(clientHei*0.6)+'px; font-size: 100px'














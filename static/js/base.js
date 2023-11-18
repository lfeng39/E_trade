
// index img auto height

// 获取 page_id
var page_id = document.getElementsByTagName('body')[0].getAttribute('page_id')
console.log('base.js has get page_id:', page_id)

// var _asin_ = ['B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR']
// 通过class = wrap取得当前页面的asin及个数
var wrap_list = document.getElementsByClassName('wrap')
var asin_code = []
for(i=0; i<wrap_list.length; i++)
{
    if(wrap_list[i].id != '')
    {
        asin_code.push(wrap_list[i].id)
    }
}
console.log('this page have asin_code:', asin_code.length)
// console.log(asin_code)


// 临时使用
var app_list = ['index', 'about', 'products', 'B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR', 'login', 'signUp']

// 暂时首页使用，获取包含有asin的标签，重新定义高度
var get_asin_element = [
    document.getElementById(asin_code[0]),
    document.getElementById(asin_code[1]),
    document.getElementById(asin_code[2]),
    document.getElementById(asin_code[3]),
]

var _nav_ = document.getElementById('app_list')
console.log('app_list_url:',_nav_.getElementsByTagName('a')[0].href)
console.log('app_list_conut:',_nav_.children.length)

// 控制导航焦点
// 改变 _nav_ 长度时，改变 i < int 
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



//仅首页执行背景图片控制器
if(page_id == 'index' || page_id == 'products')
{
    // 函数体：监听首页浏览器变化，动态控制图片大小
    function resizeFunction()
    {
        // 打印页面默认加载时的宽度
        console.log('bodyWid:', document.body.clientWidth)
        // 测试代码，显示当前浏览器窗口的实时宽度
        // document.getElementById('width').textContent = document.body.clientWidth
        // document.getElementById('width-mini').textContent = document.body.clientWidth

        var bodyWid = document.body.clientWidth

        var newHei = []
        for(i=0; i<asin_code.length; i++)
        {
            newHei[i] = get_asin_element[i].clientWidth * 0.6 + 'px'
            if(bodyWid < 1280)
            {
                get_asin_element[i].style.height = newHei[i]
            }
        }
    }

    // 监听事件及运行函数体
    window.addEventListener("resize", resizeFunction);

    // 页面加载时，运行函数体
    window.onload = function()
    {  
        // console.log(document.getElementById('side_bar'))
        
        resizeFunction()
        var img_name = []
        for(i=0; i<asin_code.length; i++)
        {
            img_name[i] = get_asin_element[i].getAttribute('img_name')
            // console.log(asin_code[i], ':', img_name[i])
            asin_code[i] = "background: url('/static/image/show/" + asin_code[i] + "/" + img_name[i] + ".jpg') no-repeat; background-size: 100%; height:" + get_asin_element[i].clientWidth * 0.6 + "px;"
            get_asin_element[i].style = asin_code[i]
        }
    }
    
}



function onClick()
{
    document.getElementById('side_bar').style = "width: 300px; height:100px; background: rgb(250,250,250); position: absolute; index: 1000; right: 2%; top: 10%; display: block;"
}
// function onClosed()
// {
//     document.getElementById('side_bar').style = "display: none;"
// }


// if(page_id == 'products')
// {
//     // price
//     var get_price = document.getElementById('price').textContent
//     var get_price_int = document.getElementById('price_int')
//     console.log('price $', get_price)
//     get_price = get_price.split('.')
//     console.log('price $ split:', get_price)
//     document.getElementById('price').textContent = get_price[1]
//     document.getElementById('price_int').textContent = get_price[0]
// }
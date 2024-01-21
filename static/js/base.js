console.log('/=== base set ===/')
// get page_id
var page_id = document.getElementsByTagName('body')[0].getAttribute('page_id')
console.log('base.js has get page_id:', page_id)



// ================ //
//   set nav        //
// ================ //
// 临时使用var app_list = ['index', 'about', 'products', 'B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR', 'login', 'signUp']
// var _nav_ = document.getElementById('app_list')
// console.log('app_url:',_nav_.getElementsByTagName('a')[0].href)
// console.log('app_conut:',_nav_.children.length)
// // console.log('app_list_conut:',wrap_list)
// for(i=0; i<_nav_.children.length; i++)
// {
//     if(app_list[i+1] == page_id && page_id != 'B09YLLXKDT' && page_id != 'B09YLKWBMV')
//     {
//         _nav_.children[i].className = '-focus-'
//     }
//     if(page_id == app_list[2] || page_id == app_list[3] || page_id == app_list[4] || page_id == app_list[5])
//     {
//         _nav_.children[1].className = '-focus-'
//     }
// }
// 

function navCol(event)
{
    if(event=='enter')
    {
        document.getElementById('nav-account-list').style.display = 'block'
        
        // console.log('bbb is bbb',document.getElementById('account-list'))
    }
    if(event=='leave')
    {
        document.getElementById('nav-account-list').style.display = 'none'
    }
}
function mobNavCol(module)
{
    if(module == 'nav')
    {
        var nav_app_mini_list = document.getElementById('nav-app-mini-list')
        var list_status = window.getComputedStyle(nav_app_mini_list).display
        if(list_status == 'none')
        {
            document.getElementById('nav-app-mini-list').style.display = 'block'
            document.getElementById('nav-account-mini-list').style.display = 'none'
        }
        else
        {
            document.getElementById('nav-app-mini-list').style.display = 'none'
        }
    }
    if(module == 'account')
    {
        var account_mini_list = document.getElementById('nav-account-mini-list')
        var list_status = window.getComputedStyle(account_mini_list).display
        if(list_status == 'none')
        {
            document.getElementById('nav-account-mini-list').style.display = 'block'
            document.getElementById('nav-app-mini-list').style.display = 'none'
        }
        else
        {
            document.getElementById('nav-account-mini-list').style.display = 'none'
        }
    }
}


// ================ //
//  set bodyHeight  //
// ================ //
var hei = document.getElementById('hei')
var clientHei = document.documentElement.clientHeight
var bodyHei = document.body.clientHeight
console.log('clientHei:', clientHei)
// hei.textContent = 'clientHei: '+clientHei+' | '+'bodyHei: '+bodyHei+ '| w: '+document.body.clientWidth
var footerTag = document.getElementsByTagName('footer')[0]
var footerHeight = window.getComputedStyle(footerTag,null).height
console.log('footerHeight:', footerHeight)
if(bodyHei < clientHei)
{
    // hei.textContent = 'clientHei: '+clientHei+' | '+'bodyHei: '+bodyHei +' | '+'newHei: '+clientHei 
    document.body.style.height = clientHei +'px'
}
console.log('\n')



// ================ //
//  set banner img  //
// ================ //
if(page_id == 'index')
{
    window.addEventListener
    (
        'load', 
        function load()
        {
            // create new tag after onload the page, promise the first image onload width 100%, not display more than two
            var insertTag = document.createElement('div')
            insertTag.style = banner_child[0].getAttribute('style')
            banner_container.appendChild(insertTag)
            console.log('created a new div after load the page done, now the banner_child_count:',banner_child.length)

            clon_first = document.getElementById('first_banner_tip').cloneNode(true)
            banner_container.lastChild.appendChild(clon_first)

            if(banner_child.length == 2)
            {
                clearInterval(tempo)
                console.log('banner_child_count less than', banner_child.length, ', can not move')
            }
            // tempo = setInterval(move, 6000)
            
            console.log('load done \n')
        }
    )
    window.addEventListener
    (
        'resize', 
        function resize()
        {
            // clearInterval(tempo)
            setBanner()
            console.log('resize')
            new_position = document.body.clientWidth * -(nth_img-1)
            document.getElementById('banner-container').style.left = new_position + 'px'
            // if(document.body.clientWidth > 1280)
            // {
            //     tempo = setInterval(move, 6000)
            // }
            // if(document.body.clientWidth < 1280)
            // {
            //     clearInterval(tempo)
            //     console.log('less 1280, stop tempo')
            // }
        }
    )
    window.addEventListener
    (
        'visibilitychange', 
        function visibilitychange()
        {
            if(document.visibilityState == 'visible')
            {
                tempo = setInterval(move, 6000)
                console.log('visible, start tempo')
            }
            if(document.visibilityState == 'hidden')
            {
                clearInterval(tempo)
                console.log('hidden, stop tempo')
            }
        }
    )
    // document.getElementById('banner').addEventListener
    // (
    //     'touchstart',
    //     function touchStart(start)
    //     {   
    //         s = start.touches[0].pageX
    //         clearInterval(tempo)
    //     }
    // )
    // var xxx = 0
    // document.getElementById('banner').addEventListener
    // (
    //     'touchmove', 
    //     function touchMove(move)
    //     {
    //         clearInterval(tempo)
    //         m = move.changedTouches[0].pageX
    //         n = s - m
    //         var tempX = xxx - n
    //         document.getElementById('banner-container').style.left = tempX + 'px'
    //         if(n < 0)
    //         {
    //             console.log('>>>')
    //         }
    //         if(n > 0)
    //         {
    //             console.log('<<<')
    //             if(n > 300)
    //             {
    //                 console.log('300')
    //                 // move = move()
    //                 // move('-')
    //             }
    //         }
    //     }
    // )
    // document.getElementById('banner').addEventListener
    // (
    //     'touchend', 
    //     function touchEnd(end)
    //     {
    //         e = end.changedTouches[0].pageX
    //         // console.log('bbb:' + bbb.changedTouches[0].pageX)
    //         // return e
    //         n = s - e
    //         xxx = xxx - n
    //         console.log('end-postion:', xxx)
    //         // moveImg = move()
    //         // moveImg()
    //     }
    // )

    // set banner-mini
    // var insertTag00 = document.createElement('div')
    // insertTag00.id = '0'
    // jessie.insertBefore(insertTag00, document.getElementById('1'))
    // var insertTag01 = document.createElement('div')
    // insertTag01.id = '3'
    // jessie.appendChild(insertTag01)
    // var insertTag02 = document.createElement('div')
    // insertTag02.id = '4'
    // jessie.appendChild(insertTag02)

    // clon_0 = document.getElementById('2').children[0].cloneNode(true)
    // document.getElementById('0').appendChild(clon_0)
    // clon_a = document.getElementById('1').children[0].cloneNode(true)
    // document.getElementById('3').appendChild(clon_a)
    // clon_b = document.getElementById('2').children[0].cloneNode(true)
    // document.getElementById('4').appendChild(clon_b)

    
    console.log('/=== set banner img ===/')
    // get banner object
    var banner = document.getElementById('banner')
    var banner_container = document.getElementById('banner-container')
    var banner_child = banner_container.children
    var banner_child_count = banner_child.length
    console.log('banner_child_count: ', banner_child_count)
    console.log('bodyWid: ', document.body.clientWidth)
    console.log('/=== set banner img initialization done===/')

    banner_code = banner_container.children[0]
    var current_obj = [
        banner_container.children[0].getAttribute('code'),
        banner_container.children[1].getAttribute('code'),
        banner_container.children[2].getAttribute('code'),
        banner_container.children[3].getAttribute('code')
    ]
    console.log('current_obj', current_obj)

    function setBanner()
    {
        
        // set index banner auto width
        var bodyWid = document.body.clientWidth

        // set banner_container width
        banner_container.style.width = bodyWid * (banner_child.length+1) + 'px'

        // set banner & banner_container height
        if(bodyWid > 1280)
        {
            banner.style.height = 680 + 'px'
            banner_container.style.height = 680 + 'px'
            // banner.style = banner_hei
            // tempo = setInterval(move, 6000)
        }
        if(bodyWid < 1280)
        {
            banner.style.height = bodyWid + 'px'
            banner_container.style.height = bodyWid + 'px'
            // clearInterval(tempo)
            // console.log('less 1280, stop tempo')
        }

        // set banner_child width & height
        for(i=0; i<banner_child.length; i++)
        {
            // set banner_child width
            banner_child[i].style.width = bodyWid + 'px'
            
            // set banner_child height
            if(bodyWid > 1280)
            {
                banner_child[i].style.height = 680 + 'px'
            }
            if(bodyWid < 1280)
            {
                banner_child[i].style.height =  bodyWid + 'px'
            }
        }
    }
}



// ================ //
// set listing img  //
// ================ //
if(page_id == 'listing')
{
    window.addEventListener
    (
        'load', 
        function load()
        {
            var img_7_mini = document.getElementById('img_7_mini')
            var img_7_1 = window.getComputedStyle(document.getElementById('7_1'))
            console.log('img: ', img_7_1.width)
            for(i=0; i<img_7_mini.children.length; i++)
            {
                img_7_mini.children[i].style.height = img_7_1.width
            }
        }
    )
    // get external css
    // var get_listing_img_style = window.getComputedStyle(img_7,null).left
    // set mob img_7
    var img_7_object = document.getElementById('img_7')
    var img_7_mob = document.getElementsByClassName('img-7')[0].children[0]
    var img_7_mob_width = window.getComputedStyle(img_7_mob).width
    console.log('img-7: ', img_7_mob_width)
    document.getElementsByClassName('img-7')[0].children[0].children[0].style.width = img_7_mob_width
    document.getElementsByClassName('img-7')[0].children[0].children[0].style.height = img_7_mob_width
    document.getElementById('img_7').style.width = img_7_mob_width
    document.getElementById('img_7').style.height = img_7_mob_width
    for(i=0; i<7; i++)
    {
        document.getElementById('img_7').children[i].children[0].style.width = img_7_mob_width
        document.getElementById('img_7').children[i].children[0].style.height = img_7_mob_width
    }
    
    function nex()
    {
        // must be in real time to get img_7_object.style.left value
        var img_7_move_range = (img_7_object.children.length-1) * -img_listing_width
        if(parseInt(img_7_css.left) > img_7_move_range)
        {
            img_7_object.style.left = parseInt(img_7_css.left) - img_listing_width + 'px'
            console.log('position_nex: ', img_7_css.left)
        }
    }
    function pre()
    {
        // must be in real time to get img_7_object.style.left value
        if(parseInt(img_7_object.style.left) < 0)
        {
            img_7_object.style.left = parseInt(img_7_css.left) + img_listing_width + 'px'
            console.log('position_pre: ', img_7_css.left)
        }
    }
    function cho(num)
    {
        var num = parseInt(num)
        var position = (num-1) * parseFloat(img_7_mob_width)
        img_7_object.style.left = -position + 'px'
        console.log('position_cho: ', position)
    }
}



var come_soon = document.getElementById('come_soon')
if(come_soon == true)
{
    console.log('come_soon',come_soon)
    come_soon.style = 'border: 3px solid #ff8800; height: '+(clientHei*0.6)+'px; text-align: center; line-height: '+(clientHei*0.6)+'px; font-size: 100px'
}



// =================== //
// touchScreen Module  //
// =================== //
// function touchScreen(jj)
// {
    
//     var s, e
//     document.getElementById('banner').addEventListener
//     (
//         'touchstart',
//         function touchStart(start)
//         {   
//             s = start.touches[0].pageX
//             // console.log('aaa:' + aaa.touches[0].pageX)
//             // return s
//         }
//     )
//     document.getElementById('banner').addEventListener
//     (
//         'touchend', 
//         function touchEnd(end)
//         {
//             e = end.changedTouches[0].pageX
//             // console.log('bbb:' + bbb.changedTouches[0].pageX)
//             // return e
//             n = s - e
//             if(n>0)
//             {
//                 console.log('to the left',eval(5+jj+3))
//                 // return x+y;
//                 move('-')
//             }
//             if(n<0)
//             {
//                 console.log('to the right',eval(6+jj+3))
//                 move('+')
//             }
//         }
//     )
    
// }
// touchScreen('-')
// function aaa()
// {
//     function bbb(x,y)
//     {
//         console.log('>>> jessie <<<', x*y)
//     }
//     return bbb
// }
// je = aaa()
// je(2,5)


// test.html
if(page_id == 'test')
{
        
    var kris = document.getElementById('kris')
    var jessie = document.getElementById('jessie')
    jessie.style.left = -document.body.clientWidth + 'px'

    var insertTag00 = document.createElement('div')
    insertTag00.id = '0'
    jessie.insertBefore(insertTag00, document.getElementById('1'))
    var insertTag01 = document.createElement('div')
    insertTag01.id = '3'
    jessie.appendChild(insertTag01)
    var insertTag02 = document.createElement('div')
    insertTag02.id = '4'
    jessie.appendChild(insertTag02)

    clon_0 = document.getElementById('2').children[0].cloneNode(true)
    document.getElementById('0').appendChild(clon_0)
    clon_a = document.getElementById('1').children[0].cloneNode(true)
    document.getElementById('3').appendChild(clon_a)
    clon_b = document.getElementById('2').children[0].cloneNode(true)
    document.getElementById('4').appendChild(clon_b)



    var s
    kris.addEventListener
    (
        'touchstart',
        function touchStart(start)
        {   
            s = start.touches[0].clientX
            // console.log('now',jessie.style.left)
        }
    )
    var xxx = 0
    var nnn = 1
    console.log('current', nnn)
    nnn = 2
    kris.addEventListener
    (
        'touchmove', 
        function touchMove(move)
        {
            m = move.changedTouches[0].clientX
            n = s - m
            // console.log('>>>:',jessie.style.left ,'-', n)
            var tempX = xxx - n - document.body.clientWidth
            jessie.style.left = tempX + 'px'
            // console.log('current img', n)
            
            if(n < 0)
            {
                console.log('>>>')
                if(Math.abs(xxx) > document.body.clientWidth*nnn)
                {
                    console.log('current', nnn)
                    nnn -= 1
                }
            }
            if(n > 0)
            {
                console.log('<<<')
                if(Math.abs(tempX) > document.body.clientWidth*nnn)
                {
                    console.log('current', nnn)
                    nnn += 1
                }
            }
            // if(Math.abs(tempX) > document.body.clientWidth*nnn)
            // {
            //     console.log('current', nnn)
            //     nnn += 1
            // }
            
        }
    )

    kris.addEventListener
    (
        'touchend',
        function touchEnd(end)
        {   
            // var bodyWid = document.body.clientWidth
            e = end.changedTouches[0].pageX
            n = s - e
            xxx = xxx - n
            // console.log('end-postion:', xxx)

        }
    )
    // 定义三个图片元素
    // const imgs = document.querySelectorAll("img");
    // // const img2 = document.getElementById("img2");
    // // const img3 = document.getElementById("img3");
    // console.log('current', imgs)
    // // 定义当前显示的图片索引
    // let currentImageIndex = 0;

    // // 定时器函数
    // function timer() {
    //   // 切换图片
    //   currentImageIndex = (currentImageIndex + 1) % 3;

    //   for (const img of imgs) {
    //     img.style.display = "none";
    //   }

    //   imgs[currentImageIndex].style.display = "block";
    // }

    // // 启动定时器
    // setInterval(timer, 5000);
}



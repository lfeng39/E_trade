console.log('/=== base set ===/')
// get page_id
var page_id = document.getElementsByTagName('body')[0].getAttribute('page_id')
console.log('base.js has get page_id:', page_id)



// ================ //
//   set nav        //
// ================ //
// 临时使用
var app_list = ['index', 'about', 'products', 'B09YLLXKDT', 'B09YLKWBMV', 'B09KG4R3YR', 'login', 'signUp']
var _nav_ = document.getElementById('app_list')
console.log('app_url:',_nav_.getElementsByTagName('a')[0].href)
console.log('app_conut:',_nav_.children.length)
// console.log('app_list_conut:',wrap_list)
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

            clon_first = document.getElementById('leo').cloneNode(true)
            banner_container.lastChild.appendChild(clon_first)

            if(banner_child.length == 2)
            {
                clearInterval(tempo)
                console.log('banner_child_count less than', banner_child.length, ', can not moveImg')
            }
            console.log('in load, done \n')
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
        }
    )
    window.addEventListener
    (
        'visibilitychange', 
        function visibilitychange()
        {
            if(document.visibilityState == 'visible')
            {
                tempo = setInterval(moveImg, 6000)
                console.log('visible, start tempo')
            }
            if(document.visibilityState == 'hidden')
            {
                clearInterval(tempo)
                console.log('hidden, stop tempo')
            }
        }
    )
    document.getElementById('banner').addEventListener
    (
        'touchstart',
        function touchStart(start)
        {   
            s = start.touches[0].pageX
            // console.log('aaa:' + aaa.touches[0].pageX)
            // return s
        }
    )
    document.getElementById('banner').addEventListener
    (
        'touchend', 
        function touchEnd(end)
        {
            e = end.changedTouches[0].pageX
            // console.log('bbb:' + bbb.changedTouches[0].pageX)
            // return e
            n = s - e
            if(n>0)
            {
                console.log('to the left')
                // return x+y;
                move = moveImg()
                move('-')
            }
            if(n<0)
            {
                console.log('to the right')
                move = moveImg()
                move('+')
            }
        }
    )

    console.log('/=== set banner img ===/')
    // get banner object
    var banner = document.getElementById('banner')
    var banner_container = document.getElementById('banner-container')
    var banner_child = banner_container.children
    var banner_child_count = banner_child.length
    console.log('banner_child_count: ', banner_child_count)
    console.log('bodyWid: ', document.body.clientWidth)
    console.log('/=== set banner img initialization done===/')

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
        }
        if(bodyWid < 1280)
        {
            banner.style.height = bodyWid + 'px'
            banner_container.style.height = bodyWid + 'px'
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

    // create new tag
    // var insertTag = document.createElement('div')
    // insertTag.style = banner_child[0].getAttribute('style')
    // insertTag.id ='jessie'
    // banner_container.appendChild(insertTag)
    // console.log('create new tag?',banner_child.length)

    

    // after page load, start moveImg
    tempo = setInterval(moveImg, 6000)
    var nth_run = 0
    var nth_img = 1
    function moveImg()
    {
        var velocity = setInterval(move, 10, '-');

        function moveStep()
        {
            for(i=2; i<document.body.clientWidth; i++)
            {
                var cou = (1+i)*i/2
                if(cou>document.body.clientWidth)
                {
                    return i - 1
                }
            }
        }

        var speed = 1
        function move(test)
        {
            // must be in real time to get img_7_object.style.left value
            var banner_move_range = (banner_child.length-1) * -document.body.clientWidth
            var position = banner_container.style.left
            // console.log('speed: ',speed, '/', 'banner_wid: ', document.body.clientWidth, '/', 'range: ', banner_move_range)
            // console.log('banner_container.position: ', position)

            if(parseInt(banner_container.style.left) > banner_move_range)
            {
                banner_container.style.left = eval(parseInt(banner_container.style.left) +test+ speed) + 'px'
                // console.log('after_move: ', banner_container.style.left)
                // var less = document.body.clientWidth - -parseInt(banner_container.style.left)
                if(speed == moveStep())
                {
                    var less = document.body.clientWidth - (1 + moveStep()) * moveStep()/2
                    // console.log('less: ', less)
                    banner_container.style.left = eval(parseInt(banner_container.style.left) +test+ less) + 'px'
                    window.clearInterval(velocity)
                    if(nth_img>banner_child.length-1)
                    {
                        nth_img = banner_child.length-(banner_child.length-1)
                        // console.log('current the', nth_img, 'th img vs', banner_child.length)
                        dis = document.querySelectorAll('.banner-tip')[nth_img-1].style.display = ''
                        // console.log('dis',dis)
                    }else{
                        // console.log('current the', nth_img +'th img')
                        dis = document.getElementsByClassName('banner-tip')[nth_img-1].style.display = ''
                        // console.log('dis',dis)
                    }
                    // console.log('banner_container.style.left: ',banner_container.style.left)
                    // console.log('run the ', nth_run +'th')
                }
            }else{
                clearInterval(velocity)
                // clearInterval(tempo)
                banner_container.style.left = 0 + 'px'
                nth_img = 1
                console.log('out range, stop velocity, but tempo running also')
            }
            speed ++
            console.log('\n')
        }
        nth_run++
        nth_img++
        return move
    }

    // function flipImg()
    // {
    // var co = 0
    // function flipImg()
    // {
    //     var banner = document.getElementById('banner-02')
    //     var img = [
    //         "background: url('/static/image/show/B0BZ3MGYXL/2-A+-970.jpg') no-repeat 50% 50%;",
    //         "background: url('/static/image/show/B0C6F3CK4F/2-A+-970.jpg') no-repeat 50% 50%;",
    //         "background: url('/static/image/show/B0BTWT5GL8/2-A+-970.jpg') no-repeat 50% 50%;",
    //     ]
    //     if(co < img.length)
    //     {
    //         var banner_bg_img = img[co]
    //         var banner_bg_size = 'background-size: cover;'
    //         var banner_hei = 'height:' + 680 + 'px'
    //         banner.style = banner_bg_img + banner_bg_size + banner_hei
    //         co ++
    //     }
    //     if(co == img.length)
    //     {
    //         co = 0
    //     }
    //     banner.style.opacity = 1
    //     console.log('i',i)
    //     var i = banner.style.opacity * 100
    //     var hid = setInterval(hidden, 30)
    //     function hidden()
    //     {
    //         i--
    //         banner.style.opacity = i/100
    //         console.log('??',banner.style.opacity)
    //         if(i == 0)
    //         {
    //             clearInterval(hid)
    //             console.log('co: ',co)
    //         }
    //     }
    // }
    // }
}



// ================ //
// set listing img  //
// ================ //
if(page_id == 'listing')
{
    // get external css
    // var get_listing_img_style = window.getComputedStyle(img_7,null).left
    var img_7_object = document.getElementById('img_7')
    var img_listing_width = parseInt(img_7_object.children[0].children[0].getAttribute('style').split(':')[1])
    console.log('img: ', img_listing_width)
    function nex()
    {
        // must be in real time to get img_7_object.style.left value
        var img_7_move_range = (img_7_object.children.length-1) * -590
        if(parseInt(img_7_object.style.left) > img_7_move_range)
        {
            img_7_object.style.left = parseInt(img_7_object.style.left) - 590 + 'px'
            console.log('position_nex: ', img_7_object.style.left)
        }
    }
    function pre()
    {
        // must be in real time to get img_7_object.style.left value
        if(parseInt(img_7_object.style.left) < 0)
        {
            img_7_object.style.left = parseInt(img_7_object.style.left) + 590 + 'px'
            console.log('position_pre: ', img_7_object.style.left)
        }
    }
    function cho(num)
    {
        var num = parseInt(num)
        var position = (num-1) * 590
        img_7.style.left = -position + 'px'
        // document.getElementById('7-'+num).style.border = '2px solid #ff0000'
        console.log('position_cho: ', img_7_object.style.left)

        console.log('listing_img-', num, typeof('1'), parseInt('1'), typeof(Number('1')))
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






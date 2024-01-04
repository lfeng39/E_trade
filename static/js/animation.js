console.log('/=== base set ===/')
// get page_id
var page_id = document.getElementsByTagName('body')[0].getAttribute('page_id')
console.log('base.js has get page_id:', page_id)


// after page load, start moveImg
// setInterval(function, milliseconds, param1, param2, ...)
var tempo = setInterval(move, 6000)
var nth_img = 1
function move()
{
    // setInterval(function, milliseconds, param1, param2, ...)
    var velocity = setInterval(moveImg, 10)

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

    function repairPostion()
    {
        if(speed == moveStep())
        {
            var less = document.body.clientWidth - (1 + moveStep()) * moveStep()/2
            // console.log('less: ', less)
            banner_container.style.left = eval(parseInt(banner_container.style.left) - less) + 'px'
            clearInterval(velocity)
            showTip()
            // console.log('banner_container.style.left: ',banner_container.style.left)
            // console.log('run the ', nth_run +'th')
        }
    }

    var speed = 1
    function moveImg()
    {
        // must be in real time to get img_7_object.style.left value
        var banner_move_range = (banner_child.length-1) * -document.body.clientWidth
        // console.log('speed: ',speed, '/', 'banner_wid: ', document.body.clientWidth, '/', 'range: ', banner_move_range)
        // console.log('banner_container.position: ', position)
        banner_container.style.left = eval(parseInt(banner_container.style.left) - speed) + 'px'
        if(parseInt(banner_container.style.left) > banner_move_range)
        {
            // console.log('after_move: ', banner_container.style.left)
            // var less = document.body.clientWidth - -parseInt(banner_container.style.left)
            repairPostion()
        }
        else
        {
            clearInterval(velocity)
            // clearInterval(tempo)
            banner_container.style.left = 0 + 'px'
            // nth_img = 1
            console.log('out range, stop velocity, but tempo running also')
        }
        speed += 1
        console.log('\n')
    }
    nth_img++
    return moveImg
}

function showTip()
{
    if(nth_img>banner_child.length-1)
    {
        nth_img = banner_child.length-(banner_child.length-1)
        // console.log('current the', nth_img, 'th img vs', banner_child.length)
        document.querySelectorAll('.banner-tip')[nth_img-1].style.display = ''
        // console.log('dis',dis)
    }
    else
    {
        // console.log('current the', nth_img +'th img')
        document.getElementsByClassName('banner-tip')[nth_img-1].style.display = ''
        // console.log('dis',dis)
    }
}


leo = '-'
abc = '-3'
function je()
{
    console.log('>>>>>>', leo + abc)
}
je()

// var kris = document.getElementById('kris')
// var jessie = document.getElementById('jessie')
// var s
// kris.addEventListener
// (
//     'touchstart',
//     function touchStart(start)
//     {   
//         s = start.touches[0].clientX
//         console.log('now',jessie.style.left)
//     }
// )
// var xxx = 0

// kris.addEventListener
// (
//     'touchmove', 
//     function touchMove(move)
//     {
//         m = move.touches[0].clientX
//         n = s - m
//         // console.log('>>>:',jessie.style.left ,'-', n)
//         var tempX = xxx - n
//         jessie.style.left = tempX + 'px'
//     }
// )

// kris.addEventListener
// (
//     'touchend',
//     function touchEnd(end)
//     {   
//         // var bodyWid = document.body.clientWidth
//         e = end.changedTouches[0].pageX
//         n = s - e
//         xxx = xxx - n
//         console.log('end-postion:', xxx)

//         if(n>30)
//         {
//             moveImg = move()
//             moveImg('-')
//         }
//     }
// )

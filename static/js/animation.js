// console.log('/=== base set ===/')
// // get page_id
// var page_id = document.getElementsByTagName('body')[0].getAttribute('page_id')
// console.log('base.js has get page_id:', page_id)


// after page load, start moveImg
// setInterval(function, milliseconds, param1, param2, ...)
if(page_id == 'index')
{
    tempo = setInterval(move, 6000)
}
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


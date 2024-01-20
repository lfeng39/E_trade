// console.log('/=== base set ===/')
// // get page_id
// var page_id = document.getElementsByTagName('body')[0].getAttribute('page_id')
// console.log('base.js has get page_id:', page_id)


// after page load, start moveImg
// setInterval(function, milliseconds, param1, param2, ...)
if(page_id == 'index')
{
    tempo = setInterval(move, 6000)
    // console.log('var_nth_img',nth_img)
    function stop()
    {
        clearInterval(tempo)
    }
}

// document.getElementsByClassName('banner-mini')[0].children[0].style.background = '#fff'

var nth_img = 1
function move()
{

    // setInterval(function, milliseconds, param1, param2, ...)
    var velocity = setInterval(moveImg, 10)
    // if(parseInt(banner_container.style.left) == (banner_child.length-1) * -document.body.clientWidth)
    // {
    //     console.log('000000000',parseInt(banner_container.style.left))
    //     nth_img = 1
    // }
    // else
    // {
    //     nth_img += 1
    // }
    // document.getElementsByClassName('banner-mini')[0].children[nth_img-1].className = 'banner-mini-focus'
    
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
        var banner_move_range = (banner_child.length-2) * -document.body.clientWidth
        banner_container.style.left = eval(parseInt(banner_container.style.left) - speed) + 'px'
        if(parseInt(banner_container.style.left) > banner_move_range)
        {
            repairPostion()
        }
        else
        {
            clearInterval(velocity)
            banner_container.style.left = 0 + 'px'
            // nth_img -= 1
            console.log('out range, stop velocity, but tempo running also',nth_img)
        }
        speed += 1
        console.log('\n')
    }
    
    // return moveImg
    nth_img += 1
    if(nth_img<5)
    {
        console.log('_nth_img',nth_img,parseInt(document.getElementById('banner-container').style.left))
        console.log('var_nth_code',banner_container.children[nth_img-1].getAttribute('code'))
        var banner_mini = document.getElementsByClassName('banner-mini')[0].children[nth_img-2].className = ''
        var banner_mini = document.getElementsByClassName('banner-mini')[0].children[nth_img-1].className = 'banner-mini-focus'
        // var banner_mini = document.getElementsByClassName('banner-mini')[0].children[nth_img-0].className = ''
        // var banner_mini = document.getElementsByClassName('banner-mini')[0].children[nth_img+1].className = ''
        console.log('banner_mini',banner_mini)
        
    }
    else
    {
        nth_img = 1
        console.log('5_nth_img',nth_img,parseInt(document.getElementById('banner-container').style.left))
        console.log('var_nth_img',banner_container.children[nth_img-1].getAttribute('code'))
        var banner_mini = document.getElementsByClassName('banner-mini')[0].children[nth_img+2].className = ''
        var banner_mini = document.getElementsByClassName('banner-mini')[0].children[nth_img-1].className = 'banner-mini-focus'
        // nth_img -= 1
        console.log('reset_nth_img',nth_img)
    }
    // if(parseInt(banner_container.style.left) == (banner_child.length-2) * -document.body.clientWidth)
    // {
    //     console.log('000000000',parseInt(banner_container.style.left))
    //     // clearInterval(velocity)
    //     nth_img = 1
    //     console.log('reset_nth_img',nth_img)

    // }
}

function showTip()
{
    if(nth_img>banner_child.length-1)
    {
        nth_img = banner_child.length-(banner_child.length-1)
        // console.log('current the', nth_img, 'th img vs', banner_child.length)
        document.querySelectorAll('.banner-tip')[nth_img-1].style.display = ''
        // console.log('dis',nth_img)
    }
    else
    {
        // console.log('current the', nth_img +'th img')
        document.getElementsByClassName('banner-tip')[nth_img-1].style.display = ''
        // console.log('dis',nth_img)
    }
}


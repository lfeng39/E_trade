window.addEventListener('load', function()
    {
        var p1 = document.getElementById('us')
        // console.log(p1)

        var btn = document.getElementById('btn')
        btn.addEventListener('click', function()
            {

                p1.innerText = 'Kris'
            }
        )
    }
)

window.onload = function()
{
    var bodyWid = document.body.clientWidth
    var widB09YLLXKDT = document.getElementById('B09YLLXKDT').clientWidth * 0.6
    var widB09YLKWBMV = document.getElementById('B09YLKWBMV').clientWidth * 0.6
    var widB09KG4R3YR = document.getElementById('B09KG4R3YR').clientWidth * 0.6
    var heiB09YLLXKDT = widB09YLLXKDT + 'px'
    var heiB09YLKWBMV = widB09YLKWBMV + 'px'
    var heiB09KG4R3YR = widB09KG4R3YR + 'px'
    if(bodyWid < 1280)
    {
        document.getElementById('B09YLLXKDT').style.height = heiB09YLLXKDT
        document.getElementById('B09YLKWBMV').style.height = heiB09YLKWBMV
        document.getElementById('B09KG4R3YR').style.height = heiB09KG4R3YR
    }
}        

function myfunction()
{
    console.log(document.body.clientWidth)
    var bodyWid = document.body.clientWidth
    var widB09YLLXKDT = document.getElementById('B09YLLXKDT').clientWidth * 0.6
    var widB09YLKWBMV = document.getElementById('B09YLKWBMV').clientWidth * 0.6
    var widB09KG4R3YR = document.getElementById('B09KG4R3YR').clientWidth * 0.6
    var heiB09YLLXKDT = widB09YLLXKDT + 'px'
    var heiB09YLKWBMV = widB09YLKWBMV + 'px'
    var heiB09KG4R3YR = widB09KG4R3YR + 'px'
    if(bodyWid < 1280)
    {
        document.getElementById('B09YLLXKDT').style.height = heiB09YLLXKDT
        document.getElementById('B09YLKWBMV').style.height = heiB09YLKWBMV
        document.getElementById('B09KG4R3YR').style.height = heiB09KG4R3YR
    }
}

window.addEventListener("resize", myfunction);

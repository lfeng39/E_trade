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
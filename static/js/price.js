// ================================================//
// set price format, big int small float, no point //
// ================================================//

// var price_symbol = document.getElementsByTagName('span')[0].children[0].textContent
// var price_int = document.getElementsByTagName('span')[0].children[1].textContent
// var price_float = document.getElementsByTagName('span')[0].children[2].textContent
// var get_price_float_all = document.querySelectorAll('.price-float')
// var get_price_int_all = document.querySelectorAll('.price-int')
// how many price count
// console.log('get_price_float_all', get_price_float_all.length)

// for(i = 0; i < get_price_float_all.length; i++)
// {
//     var price_split = get_price_int_all[i].textContent.split('.')
//     console.log(price_split)
//     // get_price_int_all[i].innerHTML = '<h2>'+price_split[0]+'</h2>'
//     get_price_int_all[i].textContent = price_split[0]
//     get_price_float_all[i].textContent = price_split[1]
// }

// if(page_id == 'products' || page_id == 'listing')
// {
// get price_obj by className
var price_obj = document.getElementsByClassName('price')
if(price_obj.length != 0)
{
    console.log('price_obj_all', price_obj.length)
    console.log('price_int', price_obj[0].getElementsByClassName('price-int')[0].textContent.split('.'))
    for(i = 0; i < price_obj.length; i++)
    {
        var price_split = price_obj[i].getElementsByClassName('price-int')[0].textContent.split('.')
        price_obj[i].getElementsByClassName('price-int')[0].textContent = price_split[0]
        price_obj[i].getElementsByClassName('price-float')[0].textContent = price_split[1]
    }
}
else
{
    console.log('price_obj_???', price_obj.length, price_obj)
}







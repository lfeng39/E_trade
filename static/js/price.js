
// set price format, big int small float, no point 
var get_price_float_all = document.querySelectorAll('.price_float')
var get_price_int_all = document.querySelectorAll('.price_int')
// how many price count
console.log('get_price_float_all', get_price_float_all.length)

for (i = 0; i < get_price_float_all.length; i++)
{
    var price_split = get_price_float_all[i].textContent.split('.')
    console.log(price_split)
    get_price_float_all[i].textContent = price_split[0]
    get_price_int_all[i].textContent = price_split[1]
}









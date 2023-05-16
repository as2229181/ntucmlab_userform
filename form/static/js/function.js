$(document).ready(function(){
    $("#sample").on('input',function(){
        let number = parseInt($('#sample').val());
        console.log('number');
        if (isNaN(number) ){
            $('#total-price').text(0);
            return false;
        }
        else{
            let price = number * 4650;
            $('#total-price').text(price);}
    })
})
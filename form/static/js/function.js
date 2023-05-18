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
    $("#sample-serum , #sample-blood ") .on('input',function(){
        let serum = parseInt($('#sample-serum').val());
        let blood = parseInt($('#sample-blood').val());
        if (isNaN(serum) && isNaN(blood)) {
            $('#sc-total-price').text(0);
          } else if (isNaN(serum)) {
            let price = blood * 450;
            $('#sc-total-price').text(price);
          } else if (isNaN(blood)) {
            let price = serum * 110;
            $('#sc-total-price').text(price);
          } else {
            let price = serum * 110 + blood * 450;
            $('#sc-total-price').text(price);
          }
            return false;
    })
    $(".pc").on('input',function(){
        let a =parseInt($('#sample-pc-a').val());
        let b =parseInt($('#sample-pc-b').val());
        let c =parseInt($('#sample-pc-c').val());
        let d =parseInt($('#sample-pc-d').val());
        let e =parseInt($('#sample-pc-e').val());
        let f =parseInt($('#sample-pc-f').val());
        let g =parseInt($('#sample-pc-g').val());
        let h =parseInt($('#sample-pc-h').val());
        let i =parseInt($('#sample-pc-i').val());
        let j =parseInt($('#sample-pc-j').val());
        let k =parseInt($('#sample-pc-k').val());
        a = isNaN(a) ? 0 : a;
        b = isNaN(b) ? 0 : b;
        c = isNaN(c) ? 0 : c;
        d = isNaN(d) ? 0 : d;
        e = isNaN(e) ? 0 : e;
        f = isNaN(f) ? 0 : f;
        g = isNaN(g) ? 0 : g;
        h = isNaN(h) ? 0 : h;
        i = isNaN(i) ? 0 : i;
        j = isNaN(j) ? 0 : j;
        k = isNaN(k) ? 0 : k;
        let price_in_sch = a * 60 +b * 60+ c * 70+ d * 60+ e * 200+ f * 100+ g * 70+ h * 100+ i * 550+ j * 150+ k * 150
        $('#pc-total-price-in-sch').text(price_in_sch);
        let price_out_sch = a * 70 +b * 70+ c * 85+ d * 70+ e * 215+ f * 140+ g * 85+ h * 140+ i * 850+ j * 200+ k * 200
        $('#pc-total-price-out-sch').text(price_out_sch);
        let price_out_ind = a * 140 +b * 110+ c * 130+ d * 110+ e * 300+ f * 200+ g * 120+ h * 200+ i * 1100+ j * 280+ k * 280
        $('#pc-total-price-ind').text(price_out_ind);
       
    })





})
$(document).ready(function(){
    $("#mus , #rat, #discount").on('input',function(){
        let mus = parseInt($('#mus').val());
        let rat = parseInt($('#rat').val());
        let discount =parseInt($('#discount').val())/100;
        let taxChecked = $('#tax:checked').length > 0;
        if (!taxChecked){
            if (isNaN(mus) && isNaN(rat) ){
                $('#total-price').text(0);
            } else if (isNaN(mus)) {
              let price = Math.ceil((rat * 3020)*discount);
              $('#total-price').text(price);
            }else if (isNaN(rat)) {
              let price = Math.ceil((mus * 4650)*discount);
              $('#total-price').text(price);
            }
            else{
                let price = Math.ceil((mus * 4650 + rat * 3020)*discount);
                $('#total-price').text(price);
              }
                return false;}
        else{
          if (isNaN(mus) && isNaN(rat) ){
            $('#total-price').text(0);
          } 
        else if (isNaN(mus)) {
          let price = Math.ceil((rat * 3020)*discount*1.05);
          $('#total-price').text(price);
        }else if (isNaN(rat)) {
          let price = Math.ceil((mus * 4650)*discount*1.05);
          $('#total-price').text(price);
        }
        else{
          let price = Math.ceil((mus * 4650 + rat * 3020)*discount*1.05);
          $('#total-price').text(price);
        }
          return false;}
    });
    $("#no").on('blur', function() {
      let form_number = $(this).val(); // 獲取輸入框的值
      let form_type = $(this).attr('form-type')
      if (form_type === "QC"){
      if (form_number.length === 10 && form_number.charAt(4) === form_type.charAt(0) && form_number.charAt(5) === form_type.charAt(1)) {
        // 如果長度等於 10，啟用提交按鈕
        $("#submitBtn").prop("disabled", false);
      } else {
        // 如果長度不等於 10，禁用提交按鈕
        $("#submitBtn").prop("disabled", true);
        alert("編號格式輸入錯誤");
      }
      } else if(form_type ==="PC" ){
        if (form_number.length === 9 && form_number.charAt(4) === form_type.charAt(0)){
          $("#submitBtn").prop("disabled", false);
        }
        else {
          // 如果長度不等於 9，禁用提交按鈕
          $("#submitBtn").prop("disabled", true);
          alert("編號格式輸入錯誤");
      }
    } 
    });

    



    $("#sample-serum , #sample-blood, #discount ") .on('input',function(){
        let serum = parseInt($('#sample-serum').val());
        let blood = parseInt($('#sample-blood').val());
        let discount =parseInt($('#discount').val())/100;
        let taxChecked = $('#tax:checked').length > 0;
        if (!taxChecked){
        if (isNaN(serum) && isNaN(blood)) {
            $('#sc-total-price').text(0);
          } else if (isNaN(serum)) {
            let price = Math.ceil((blood * 450) *discount);
            $('#sc-total-price').text(price);
          } else if (isNaN(blood)) {
            let price = Math.ceil((serum * 110)* discount);
            $('#sc-total-price').text(price);
          } else {
            let price = Math.ceil((serum * 110 + blood * 450)*discount);
            $('#sc-total-price').text(price);
          }
            return false;}
        else{
          if (isNaN(serum) && isNaN(blood)) {
            $('#sc-total-price').text(0);
          } else if (isNaN(serum)) {
            let price = Math.ceil((blood * 450)*discount*1.05);
            $('#sc-total-price').text(price);
          } else if (isNaN(blood)) {
            let price = Math.ceil((serum * 110)*discount*1.05);
            $('#sc-total-price').text(price);
          } else {
            let price = Math.ceil((serum * 110 + blood * 450)*discount*1.05);
            $('#sc-total-price').text(price);
          }
            return false;
        }    
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
        let l =parseInt($('#sample-pc-l').val());
        let discount =parseInt($('#discount').val())/100;
        let taxChecked = $('#tax:checked').length > 0;
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
        l = isNaN(l) ? 0 : l;
        discount = isNaN(discount) ? 0 : discount;
        console.log(discount);
        if (!taxChecked){
            let price_in_sch = Math.ceil((a * 60 +b * 60+ c * 70+ d * 60+ e * 200+ f * 100+ g * 70+ h * 100+ i * 550+ j * 150+ k * 150+ l * 200)*discount);
            $('#pc-total-price-in-sch').text(price_in_sch);
            let price_out_sch = Math.ceil((a * 70 +b * 70+ c * 85+ d * 70+ e * 215+ f * 140+ g * 85+ h * 140+ i * 850+ j * 200+ k * 200+ l * 200)*discount);
            $('#pc-total-price-out-sch').text(price_out_sch);
            let price_out_ind = Math.ceil(a * 140 +b * 110+ c * 130+ d * 110+ e * 300+ f * 200+ g * 120+ h * 200+ i * 1100+ j * 280+ k * 280+ l * 200);
            $('#pc-total-price-ind').text(price_out_ind);
            }
        else {
            let price_in_sch = Math.ceil((a * 60 +b * 60+ c * 70+ d * 60+ e * 200+ f * 100+ g * 70+ h * 100+ i * 550+ j * 150+ k * 150+ l * 200)*discount*1.05);
            $('#pc-total-price-in-sch').text(price_in_sch);
            let price_out_sch = Math.ceil((a * 70 +b * 70+ c * 85+ d * 70+ e * 215+ f * 140+ g * 85+ h * 140+ i * 850+ j * 200+ k * 200+ l * 200)*discount*1.05);
            $('#pc-total-price-out-sch').text(price_out_sch);
            let price_out_ind = Math.ceil((a * 140 +b * 110+ c * 130+ d * 110+ e * 300+ f * 200+ g * 120+ h * 200+ i * 1100+ j * 280+ k * 280+ l * 200)*1.05);
            $('#pc-total-price-ind').text(price_out_ind);
        }
    }) 
})

$(document).on('click', '.delete-but', function() {
  let id = $(this).attr('data-id')
  let form_type =$(this).attr('data-formtype')
    $.ajax({
      url:'/form/delete_form',
      data:{
        'id':id,
        'form_type':form_type
      },
      datatype:'json',
      
      success:function(response){
        if(response.data){
        $('#form_table').html(response.data);}
        else {
          alert("請先關閉檔案再刪除");
          window.location.reload();
        }
      }
    })
})
$(document).on('click', '.update-but', function() {
  let id = $(this).attr('data-id')
  let form_type =$(this).attr('data-formtype')
    $.ajax({
      url:'/form/update_pay',
      data:{
        'id':id,
        'form_type':form_type
      },
      datatype:'json',
      success:function(response){
        $('#form_table').html(response.data)
      }
    })
})



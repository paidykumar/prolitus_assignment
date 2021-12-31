$(document).ready(function () {
var product = $('.product_template_id').val();

 var settings = {
          "url": "/get_product_config/"+product,
          "method": "POST",
          "headers": {
            "Content-Type": "application/json"
          },
          "data": JSON.stringify({"jsonrpc":"2.0","params":{}}),

        };


 var launch_settings = {
          "url": "/auto_check_is_launched/"+product,
          "method": "POST",
          "headers": {
            "Content-Type": "application/json"
          },
          "data": JSON.stringify({"jsonrpc":"2.0","params":{}}),

        };

        $.ajax(settings).done(function (sub_response) {
        var x = setInterval(function() {
        var launch_date = new Date(sub_response.result.response.launch_date).getTime();

        var active =sub_response.result.response.active
        var launch = sub_response.result.response.is_launched
        var add_cart = document.getElementById("add_to_cart")

        var now = new Date().getTime();
        var distance = launch_date - now;
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);
        if(active){
             if(launch){ }
             else{
                     document.getElementById("product_timer").innerHTML = days + "D:" + hours + "h:"
                     + minutes + "m:" + seconds + "s";
                     $("#add_to_cart").attr("style", "display:none !important")
              }
        }


         if (distance < 0) {
                clearInterval(x);
                document.getElementById("product_timer").innerHTML = "";
                 $.ajax(launch_settings).done(function (sub_response) {});
//                add_cart.style.display = "block";
          }


        }, 1000);


        });




});


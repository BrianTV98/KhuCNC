$(document).ready(function () {
// Click
        var c,d;
        var arr = [];

         var object = {
            from: 2003,
            to: 2010
        };

        $(".add").click(function(){
            console.log("1");
        })


        var objectStringify = JSON.stringify(object);
            $(".add").click(function (e) {
                 e.preventDefault();
                 console.log("1");

                var a = $("#example1").val();
                var b = $("#example2").val();

                console.log(a);
                console.log(b);

                $.ajax({
                    method: "POST",
                    url: "http://192.168.1.26:8000/api/khucnc/thongkedautu",
                    headers: {
                    'Content-Type': 'application/json; charset=utf8'
                },
                data: JSON.stringify(object),
                success: function (data) {
                    var i = 0;
                    $.each(data, function (key, value) {
                        arr[i++] = value;
                    });
                    console.log("1",arr);
                    console.log(arr[2]);
                    console.log(arr[3]);
                    $("#soluong").val(arr[2]);
                    $("#vondautu").val(arr[3]);

                     arr.map((val) => {
                          $(` <span> ${arr[2]} </span>`).appendTo(".modal-1 .list-group .soloing");
                     });
                     arr.map((val) => {
                          $(` <span> ${arr[3]} </span>`).appendTo(".modal-1 .list-group .vaunt");
                     });

                }
            });
        });


});
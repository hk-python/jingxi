$(document).ready(function(){

//	修改购物车中商品的数量
	var reduce_num = document.getElementsByClassName("reduce_num")
	var add_num = document.getElementsByClassName("add_num")

    for(var i=0;i<add_num.length;i++){
        add_num = add_num[i]
        add_num.addEventListener("click",function(){
            pid = this.getAttribute("ga")
            console.log(pid)
            $.post("/sub/",{"productid":pid},function(data){
                if(data.status == "success"){
//                    添加成功，就改变中间的span标签的数量
                    console.log(data.data)
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid+"price").innerHTML = "￥"+data.price
                }else{
//                视图中返回的-1 表示未登录  所有不能直接添加购物车
                    if(data.data == -1){
                    	window.location.href = "http://127.0.0.1:8000/sqlapp/login/"
                    }
                }
            })
        },false)
    }


    for(var i=0;i<reduce_num.length;i++){
        reduce_num = reduce_num[i]
        reduce_num.addEventListener("click",function(){
            pid = this.getAttribute("ga")
            $.post("/add/",{"productid":pid},function(data){
                if(data.status == "success"){
//                    添加成功，就改变中间的span标签的数量
                    document.getElementById(pid).innerHTML = data.data
                    document.getElementById(pid+"price").innerHTML = "￥"+data.price
                    if(data.data == 0){
//                        window.location.href = "http://127.0.0.1:8000/sqlapp/cart/"
                        var li = document.getElementById(pid+"li")
                        li.parentNode.removeChild(li)
                    }
                }
            })
        },false)
    }
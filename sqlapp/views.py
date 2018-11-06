from django.shortcuts import render
from sqlapp.models import us,seller,carts,address,indent,indentss
from django.http import HttpResponse
import random
from django.core.paginator import Paginator

# Create your views here.
def boss(request):
    sell=seller.objects.filter()
    return render(request,"BOSS.html",{"sell":sell})

def cart(request):
    dllo=0
    username = request.session.get("username")
    ca=carts.objects.filter(causname=username)
    for cat in ca:
        dllo+=int(cat.cartsellnum)*int(cat.cartjiage)
    #购物车中所有商品信息和小计
    return render(request, "cart.html",{"ca":ca,"username":username,"dllo":dllo})

def sub(request):
    # str=""
    # productid=request.POST.get("productid")
    # username = request.session.get("username")
    # ca=carts.objects.get(causname=username)
    # sidlist=ca.cartsid(";")
    # index=sidlist.index(productid)
    # num=ca.cartssellnum.split(";")
    # nums=num[index]-1
    # num.insert(index,nums)
    # for i in num:
    #     str+=str(i)+";"
    # carts.objects.get(causname=username).update(cartsellnum=str)
    # return render()
    pass
def add(request):
    pass


def jiadian(request):

    return render(request,"jiadian.html")

def shouji(request,pagenum):
    username = request.session.get("username")
    se=seller.objects.filter(selltype="phone")
    pi=Paginator(se,8)
    pnums=pi.num_pages
    page= pi.page(pagenum)
    pnum=page.number
    sslist=page.object_list
    return render(request,"phone.html",{"username":username,"se":se,"pnum":pnum,"pnums":pnums,"sslist":sslist})

def wt(request):
    return render(request,"wt.html")

def shuma(request):
    return render(request,"shuma.html")

def diannao(request):
    return render(request,"diannao.html")

def bg(request):
    return render(request,"bg.html")


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request,"register.html")

def regcheck(request):
    username1 = request.POST.get("username")
    password = request.POST.get("password")
    tel=request.POST.get("tel")
    user=us(username=username1,password=password,usertel=tel)
    user.save()
    return render(request,"BOSS.html",{"username":username1})

def check(request):
    ss = []
    username=request.POST.get("username")
    password = request.POST.get("password")
    us1 = us.objects.all()
    for us2 in us1:
        ss.append(us2.username)
    if username in ss:
        us3 = us.objects.get(username=username)
        if password == us3.password:
            request.session["username"]=username
            request.session["password"] = password
            request.session.set_expiry(86400)
            return  render(request,"BOSS.html",{"username":username})
        else:
            return HttpResponse("账号或密码错误！")
    else:
        return HttpResponse("账号或密码错误！")

def cart2(request):
    username = request.session.get("username")
    try:
        ad=address.objects.get(uname=username)
        addname=ad.addname
        addres=ad.addres
        addtel=ad.addtel
        addpost=ad.addpost
        dllo=0
        ca=carts.objects.filter(causname=username)
        for cat in ca:
            dllo+=int(cat.cartsellnum)*int(cat.cartjiage)
        cd=len(ca)
        return render(request,"cart2.html",{"username":username,"addname":addname,"addres":addres,"addtel":addtel,"addpost":addpost,"ca":ca,"cd":cd,"dllo":dllo})
    except:
        addname=""
        addres=""
        addtel=""
        addpost=""
        dllo = 0
        ca=carts.objects.filter(causname=username)
        for cat in ca:
            dllo+=int(cat.cartsellnum)*int(cat.cartjiage)
        cd=len(ca)
        return render(request, "cart2.html",
                      {"username": username, "addname": addname, "addres": addres, "addtel": addtel, "addpost": addpost,
                       "ca": ca, "cd": cd, "dllo": dllo})

def xiugai(request):
    username = request.session.get("username")
    uname=request.POST.get("uname")
    cmbProvince=request.POST.get("cmbProvince")
    cmbCity=request.POST.get("cmbCity")
    cmbArea=request.POST.get("cmbArea")
    addres=request.POST.get("address")
    tel=request.POST.get("tel")
    apost=request.POST.get("apost")
    ads=str(cmbProvince)+str(cmbCity)+str(cmbArea+addres)
    address(uname=username,addname=uname,addres=ads,addtel=tel,addpost=apost).save()

    ad = address.objects.get(uname=username)
    addname = uname
    addres = ads
    addtel = tel
    addpost = apost
    dllo = 0
    ca = carts.objects.filter(causname=username)
    for cat in ca:
        dllo += int(cat.cartsellnum) * int(cat.cartjiage)
    cd = len(ca)
    return render(request, "cart2.html",
                  {"username": username, "addname": addname, "addres": addres, "addtel": addtel, "addpost": addpost,
                   "ca": ca, "cd": cd, "dllo": dllo})


def cart3(request):
    username = request.session.get("username")
    sui=""
    caid=""
    ca=carts.objects.filter(causname=username)
    for cat in ca:
        caid+=str(cat.cartsid)+";"
    for i in range(1, 17):
        sui += str(random.randrange(10))
    indent(inname=username,indsellid=sui,inseid=caid).save()
    return render(request,"cart3.html",{"username":username})

# def delcart(request,caid):
#     username = request.session.get("username")
#     caas=carts.objects.filter(causname=username)
#     ca1=caas.get(cartid=caid)
#     print(ca1)
#     return render(request,"BOSS.html")


def user(request):
    username = request.session.get("username")
    try:
        addd=address.objects.get(uname=username)
        addre = addd.addres
        adtel = addd.addtel
        addname = addd.addname
        return render(request, "user.html", {"username": username, "addre": addre, "adtel": adtel, "addname": addname})
    except:
        addre = ""
        adtel = ""
        addname = ""
        return render(request,"user.html",{"username":username,"addre":addre,"adtel":adtel,"addname":addname})


def addr(request):
    username = request.session.get("username")
    try:
        ads=address.objects.get(uname=username)
        adname=ads.addname
        addre=ads.addres
        adtel=ads.addtel

        dllo = 0
        username = request.session.get("username")
        ca = carts.objects.filter(causname=username)
        for cat in ca:
            dllo += int(cat.cartsellnum) * int(cat.cartjiage)
        return render(request,"indent.html",{"username":username,"addre":addre,"adtel":adtel,"adname":adname,"ca":ca,"dllo":dllo})
    except:
        adname = ""
        addre = ""
        adtel = ""
        s = ""
        dllo = ""
        return render(request, "indent.html",
                      {"username": username, "addre": addre, "adtel": adtel, "adname": adname, "s": s, "dllo": dllo})

def inaddress(request):
    username = request.session.get("username")
    try:
        ad=address.objects.get(uname=username)
        addname=ad.addname
        addres=ad.addres
        addtel=ad.addtel
        return render(request,"inaddress.html",{"addname":addname,"addres":addres,"addtel":addtel})
    except:
        addname=""
        addres=""
        addtel=""
        return render(request, "inaddress.html", {"addname": addname, "addres": addres, "addtel": addtel})


def addelete(request):
    username = request.session.get("username")
    address.objects.get(uname=username).delete()
    try:
        ad=address.objects.get(uname=username)
        addname=ad.addname
        addres=ad.addres
        addtel=ad.addtel
        return render(request,"inaddress.html",{"addname":addname,"addres":addres,"addtel":addtel})
    except:
        addname=""
        addres=""
        addtel=""
        return render(request, "inaddress.html", {"addname": addname, "addres": addres, "addtel": addtel})

def addalrt(request):
    username = request.session.get("username")


def wechatpay(request):
    username = request.session.get("username")
    sui=""
    caid=""
    ca=carts.objects.filter(causname=username)
    for cat in ca:
        caid+=str(cat.cartsid)+";"
    print(caid)
    for i in range(1, 17):
        sui += str(random.randrange(10))
    indent(inname=username,indsellid=sui,inseid=caid).save()
    return render(request,"wechatpay.html",{"username":username})

def comm(request):
    return render(request,"comm.html")

def comms(request,sellid):
    ses=seller.objects.get(sellid=sellid)
    return render(request,"comms.html",{"ses":ses})

def tijiao(request,sellid):
    username = request.session.get("username")
    sed=seller.objects.get(sellid=sellid)
    cauname=sed.sellname
    caimg=sed.sellimg
    cajiage=sed.selljiage
    cacolor=sed.sellcolor
    casize=sed.sellsize
    canum="1"
    carts(cartsid=sellid,cartname=cauname,causname=username,cartimg=caimg,cartjiage=cajiage,cartcolor=cacolor,cartsize=casize,cartsellnum=canum).save()
    return render(request,"secus.html")

def secus(request):
    return render(request,"secus.html")

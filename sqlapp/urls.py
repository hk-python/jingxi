from django.conf.urls import url
from sqlapp import views


urlpatterns = [
    url(r'^BOSS/$',views.boss),
    url(r'^jiadian/$',views.jiadian),
    url(r'^shouji/(\d+)/$',views.shouji),
    url(r'^wt/$',views.wt),
    url(r'^shuma/$',views.shuma),
    url(r'^diannao/$',views.diannao),
    url(r'^bg/$',views.bg),
    url(r'^login/$',views.login),
    url(r'^register/$',views.register),
    url(r'^regcheck/$',views.regcheck),
    url(r'^check/$',views.check),
    url(r'^cart/$',views.cart),
    url(r'^cart2/$',views.cart2),
    url(r'^cart3/$',views.cart3),
    url(r'^user/$',views.user),
    url(r'^addr/$',views.addr),
    url(r'^inaddress/$',views.inaddress),
    url(r'^addalrt/$',views.addalrt),
    url(r'^addelete/$',views.addelete),
    url(r'^sub/$',views.sub),
    url(r'^add/$',views.add),
    url(r'^wechatpay/$',views.wechatpay),
    url(r'^comm/$',views.comm),
    url(r'^comms/(\d+)/$',views.comms),
    url(r'^tijiao/(\d+)/$',views.tijiao),
    url(r'^secus/$',views.secus),
    url(r'^xiugai/$',views.xiugai),
    # url(r'^delcart/(\d+)/$',views.delcart),

]
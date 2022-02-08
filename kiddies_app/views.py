from django.shortcuts import render,redirect
from kiddies_app.models import tbllogin,tblproduct,tblcustomer,tblreview,tblcomplaint,tblcart,tblorder,tblpayment,tblorder_details
from django.core.files.storage import FileSystemStorage
import datetime
from django.db.models import Sum
# Create your views here.

def home(request):
    return render(request,"home.html")

    
def login(request):
    return render(request,"login.html")

def login1(request):
    if request.method == 'POST':
        data = tbllogin.objects.all()
        usrname = request.POST.get('username')
        pswd = request.POST.get('password')
        flag = 0
        for d in data:
            if usrname == d.username and pswd == d.password:
                type = d.category
                request.session['userid'] = usrname
                flag = 1
                if type == "Admin" :
                    return redirect('/adminhead/')
                elif type == "Customer" :
                    return redirect('/customerhead/')
                else:
                    return HttpResponse("invalid acc type")
                    if flag == 0:
                        return render(request,"login.html")

def adminhead(request):
    return render(request,"admin-header.html")

def customerhead(request):
    return render(request,"customer-header.html")

def uploadproduct(request):
    return render(request,"upload_product.html")

def uploadproduct1(request):
    if request.method == 'POST':
        data = tblproduct()
        data.product_id="pr"
        data.product_name = request.POST.get('productname')
        data.category = request.POST.get('category')
        data.unit_price = request.POST.get('unitprice')
        data.stock_qty = request.POST.get('stockquantity')
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name,photo)
        uploaded_file_url = fs.url(filename)
        data.photo = uploaded_file_url
        data.size = request.POST.get('size')
        data.colour = request.POST.get('colour')
        data.age_group = request.POST.get('agegroup')
        data.remark = request.POST.get('remark')
        data.save()

        data.product_id = "prdct00" + str(data.id)
        data.save()
        return render(request,"upload_product.html")

def changeprice(request):
    items = tblproduct.objects.all()
    return render(request,"change_price.html",{'prd':items})

def changeprice1(request,id):
    items = tblproduct.objects.get(id=id)
    return render(request,"change_price1.html",{'pr':items})

def changeprice2(request,id):
    data = tblproduct.objects.get(id=id)
    if request.method == 'POST':
        data.unit_price = request.POST.get('unitprice')
        data.save()
        return render(request,"upload_product.html")

def removeproduct(request):
    data = tblproduct.objects.all()
    return render(request,"removeproduct.html",{'rmv':data})

def removeproduct1(request,id):
    data = tblproduct.objects.get(id=id)
    data.delete()
    return redirect('/removeproduct')

def regcustomer(request):
    return render(request,"customer_registration.html")

def regcustomer1(request):
    if request.method == 'POST':
        data = tblcustomer()
        data.cust_id = "ci"
        data.first_name = request.POST.get('firstname')
        data.last_name = request.POST.get('lastname')
        data.address = request.POST.get('address')
        data.pincode = request.POST.get('pincode')
        data.city = request.POST.get('city')
        data.state = request.POST.get('state')
        data.country = request.POST.get('country')
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.save()

        data.cust_id = "cust00" + str(data.id)
        data.save()

        data1 = tbllogin()
        data1.username = data.cust_id
        data1.password = request.POST.get('phone')
        data1.category = "Customer"
        data1.save()
        return render(request,"customer_registration.html")

def category(request):
    return render(request,"category.html")

def viewproduct(request):
    data = tblproduct.objects.filter(category=request.POST.get('category'))
    return render(request,"viewproduct.html",{'prd':data})

def givereview(request):
    data = tblproduct.objects.all()
    return render(request,"viewproduct1.html",{'vw':data})

def givereview1(request,id):
    uid = request.session['userid']
    data = tblproduct.objects.get(id=id)
    return render(request,"givereview.html",{'itm':data, 'uid' :uid })


def givereview2(request):
    if request.method == 'POST':
        data = tblreview()
        data.review_id = "ri"
        data.product_id = request.POST.get('productid')
        data.user_id = request.POST.get('userid')
        data.review = request.POST.get('review')
        now = datetime.datetime.now()
        time = now.strftime("%y-%m-%d")
        data.review_date = time
        data.save()

        data.review_id = "rvw00" + str(data.id)
        data.save()
        return render(request,"givereview.html")

def viewproduct1(request):
    data = tblproduct.objects.all()
    return render(request,"viewproduct2.html",{'cmp':data})

def givecomplaint(request,id):
    uid = request.session['userid']
    data = tblproduct.objects.get(id=id)
    return render(request,"givecomplaint.html",{'itm':data,'uid':uid})

def givecomplaint1(request):
    if request.method == 'POST':
        data = tblcomplaint()
        data.complaint_id = "ci"
        data.product_id = request.POST.get('productid')
        data.user_id = request.POST.get('userid')
        data.complaint = request.POST.get('complaint')
        now = datetime.datetime.now()
        time = now.strftime("%y-%m-%d")
        data.complaint_date = time
        data.save()

        data.complaint_id = "cid00" + str(data.id)
        data.save()
        return render(request,"givecomplaint.html")


def categorycart(request):
    return render(request,"category_cart.html")

def viewprdctcart(request):
    data = tblproduct.objects.filter(category = request.POST.get('category'))
    return render(request,"viewprdct_cart.html",{'prd' : data})

def order(request,id):
    uid = request.session['userid']
    data = tblproduct.objects.get(id = id)
    return render(request,"order.html",{'itm':data, 'uid':uid})

def order1(request):
    if request.method == 'POST':
        data = tblcart()
        data.cart_id = "ci"
        data.user_id = request.POST.get('userid')
        data.product_id = request.POST.get('productid')
        data.quantity = request.POST.get('quantity')
        q = int(request.POST.get('quantity'))
        p = int(request.POST.get('price'))
        amount = int(q * p)
        data.price = amount
        data.status = "pending"
        data.save()

        data.cart_id = "crt00" + str(data.id)
        data.save()
        return render(request,"category_cart.html")

def finishorder1(request):
   data = tblorder()
   data.order_no = request.session['oid']
   data.user_id = request.POST.get('customer_id')
   now = datetime.datetime.now()
   time = now.strftime('%y-%m-%d')
   data.order_date = time
   data.amount=request.POST.get('amount')
   data.payment_mode = request.POST.get('payment')
   data.order_status="pending"
   data.save()
   data1 = tblpayment()
   data1.pay_id = "pi"
   data1.order_no =request.session['oid']
   data1.card_no = request.POST.get('cardno')
   data1.cvv = request.POST.get('cvv')
   data1.mobile_no = request.POST.get('mobileno')
   data1.amt = request.POST.get('amount')
   now = datetime.datetime.now()
   date = now.strftime('%y-%m-%d')
   data1.tran_date = date
   time1 = datetime.datetime.now()
   data1.time = time1
   data1.save()

   data1.pay_id = "pay00" + str(data1.id)
   data1.save()
   del request.session['oid']
   return render(request,"customer-header.html")
def finishorder(request):
    td=request.session['userid']
    oo=request.session['oid']
    amount =tblorder_details.objects.filter(order_no=oo).aggregate(sum=Sum('price'))['sum']
    return render(request,'order1.html',{'u':td,'amt':amount})
      

def reviewcategory(request):
    return render(request,"category-review.html")

def viewprdctreview(request):
    data = tblproduct.objects.filter(category = request.POST.get('category'))
    return render(request,"viewprdct-review.html",{'rvw':data})

def viewreview(request,id):
    data = tblreview.objects.filter(product_id=id)
    return render(request,"viewreview.html",{'vw':data})

def reviewcategory_public(request):
    return render(request,"ctgry-review-public.html")

def viewprdctreview_public(request):
    data = tblproduct.objects.filter(category = request.POST.get('category'))
    return render(request,"viewprdct-review-public.html",{'rvw':data})

def viewreview_public(request,id):
    data = tblreview.objects.filter(product_id=id)
    return render(request,"viewreview-public.html",{'vw':data})

def reviewcategory_admin(request):
    return render(request,"ctgry-review-admin.html")

def viewprdctreview_admin(request):
    data = tblproduct.objects.filter(category = request.POST.get('category'))
    return render(request,"viewprdct-review-admin.html",{'rvw':data})

def viewreview_admin(request,id):
    data = tblreview.objects.filter(product_id=id)
    return render(request,"viewreview-admin.html",{'vv':data})

def complaint_category(request):
    return render(request,"complaint-category.html")

def viewprdct_complaint(request):
    data = tblproduct.objects.filter(category = request.POST.get('category'))
    return render(request,"viewcomplaint-product.html",{'vc':data})

def viewcomplaint(request,id):
    data = tblcomplaint.objects.filter(product_id=id)
    return render(request,"viewcomplaint.html",{'cmp':data})

def placeorder(request):
    data = tblcart.objects.filter(status = "pending").filter(user_id = request.session['userid'])
    return render(request,"placeorder.html",{'itm':data})

def orderdetails(request,id):
    if 'oid' not in request.session:
        
        if request.method == 'POST':
            data = tblcart.objects.get(id=id)
            data1 = tblorder_details()
            data1.order_details_id = "oi"
            data1.user_id = request.POST.get('userid')
            data1.product_id = request.POST.get('productid')
            data1.quantity = request.POST.get('quantity')
            now = datetime.datetime.now()
            date = now.strftime('%y-%m_%d')
            data1.date = date
            data1.price = request.POST.get('price')
            data1.order_no = "na"
            data1.status = "pending"
            data1.save()

            data1.order_details_id = "ordi00" + str(data1.id)
            ordid = "ordno" + str(data1.id)
            data1.order_no = ordid
            request.session['oid']=ordid
            data1.save()
            data.delete()
            return redirect('/placeorder')

    else:
       
        if request.method == 'POST':
            data = tblcart.objects.get(id=id)
            data1 = tblorder_details()
            data1.order_details_id = "oi"
            data1.user_id = request.POST.get('userid')
            data1.product_id = request.POST.get('productid')
            data1.quantity = request.POST.get('quantity')
            now = datetime.datetime.now()
            date = now.strftime('%y-%m_%d')
            data1.date = date
            data1.price = request.POST.get('price')
            data1.order_no = "na"
            data1.status = "pending"
            data1.save()

            data1.order_details_id = "ordi00" + str(data1.id)
            data1.order_no = request.session['oid']
            data1.save()
            data.delete()
            return redirect('/placeorder')
def orderaccept(request,id):
    data = tblcart.objects.get(id=id)
    uid = request.session['userid']
    return render(request,"order_details.html",{'itm':data,'uid':uid})


def orderreject(request,id):
    data = tblcart.objects.get(id=id)
    data.delete()
    return redirect('/placeorder')

def vieworder(request):
    data = tblorder.objects.filter(order_status = "pending")
    return render(request,"vieworder.html",{'vw':data})


def vieworderdetails(request,id):
    data = tblorder_details.objects.filter(order_no=id)
    return render(request,"view_orderdetails.html",{'vw':data})

def detailaccept(request,id):
    data = tblorder_details.objects.get(id=id)
    data.status = "Order Accepted"
    data.save()
    
    count = tblorder_details.objects.filter(order_no=data.order_no).filter(status="pending").count()
    if count==0:
        data1=tblorder.objects.get(order_no=data.order_no)
        data1.order_status = "completed"
        data1.save()
    data1 = tblorder_details.objects.filter(order_no=data.order_no).filter(status="pending")

    return render(request,"view_orderdetails.html",{'vw':data1})
    
def detailreject(request,id):
    data = tblorder_details.objects.get(id=id)
    data.status = "Order Rejected"
    data.save()
    return redirect('/adminhead')

def viewpaymentdetails(request,id):
    data = tblpayment.objects.filter(order_no=id)
    return render(request,"viewpayment.html",{'vw':data})

def orderstatus(request):
    data = tblorder.objects.filter(user_id = request.session['userid']).filter(order_status = "completed")
    return render(request,"view_orderstatus.html",{'vw':data})

def vieworderdetails1(request):
    data = tblorder_details.objects.filter(user_id = request.session['userid'])
    return render(request,"view_orderdetails1.html",{'vw':data})
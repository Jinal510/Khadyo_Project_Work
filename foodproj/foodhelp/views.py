

from django.shortcuts import redirect, render
import random
from .models import*
from random import*
from django.core.mail import send_mail

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .paytm import generate_checksum, verify_checksum


def home(request):
    data=AddFood.objects.all()
    adata=Feedback.objects.all()
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=='foodhelper':
            fid=foodhelper.objects.get(user_id=uid)
            return render(request,"foodhelp/index.html", {'uid':uid,'fid':fid,'data':data,'adata':adata})
        else:
            nid=NGO.objects.get(user_id=uid)
            return render(request,"foodhelp/index.html", {'uid':uid,'nid':nid,'data':data,'adata':adata})
        
    else:
        return render(request,"foodhelp/index.html",{'data':data,'adata':adata})

def login(request):
    if "email" in request.session:
        return redirect('home')
    
    else:
        try:
            if request.POST: 
                email=request.POST["email"]
                password=request.POST["password"]
                uid=User.objects.get(email=email,password=password)
                if uid.role=='foodhelper':
                    fid=foodhelper.objects.get(user_id=uid)
                    request.session["email"]=uid.email
                    return redirect('home')
                else:
                    nid=NGO.objects.get(user_id=uid)
                    request.session["email"]=uid.email
                    return redirect('home')
            else:
                return render(request,"foodhelp/login.html")
        except:
            e_msg="Invalid Email or Password"
            return render(request,"foodhelp/login.html",{'e_msg':e_msg})
def register(request):
    if "email" in request.session:
        return redirect('home')
    else:
        if request.POST:
            role=request.POST["role"]
            name=request.POST["name"]
            email=request.POST["email"]
            password=request.POST['password']
            confirmpassword=request.POST['confirmpassword']
            if password == confirmpassword:
                uid=User.objects.create(email=email,password=password,role=role)
                if role=="foodhelper":
                    fid=foodhelper.objects.create(user_id=uid,name=name)
                    s_msg="successfully  account created"
                    return render(request,"foodhelp/login.html",{'s_msg':s_msg,'fid':fid}) 
                else:
                    nid=NGO.objects.create(user_id=uid,name=name)
                    s_msg="successfully  account created"
                    return render(request,"foodhelp/login.html",{'s_msg':s_msg,'nid':nid}) 
            else:
                print("Error: Password and Confirm Password does not exits")
                
        else:
            return render(request,"foodhelp/register.html")
           
def forgot_password(request):
    if request.POST:
        try:
            email=request.POST['email']
            uid=User.objects.get(email=email)
            otp=randint(1111,9999)
            if uid:
                uid.otp=otp
                uid.save()
                send_mail("Forgot Password","Your otp is:"+str(otp),"jinalpatel.learn@gmail.com",[email])
                return render(request,"foodhelp/forgot-repassword.html",{'email':email})
        except:
            e_msg="email does not exist"
            return render(request,"foodhelp/forgot-password.html",{'e_msg':e_msg})
    else:
        return render(request,"foodhelp/forgot-password.html")

def forgot_repassword(request):
    if request.POST:
        email=request.POST['email']
        otp=request.POST['otp']
        newpassword=request.POST['newpassword']
        repassword=request.POST['repassword']

        uid=User.objects.get(email=email)
        if str(otp) == otp:
            if newpassword==repassword:
                uid.password=newpassword
                uid.save()
                return redirect('login')
            else:
                e_msg="Password does not match"
                return render(request,"foodhelp/forgot-repassword.html",{'e_msg':e_msg,'email':email})
        else:
            e_msg="Invalid OTP"
            return render(request,"foodhelp/forgot-repassword.html",{'e_msg':e_msg,'email':email})
    else:
        return render(request,"foodhelp/forgot-repassword.html")

def reset_password(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=='foodhelper':
            fid=foodhelper.objects.get(user_id=uid)
            
            if request.POST:
                email=request.POST['email']
                password=request.POST['password']
                newpassword=request.POST['newpassword']
                repassword=request.POST['repassword']

                uid=User.objects.get(email=email)
                if newpassword==repassword:
                    uid.password=newpassword
                    uid.save()
                    return redirect('login')
                else:
                    e_msg="Password does not match"
                    return render(request,"foodhelp/reset-password.html",{'e_msg':e_msg,'email':email})
            else:
                return render(request,"foodhelp/reset-password.html",{'uid':uid,'fid':fid})
        else:
            nid=NGO.objects.get(user_id=uid)
            
            if request.POST:
                email=request.POST['email']
                password=request.POST['password']
                newpassword=request.POST['newpassword']
                repassword=request.POST['repassword']

                uid=User.objects.get(email=email)
                if newpassword==repassword:
                    uid.password=newpassword
                    uid.save()
                    return redirect('login')
                else:
                    e_msg="Password does not match"
                    return render(request,"foodhelp/reset-password.html",{'e_msg':e_msg,'email':email})
            else:
                return render(request,"foodhelp/reset-password.html",{'uid':uid,'nid':nid})
    else:
        return render(request,"foodhelp/reset-password.html")

def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return redirect('home')
    
    else:
        return redirect('home')

def food_supplier(request):
    data=foodhelper.objects.all()
    if "email" in request.session:
        
        uid=User.objects.get(email=request.session["email"])
        if uid.role=='foodhelper':
            fid=foodhelper.objects.get(user_id=uid)
            data=foodhelper.objects.exclude(id=fid.id)
            return render(request,"foodhelp/food-supplier.html", {'uid':uid,'fid':fid,'data':data})
        else:
            nid=NGO.objects.get(user_id=uid)
            data=foodhelper.objects.all()
            return render(request,"foodhelp/food-supplier.html", {'uid':uid,'nid':nid,'data':data})
    else:
        return render(request,"foodhelp/food-supplier.html", {'data':data})

def profile_food_supplier(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        fid=foodhelper.objects.get(user_id=uid)
       
        return render(request,"foodhelp/profile-food-supplier.html",{'uid':uid,'fid':fid})
    else:
        return redirect('home')

def profile_ngo(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        nid=NGO.objects.get(user_id=uid)
        return render(request,"foodhelp/profile-ngo.html",{'uid':uid,'nid':nid})
    else:
        return redirect('home')
            

def update_profile(request):
    
    if request.POST:
        email=request.POST['email']

        uid=User.objects.get(email=email)
        fid=foodhelper.objects.get(user_id=uid)

        name=request.POST['name']
        lastname=request.POST['lastname']
        contact=request.POST['contact']
        city=request.POST['city']
        area=request.POST['area']

        fid.name=name
        fid.lastname=lastname
        fid.contact=contact
        fid.city=city
        fid.area=area
        fid.save()
        if "profile_pic" in request.FILES:
            profile=request.FILES['profile_pic']
            fid.profile_pic=profile               
            fid.save()

          
            s_msg="successfully profile updated"
            return render(request,"foodhelp/profile-food-supplier.html",{'uid':uid,'fid':fid,'s_msg':s_msg})
        
        else:
            return redirect('home')

def ngo_update_profile(request):
    
    if request.POST:
        email=request.POST['email']

        uid=User.objects.get(email=email)
        nid=NGO.objects.get(user_id=uid)
        name=request.POST['name']
        lastname=request.POST['lastname']
        contact=request.POST['contact']
        
        area=request.POST['area']

        nid.name=name
        nid.lastname=lastname
        nid.contact=contact
      
        nid.area=area
        nid.save()
        if "profile_pic" in request.FILES:
            profile=request.FILES['profile_pic']
            nid.profile_pic=profile               
            nid.save()
            s_msg="successfully profile updated"
            return render(request,"foodhelp/profile-food-supplier.html",{'uid':uid,'nid':nid,'s_msg':s_msg})
            
        else:
            return redirect('home')

def add_food(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        fid=foodhelper.objects.get(user_id=uid)
        if request.POST: 
            
            food_type=UserRole.objects.all()
            foodaddrole=request.POST['foodaddrole']
            person_type_id=UserRole.objects.get(role = foodaddrole)
            
            aid=AddFood.objects.create(
                user_id=uid,
                fid=fid,
                person_type=person_type_id,
                reason=request.POST['reason'],
                foodquantity=request.POST['foodquantity'],
                foodquality=request.POST['foodquality'],
                cooktime=request.POST['cooktime'],
                expirytime=request.POST['expirytime'],
                food_categories=request.POST['food_categories'],
                pickup_address=request.POST['pickup_address'],
                contact_person_name=request.POST['contact_person_name'],
                contact_person_number=request.POST['contact_person_number'],
                zipcode=request.POST['zipcode']
            )

            if 'picture' in request.FILES:
                aid.food_picture=request.FILES['picture']
                aid.save()

                s_msg="Successfully Add Food Post"
                return render(request,"foodhelp/add-food.html",{'uid':uid,'fid':fid,'s_msg':s_msg, 'food_type':food_type})
            else:
                return render(request,"foodhelp/add-food.html",{'uid':uid})
        else:
            return render(request,"foodhelp/add-food.html",{'uid':uid,'fid':fid})
    else:
        return render(request,"foodhelp/add-food.html")
    

def view_food(request):
    data=AddFood.objects.all()
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=='foodhelper':
            fid=foodhelper.objects.get(user_id=uid)
            return render(request,'foodhelp/view-food.html',{'uid':uid,'fid':fid,'data':data})
        else:
            nid=NGO.objects.get(user_id=uid)
            return render(request,'foodhelp/view-food.html',{'uid':uid,'nid':nid,'data':data})
    else:
        
        return render(request,'foodhelp/view-food.html',{'data':data})

def view_food_details(request,pk):
    fooddetails=AddFood.objects.get(id=pk)
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        fid=foodhelper.objects.get(user_id=uid)
        return render(request,'foodhelp/view-food-details.html',{'uid':uid,'fid':fid,'fooddetails':fooddetails})
    elif "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        nid=NGO.objects.get(user_id=uid)
        return render(request,'foodhelp/view-food-details.html',{'uid':uid,'nid':nid,'fooddetails':fooddetails})
    else:
        return render(request,'foodhelp/view-food-details.html',{'fooddetails':fooddetails})

def ngo(request):
    data1=NGO.objects.all()
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=='foodhelper':
            fid=foodhelper.objects.get(user_id=uid)
            data1=NGO.objects.exclude(id=fid.id)
            return render(request,"foodhelp/ngo.html", {'uid':uid,'fid':fid,'data1':data1})
        else:
            nid=NGO.objects.get(user_id=uid)
            data1=NGO.objects.exclude(id=nid.id)
            return render(request,"foodhelp/ngo.html", {'uid':uid,'nid':nid,'data1':data1})
    else:
        return render(request,"foodhelp/ngo.html", {'data1':data1})

def feedback(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=='foodhelper':
            fid=foodhelper.objects.get(user_id=uid)
            if request.POST:
                feedback=request.POST['feedback']
               
                feed=Feedback.objects.create(feedback=feedback,name=fid.name,profile_pic=fid.profile_pic)
                return render(request,"foodhelp/feedback.html",{'uid':uid,'fid':fid,'feedback':feedback,'feed':feed})
            else:
                return render(request,"foodhelp/feedback.html",{'uid':uid,'fid':fid})
        else:
            nid=NGO.objects.get(user_id=uid)
            if request.POST:
                feedback=request.POST['feedback']
                feed=Feedback.objects.create(feedback=feedback,name=nid.name,profile_pic=nid.profile_pic)
                return render(request,"foodhelp/feedback.html",{'feed':feed,'uid':uid,'nid':nid,'feedback':feedback})
            else:
                return render(request,"foodhelp/feedback.html",{'uid':uid,'nid':nid})
    else:
        return render(request,"foodhelp/feedback.html")

def view_feedback(request):
   
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=='foodhelper':
            fid=foodhelper.objects.get(user_id=uid)
            adata=Feedback.objects.all()
            return render(request,'foodhelp/view-feedback.html',{'uid':uid,'fid':fid,'adata':adata})
        else:
            nid=NGO.objects.get(user_id=uid)
            adata=Feedback.objects.all()
            return render(request,'foodhelp/view-feedback.html',{'uid':uid,'nid':nid,'adata':adata})

def contactus(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        if uid.role=='foodhelper':
            fid=foodhelper.objects.get(user_id=uid)
            return render(request,'foodhelp/contactus.html',{'uid':uid,'fid':fid})
        else:
            
            nid=NGO.objects.get(user_id=uid)
            return render(request,'foodhelp/contactus.html',{'uid':uid,'nid':nid})


def paytmhome(request):
    if "email" in request.session:
        uid = User.objects.get(email=request.session['email'])
        if uid.role == "foodhelper":
            fid = foodhelper.objects.get(user_id=uid)
            return render(request,"foodhelp/pay.html",{'fid':fid,'uid':uid})
        else:
            
            fid = foodhelper.objects.get(user_id=uid)
            nid = NGO.objects.get(user_id=uid)
            return render(request,"foodhelp/pay.html",{'fid':fid,'nid':nid,'uid':uid})       
    else:
        return render(request,"foodhelp/index.html") 

@csrf_exempt
def initiate_payment(request):
    print("------------>>>> called")
    if request.method == "GET":
        return render(request, 'foodhelp/pay.html')
    
    id = request.POST['id']
    amount = int(request.POST['price'])
    print("---->amount ",amount)
    uid = User.objects.get(id=id)
    

    transaction = Transaction.objects.create(made_by=uid, amount=amount)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.made_by.email)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)
    return render(request, 'foodhelp/redirect.html', context=paytm_params)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        paytm_checksum = ''
        print(request.body)
        print(request.POST)
        received_data = dict(request.POST)
        print(received_data)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            print("Checksum Matched")
            received_data['message'] = "Checksum Matched"
        else:
            print("Checksum Mismatched")
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'foodhelp/callback.html', context=received_data)
        return render(request, 'foodhelp/callback.html', context=received_data)
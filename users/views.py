 


from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages
from users.models import *
import re,uuid
#from .helpers import send_forgot_password_email


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
pattern = re.compile("(0|91)?[6-9][0-9]{9}")


def donor_login_check(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print('login successful')
            return redirect('donor_main')
        else:
            print('!!invalid user')
            messages.info(request,'!Invalid user')
            return redirect('donor_login')

    else:
        return render(request,'donor_login.html')
def volunteer_login_check(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        
        if user is not None:
            user_obj = User.objects.get(username=username)
            id=user_obj.id
            vol_obj=volunteer_table.objects.get(user_id=id)
            status=vol_obj.status
            print(status)
            if status=='accepted':
                auth.login(request,user)
                print('login successful')
                return redirect('volunteer_main')
            else:
                print('status is still pending')
                messages.info(request,'!Status is still pending')
                return redirect('volunteer_login')
        else:
            print('!invalid user')
            messages.info(request,'!Invalid user')
            return redirect('volunteer_login')

    else:
        print("yes")
        return render(request,'volunteer_login.html')


def volunteer_register_check(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        mobile_no=request.POST['mobile_no']
        address=request.POST['address']
        id_pic = request.FILES['id_pic']
        if(len(username)==0 or len(first_name)==0 or len(last_name)==0 or len(email)==0 or len(password1)==0 or len(password2)==0\
            or len(mobile_no)==0 or len(address)==0):
            print("yes")
            messages.info(request,'!Enter all the details')
            return redirect('volunteer_register')
        if len(username)<6:
            messages.info(request,'!Username must have min. 8 characters')
            return redirect('volunteer_register')
        if(not re.fullmatch(regex, email)):
            messages.info(request,'!Enter valid email')
            return redirect('volunteer_register')
        if(not pattern.match(mobile_no)):
            messages.info(request,'!Enter valid mobile number')
            return redirect('volunteer_register')
        elif password1==password2:
            if 6<=len(password1)<=12 and re.search("[a-z]",password1) and re.search("[A-Z]",password1)\
        and re.search("[0-9]",password1) and re.search("[$#@]",password1):
                if User.objects.filter(username=username).exists() :
                    messages.info(request,'username taken')
                    print('username taken')

                    return redirect('volunteer_register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email taken')
                    print('email taken')

                    return redirect('volunteer_register')
                else:
                    user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    user = User.objects.get(username=username)
                    det=volunteer_table.objects.create(user=user,idpic=id_pic,status="pending",mobile_no=mobile_no,address=address)
                    if User.objects.filter(username=username).exists() and volunteer_table.objects.filter(user_id=user.id).exists():
                        user.save()
                        det.save()
                    print('user created')
                    messages.success(request,'Registration successful! You can login once your ID is accepted')
                    return redirect('check_id')
            else:
                messages.info(request,'!Password didnt meet given constraints')
                print('!Password didnt meet given constraints')
                return redirect('volunteer_register')
                
        else:
            messages.info(request,'password didnt match')
            print('password didnt match')
            return redirect('volunteer_register')


    else:
        return render(request,'volunteer_register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def donor_register_check(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        mobile_no=request.POST['mobile_no']
        address=request.POST['address']
        print(username,first_name,last_name,email,password1,mobile_no,address)
        print(type(username),type(first_name),type(last_name),type(email),type(password1),type(mobile_no),type(address))
        if(len(username)==0 or len(first_name)==0 or len(last_name)==0 or len(email)==0 or len(password1)==0 or len(password2)==0\
            or len(mobile_no)==0 or len(address)==0):
            print("yes")
            messages.info(request,'!Enter all the details')
            return redirect('donor_register')
        if len(username)<6:
            messages.info(request,'!Username must have min. 8 characters')
            return redirect('donor_register')
        if(not re.fullmatch(regex, email)):
            messages.info(request,'!Enter valid email')
            return redirect('donor_register')
        if(not pattern.match(mobile_no)):
            messages.info(request,'!Enter valid mobile number')
            return redirect('donor_register')
        elif password1==password2:
            if 6<=len(password1)<=12 and re.search("[a-z]",password1) and re.search("[A-Z]",password1)\
        and re.search("[0-9]",password1) and re.search("[$#@]",password1):
                if User.objects.filter(username=username).exists():
                    messages.info(request,'!Username taken')
                    print('username taken')

                    return redirect('donor_register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'!Email taken')
                    print('email taken')

                    return redirect('donor_register')
                else:
                    user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                    user = User.objects.get(username=username)
                    det=donor_table.objects.create(user=user,mobile_no=mobile_no,address=address)
                    if User.objects.filter(username=username).exists() and donor_table.objects.filter(user_id=user.id).exists():
                        user.save()
                        det.save()
                    print('user created')
                    messages.success(request,'Registration successful! Please login')
                    return redirect('donor_login')
                
            else:
                messages.info(request,'!Password didnt meet given constraints')
                print('!Password didnt meet given constraints')
                return redirect('donor_register')
        else:
            messages.info(request,'!Password and confirm password didnt match')
            print('password didnt match')
            return redirect('donor_register')



    else:
        return render(request,'donor_register.html')
    
def donor_main(request):
    return render(request,'donor_main.html')

def volunteer_main(request):
    return render(request,'volunteer_main.html')

def donate(request):
    return render(request,'donate.html')

def login(request):
    return render(request,'login.html')

def change_password_success(request):
    return render(request,'change-password-success.html')

def receive(request):
    obj1=donate_items_details.objects.all().filter(volunteer_username='null', item_type='clothing')
    obj2=donate_items_details.objects.all().filter(volunteer_username='null', item_type='furniture')
    obj3=donate_items_details.objects.all().filter(volunteer_username='null', item_type='books')
    obj4=donate_items_details.objects.all().filter(volunteer_username='null', item_type='others')
    context = {
                'objs1': obj1,
                'objs2': obj2,
                'objs3': obj3,
                'objs4': obj4,
            }
    print(type(obj1))
    return render(request, 'receive.html',context)

def single(request, id):
    print(id)
    obj1=donate_items_details.objects.get(id=id)
    print(obj1.item_name)
    context = {
                'obj1': obj1,
            }
    return render(request,'single.html', context)

def view_all(request, type):
    obj1=donate_items_details.objects.all().filter(item_type=type,volunteer_username='null')
    context = {
                'obj': obj1,
                'item_type':type,
    }
    return render(request,'view_all.html', context)

def single_post(request, id):
    print(id)
    obj1=post_items_details.objects.get(id=id)
    print(obj1.item_name)
    context = {
                'obj1': obj1,
            }
    return render(request,'single_post.html', context)

def view_posts(request):
    obj1=post_items_details.objects.all().filter(donor_username='null', item_type='clothing')
    obj2=post_items_details.objects.all().filter(donor_username='null', item_type='furniture')
    obj3=post_items_details.objects.all().filter(donor_username='null', item_type='books')
    obj4=post_items_details.objects.all().filter(donor_username='null', item_type='others')
    context = {
                'objs1': obj1,
                'objs2': obj2,
                'objs3': obj3,
                'objs4': obj4,
            }
    print(type(obj1))
    return render(request, 'view_posts.html',context)


def view_all_posts(request, type):
    obj1=post_items_details.objects.all().filter(item_type=type,donor_username='null')
    context = {
                'obj': obj1,
                'item_type':type,
    }
    return render(request,'view_all_posts.html', context)


def donor_login(request):
    return render(request,'donor_login.html')

def volunteer_login(request):
    return render(request,'volunteer_login.html')

def donor_register(request):
    return render(request,'donor_register.html')

def volunteer_register(request):
    return render(request,'volunteer_register.html')

def check_id(request):
    return render(request,'check_id.html')

def check_id_status(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            user_obj = User.objects.get(username=username)
            id=user_obj.id
            vol_obj=volunteer_table.objects.get(user_id=id)
            status=vol_obj.status
            if status=='accepted':
                messages.info(request,'ID is accepted! You can login')
            elif status=='rejected':
                messages.info(request,'Your ID is rejected! Please register again with valid ID')
                return render(request,'volunteer_register.html')
            else:
                messages.info(request,'ID confirmation is still pending')
        else:
            messages.info(request,'!Invalid username')

    return render(request,'check_id.html')

def donate_item(request):
    if request.method=='POST':
        item_name=request.POST['item_name']
        item_type=request.POST['item_type']
        item_desc=request.POST['item_desc']
        print(request.FILES)
        item_image = request.FILES['item_image']
        if(len(item_name)==0 or len(item_type)==0 or len(item_desc)==0):
            print("yes")
            messages.info(request,'!Enter all the details')
            return redirect('donate')
        if request.user.is_authenticated:
            current_user=request.user
            user_obj=User.objects.get(username=current_user.username)
            print(user_obj.id,user_obj.username)
            donor_obj=donor_table.objects.get(user_id=user_obj.id)
            item=donate_items_details.objects.create(item_name=item_name,item_type=item_type,item_image=item_image,item_desc=item_desc,\
            donor_username=current_user.username,donor_mobile_no=donor_obj.mobile_no,donor_address=donor_obj.address,volunteer_username='null'\
                ,volunteer_mobile_no='null',volunteer_address='null')
            item.save()
            
            context = {
                'item_obj': item,
            }

            return render(request, 'donation_done.html',context)

def post(request):
    return render(request,'requirements.html')

def post_item(request):
    if request.method=='POST':
        item_name=request.POST['item_name']
        item_type=request.POST['item_type']
        item_desc=request.POST['item_desc']
        if(len(item_name)==0 or len(item_type)==0 or len(item_desc)==0):
            print("yes")
            messages.info(request,'!Enter all the details')
            return redirect('post')
        if request.user.is_authenticated:
            current_user=request.user
            user_obj=User.objects.get(username=current_user.username)
            print(user_obj.id,user_obj.username)
            vol_obj=volunteer_table.objects.get(user_id=user_obj.id)
            item=post_items_details.objects.create(item_name=item_name,item_type=item_type,item_desc=item_desc,\
            volunteer_username=current_user.username,volunteer_mobile_no=vol_obj.mobile_no,volunteer_address=vol_obj.address,donor_username='null'\
                ,donor_mobile_no='null',donor_address='null')
            item.save()
            
            context = {
                'item_obj': item,
            }

            return render(request, 'post_done.html',context)

def all_donations(request):
    if request.user.is_authenticated:
            current_user=request.user
            obj=donate_items_details.objects.all().filter(donor_username=current_user.username)
            obj1=post_items_details.objects.all().filter(donor_username=current_user.username)
            context = {
                'item_objs': obj,
                'post_objs': obj1,
            }
            
            return render(request, 'all_donations.html',context)

def all_receptions(request):
    if request.user.is_authenticated:
            current_user=request.user
            obj=donate_items_details.objects.all().filter(volunteer_username=current_user.username)
            obj1=post_items_details.objects.all().filter(volunteer_username=current_user.username).exclude(donor_username='null')
            context = {
                'item_objs': obj,
                'post_objs': obj1,
            }
            
            return render(request, 'all_receptions.html',context)
def all_posts(request):
    if request.user.is_authenticated:
            current_user=request.user
            obj=post_items_details.objects.all().filter(volunteer_username=current_user.username)
            context = {
                'item_objs': obj,
            }
            
            return render(request, 'all_posts.html',context)


def added(request,id):
    if request.user.is_authenticated:
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)
        volunteer_obj=volunteer_table.objects.get(user_id=user_obj.id)
        obj1=donate_items_details.objects.get(id=id)
        obj1.volunteer_username=current_user.username
        obj1.volunteer_mobile_no=volunteer_obj.mobile_no
        obj1.volunteer_address=volunteer_obj.address

        obj1.save()
        user_obj=User.objects.get(username=obj1.donor_username)
        print(user_obj.id,user_obj.username)
        donor_obj=donor_table.objects.get(user_id=user_obj.id)
        context={
            'obj':obj1,
            'd_obj':donor_obj,
        }
    return render(request, 'added.html',context)


def added_post(request,id):
    if request.user.is_authenticated:
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)
        donor_obj=donor_table.objects.get(user_id=user_obj.id)
        obj1=post_items_details.objects.get(id=id)
        obj1.donor_username=current_user.username
        obj1.donor_mobile_no=donor_obj.mobile_no
        obj1.donor_address=donor_obj.address

        obj1.save()
        user_obj=User.objects.get(username=obj1.volunteer_username)
        print(user_obj.id,user_obj.username)
        volunteer_obj=volunteer_table.objects.get(user_id=user_obj.id)
        context={
            'obj':obj1,
            'v_obj':volunteer_obj,
        }
    return render(request, 'added_post.html',context)


def history(request):
    donors=donor_table.objects.all().count()
    volunteers=volunteer_table.objects.all().count()
    d1=donate_items_details.objects.all().count()
    d2=donate_items_details.objects.filter(volunteer_username='null').count()
    don_objs=donate_items_details.objects.exclude(volunteer_username='null')
    donations=d1-d2
    context={
        'donors':donors,
        'volunteers':volunteers,
        'donations':donations,
        'don_objs':don_objs,
    }

    return render(request,'history.html',context)


def donor_profile(request):
    if request.user.is_authenticated:
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)
        donor_obj=donor_table.objects.get(user_id=user_obj.id)
        context={
            'user_obj':user_obj,
            'donor_obj':donor_obj,
        }
    return render(request,'donor_profile.html',context)


def update_donor(request):
    if request.user.is_authenticated and request.method=='POST':
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)
        donor_obj=donor_table.objects.get(user_id=user_obj.id)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        mobile_no=request.POST['mobile_no']
        address=request.POST['address']

        user_obj.first_name=first_name
        user_obj.last_name=last_name
        donor_obj.mobile_no=mobile_no
        donor_obj.address=address

        user_obj.save()
        donor_obj.save()

        context={
            'user_obj':user_obj,
            'donor_obj':donor_obj,
        }
        return render(request,'donor_profile.html',context)


def change_donor_password(request):
    if request.user.is_authenticated and request.method=='POST':
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)
        donor_obj=donor_table.objects.get(user_id=user_obj.id)
        password=request.POST['password']
        user_obj.set_password('password')

        messages.info(request,'Password changed, please login')
        return render(request,'donor_login.html')




def volunteer_profile(request):
    if request.user.is_authenticated:
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)
        volunteer_obj=volunteer_table.objects.get(user_id=user_obj.id)
        context={
            'user_obj':user_obj,
            'volunteer_obj':volunteer_obj,
        }
    return render(request,'volunteer_profile.html',context)


def update_volunteer(request):
    if request.user.is_authenticated and request.method=='POST':
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)
        volunteer_obj=volunteer_table.objects.get(user_id=user_obj.id)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        mobile_no=request.POST['mobile_no']
        address=request.POST['address']

        user_obj.first_name=first_name
        user_obj.last_name=last_name
        volunteer_obj.mobile_no=mobile_no
        volunteer_obj.address=address

        user_obj.save()
        volunteer_obj.save()

        context={
            'user_obj':user_obj,
            'volunteer_obj':volunteer_obj,
        }
        return render(request,'volunteer_profile.html',context)


def change_volunteer_password(request):
    if request.user.is_authenticated and request.method=='POST':
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)
        volunteer_obj=volunteer_table.objects.get(user_id=user_obj.id)
        password1=request.POST['password']
        user_obj.set_password(password1)

        user_obj.save()

        context={
            'user_obj':user_obj,
            'volunteer_obj':volunteer_obj,
        }
        return render(request,'volunteer_profile.html',context)

def change_volunteer_id(request):
    if request.user.is_authenticated and request.method=='POST':
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)
        volunteer_obj=volunteer_table.objects.get(user_id=user_obj.id)
        id_pic = request.FILES['id_pic']
        volunteer_obj.idpic=id_pic
        volunteer_obj.status="pending"
        user_obj.save()
        volunteer_obj.save()
        auth.logout(request)
        messages.info(request,'Please wait until your id is accepted and then login')
        return render(request,'check_id.html')


def home_check(request):
    if request.user.is_authenticated:
        
        current_user=request.user
        user_obj=User.objects.get(username=current_user.username)

        if(donor_table.objects.filter(user_id=user_obj.id).count()==1):
            return render(request,'donor_main.html')
        else:
            return render(request,'volunteer_main.html')

    else:
        return render(request,'index.html')


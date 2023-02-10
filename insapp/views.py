from django.shortcuts import render,redirect
from django.core.mail import send_mail
from ins_pro.settings import EMAIL_HOST_USER
from .models import *
from .forms import *
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request,'index.html')

#user registration
def registration(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['name']
            un=a.cleaned_data['address']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            g=a.cleaned_data['gender']
            ps=a.cleaned_data['password']
            cs=a.cleaned_data['confirm_password']
            b=usermodel(name=fn,address=un,email=em,phone=ph,gender=g,password=ps)

            if ps==cs:
                b.save()
                return redirect(login)
            else:
                return HttpResponse('registration failed')
    else:
        return render(request,'reg.html')

def login(request):
    if request.method=='POST':
        x=logform(request.POST)
        if x.is_valid():
            un=x.cleaned_data['email']
            ps=x.cleaned_data['password']
            y=usermodel.objects.all()
            for i in y:
                if un==i.email and ps==i.password:

                    return redirect(usernav)
            else:
                return HttpResponse("login failed")
    else:
        return render(request,'login.html')


##################
##adding polices
##############
def vehicle(request):
    if request.method=='POST':
        a=vehicleform(request.POST)
        if a.is_valid():
            ins=a.cleaned_data['ins_name']
            sa=a.cleaned_data['Sum_Assurance']
            pe=a.cleaned_data['Premium']
            te=a.cleaned_data['Tenure']
            ca=a.cleaned_data['category']
            if ca=="VechicleInsurance":
               b=VechicleInsurance(ins_name=ins,Sum_Assurance=sa,Premium=pe,Tenure=te,category=ca)
               b.save()
            elif ca=="HealthInsurance":
                v = HealthInsModel (ins_name=ins, Sum_Assurance=sa, Premium=pe, Tenure=te, category=ca)
                v.save()
            elif ca=="LifeInsurance":
                l = LifeInsModel(ins_name=ins, Sum_Assurance=sa, Premium=pe, Tenure=te, category=ca)
                l.save()


            return redirect(vehicle)
        else:
            return HttpResponse("file upload failed")
    else:
        return render(request,"add_policy.html")



def show(request):
    a=VechicleInsurance.objects.all()

    return render(request,'vehicle_policy.html',{'a':a})

def adminshow(request):
    a = VechicleInsurance.objects.all()
    return render(request, 'adminshow.html', {'a': a})


def delete(request,id):
    a=VechicleInsurance.objects.get(id=id)
    a.delete()
    return redirect(adminshow)


###############################################
#apply insurance
##VEHICLE INSURANCE
#######################
def apply(request,id):
    a=VechicleInsurance.objects.get(id=id)
    if request.method == 'POST':
        b=vehicleDeatails(request.POST,request.FILES)
        if b.is_valid():
            po=b.cleaned_data['policy']
            ho=b.cleaned_data['holder']
            am=b.cleaned_data['amount']
            im=b.cleaned_data['image']
            ad=b.cleaned_data['address']
            ve=b.cleaned_data['vehicle']
            re=b.cleaned_data['reg']
            de=b.cleaned_data['regdate']

            c=vehicleModel(policy=po,holder=ho,amount=am,image=im,address=ad,vehicle=ve,reg=re,regdate=de)
            c.save()
            return render(request,'regshow.html',{'po':po,'ho':ho,'am':am,'ad':ad,'ve':ve,'re':re,'de':de})
        else:
            return HttpResponse("upload failed")
    else:
        return render(request,'vehicle_details.html',{'a':a})



###VEHICLE INSURANCE SHOW#############

def admin_vehicle_show(request):
    x=vehicleModel.objects.all()
    poli=[]
    hol=[]
    am=[]
    add=[]
    veh=[]
    reg1=[]
    rdate=[]
    img=[]
    cre=[]
    id=[]


    for i in x:
        po=i.policy
        poli.append(po)
        ho=i.holder
        hol.append(ho)
        amo=i.amount
        am.append(amo)
        ad=i.address
        add.append(ad)
        ve=i.vehicle
        veh.append(ve)
        r=i.reg
        reg1.append(r)
        rd=i.regdate
        rdate.append(rd)
        path=i.image
        img.append(str(path).split("/")[-1])
        cr=i.created
        cre.append(cr)
        id1=i.id
        id.append(id1)


    mylist=zip(poli,hol,am,add,veh,reg1,rdate,img,cre,id)
    return render(request,'admin_vehicle_show.html',{'mylist':mylist,'x':x})





##payment
def pay(request,ho,amount):
    a=ho
    b=amount

    if request.method=='POST':
         b=paymentform(request.POST)
         if b.is_valid():
             am=b.cleaned_data['price']
             em=b.cleaned_data['email']
             ho=b.cleaned_data['holder']
             po=b.cleaned_data['card']
             ve=b.cleaned_data['cvv']
             re=b.cleaned_data['expiry']
             mo=b.cleaned_data['month']
             c=payment(price=am,email=em,holder=ho,card=po,cvv=ve,expiry=re,month=mo)
             c.save()
             messeage="your payment was sucessfully done"
             send_mail(str(ho) + '|betterFund|₹'+str(am), messeage, EMAIL_HOST_USER, [em], fail_silently=False)
             return render (request,'msgpage.html')
         else:
             return HttpResponse("failed")
    else:

       return render(request, 'payment.html',{'a':a,'b':b})



def viewpay(request,id):
    a=payment.objects.get(id=id)
    return render(request,'paymentshow.html',{'a':a})

def messeage(request):
    return render(request,'msgpage.html')

#########################################################################


def usernav(request):
    a=usermodel.objects.all()
    for i in a:
        uname=i.name

    return render(request,'user_profile.html',{'uname': uname})

def pro(request):
    return render(request,'navbar.html')



###admin registartion
def adminreg(request):
    if request.method=='POST':
        a=adminform(request.POST)
        if a.is_valid():
            fn=a.cleaned_data['name']
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            cs=a.cleaned_data['cpassword']
            b=adminmodel(name=fn,email=em,password=ps)

            if ps==cs:
                b.save()
                return redirect(adminlogin)
            else:
                return HttpResponse('registration failed')
    else:
        return render(request,'adminreg.html')


def adminlogin(request):
    if request.method=='POST':
        x=adlog(request.POST)
        if x.is_valid():
            un=x.cleaned_data['email']
            ps=x.cleaned_data['password']
            y=adminmodel.objects.all()
            for i in y:
                if un==i.email and ps==i.password:

                    return redirect(adminindex)
            else:
                return HttpResponse("login failed")
    else:
        return render(request,'adminlog.html')

def adminindex(request):
    u = usermodel.objects.all()
    return render (request,'adminIndex.html',{'u':u})

def adminuser(request):
    a=usermodel.object.all()

def adminpolicy(request):
    return render(request,'admin_policy.html')

# def userlist(request):
#     u=usermodel.objects.all()
#     return render(request,'adminIndex.html',{'u':u})

def footerview(request):
    return render(request,'footer.html')

def adminnav(request):
    return render(request,'adminnav.html')

# def regishow(request):
#     a=vehicleModel.objects.all()
#
#     return render(request,'regshow.html',{'a':a})

def useredit(request):
    a=usermodel.objects.all()
    return render(request,'usershow.html',{'a':a})

def userdelete(request,id):
    a=usermodel.objects.get(id=id)
    a.delete()
    return redirect(useredit)



#<------HEALTH INSURANCE----->
###############################

def health(request,id):
    a=HealthInsModel.objects.get(id=id)
    if request.method == 'POST':
        b=healthform(request.POST,request.FILES)
        if b.is_valid():
            po=b.cleaned_data['policy_name']
            ph=b.cleaned_data['policy_holder']
            am=b.cleaned_data['amount']
            im=b.cleaned_data['image']
            ag=b.cleaned_data['age']
            ge=b.cleaned_data['gender']
            ho=b.cleaned_data['holder_status']
            do=b.cleaned_data['date_of_birth']
            ad=b.cleaned_data['address']
            em=b.cleaned_data['email']
            nu=b.cleaned_data['phone']
            c=healthInsurance(policy_name=po,policy_holder=ph,amount=am,image=im,age=ag,gender=ge,holder_status=ho,
                              date_of_birth=do,address=ad,email=em,phone=nu)
            c.save()
            return render(request,'healthshow.html',{'po':po,'ph':ph,'am':am,'im':im,'ag':ag,'ge':ge,'ho':ho,'do':do,'ad':ad,'em':em,'nu':nu})
        else:
            return HttpResponse("upload failed")
    else:
        return render(request,'health.html',{'a':a})

def healthpolicy(request):
    a=HealthInsModel.objects.all()

    return render(request,'health_policy.html',{'a':a})




def payh(request,ph,am):
    a=ph
    b=am

    if request.method=='POST':
         b=paymentform(request.POST)
         if b.is_valid():
             am=b.cleaned_data['price']
             em=b.cleaned_data['email']
             ho=b.cleaned_data['holder']
             po=b.cleaned_data['card']
             ve=b.cleaned_data['cvv']
             re=b.cleaned_data['expiry']
             mo=b.cleaned_data['month']
             c=helathpayment(price=am,email=em,holder=ho,card=po,cvv=ve,expiry=re,month=mo)
             c.save()
             messeage="your payment was sucessfully done"
             send_mail(str(ho) + '|betterFund|₹'+str(am), messeage, EMAIL_HOST_USER, [em], fail_silently=False)
             return render (request,'msgpage.html')
         else:
             return HttpResponse("failed")
    else:

       return render(request, 'payment.html',{'a':a,'b':b})

def health_payment_show(request,id):
    a = helathpayment.objects.get(id=id)
    return render(request, 'paymentshow.html', {'a': a})


def admin_health_show(request):
    x=healthInsurance.objects.all()
    pname=[]
    pholder=[]
    amt=[]
    img=[]
    ag=[]
    gen=[]
    hstatus=[]
    dob=[]
    adr=[]
    ema=[]
    phn=[]
    cre=[]
    id=[]

    for i in x:
        name=i.policy_name
        pname.append(name)
        holder=i.policy_holder
        pholder.append(holder)
        am=i.amount
        amt.append(am)
        path=i.image
        img.append(str(path).split("/")[-1])
        age1=i.age
        ag.append(age1)
        ge=i.gender
        gen.append(ge)
        stat=i.holder_status
        hstatus.append(stat)
        do=i.date_of_birth
        dob.append(do)
        add=i.address
        adr.append(add)
        em=i.email
        ema.append(em)
        ph=i.phone
        phn.append(ph)
        cr=i.created
        cre.append(cr)
        id1=i.id
        id.append(id1)
    mylist=zip(pname,pholder,amt,img,ag,gen,hstatus,dob,adr,ema,phn,cre,id)
    return render(request,'admin_healthshow.html',{'mylist':mylist,'x':x})


def adminshow2(request):
    a =HealthInsModel.objects.all()
    return render(request, 'adminshow2.html', {'a': a})

def healthdelete(request,id):
    a=HealthInsModel.objects.get(id=id)
    a.delete()
    return redirect(adminshow2)




#### LIFE INSURANCE ######
#######################################

def life(request,id):
    a=LifeInsModel.objects.get(id=id)
    if request.method == 'POST':
        b=lifeForm(request.POST,request.FILES)
        if b.is_valid():
            na=b.cleaned_data['name']
            ad=b.cleaned_data['address']
            ph=b.cleaned_data['phone']
            em=b.cleaned_data['email']
            do=b.cleaned_data['dateofbirth']
            au=b.cleaned_data['amount']
            pl=b.cleaned_data['plan']
            he=b.cleaned_data['height']
            we=b.cleaned_data['weight']
            de=b.cleaned_data['description']
            im=b.cleaned_data['image']

            c=lifeInsurance(name=na,address=ad,phone=ph,email=em,dateofbirth=do,plan=pl,height=he,weight=we,description=de,image=im,amount=au)
            c.save()
            return render(request,'lifeshow.html',{'na':na,'ad':ad,'ph':ph,'em':em,'do':do,'au':au,'pl':pl,'he':he,'we':we,'de':de,'im':im})
        else:
            return HttpResponse("upload failed")
    else:
        return render(request,'life_ins.html',{'a':a})

def lifepolicy(request):
    a=LifeInsModel.objects.all()
    return render(request,'life_policy.html',{'a':a})



def admin_life_show(request):
    x=lifeInsurance.objects.all()
    nam=[]
    adr=[]
    phn=[]
    em=[]
    amo=[]
    dob=[]
    pl=[]
    hei=[]
    wei=[]
    des=[]
    img=[]
    cre=[]
    id=[]


    for i in x:
        name=i.name
        nam.append(name)
        addr=i.address
        adr.append(addr)
        ph=i.phone
        phn.append(ph)
        ema=i.email
        em.append(ema)
        am=i.amount
        amo.append(am)
        da=i.dateofbirth
        dob.append(da)
        pla=i.plan
        pl.append(pla)
        he=i.height
        hei.append(he)
        we=i.weight
        wei.append(we)
        des1=i.description
        des.append(des1)
        path=i.image
        img.append(str(path).split("/")[-1])
        crea=i.created
        cre.append(crea)
        id1=i.id
        id.append(id1)


    mylist=zip(nam,adr,phn,em,amo,dob,pl,hei,wei,des,img,cre,id)
    return render(request,'admin_life_ins.html',{'mylist':mylist,'x':x})


def lifepay(request,na,au):
    a=na
    b=au

    if request.method=='POST':
         b=paymentform(request.POST)
         if b.is_valid():
             am=b.cleaned_data['price']
             em=b.cleaned_data['email']
             ho=b.cleaned_data['holder']
             po=b.cleaned_data['card']
             ve=b.cleaned_data['cvv']
             re=b.cleaned_data['expiry']
             mo=b.cleaned_data['month']
             c=lifepayment(price=am,email=em,holder=ho,card=po,cvv=ve,expiry=re,month=mo)
             c.save()
             messeage="your payment was sucessfully done"
             send_mail(str(ho) + '|betterFund|₹'+str(am), messeage, EMAIL_HOST_USER, [em], fail_silently=False)
             return render (request,'msgpage.html')

         else:
             return HttpResponse("failed")
    else:

       return render(request, 'payment.html',{'a':a,'b':b})


def lifepayshow(request,id):
    a =lifepayment.objects.get(id=id)
    return render(request, 'paymentshow.html', {'a': a})


def adminshow3(request):
    a =LifeInsModel.objects.all()
    return render(request, 'adminshow3.html', {'a': a})

def lifedelete(request,id):
    a=LifeInsModel.objects.get(id=id)
    a.delete()
    return redirect(adminshow3)



def logout_view(request):
    request.session.flush()
    return redirect(index)

def admin_holder_list(request):
    return render(request,'policy_holders_list.html')

#####contact form ######

def contact(request):
    sub=contactusForm()
    if request.method =='POST':
        sub=contactusForm(request.POST)
        if sub.is_valid():
            email= sub.cleaned_data['Email']
            name= sub.cleaned_data['Name']
            message=sub.cleaned_data['Messeage']

            send_mail(str(name)+'|betterFund|'+str(email),message,EMAIL_HOST_USER,['abhijithvlog321@gmail.com'],fail_silently=False)
            return(render(request,'contactsuccess.html'))

    return render(request,'contact_form.html',{'form':sub})




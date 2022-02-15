from django.shortcuts import render,redirect,get_object_or_404
from django.http.response import HttpResponseRedirect,HttpResponse
from django.contrib.auth import get_user_model, authenticate
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import DataFileUpload
import joblib
import pandas as pd
def base(request):
	return render(request,'homeApp/landing_page.html')
	
def userlogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('/userhome')
		else:
			messages.info(request, 'Username OR password is incorrect')
	return render(request,'homeApp/userlogin.html')
def usersignup(request):
	form = CreateUserForm()
	if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return render(request,'homeApp/userlogin.html')
	context = {'form':form}
	return render(request,'homeApp/usersignup.html',context)  
def userhome(request):
	return render(request,'homeApp/userhome.html')	      
def upload_credit_data(request):
	return render(request,'homeApp/upload_credit_data.html')
def prediction_button(request):
	return render(request,'homeApp/fraud_detection.html')
	
def reports(request):
	all_data_files_objs=DataFileUpload.objects.all()
	return render(request,'homeApp/reports.html',{'all_files':all_data_files_objs})
	
def enter_form_data_manually(request):
	return render(request,'homeApp/enter_form_data_manually.html')
def predict_data_manually(request):
	svm = joblib.load('svmmodel.sav')
	lis=[]
	lis.append(float(request.POST['time']))
	lis.append(float(request.POST['v1']))
	lis.append(float(request.POST['v2']))
	lis.append(float(request.POST['v3']))
	lis.append(float(request.POST['v4']))
	lis.append(float(request.POST['v5']))
	lis.append(float(request.POST['v6']))
	lis.append(float(request.POST['v7']))
	lis.append(float(request.POST['v8']))
	lis.append(float(request.POST['v9']))
	lis.append(float(request.POST['v10']))
	lis.append(float(request.POST['v11']))
	lis.append(float(request.POST['v12']))
	lis.append(float(request.POST['v13']))
	lis.append(float(request.POST['v14']))
	lis.append(float(request.POST['v15']))
	lis.append(float(request.POST['v16']))
	lis.append(float(request.POST['v17']))
	lis.append(float(request.POST['v18']))
	lis.append(float(request.POST['v19']))
	lis.append(float(request.POST['v20']))
	lis.append(float(request.POST['v21']))
	lis.append(float(request.POST['v22']))
	lis.append(float(request.POST['v23']))
	lis.append(float(request.POST['v24']))
	lis.append(float(request.POST['v25']))
	lis.append(float(request.POST['v26']))
	lis.append(float(request.POST['v27']))
	lis.append(float(request.POST['v28']))
	lis.append(float(request.POST['amount']))

	ans = svm.predict([lis])
	result=''
	color=''
	if(ans[0]==1):
		result='Invalid Transcation'
		color='red'
	else:
		 result='Valid Transcation'
		 color='green'   
	return render(request,'homeApp/predict_data_manually.html',{'color':color,'result':result,'time':request.POST['time'],'v1':request.POST['v1'],'v2':request.POST['v2'],'v3':request.POST['v3'],'v4':request.POST['v4'],'v5':request.POST['v5'],'v6':request.POST['v6'],'v7':request.POST['v7'],'v8':request.POST['v8'],'v9':request.POST['v9'],'v10':request.POST['v10'],'v11':request.POST['v11'],'v12':request.POST['v12'],'v13':request.POST['v13'],'v14':request.POST['v14'],'v15':request.POST['v15'],'v16':request.POST['v16'],'v17':request.POST['v17'],'v18':request.POST['v18'],'v19':request.POST['v19'],'v20':request.POST['v20'],'v21':request.POST['v21'],'v22':request.POST['v22'],'v23':request.POST['v23'],'v24':request.POST['v24'],'v25':request.POST['v25'],'v26':request.POST['v26'],'v27':request.POST['v27'],'v28':request.POST['v28'],'amount':request.POST['amount']})

def add_files_single(request):
	return render(request,'homeApp/add_files_single.html')
def predict_csv_single(request):
	 if request.method == 'POST':
		 svm = joblib.load('svmmodel.sav')
		 fil = request.FILES["myfile"]
		 csv = pd.read_csv(fil)
		 lis = []
		 print(csv.columns)
		 for i in csv.columns:
			  lis.append(float(i))
		 ans = svm.predict([lis])
		 result=''
		 color=''
		 if(ans[0]==1):
			 result='Invalid Transcation'
			 color='red'
		 else:
			 result='Valid Transcation'
			 color='green' 
	 return render(request,'homeApp/predict_csv_single.html',{'result':result,'color':color,'lis':lis})

def add_files_multi(request):
	return render(request,'homeApp/add_files_multi.html')
	
def predict_csv_multi(request):
	if request.method == 'POST':
	 svm = joblib.load('svmmodel.sav')
	 fil = request.FILES['mymultfile']
	 csv = pd.read_csv(fil)
	 arr = csv.iloc[:,:].to_numpy()
	 arr1 = arr.tolist()
	 arr2 = svm.predict(arr1)
	 niv=0
	 nv=0
	 for i in arr2:
		 if(i==0):
			 nv=nv+1
		 else:
			 niv=niv+1           
	 return render(request,'homeApp/predict_csv_multi.html',{'niv':niv,'nv':nv})

def account_details(request):
	return render(request,'homeApp/account_details.html')
def change_password(request):
	return render(request,'homeApp/change_password.html')
def analysis(request):
	return render(request,'homeApp/analysis.html')
def view_data(request):
	return render(request,'homeApp/view_data.html')
def delete_data(request,id):
	obj=DataFileUpload.objects.get(id=id)
	obj.delete()
	messages.success(request, "File Deleted succesfully",extra_tags = 'alert alert-success alert-dismissible show')
	return HttpResponseRedirect('/reports')
def upload_data(request):
	if request.method == 'POST':
			data_file_name  = request.POST.get('data_file_name')
			try:
				actual_file = request.FILES['actual_file_name']
				
			except:
				messages.warning(request, "Invalid/wrong format. Please upload File.")
				return redirect('/upload_credit_data')
			description  = request.POST.get('description')

			DataFileUpload.objects.create(
						file_name=data_file_name,
						actual_file=actual_file,
						description=description,
						
					)
			messages.success(request, "File Uploaded succesfully",extra_tags = 'alert alert-success alert-dismissible show')
			return HttpResponseRedirect('/reports')
	# return HttpResponseRedirect('reports')
	

def userLogout(request):
	try:
	  del request.session['username']
	except:
	  pass
	logout(request)
	return HttpResponseRedirect('/') 
	

def login2(request):
	data = {}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print(user)
		if user:
			login(request, user)
			return HttpResponseRedirect('/prediction_button')
		
		else:    
			data['error'] = "Username or Password is incorrect"
			res = render(request, 'homeApp/login.html', data)
			return res
	else:
		return render(request, 'homeApp/login.html', data)


def about(request):
	return render(request,'homeApp/about.html')

def dashboard(request):
	return render(request,'homeApp/dashboard.html')
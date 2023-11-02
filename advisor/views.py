from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages
from .models import User, Contact
import pickle
import numpy as np
from bs4 import BeautifulSoup
import requests

#loading AI model
model = pickle.load(open('demModel.pkl', 'rb'))
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def contactInfo(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        phoneNo = request.POST.get('phoneNo')
        email = request.POST.get('email')
        userMessage = request.POST.get('userMessage')
        contactDetails = Contact(email = email, phoneNo = phoneNo, firstName = firstName, lastName  = lastName, userMessage = userMessage)
        contactDetails.save()
        messages.success(request, "Thanks for contacting us. We will get to you ASAP.")
        return redirect('home')
    else:
        return redirect('home')

def login_page(request):
    return render(request, 'login.html')

def login_user(request):
    if request.method == 'POST':
        # is_private = request.POST.get('is_private', False);
        username = request.POST.get('username', False)
        password = request.POST.get('password', 'skywars')
        print(f'Username: {username}')
        print(f'Password: {password}')
        #Authenticate
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            # messages.success(request, "You Have Been Logged In!")
            return redirect('survey')
        else:
            messages.success(request, "There was an error loggin In, Please try again...")
            return redirect('login_page')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        # ------------------
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            firstName = form.cleaned_data['first_name']
            lastName= form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phoneNo = form.cleaned_data['phoneNo']
            password = form.cleaned_data['password1']
            newUser = User(username = username, firstName = firstName, lastName = lastName, email = email, phoneNo = phoneNo, password = password)
            newUser.save()
        # ------------------
            # Authenticate and login
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('login_page')
        else:
            messages.success(request, "There was an error during registration. Please try again by changing username and with correct details..")
            return redirect('register')

    else:
        # form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    #not required codes
    #     #return render(request, 'register.html', )  #return render(request, 'register.html', {'form':form})
    # return render(request, 'register.html', {'form':form})
    # # return render(request, 'register.html', )
    

def survey(request):
    return render(request, 'survey.html')

def predict(request):
    skills = ['Database Fundamentals', 'Computer Architecture',
         'Distributed Computing Systems', 'Cyber Security', 'Networking',
        'Software Development', 'Programming Skills', 'Project Management',
        'Computer Forensics Fundamentals', 'Technical Communication', 'AI ML',
        'Software Engineering', 'Business Analysis', 'Communication skills',
        'Data Science', 'Troubleshooting skills', 'Graphics Designing']

    skillsCat = ['Average', 'Beginner', 'Excellent','Intermediate','Not Interested','Poor','Professional']

    userSkills = []
    xTest = []
    # test = request.POST['Database Fundamentals']
    for skill in skills:
        userSkills.append(request.POST[skill])

    # print(userSkills)

    for user in userSkills:
        for skiCat in skillsCat:
            if skiCat == user:
                xTest.append(1)
            else:
                xTest.append(0)

    xTest= np.reshape(xTest,(1,119)) 
    # print(xTest) 

    # print(f'UserInput: {userSkills}/n')
    # result = model.predict(xTest)
    # print(result)
    
    pred = model.predict_proba(xTest)
    careers = {}
    pred = pred.reshape(1,17)

    for x in range(16):
        careers[skills[x]] = pred[0][x]
    # print(careers)

    # print(pred)
    # endSkills = []
    # endPred = []
    # for key, value in careers.items():
    #     if value > 0:
    #         endSkills.append(key)
    #         endPred.append(value)


    finCareer = {}
    for key, value in careers.items():
        if value > 0:
            finCareer[key] = round(value  * 100, 2)

    jobs = {
            'Database Fundamentals':'Database Administrator',
            'Computer Architecture':'Hardware Engineer',
            'Distributed Computing Systems':'Application Support Engineer',
            'Cyber Security':'Cyber Security Specialist',
            'Networking':'Networking Engineer',
            'Software Development':'Software Developer',
            'Programming Skills':'API Specialist', 
            'Project Management':'Project Manager',
            'Computer Forensics Fundamentals':'Information Security Specialist',
            'Technical Communication':'Technical Writer',
            'AI ML':'AI ML Specialist',
            'Software Engineering':'Software tester',
            'Business Analysis':'Business Analyst',
            'Communication skills':'Customer Service Executive',
            'Data Science':'Data Scientist', 
            'Troubleshooting skills':'Helpdesk Engineer',
            'Graphics Designing': 'Graphics Designer'}
    
    finJobs = {}
    for key, value in jobs.items():
        if key in finCareer:
            finJobs[value] = finCareer[key]
    
    print(finJobs)
    # print(f'/nFincareertrye: {type(finCareer)}')
    # endLength = len(endSkills)
    # print(endLength)
    return render(request, 'predictions.html', {'finJobs':finJobs})
    # return test

def scrape(request):
    totalLi = []
    #jobField = 'software' #request.POST['jobField']
    newField = request.POST['jobField']
    jobField = list((newField.split(' ')))
    # print(newField)
    html_text = requests.get(f'https://merojob.com/search/?q={jobField[0]}').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_ = 'row job-card text-center text-lg-left ml-2')
    for job in jobs:
        li = []

        skills  = None
        location = None
        job_title = None
        company_name  = None
        more_info = None

        if job.find('h1', itemprop = 'title') is not None:
            job_title = job.find('h1', itemprop = 'title').text

        if job.find('h3', class_ = 'h6') is not None:
            company_name = job.find('h3', class_ = 'h6').text

        if job.find('span', itemprop = 'skills') is not None:
            skills = job.find('span', itemprop = 'skills').text

        if job.find('span',itemprop = 'address' ) is not None:
            location = job.find('span',itemprop = 'address' ).text

        more_info = job.find('div', class_ = 'col-8 col-lg-9 col-md-9 pl-3 pl-md-0 text-left').h1.a['href']

        if job_title is not None:
            li.append(job_title.strip())
        else:
            li.append("Title not Provided")
        if company_name is not None:
            li.append(company_name.strip())
        else:
            li.append("Company name not provided")

        if skills is not None:
            li.append(skills.strip())
        else:
            li.append("Requirements not provided")

        if location is not None:
            li.append(location.strip())

        elif location == "":
            li.append("Location not provided.")
        else:
            li.append("Location not provided.")

        li.append(f'https://merojob.com{more_info.strip()}')
        totalLi.append(li)
    # print(totalLi)
    return render(request, 'jobs.html', {'totalLi':totalLi})
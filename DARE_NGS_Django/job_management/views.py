from django.shortcuts import render,render_to_response, RequestContext
from django_tables2   import RequestConfig
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models  import Job
from .tables  import JobTable
from .forms import JobForm
from .forms2 import IbiomesForm
import subprocess
import pipes
from django.http import HttpResponseRedirect,HttpResponse
#from django.core.context_processors import csrf
#from django.conrib.auth.decorators import login_required
from .tables2 import IbiomesTable
import action as action
import urllib
from django.db.models.loading import get_models
from django.contrib.auth.decorators import login_required
import os
#from .models import JobManager,my_costum_sql
# Create your views here.
@login_required
def Jobs(request):
	if request.method == 'POST':
		form= JobForm(request.POST, request.FILES)
		pks=request.POST.getlist("Select")
		current_user=str(request.user)
                table = JobTable(Job.objects.filter(userid=current_user))
		print "kos %s" %pks
		for pk in pks:	
			pk=str(pk)
			print pk
			path="/home/cctsg/software/DARE-NGS/darengs/lib/DARE/darefiles/"+pk+"/assembly.log"
			if ( not os.path.isfile(path)):
			#	content="Your Job"+pk+" is still running"
				l=exists_remote('kimjh@smic.hpc.lsu.edu', 'preprocess.txt')
				if l:
					h=exists_remote('kimjh@smic.hpc.lsu.edu', 'assem.finish')
					if h:	
						d=exists_remote('kimjh@smic.hpc.lsu.edu', 'done')									
						if d:
							content="Your Job"+pk+" is finished"						
						if not d: 
							content="Your Job"+pk+" assembly is done and it is in preprocessing step"
					if not h:
						content="Your Job"+pk+" is in assembly step"
				if not l:
					content="Your Job"+pk+" is queued"
			else:
				log=open(path, 'r')
				content=log.read()
			return render_to_response("edit.html",{ 'content': content },context_instance=RequestContext(request))
			#return HttpResponseRedirect(request,'edit.html',{ 'content': content })
			#return render(request, 'Jobs.html', {'table': table})
		
	else:	
		current_user=str(request.user)
		table = JobTable(Job.objects.filter(userid=current_user))
		object_list=Job.objects.all()
		RequestConfig(request).configure(table)
		variable={
		'table': table,
		'object_list': object_list,
		'form' : JobForm
		}
		return render(request,'Jobs.html',variable)
	return render('/results/result_'+ jobid+'.mako')
def exists_remote(host, path):
	"""Test if a file exists at path on a host accessible with SSH."""
	status = subprocess.call(['ssh', host, 'test -f {}'.format(pipes.quote(path))])
	if status == 0:
		return True
	if status == 1:
		return False
	raise Exception('SSH failed')
def edit(request):
        if request.method=="POST":
		pks=request.POST.getlist("select")
		print "kos %s" %pks
		current_user=str(request.user)
		table = JobTable(Job.objects.filter(userid=current_user))
		return render(request, 'Jobs.html', {'table': table})
def update(request):
	f=open('shayan.txt','w')
	#for p in JobManager('Select * FROM job_management_job'):
        #for p in Job.objects:
               #f.write(p)
        lol=str(Job.objects)
        f.write(lol)
        f.close()
        current_user=str(request.user)
	table = JobTable(Job.objects.filter(userid=current_user))
        #table = JobTable(Job.objects.filter(userid=request.user.user_id))
	RequestConfig(request).configure(table)
        #if(request.GET.get('delAction')):
            #os.system('echo "y" | starcluster terminate restmd_cluster')
	return render(request, 'Jobs.html', {'table': table})




def forms(request):
	#if request.method == 'POST':
		#form = UserProfileForm(request.POST, instance=request.user.profile)
		#if form.is_valid():
			#form.save()
	#else:
	#user = request.user
	#profile = user.profile
	#form = UserProfileForm (instance = profile)

	form= JobForm(request.POST or None)
	if form.is_valid():
		#save_it= form.save(commit=False)
		#save_it.save()
	#args = {}
	#args.update(csrf(request))

	#args["forms"] = forms
		values={}
		us = request.user
		values['user'] = us
		data = urllib.urlencode(values) 

		url =  "http://dare.cct.lsu.edu:8080/gateways/ngs/ngs/rnnotator_form"
		full_url = url + '?' + data 
		return HttpResponseRedirect(full_url)
	else:
		return render_to_response("forms.html",
                              	   	   locals(),
                              		   context_instance=RequestContext(request))

	#return render_to_response("forms.html",
                              #locals(),
                              #context_instance=RequestContext(request))
def forms2(request):
	form= IbiomesForm(request.POST or None)
	if form.is_valid():
		save_it= form.save(commit=False)
		save_it.save()
		return render_to_response("forms2.html",
                              	   	   locals(),
                              		   context_instance=RequestContext(request))
#@login_required
def Ibiomes(request):
	#table = JobTable(Job.objects.all())
	table = IbiomesTable(Job.objects.filter())
	RequestConfig(request).configure(table)
	return render(request, 'dataAnalysis.html', {'table': table})

    
#def action(Deleteview):
    #model=Job
    #template_name='Jobs.html'
    #success_url=reverse_lazy('Jobs')

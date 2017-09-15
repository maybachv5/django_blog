from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm
from django.contrib import messages
# Create your views here.

@login_required
def profile_view(request):
    return render(request,'oauth/profile.html')

@login_required
def change_profile_view(request):
    if request.method == 'POST':
        # 上传文件需要使用request.FILES
        form = ProfileForm(request.POST,request.FILES,instance=request.user)
        print(form)
        if form.is_valid():
            form.save()
            # 添加一条信息,重定向到个人信息页面
            messages.add_message(request,messages.SUCCESS,'个人信息更新成功！')
            return redirect('oauth:profile')
    else:
        form = ProfileForm(instance=request.user)
        return render(request,'oauth/change_profile.html',context={'form':form})

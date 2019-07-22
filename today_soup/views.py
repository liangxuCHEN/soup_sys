from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from today_soup.forms import AuthenticationForm
from today_soup.models import SoupModel
# Create your views here.
def home_page(request):
    if request.user.is_authenticated:

        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/login')

def LoginView(request):
    """
    Log in view
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        content = {}
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                content['info'] = u"帐号或密码错误"
                content['form'] = AuthenticationForm()
                return render(request, 'login.html', content)
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def LogoutView(request):
    logout(request)
    return redirect('/')


def soups_list(request):
    contact_list = SoupModel.objects.all()

    text = request.GET.get('text')

    if text:
        contact_list = contact_list.filter(content__contains=text)


    title = request.GET.get('title')
    if title:
        contact_list = contact_list.filter(title__contains=title)

    paginator = Paginator(contact_list, 8)

    page = request.GET.get('page')
    try:
        content = paginator.page(page)  # contacts为Page对象！
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        content = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        content = paginator.page(paginator.num_pages)

    return render(request, 'soups.html', {'content': content})


def soup_detail(request, p_id):
    soup = get_object_or_404(SoupModel, pk=p_id)
    # 图片拆分
    imgs = soup.pic_urls.split(';')
    lines = soup.content.split('\n')
    lines += soup.how_to_do.split('\n')
    # 内容拆分
    return render(request, 'soup_detail.html', {'soup':soup, 'imgs':imgs, 'lines':lines})

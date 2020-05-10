from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.urls import reverse, reverse_lazy
from django import forms
from pagedown.widgets import PagedownWidget
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.dates import MonthArchiveView
import datetime

MONTH_NAMES = ('', 'January', 'Feburary', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December')

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "date_posted"
    allow_future = True
    date_list_period = 'month'

def test(request):
    return render(request, 'blog/base2.html')

def is_valid_queryparam(param):
    return param != '' and param is not None

def home(request):
    posts = Post.objects.all()
    tag_search = request.GET.get('tag_search')
    common_tags = Post.tags.most_common()[:4]

    if is_valid_queryparam(tag_search):
        posts = posts.filter(tags__slug=tag_search)

    posts = posts[::-1]
    recent_posts = posts[:4]

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    events = Post.objects.filter().order_by('-date_posted')
    now = datetime.datetime.now()
 
    #create a dict with the years and months:events 
    event_dict = {}
    for i in range(events[0].date_posted.year, events[len(events)-1].date_posted.year-1, -1):
        event_dict[i] = {}
        for month in range(1,13):
            event_dict[i][month] = []
    for event in events:
        event_dict[event.date_posted.year][event.date_posted.month].append(event)
 
    #this is necessary for the years to be sorted
    event_sorted_keys = list(reversed(sorted(event_dict.keys())))
    list_events = []
    for key in event_sorted_keys:
        adict = {key:event_dict[key]}
        list_events.append(adict)

    context = {
        'posts': posts,
        'common_tags': common_tags,
        'recent_posts': recent_posts,
        'now': now,
        'list_events':list_events,
    }
    return render(request, 'blog/home.html', context)

"""

class PostListView2(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

class PostListView(ListView):
    model = Post
    template_name = 'blog/home2.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

'''
class PostDetailView(DetailView):
    model = Post
'''
"""
def post_detail(request, pk):
    object = get_object_or_404(Post, pk=pk)
    comments = object.comments.filter(Parent__isnull=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            Parent_obj = None
            try:
                Parent_id = int(request.POST.get('Parent_id'))
            except:
                Parent_id = None
            if Parent_id:
                Parent_obj = Comment.objects.get(id=Parent_id)
                if Parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.Parent = Parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.post = object
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog:post-detail', object.id)
            
    else:
        comment_form = CommentForm()


    return render(request, 'blog/post_detail.html', {'object': object, 'comments': comments, 'comment_form': comment_form})

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, "blog/home.html", context)

'''
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:home')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
'''
"""
@login_required
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    common_tags = Post.tags.most_common()[:4]
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        form.save_m2m()
        # message success
        #messages.success(request, "Successfully Created")
        return redirect('blog:home')
    context = {
        "form": form,
        "common_tags": common_tags,
    }
    return render(request, "blog/post_form.html", context)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

'''
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:home')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
'''

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:home')
"""
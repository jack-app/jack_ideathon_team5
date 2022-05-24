from .forms import LoginForm# , Signupform # 追加
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView # 追加
from django.contrib.auth import get_user_model # 追加
from django.contrib.auth.mixins import UserPassesTestMixin # 追加
from django.views import generic

# ユーザーモデル取得
User = get_user_model()

'''トップページ'''
class TempView(generic.TemplateView):
    template_name = 'frog/top.html'
    
'''ログイン'''
class Login(LoginView):
    form_class = LoginForm
    template_name = 'frog/login.html'
    
'''ログアウト'''
class Logout(LogoutView):
    template_name = 'frog/logout_done.html'
    
'''自分しかアクセスできないようにするMixin(My Pageのため)'''
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']

'''マイページ'''
class MyPage(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'frog/my_page.html'
    # モデル名小文字(user)でモデルインスタンスがテンプレートファイルに渡される

"""
'''サインアップ'''
class Signup(generic.CreateView):
    template_name = 'frog/user_form.html'
    form_class =SignupForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('frog:signup_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context

'''サインアップ完了'''
class SignupDone(generic.TemplateView):
    template_name = 'frog/signup_done.html'
    
"""
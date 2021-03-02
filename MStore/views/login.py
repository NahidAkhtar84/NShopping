from django.shortcuts import render, redirect, HttpResponseRedirect
from MStore.models.customerModel import Customer
from django.contrib.auth.hashers import check_password
from django.views import View

#login class
class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_message = None
        customer = Customer.loginCustomer(email)

        if customer:
            if check_password(password, customer.password):
                request.session["customer_id"] = customer.id
                request.session["fname"] = customer.first_name
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = "Email or Password is Invalid!!!"
        else:
            error_message = "Email or Password is Invalid!!!"

        return render(request, 'login.html', {'error': error_message})
    
    
#logout
def logout(request):
    request.session.clear()
    return redirect('login')
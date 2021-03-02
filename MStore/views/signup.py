from django.shortcuts import render, redirect
from django.http import  HttpResponse
from MStore.models.customerModel import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

#signup class
class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.method == 'POST':
            pst = request.POST
            fname = pst.get('firstname')
            lname = pst.get('lastname')
            phone = pst.get('mobilenumber')
            email = pst.get('email')
            password = pst.get('password')

            # validation data
            existing_value = {
                'fname': fname,
                'lname': lname,
                'phone': phone,
                'email': email
            }

            customer = Customer(
                first_name=fname,
                last_name=lname,
                phone_number=phone,
                email=email,
                password=password
            )

            # calling validation
            error_message = self.validationCustomer(customer)

            reformdata = {'exvalues': existing_value, 'error': error_message}

            if len(error_message) == 0:
                # password hashing
                customer.password = make_password(customer.password)

                # save data
                customer.register()
                return redirect('homepage')
            else:
                return render(request, 'signup.html', reformdata)



    def validationCustomer(self, customer):
        error_message = []
        if not customer.first_name:
            error_message.append("First Name is Required")
        elif len(customer.first_name) < 3:
            error_message.append("Minimum 3 characters is required for First Name")

        if not customer.last_name:
            error_message.append("Last Name is Required")
        elif len(customer.last_name) < 3:
            error_message.append("Minimum 3 characters is required for Last Name")
        if not customer.email:
            error_message.append("Email is Required")

        if not customer.password:
            error_message.append("Password is Required")

        elif len(customer.password) < 6:
            error_message.append("Minimum required length for password is 6")

        if customer.isExist():
            error_message.append("Email already exists!")

        if not customer.phone_number:
            error_message.append("Phone Number is Required")

        elif (len(customer.phone_number) == 14 and customer.phone_number.startswith('+88') == True) or (
                len(customer.phone_number) == 11 and customer.phone_number.startswith('0') == True):
            pass
        else:
            error_message.append("The Phone number is not valid!")
        return error_message
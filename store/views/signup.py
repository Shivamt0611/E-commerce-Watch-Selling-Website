from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        mobile_number = postData.get('mobilenumber')
        email_address = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile_number': mobile_number,
            'email_address': email_address
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            mobile_number=mobile_number,
                            email_address=email_address,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, mobile_number, email_address, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required....!!"
        elif len(customer.first_name) < 2:
            error_message = 'First Name must be 2 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required....!!'
        elif len(customer.last_name) < 2:
            error_message = 'last Name must be 2 char long or more'
        elif not customer.mobile_number:
            error_message = 'Phone Number Required....!!'
        elif len(customer.mobile_number) < 10:
            error_message = 'Please Enter Valid Phone Number '
        elif not customer.password:
            error_message = 'Password Required....!!'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email_address) < 10:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered....!!'

            # saving

        return error_message

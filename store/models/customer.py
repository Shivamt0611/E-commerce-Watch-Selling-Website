from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    mobile_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    password = models.CharField(max_length=15)


    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email_address(email):
        try:
            return Customer.objects.get(email_address = email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email_address = self.email_address):
            return True

        return False


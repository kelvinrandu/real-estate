from django.db import models

# Create your models here.

class Property(models.Model):
    propertyName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=100)
    picture = models.ImageField()

    def __str__(self):
        return self.propertyName

class Unit(models.Model):
    unitNumber = models.CharField(max_length=255)
    propertyId = models.ForeignKey(Property, on_delete=models.CASCADE)
    floor = models.CharField(max_length=255)
    bedrooms = models.CharField(max_length=100)
    bathrooms = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.unitNumber

class Tenant(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName

class Vendor(models.Model):
    vendorName = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    contactPerson = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.vendorName


class Lease(models.Model):
    propertyId = models.ForeignKey(Property, on_delete=models.CASCADE)
    unitId = models.ForeignKey(Unit, on_delete=models.CASCADE)
    tenantId = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    active = models.CharField(max_length=3)
    rent = models.CharField(max_length=100)

    def __str__(self):
        return self.leaseId
 

class Payment(models.Model):
    unitId = models.ForeignKey(Unit, on_delete=models.CASCADE)
    leaseId = models.ForeignKey(Lease, on_delete=models.CASCADE)
    paymentAmount = models.IntegerField()	
    paymentDate = models.DateField()

    def __str__(self):
        return self.paymentId

class Expense(models.Model):
    unitId = models.ForeignKey(Unit, on_delete=models.CASCADE)
    vendorId = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    expensetype = models.CharField(max_length=100)
    cost = models.IntegerField()
    date = models.DateField()
    receipt = models.FileField()
    isPaid = models.CharField(max_length=100)

    def __str__(self):
        return self.expenseId
 
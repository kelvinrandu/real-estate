from django.db import models

# Create your models here.

class Property(models.Model):
    propertyName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    county = models.CharField(max_length=100)
    # picture = models.CharField(max_length=100)

class Unit(models.Model):
    unitNumber = models.CharField(max_length=255)
    propertyId = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)
    bedrooms = models.CharField(max_length=100)
    bathrooms = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    # picture = models.CharField(max_length=100)

class Tenant(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)


class Vendor(models.Model):
    vendorName = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    contactPerson = models.CharField(max_length=255)
    email = models.CharField(max_length=100)


class Lease(models.Model):
    propertyId = models.CharField(max_length=255)
    unitId = models.CharField(max_length=255)
    tenantId = models.CharField(max_length=255)
    startDate = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)
    active = models.CharField(max_length=100)
    rent = models.CharField(max_length=100)
 

class Payment(models.Model):
    unitId = models.CharField(max_length=255)
    leaseId = models.CharField(max_length=255)
    paymentAmount = models.CharField(max_length=100)
    paymentDate = models.CharField(max_length=100)

class Expense(models.Model):
    propertyId = models.CharField(max_length=255)
    unitId = models.CharField(max_length=255)
    vendorId = models.CharField(max_length=255)
    expensetype = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    receipt = models.CharField(max_length=100)
    isPaid = models.CharField(max_length=100)
    # picture = models.CharField(max_length=100)
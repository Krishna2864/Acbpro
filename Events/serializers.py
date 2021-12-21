from .models import *
from rest_framework import serializers


class Admin_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Admin_Management
        fields=('__all__')


class User_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=User_Management
        fields=('__all__')



class Vehicle_MangementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle_Management
        fields=('__all__')

class Driver_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Driver_Management
        fields=('__all__')


class Country_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Country_Management
        fields=('__all__')




class State_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=State_Management
        fields=('__all__')



class City_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=City_Management
        fields=('__all__')



class Advertisement_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Advertisement_Management
        fields=('__all__')

'''
class Refund_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Refund_Management
        fields=('__all__')
  '''     
class Refral_ManagemntSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Refral_Managemnt
        fields=('__all__')



class Fuel_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Fuel_Management
        fields=('__all__')



class Maintenance_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Maintenance_Management
        fields=('__all__')
'''
class Route_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Route_Management
        fields=('__all__')

'''

class Fare_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Fare_Management
        fields=('__all__')

'''
class Time_Schedule_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Time_Schedule_Management
        fields=('__all__')


class Pickup_PointSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Pickup_Point
        fields=('__all__')



class Pickup_PointSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Drop_Points
        fields=('__all__')
'''
class Listing_Assign_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Listing_Assign_Management
        fields=('__all__')


class Co_Partner_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Co_Partner_Management
        fields=('__all__')


class Notification_to_RidderSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Notification_to_Ridder
        fields=('__all__')

class Notification_to_DriverSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Notification_to_Driver
        fields=('__all__')
'''
class Consignment_TrackingSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Consignment_Tracking
        fields=('__all__')
'''





class List_Your_Vehicle_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=List_Your_Vehicle_Management
        fields=('__all__')




class Feedbackserializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=('__all__')


'''
class Seat_MangementSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Seat_Management
        fields=('__all__')

 '''


class SOSSerailizer(serializers.ModelSerializer):
    class Meta:
        model=SOS
        fields=('__all__')




class Support_HelpSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Support_Help
        fields=('__all__')





class TERMS_CONDITIONSSerailizer(serializers.ModelSerializer):
    class Meta:
        model=TERMS_CONDITIONS
        fields=('__all__')



class PRIVACY_POLICYSerailizer(serializers.ModelSerializer):
    class Meta:
        model=PRIVACY_POLICY
        fields=('__all__')


##
class  Templates_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model= Templates_Management
        fields=('__all__')



##
class  Transaction_ManagementSerailizer(serializers.ModelSerializer):
    class Meta:
        model= Transaction_Management
        fields=('__all__')

from django.shortcuts import render

from django.db.models.query import QuerySet

from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import viewsets
from .models import *
from .serializers import *


class AdminManagementViewset(viewsets.ModelViewSet):
    queryset = Admin_Management.objects.all()
    serializer_class = Admin_ManagementSerailizer


class User_ManagementViewset(viewsets.ModelViewSet):
    queryset = User_Management.objects.all()
    serializer_class = User_ManagementSerailizer

class VehicleManagementViewset(viewsets.ModelViewSet):
    queryset = Vehicle_Management.objects.all()
    serializer_class = Vehicle_MangementSerailizer

class DriverManagementViewset(viewsets.ModelViewSet):
    queryset = Driver_Management.objects.all()
    serializer_class = Driver_ManagementSerailizer

class CountryManagementViewset(viewsets.ModelViewSet):
    queryset = Country_Management.objects.all()
    serializer_class = Country_ManagementSerailizer

class StateManagementViewset(viewsets.ModelViewSet):
    queryset = State_Management.objects.all()
    serializer_class = State_ManagementSerailizer

class CityManagementViewset(viewsets.ModelViewSet):
    queryset = City_Management.objects.all()
    serializer_class = City_ManagementSerailizer

class AdvertisementManagementViewset(viewsets.ModelViewSet):
    queryset = Advertisement_Management.objects.all()
    serializer_class = Advertisement_ManagementSerailizer

class RefralManagementViewset(viewsets.ModelViewSet):
    queryset = Refral_Managemnt.objects.all()
    serializer_class = Refral_ManagemntSerailizer
'''
class RefundManagementViewset(viewsets.ModelViewSet):
    queryset = Refund_Management.objects.all()
    serializer_class = Refund_ManagementSerailizer
'''
class FuelManagementViewset(viewsets.ModelViewSet):
    queryset = Fuel_Management.objects.all()
    serializer_class = Fuel_ManagementSerailizer

class MaintainanceManagementViewset(viewsets.ModelViewSet):
    queryset = Maintenance_Management.objects.all()
    serializer_class = Maintenance_ManagementSerailizer
'''
class RouteViewset(viewsets.ModelViewSet):
    queryset = Route_Management.objects.all()
    serializer_class = Route_ManagementSerailizer
'''
'''
class Fare_Management_OutstationViewset(viewsets.ModelViewSet):
    queryset = Fare_Management_Outstation.objects.all()
    serializer_class = Fare_Management_OutstationSerailizer

'''
class Fare_ManagementViewset(viewsets.ModelViewSet):
    queryset = Fare_Management.objects.all()
    serializer_class = Fare_ManagementSerailizer
'''
class TimeScheduleViewset(viewsets.ModelViewSet):
    queryset = Time_Schedule_Management.objects.all()
    serializer_class = Time_Schedule_ManagementSerailizer


class PickupPointViewset(viewsets.ModelViewSet):
    queryset = Pickup_Point.objects.all()
    serializer_class = Pickup_PointSerailizer


class DropUpPointViewset(viewsets.ModelViewSet):
    queryset = Pickup_Point.objects.all()
    serializer_class = Pickup_PointSerailizer
'''
class ListingAssignViewset(viewsets.ModelViewSet):
    queryset = Listing_Assign_Management.objects.all()
    serializer_class = Listing_Assign_ManagementSerailizer

class CoPartnerManagementViewset(viewsets.ModelViewSet):
    queryset = Co_Partner_Management.objects.all()
    serializer_class = Co_Partner_ManagementSerailizer

class NotificationToRiderViewset(viewsets.ModelViewSet):
    queryset = Notification_to_Ridder.objects.all()
    serializer_class = Notification_to_RidderSerailizer

class NotificationToDriverViewset(viewsets.ModelViewSet):
    queryset = Notification_to_Driver.objects.all()
    serializer_class = Notification_to_DriverSerailizer
'''
class ConsignmentTrackingViewset(viewsets.ModelViewSet):
    queryset = Consignment_Tracking.objects.all()
    serializer_class = Consignment_TrackingSerailizer

class TransactionManagementViewset(viewsets.ModelViewSet):
    queryset = Transaction_Management.objects.all()
    serializer_class = Transaction_ManagementSerailizer
'''
class ListYourVehicleViewset(viewsets.ModelViewSet):
    queryset = List_Your_Vehicle_Management.objects.all()
    serializer_class = List_Your_Vehicle_ManagementSerailizer

class FeedbackViewset(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = Feedbackserializer
'''
class SeatManagementViewset(viewsets.ModelViewSet):
    queryset = Seat_Management.objects.all()
    serializer_class = Seat_MangementSerailizer
'''
class SOSViewset(viewsets.ModelViewSet):
    queryset = SOS.objects.all()
    serializer_class = SOSSerailizer

class SupportHelpViewset(viewsets.ModelViewSet):
    queryset = Support_Help.objects.all()
    serializer_class = Support_HelpSerailizer

class TermsConditionViewset(viewsets.ModelViewSet):
    queryset = TERMS_CONDITIONS.objects.all()
    serializer_class = TERMS_CONDITIONSSerailizer

class PrivacyPolicyViewset(viewsets.ModelViewSet):
    queryset = PRIVACY_POLICY.objects.all()
    serializer_class = PRIVACY_POLICYSerailizer

##
class TemplatesManagementViewset(viewsets.ModelViewSet):
    queryset = Templates_Management.objects.all()
    serializer_class = Templates_ManagementSerailizer

class TransactionManagementViewset(viewsets.ModelViewSet):
    queryset = Transaction_Management.objects.all()
    serializer_class = Transaction_ManagementSerailizer




###


'''

class TransactionManagementViewset(viewsets.ModelViewSet):
    queryset = Context.objects.all()
    serializer_class = ContextSerailizer

class TemplatesManagementViewset(viewsets.ModelViewSet):
    queryset = TemplatesManagement.objects.all()
    serializer_class = TemplatesManagementSerailizer

    '''
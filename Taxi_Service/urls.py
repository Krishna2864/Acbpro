from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'admin', views.AdvertisementManagementViewset)

router.register(r'vehicle/', views.VehicleManagementViewset,basename='vehicle')
#Todo Aayushi Change the URL name for rest
router.register(r'driver', views.DriverManagementViewset)
router.register(r'country', views.CountryManagementViewset)
router.register(r'state', views.StateManagementViewset)
router.register(r'city', views.CityManagementViewset)
router.register(r'advertisement', views.AdvertisementManagementViewset)
router.register(r'refral', views.RefralManagementViewset)
#router.register(r'refund', views.RefundManagementViewset)
router.register(r'fuel', views.FuelManagementViewset)
router.register(r'maintainance', views.MaintainanceManagementViewset)
#router.register(r'route', views.RouteViewset)
router.register(r'fare', views.FareManagementViewset)
#router.register(r'time', views.TimeScheduleViewset)
#router.register(r'pickup', views.PickupPointViewset)
#router.register(r'dropup', views.DropUpPointViewset)
router.register(r'listingassign', views.ListingAssignViewset)
router.register(r'copartner', views.CoPartnerManagementViewset)
router.register(r'notificationtorider', views.NotificationToRiderViewset)
router.register(r'notificationtodriver', views.NotificationToDriverViewset)
#router.register(r'consignment', views.ConsignmentTrackingViewset)
#router.register(r'transaction', views.TransactionManagementViewset)
router.register(r'listyourvehicle', views.ListYourVehicleViewset)
#router.register(r'feedback', views.FeedbackViewset)
#router.register(r'seatmanagement', views.SeatManagementViewset)
router.register(r'sos', views.SOSViewset)
router.register(r'support', views.SupportHelpViewset)
router.register(r'termsconditions', views.TermsConditionViewset)
router.register(r'privacypolicy', views.PrivacyPolicyViewset)

urlpatterns=[
path('', include(router.urls)),
]
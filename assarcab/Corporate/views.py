

from .models import Admin_Management, User_Management, Vehicle_Management, Driver_Mangement, Country_Management, \
    State_Management, City_Management, Advertisement_Management, LOCAL_Second, OUTSTATION_Second, TERMS_CONDITIONS, \
    EMPLOYEE_TRANSPORTATION_Second, EMPLOYEE_TAXI, LOCAL, OUTSTATION, Templates_Management, PRIVACY_POLICY, Support_HELP, \
    SOS, Feedback, LIST_YOUR_VEHICLE_MGMT, Transaction_Management, Notification_to_Driver, Notification_to_Ridder, \
    Co_partner_Management, Listing_ASSIGN_Management, dropup_Points_Management, Pickup_Point_Management, Fare_Management,\
    Fuel_Mangement, Maintenance_Management, Route_Management
from .serializers import Admin_ManagementSerailizer, User_ManagementSerailizer, Vehicle_ManagementSerailizer, \
    Driver_MangementSerailizer, Country_ManagementSerailizer, State_ManagementSerailizer, City_ManagementSerailizer, \
    Advertisement_ManagementSerailizer, LOCAL_SecondSerailizer, OUTSTATION_SecondSerailizer, EMPLOYEE_TAXISerailizer, \
    EMPLOYEE_TRANSPORTATION_SecondSerailizer, LOCALSerailizer, OUTSTATIONSerailizer, Templates_ManagementSerailizer, \
    PRIVACY_POLICYSerailizer, TERMS_CONDITIONSSerailizer, Support_HELPSerailizer, SOSSerailizer, FeedbackSerailizer, \
    LIST_YOUR_VEHICLE_MGMTSerailizer, Transaction_ManagementSerailizer, Notification_to_DriverSerailizer, \
    Notification_to_RidderSerailizer, Co_partner_ManagementSerailizer, Listing_ASSIGN_ManagementSerailizer, \
    dropup_Points_ManagementSerailizer, Pickup_Point_ManagementSerailizer, Fare_ManagementSerailizer, Fuel_MangementSerailizer, \
    Maintenance_ManagementSerailizer, Route_ManagementSerailizer
from rest_framework import viewsets

class AdminManagementViewset(viewsets.ModelViewSet):
    queryset = Admin_Management.objects.all()
    serializer_class = Admin_ManagementSerailizer

class UserManagementViewset(viewsets.ModelViewSet):
    queryset = User_Management.objects.all()
    serializer_class = User_ManagementSerailizer

class VehicleManagementViewset(viewsets.ModelViewSet):
    queryset = Vehicle_Management.objects.all()
    serializer_class = Vehicle_ManagementSerailizer

class DriverManagementViewset(viewsets.ModelViewSet):
    queryset = Driver_Mangement.objects.all()
    serializer_class = Driver_MangementSerailizer

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

# class RefralManagementViewset(viewsets.ModelViewSet):
#     queryset = Refral_Mangemnt.objects.all()
#     serializer_class = Refral_MangemntSerailizer

# class RefundManagementViewset(viewsets.ModelViewSet):
#     queryset = Refund_Management.objects.all()
#     serializer_class = Refund_ManagementSerailizer

class FuelManagementViewset(viewsets.ModelViewSet):
    queryset = Fuel_Mangement.objects.all()
    serializer_class = Fuel_MangementSerailizer

class MaintainanceManagementViewset(viewsets.ModelViewSet):
    queryset = Maintenance_Management.objects.all()
    serializer_class = Maintenance_ManagementSerailizer

class RouteViewset(viewsets.ModelViewSet):
    queryset = Route_Management.objects.all()
    serializer_class = Route_ManagementSerailizer

class FareManagementViewset(viewsets.ModelViewSet):
    queryset = Fare_Management.objects.all()
    serializer_class = Fare_ManagementSerailizer

# class FareOutStationViewset(viewsets.ModelViewSet):
#     queryset = Fare_Management_Outstation.objects.all()
#     serializer_class = Fare_ManagementOutStationSerailizer

# class FareManagementLocalViewset(viewsets.ModelViewSet):
#     queryset = Fare_Management_Local.objects.all()
#     serializer_class = Fare_ManagementLocalSerailizer

# class TimeScheduleManagementViewset(viewsets.ModelViewSet):
#     queryset = TIME_SCHEDULE_MGMT.objects.all()
#     serializer_class = TIME_SCHEDULE_MGMTSerailizer

class PickupPointViewset(viewsets.ModelViewSet):
    queryset = Pickup_Point_Management.objects.all()
    serializer_class = Pickup_Point_ManagementSerailizer

class DropupPointViewset(viewsets.ModelViewSet):
    queryset = dropup_Points_Management.objects.all()
    serializer_class = dropup_Points_ManagementSerailizer

class ListingAssignManagementViewset(viewsets.ModelViewSet):
    queryset = Listing_ASSIGN_Management.objects.all()
    serializer_class = Listing_ASSIGN_ManagementSerailizer

class CoPartnerManagementViewset(viewsets.ModelViewSet):
    queryset = Co_partner_Management.objects.all()
    serializer_class = Co_partner_ManagementSerailizer

class NotificationToRiderViewset(viewsets.ModelViewSet):
    queryset = Notification_to_Ridder.objects.all()
    serializer_class = Notification_to_RidderSerailizer

class NotificationToDriverViewset(viewsets.ModelViewSet):
    queryset = Notification_to_Driver.objects.all()
    serializer_class = Notification_to_DriverSerailizer

class TransactionManagementViewset(viewsets.ModelViewSet):
    queryset = Transaction_Management.objects.all()
    serializer_class = Transaction_ManagementSerailizer

class ListYourVehicleViewset(viewsets.ModelViewSet):
    queryset = LIST_YOUR_VEHICLE_MGMT.objects.all()
    serializer_class = LIST_YOUR_VEHICLE_MGMTSerailizer

class FeedbackViewset(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerailizer

class SOSViewset(viewsets.ModelViewSet):
    queryset = SOS.objects.all()
    serializer_class = SOSSerailizer

class SupportHelpViewset(viewsets.ModelViewSet):
    queryset = Support_HELP.objects.all()
    serializer_class = Support_HELPSerailizer

class TermsConditionViewset(viewsets.ModelViewSet):
    queryset = TERMS_CONDITIONS.objects.all()
    serializer_class = TERMS_CONDITIONSSerailizer

class PrivacyPolicyViewset(viewsets.ModelViewSet):
    queryset = PRIVACY_POLICY.objects.all()
    serializer_class = PRIVACY_POLICYSerailizer

class TemplatesManagementViewset(viewsets.ModelViewSet):
    queryset = Templates_Management.objects.all()
    serializer_class = Templates_ManagementSerailizer

class OutstationViewset(viewsets.ModelViewSet):
    queryset = OUTSTATION.objects.all()
    serializer_class = OUTSTATIONSerailizer

class LocalViewset(viewsets.ModelViewSet):
    queryset = LOCAL.objects.all()
    serializer_class = LOCALSerailizer

class EmployeeTaxiViewset(viewsets.ModelViewSet):
    queryset = EMPLOYEE_TAXI.objects.all()
    serializer_class = EMPLOYEE_TAXISerailizer

class EmployeeTransportationViewset(viewsets.ModelViewSet):
    queryset = EMPLOYEE_TRANSPORTATION_Second.objects.all()
    serializer_class = EMPLOYEE_TRANSPORTATION_SecondSerailizer

class OutstationSecondViewset(viewsets.ModelViewSet):
    queryset = OUTSTATION_Second.objects.all()
    serializer_class = OUTSTATION_SecondSerailizer

class LocalSecondViewset(viewsets.ModelViewSet):
    queryset = LOCAL_Second.objects.all()
    serializer_class = LOCAL_SecondSerailizer

# @api_view(['GET'])
# def adminList(request):
#     admin1=Admin_Management.objects.all()
#     if admin1 is None:
#         JsonResponse("No records")
#     else:
#       serializer=Admin_ManagementSerailizer(admin1,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def adminDetail(request,pk):
#     admin1=Admin_Management.objects.get(id=pk)
#     serializer=Admin_ManagementSerailizer(admin1,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def adminCreate(request):
#     serializer=Admin_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def adminUpdate(request,pk):
#     admin1=Admin_Management.objects.get(id=pk)
#     serializer=Admin_ManagementSerailizer(instance=admin1,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def adminDelete(request,pk):
#     admin1=Admin_Management.objects.get(id=pk)
#     admin1.delete()
#     return JsonResponse("Deleted")

# @api_view(['GET'])
# def userList(request):
#     user=User_Management.objects.all()
#     if user is None:
#         JsonResponse("No records")
#     else:
#       serializer=User_ManagementSerailizer(user,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def userDetail(request,pk):
#     user=User_Management.objects.get(id=pk)
#     serializer=User_ManagementSerailizer(user,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def userCreate(request):
#     serializer=User_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def userUpdate(request,pk):
#     user=User_Management.objects.get(id=pk)
#     serializer=User_ManagementSerailizer(instance=user,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def userDelete(request,pk):
#     user=User_Management.objects.get(id=pk)
#     user.delete()
#     return JsonResponse("Deleted")

#3
# @api_view(['GET'])
# def vehicleList(request):
#     vehicle=Vehicle_Management.objects.all()
#     if vehicle is None:
#         JsonResponse("No records")
#     else:
#       serializer=Vehicle_ManagementSerailizer(vehicle,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def vehicleDetail(request,pk):
#     vehicle=Vehicle_Management.objects.get(id=pk)
#     serializer=Vehicle_ManagementSerailizer(vehicle,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def vehicleCreate(request):
#     serializer=Vehicle_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def vehicleUpdate(request,pk):
#     vehicle=Vehicle_Management.objects.get(id=pk)
#     serializer=Vehicle_ManagementSerailizer(instance=vehicle,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def vehicleDelete(request,pk):
#     vehicle=Vehicle_Management.objects.get(id=pk)
#     vehicle.delete()
#     return JsonResponse("Deleted")

#4
# @api_view(['GET'])
# def driverList(request):
#     driver=Driver_Mangement.objects.all()
#     if Driver_Mangement is None:
#         JsonResponse("No records")
#     else:
#       serializer=Driver_MangementSerailizer(driver,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def driverDetail(request,pk):
#     driver=Driver_Mangement.objects.get(id=pk)
#     serializer=Driver_MangementSerailizer(driver,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def driverCreate(request):
#     serializer=Driver_MangementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def driverUpdate(request,pk):
#     driver=Driver_Mangement.objects.get(id=pk)
#     serializer=Driver_MangementSerailizer(instance=driver,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def driverDelete(request,pk):
#     driver=Driver_Mangement.objects.get(id=pk)
#     driver.delete()
#     return JsonResponse("Deleted")

#5
# @api_view(['GET'])
# def countryList(request):
#     country=Country_Management.objects.all()
#     if country is None:
#         JsonResponse("No records")
#     else:
#       serializer=Country_ManagementSerailizer(country,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def countryDetail(request,pk):
#     country=Country_Management.objects.get(id=pk)
#     serializer=Country_ManagementSerailizer(country,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def countryCreate(request):
#     serializer=Country_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def countryUpdate(request,pk):
#     country=Country_Management.objects.get(id=pk)
#     serializer=Country_ManagementSerailizer(instance=country,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def countryDelete(request,pk):
#     country=Country_Management.objects.get(id=pk)
#     country.delete()
#     return JsonResponse("Deleted")

#6
# @api_view(['GET'])
# def stateList(request):
#     state=State_Management.objects.all()
#     if state is None:
#         JsonResponse("No records")
#     else:
#       serializer=State_ManagementSerailizer(state,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def stateDetail(request,pk):
#     state=State_Management.objects.get(id=pk)
#     serializer=State_ManagementSerailizer(state,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def stateCreate(request):
#     serializer=State_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def stateUpdate(request,pk):
#     state=State_Management.objects.get(id=pk)
#     serializer=State_ManagementSerailizer(instance=state,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def stateDelete(request,pk):
#     state=State_Management.objects.get(id=pk)
#     state.delete()
#     return JsonResponse("Deleted")
#7
# @api_view(['GET'])
# def cityList(request):
#     city=City_Management.objects.all()
#     if city is None:
#         JsonResponse("No records")
#     else:
#       serializer=City_ManagementSerailizer(city,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def cityDetail(request,pk):
#     city=City_Management.objects.get(id=pk)
#     serializer=City_ManagementSerailizer(city,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def cityCreate(request):
#     serializer=City_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def cityUpdate(request,pk):
#     city=City_Management.objects.get(id=pk)
#     serializer=City_ManagementSerailizer(instance=city,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def cityDelete(request,pk):
#     city=City_Management.objects.get(id=pk)
#     city.delete()
#     return JsonResponse("Deleted")

#8
# @api_view(['GET'])
# def advertismentList(request):
#     advertisment=Advertisement_Management.objects.all()
#     if advertisment is None:
#         JsonResponse("No records")
#     else:
#       serializer=Advertisement_ManagementSerailizer(advertisment,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def advertismentDetail(request,pk):
#     advertisment=Advertisement_Management.objects.get(id=pk)
#     serializer=Advertisement_ManagementSerailizer(advertisment,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def advertismentCreate(request):
#     serializer=Advertisement_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def advertismentUpdate(request,pk):
#     advertisment=Advertisement_Management.objects.get(id=pk)
#     serializer=Advertisement_ManagementSerailizer(instance=advertisment,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def advertismentDelete(request,pk):
#     advertisment=Advertisement_Management.objects.get(id=pk)
#     advertisment.delete()
#     return JsonResponse("Deleted")
#
#9
# @api_view(['GET'])
# def refralList(request):
#     refral=Refral_Mangemnt.objects.all()
#     if refral is None:
#         JsonResponse("No records")
#     else:
#       serializer=Refral_MangemntSerailizer(refral,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def refralDetail(request,pk):
#     refral=Refral_Mangemnt.objects.get(id=pk)
#     serializer=Refral_MangemntSerailizer(refral,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def refralCreate(request):
#     serializer=Refral_MangemntSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def refralUpdate(request,pk):
#     refral=Refral_Mangemnt.objects.get(id=pk)
#     serializer=Refral_MangemntSerailizer(instance=refral,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def refralDelete(request,pk):
#     refral=Refral_Mangemnt.objects.get(id=pk)
#     refral.delete()
#     return JsonResponse("Deleted")

#10
# @api_view(['GET'])
# def refundList(request):
#     refund=Refund_Management.objects.all()
#     if refund is None:
#         JsonResponse("No records")
#     else:
#       serializer=Refund_ManagementSerailizer(refund,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def refundDetail(request,pk):
#     refund=Refund_Management.objects.get(id=pk)
#     serializer=Refund_ManagementSerailizer(refund,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def refundCreate(request):
#     serializer=Refund_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def refundUpdate(request,pk):
#     refund=Refund_Management.objects.get(id=pk)
#     serializer=Refund_ManagementSerailizer(instance=refund,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def refundDelete(request,pk):
#     refund=Refund_Management.objects.get(id=pk)
#     refund.delete()
#     return JsonResponse("Deleted")
#11
# @api_view(['GET'])
# def fuelList(request):
#     fuel=Fuel_Mangement.objects.all()
#     if fuel is None:
#         JsonResponse("No records")
#     else:
#       serializer=Fuel_MangementSerailizer(fuel,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def fuelDetail(request,pk):
#     fuel=Fuel_Mangement.objects.get(id=pk)
#     serializer=Fuel_MangementSerailizer(fuel,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def fuelCreate(request):
#     serializer=Fuel_MangementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def fuelUpdate(request,pk):
#     fuel=Fuel_Mangement.objects.get(id=pk)
#     serializer=Fuel_MangementSerailizer(instance=fuel,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def fuelDelete(request,pk):
#     fuel=Fuel_Mangement.objects.get(id=pk)
#     fuel.delete()
#     return JsonResponse("Deleted")

#12
# @api_view(['GET'])
# def maintenanceList(request):
#     maintenance=Maintenance_Management.objects.all()
#     if maintenance is None:
#         JsonResponse("No records")
#     else:
#       serializer=Maintenance_ManagementSerailizer(maintenance,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def maintenanceDetail(request,pk):
#     maintenance=Maintenance_Management.objects.get(id=pk)
#     serializer=Maintenance_ManagementSerailizer(maintenance,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def maintenanceCreate(request):
#     serializer=Maintenance_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def maintenanceUpdate(request,pk):
#     maintenance=Maintenance_Management.objects.get(id=pk)
#     serializer=Maintenance_ManagementSerailizer(instance=maintenance,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def maintenanceDelete(request,pk):
#     maintenance=Maintenance_Management.objects.get(id=pk)
#     maintenance.delete()
#     return JsonResponse("Deleted")

#13
# @api_view(['GET'])
# def routeList(request):
#     route=Route_Management.objects.all()
#     if route is None:
#         JsonResponse("No records")
#     else:
#       serializer=Route_ManagementSerailizer(route,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def routeDetail(request,pk):
#     route=Route_Management.objects.get(id=pk)
#     serializer=Route_ManagementSerailizer(route,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def routeCreate(request):
#     serializer=Route_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def routeUpdate(request,pk):
#     route=Route_Management.objects.get(id=pk)
#     serializer=Route_ManagementSerailizer(instance=route,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def routeDelete(request,pk):
#     route=Route_Management.objects.get(id=pk)
#     route.delete()
#     return JsonResponse("Deleted")

#14
# @api_view(['GET'])
# def fareList(request):
#     fare=Fare_Management.objects.all()
#     if fare is None:
#         JsonResponse("No records")
#     else:
#       serializer=Fare_ManagementSerailizer(fare,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def fareDetail(request,pk):
#     fare=Fare_Management.objects.get(id=pk)
#     serializer=Fare_ManagementSerailizer(fare,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def fareCreate(request):
#     serializer=Fare_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def fareUpdate(request,pk):
#     fare=Fare_Management.objects.get(id=pk)
#     serializer=Fare_ManagementSerailizer(instance=fare,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def fareDelete(request,pk):
#     fare=Fare_Management.objects.get(id=pk)
#     fare.delete()
#     return JsonResponse("Deleted")
#####
#####from hereeeee
# @api_view(['GET'])
# def farelistoutstation(request):
#     fare=Fare_Management_Outstation.objects.all()
#     if fare is None:
#         JsonResponse("No records")
#     else:
#       serializer=Fare_ManagementOutStationSerailizer(fare,many=True)
#     return Response({'result':serializer.data},safe=True)
# @api_view(['GET'])
# def faredetailoutstation(request,pk):
#     fare=Fare_Management_Outstation.objects.get(id=pk)
#     serializer=Fare_ManagementOutStationSerailizer(fare,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def farecreateoutstation(request):
#     serializer=Fare_ManagementOutStationSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return jsonResponse(serializer.data,safe=True)
# @api_view(['POST'])
# def fareupdateoutstation(request,pk):
#     fare=Fare_Management_Outstation.objects.get(id=pk)
#     serializer=Fare_ManagementOutStationSerailizer(instance=fare,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def faredeleteoutstation(request,pk):
#     fare=Fare_Management_Outstation.objects.get(id=pk)
#     fare.delete()
#     return JsonResponse("Deleted")
# @api_view(['GET'])
# def farelistlocal(request):
#     fare=Fare_Management_Local.objects.all()
#     if fare is None:
#         JsonResponse("No records")
#     else:
#       serializer=Fare_ManagementLocalSerailizer(fare,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def faredetaillocal(request,pk):
#     fare=Fare_Management_Local.objects.get(id=pk)
#     serializer=Fare_ManagementLocalSerailizer(fare,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def farecreatelocal(request):
#     serializer=Fare_ManagementLocalSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def fareupdatelocal(request,pk):
#     fare=Fare_Management_Local.objects.get(id=pk)
#     serializer=Fare_ManagementLocalSerailizer(instance=fare,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def faredeletelocal(request,pk):
#     fare=Fare_Management_Local.objects.get(id=pk)
#     fare.delete()
#     return JsonResponse("Deleted")
#15
# @api_view(['GET'])
# def time_scheduleList(request):
#     time_schedule=TIME_SCHEDULE_MGMT.objects.all()
#     if time_schedule is None:
#         JsonResponse("No records")
#     else:
#       serializer=TIME_SCHEDULE_MGMTSerailizer(time_schedule,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def time_scheduleDetail(request,pk):
#     time_schedule=TIME_SCHEDULE_MGMT.objects.get(id=pk)
#     serializer=TIME_SCHEDULE_MGMTSerailizer(time_schedule,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def time_scheduleCreate(request):
#     serializer=TIME_SCHEDULE_MGMTSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def time_scheduleUpdate(request,pk):
#     time_schedule=TIME_SCHEDULE_MGMT.objects.get(id=pk)
#     serializer=TIME_SCHEDULE_MGMTSerailizer(instance=time_schedule,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def time_scheduleDelete(request,pk):
#     time_schedule=TIME_SCHEDULE_MGMT.objects.get(id=pk)
#     time_schedule.delete()
#     return JsonResponse("Deleted")

#16
# from .models import
# from .serializers import
# @api_view(['GET'])
# def pickup_pointList(request):
#     pickup_point=Pickup_Point_Management.objects.all()
#     if pickup_point is None:
#         JsonResponse("No records")
#     else:
#       serializer=Pickup_Point_ManagementSerailizer(pickup_point,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def pickup_pointDetail(request,pk):
#     pickup_point=Pickup_Point_Management.objects.get(id=pk)
#     serializer=Pickup_Point_ManagementSerailizer(pickup_point,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def pickup_pointCreate(request):
#     serializer=Pickup_Point_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def pickup_pointUpdate(request,pk):
#     pickup_point=Pickup_Point_Management.objects.get(id=pk)
#     serializer=Pickup_Point_ManagementSerailizer(instance=pickup_point,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def pickup_pointDelete(request,pk):
#     pickup_point=Pickup_Point_Management.objects.get(id=pk)
#     pickup_point.delete()
#     return JsonResponse("Deleted")




##dropup
# @api_view(['GET'])
# def dropup_pointList(request):
#     pickup_point= dropup_Points_Management.objects.all()
#     if pickup_point is None:
#         JsonResponse("No records")
#     else:
#       serializer= dropup_Points_ManagementSerailizer(pickup_point,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def dropup_pointDetail(request,pk):
#     pickup_point= dropup_Points_Management.objects.get(id=pk)
#     serializer= dropup_Points_ManagementSerailizer(pickup_point,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def dropup_pointCreate(request):
#     serializer= dropup_Points_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def dropup_pointUpdate(request,pk):
#     pickup_point= dropup_Points_Management.objects.get(id=pk)
#     serializer= dropup_Points_ManagementSerailizer(instance=pickup_point,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def dropup_pointDelete(request,pk):
#     pickup_point= dropup_Points_Management.objects.get(id=pk)
#     pickup_point.delete()
#     return JsonResponse("Deleted")


# '''
# #17
# from .models import DROPUp_Point_Management
# from .serializers import DROPUp_Point_ManagementSerailizer
# @api_view(['GET'])
# def dropup_pointList(request):
#     dropup_point=DROPUp_Point_Management.objects.all()
#     if dropup_point is None:
#         JsonResponse("No records")
#     else:
#       serializer=DROPUp_Point_ManagementSerailizer(dropup_point,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def dropup_pointDetail(request,pk):
#     dropup_point=DROPUp_Point_Management.objects.get(id=pk)
#     serializer=DROPUp_Point_ManagementSerailizer(dropup_point,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def dropup_pointCreate(request):
#     serializer=DROPUp_Point_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def dropup_pointUpdate(request,pk):
#     dropup_point=DROPUp_Point_Management.objects.get(id=pk)
#     serializer=DROPUp_Point_ManagementSerailizer(instance=dropup_point,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def dropup_pointDelete(request,pk):
#     dropup_point=DROPUp_Point_Management.objects.get(id=pk)
#     dropup_point.delete()
#     return JsonResponse("Deleted")
# '''
#18
# @api_view(['GET'])
# def listing_assignList(request):
#     listing_assign=Listing_ASSIGN_Management.objects.all()
#     if listing_assign is None:
#         JsonResponse("No records")
#     else:
#       serializer=Listing_ASSIGN_ManagementSerailizer(listing_assign,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def listing_assignDetail(request,pk):
#     listing_assign=Listing_ASSIGN_Management.objects.get(id=pk)
#     serializer=Listing_ASSIGN_ManagementSerailizer(listing_assign,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def listing_assignCreate(request):
#     serializer=Listing_ASSIGN_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def listing_assignUpdate(request,pk):
#     listing_assign=Listing_ASSIGN_Management.objects.get(id=pk)
#     serializer=Listing_ASSIGN_ManagementSerailizer(instance=listing_assign,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def listing_assignDelete(request,pk):
#     listing_assign=Listing_ASSIGN_Management.objects.get(id=pk)
#     listing_assign.delete()
#     return JsonResponse("Deleted")

#19
# @api_view(['GET'])
# def co_partnerList(request):
#     co_partner=Co_partner_Management.objects.all()
#     if co_partner is None:
#         JsonResponse("No records")
#     else:
#       serializer=Co_partner_ManagementSerailizer(co_partner,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def co_partnerDetail(request,pk):
#     co_partner=Co_partner_Management.objects.get(id=pk)
#     serializer=Co_partner_ManagementSerailizer(co_partner,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def co_partnerCreate(request):
#     serializer=Co_partner_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def co_partnerUpdate(request,pk):
#     co_partner=Co_partner_Management.objects.get(id=pk)
#     serializer=Co_partner_ManagementSerailizer(instance=co_partner,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def co_partnerDelete(request,pk):
#     co_partner=Co_partner_Management.objects.get(id=pk)
#     co_partner.delete()
#     return JsonResponse("Deleted")

#20
# @api_view(['GET'])
# def notification_to_ridderList(request):
#     notification_to_ridder=Notification_to_Ridder.objects.all()
#     if notification_to_ridder is None:
#         JsonResponse("No records")
#     else:
#       serializer=Notification_to_RidderSerailizer(notification_to_ridder,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def notification_to_ridderDetail(request,pk):
#     notification_to_ridder=Notification_to_Ridder.objects.get(id=pk)
#     serializer=Notification_to_RidderSerailizer(notification_to_ridder,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def notification_to_ridderCreate(request):
#     serializer=Notification_to_RidderSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def notification_to_ridderUpdate(request,pk):
#     notification_to_ridder=Notification_to_Ridder.objects.get(id=pk)
#     serializer=Notification_to_RidderSerailizer(instance=notification_to_ridder,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def notification_to_ridderDelete(request,pk):
#     notification_to_ridder=Notification_to_Ridder.objects.get(id=pk)
#     notification_to_ridder.delete()
#     return JsonResponse("Deleted")

#21
# @api_view(['GET'])
# def notification_to_driverList(request):
#     notification_to_driver=Notification_to_Driver.objects.all()
#     if notification_to_driver is None:
#         JsonResponse("No records")
#     else:
#       serializer=Notification_to_DriverSerailizer(notification_to_driver,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def notification_to_driverDetail(request,pk):
#     notification_to_driver=Notification_to_Driver.objects.get(id=pk)
#     serializer=Notification_to_DriverSerailizer(notification_to_driver,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def notification_to_driverCreate(request):
#     serializer=Notification_to_DriverSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def notification_to_driverUpdate(request,pk):
#     notification_to_driver=Notification_to_Driver.objects.get(id=pk)
#     serializer=Notification_to_DriverSerailizer(instance=notification_to_driver,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def notification_to_driverDelete(request,pk):
#     notification_to_driver=Notification_to_Driver.objects.get(id=pk)
#     notification_to_driver.delete()
#     return JsonResponse("Deleted")

#22
# '''
# from .models import Consignment_Tracking
# from .serializers import Consignment_TrackingSerailizer
# @api_view(['GET'])
# def consignment_trackingList(request):
#     consignment_tracking=Consignment_Tracking.objects.all()
#     if consignment_tracking is None:
#         JsonResponse("No records")
#     else:
#       serializer=Consignment_TrackingSerailizer(consignment_tracking,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def consignment_trackingDetail(request,pk):
#     consignment_tracking=Consignment_Tracking.objects.get(id=pk)
#     serializer=Consignment_TrackingSerailizer(consignment_tracking,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def consignment_trackingCreate(request):
#     serializer=Consignment_TrackingSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def consignment_trackingUpdate(request,pk):
#     consignment_tracking=Consignment_Tracking.objects.get(id=pk)
#     serializer=Consignment_TrackingSerailizer(instance=consignment_tracking,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def consignment_trackingDelete(request,pk):
#     consignment_tracking=Consignment_Tracking.objects.get(id=pk)
#     consignment_tracking.delete()
#     return JsonResponse("Deleted")
# '''
#23
# @api_view(['GET'])
# def transactionList(request):
#     transaction=Transaction_Management.objects.all()
#     if transaction is None:
#         JsonResponse("No records")
#     else:
#       serializer=Transaction_ManagementSerailizer(transaction,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def transactionDetail(request,pk):
#     transaction=Transaction_Management.objects.get(id=pk)
#     serializer=Transaction_ManagementSerailizer(transaction,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def transactionCreate(request):
#     serializer=Transaction_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def transactionUpdate(request,pk):
#     transaction=Transaction_Management.objects.get(id=pk)
#     serializer=Transaction_ManagementSerailizer(instance=transaction,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def transactionDelete(request,pk):
#     transaction=Transaction_Management.objects.get(id=pk)
#     transaction.delete()
#     return JsonResponse("Deleted")

#24
# @api_view(['GET'])
# def list_your_vehicleList(request):
#     list_your_vehicle=LIST_YOUR_VEHICLE_MGMT.objects.all()
#     if list_your_vehicle is None:
#         JsonResponse("No records")
#     else:
#       serializer=LIST_YOUR_VEHICLE_MGMTSerailizer(list_your_vehicle,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def list_your_vehicleDetail(request,pk):
#     list_your_vehicle=LIST_YOUR_VEHICLE_MGMT.objects.get(id=pk)
#     serializer=LIST_YOUR_VEHICLE_MGMTSerailizer(list_your_vehicle,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def list_your_vehicleCreate(request):
#     serializer=LIST_YOUR_VEHICLE_MGMTSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def list_your_vehicleUpdate(request,pk):
#     list_your_vehicle=LIST_YOUR_VEHICLE_MGMT.objects.get(id=pk)
#     serializer=LIST_YOUR_VEHICLE_MGMTSerailizer(instance=list_your_vehicle,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def list_your_vehicleDelete(request,pk):
#     list_your_vehicle=LIST_YOUR_VEHICLE_MGMT.objects.get(id=pk)
#     list_your_vehicle.delete()
#     return JsonResponse("Deleted")

#25
# @api_view(['GET'])
# def feedbackList(request):
#     feedback=Feedback.objects.all()
#     if feedback is None:
#         JsonResponse("No records")
#     else:
#       serializer=FeedbackSerailizer(feedback,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def feedbackDetail(request,pk):
#     feedback=Feedback.objects.get(id=pk)
#     serializer=FeedbackSerailizer(feedback,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def feedbackCreate(request):
#     serializer=FeedbackSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def feedbackUpdate(request,pk):
#     feedback=Feedback.objects.get(id=pk)
#     serializer=FeedbackSerailizer(instance=feedback,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def feedbackDelete(request,pk):
#     feedback=Feedback.objects.get(id=pk)
#     feedback.delete()
#     return JsonResponse("Deleted")


#26
# '''
# from .models import Seat_Mangement
# from .serializers import Seat_MangementSerailizer
# @api_view(['GET'])
# def seatList(request):
#     seat=Seat_Mangement.objects.all()
#     if seat is None:
#         JsonResponse("No records")
#     else:
#       serializer=Seat_MangementSerailizer(seat,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def seatDetail(request,pk):
#     seat=Seat_Mangement.objects.get(id=pk)
#     serializer=Seat_MangementSerailizer(seat,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def seatCreate(request):
#     serializer=Seat_MangementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def seatUpdate(request,pk):
#     seat=Seat_Mangement.objects.get(id=pk)
#     serializer=Seat_MangementSerailizer(instance=seat,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def seatDelete(request,pk):
#     seat=Seat_Mangement.objects.get(id=pk)
#     seat.delete()
#     return JsonResponse("Deleted")
# '''
#27
# @api_view(['GET'])
# def sosList(request):
#     sos=SOS.objects.all()
#     if sos is None:
#         JsonResponse("No records")
#     else:
#       serializer=SOSSerailizer(sos,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def sosDetail(request,pk):
#     sos=SOS.objects.get(id=pk)
#     serializer=SOSSerailizer(sos,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def sosCreate(request):
#     serializer=SOSSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def sosUpdate(request,pk):
#     sos=SOS.objects.get(id=pk)
#     serializer=SOSSerailizer(instance=sos,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def sosDelete(request,pk):
#     sos=SOS.objects.get(id=pk)
#     sos.delete()
#     return JsonResponse("Deleted")

#28
# @api_view(['GET'])
# def support_helpList(request):
#     support_help=Support_HELP.objects.all()
#     if support_help is None:
#         JsonResponse("No records")
#     else:
#       serializer=Support_HELPSerailizer(support_help,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def support_helpDetail(request,pk):
#     support_help=Support_HELP.objects.get(id=pk)
#     serializer=Support_HELPSerailizer(support_help,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def support_helpCreate(request):
#     serializer=Support_HELPSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def support_helpUpdate(request,pk):
#     support_help=Support_HELP.objects.get(id=pk)
#     serializer=Support_HELPSerailizer(instance=support_help,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def support_helpDelete(request,pk):
#     support_help=Support_HELP.objects.get(id=pk)
#     support_help.delete()
#     return JsonResponse("Deleted")

#29
# @api_view(['GET'])
# def term_conditionList(request):
#     term_condition=TERMS_CONDITIONS.objects.all()
#     if term_condition is None:
#         JsonResponse("No records")
#     else:
#       serializer=TERMS_CONDITIONS(term_condition,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def term_conditionDetail(request,pk):
#     term_condition=TERMS_CONDITIONS.objects.get(id=pk)
#     serializer=TERMS_CONDITIONSSerailizer(term_condition,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def term_conditionCreate(request):
#     serializer=TERMS_CONDITIONSSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def term_conditionUpdate(request,pk):
#     term_condition=TERMS_CONDITIONS.objects.get(id=pk)
#     serializer=TERMS_CONDITIONSSerailizer(instance=term_condition,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def term_conditionDelete(request,pk):
#     term_condition=TERMS_CONDITIONS.objects.get(id=pk)
#     term_condition.delete()
#     return JsonResponse("Deleted")

#30
# @api_view(['GET'])
# def privacy_policyList(request):
#     privacy_policy=PRIVACY_POLICY.objects.all()
#     if privacy_policy is None:
#         JsonResponse("No records")
#     else:
#       serializer=PRIVACY_POLICYSerailizer(privacy_policy,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def privacy_policyDetail(request,pk):
#     privacy_policy=PRIVACY_POLICY.objects.get(id=pk)
#     serializer=PRIVACY_POLICYSerailizer(privacy_policy,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def privacy_policyCreate(request):
#     serializer=PRIVACY_POLICYSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def privacy_policyUpdate(request,pk):
#     privacy_policy=PRIVACY_POLICY.objects.get(id=pk)
#     serializer=PRIVACY_POLICYSerailizer(instance=privacy_policy,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def privacy_policyDelete(request,pk):
#     privacy_policy=PRIVACY_POLICY.objects.get(id=pk)
#     privacy_policy.delete()
#     return JsonResponse("Deleted")



####################


################################
#
# #####
# @api_view(['GET'])
# def templateList(request):
#     admin1=Templates_Management.objects.all()
#     if admin1 is None:
#         JsonResponse("No records")
#     else:
#       serializer=Templates_ManagementSerailizer(admin1,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def templateDetail(request,pk):
#     admin1=Templates_Management.objects.get(id=pk)
#     serializer=Templates_ManagementSerailizer(admin1,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def templateCreate(request):
#     serializer=Templates_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def templateUpdate(request,pk):
#     admin1=Templates_Management.objects.get(id=pk)
#     serializer=Templates_ManagementSerailizer(instance=admin1,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def templateDelete(request,pk):
#     admin1=Templates_Management.objects.get(id=pk)
#     admin1.delete()
#     return JsonResponse("Deleted")







#####2
# @api_view(['GET'])
# def outstationList(request):
#     admin1=OUTSTATION.objects.all()
#     if admin1 is None:
#         JsonResponse("No records")
#     else:
#       serializer=Fare_ManagementOutStationSerailizer(admin1,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def outstationDetail(request,pk):
#     admin1=OUTSTATION.objects.get(id=pk)
#     serializer=Fare_ManagementOutStationSerailizer(admin1,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def outstationCreate(request):
#     serializer=Fare_ManagementOutStationSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def outstationUpdate(request,pk):
#     admin1=OUTSTATION.objects.get(id=pk)
#     serializer=Fare_ManagementOutStationSerailizer(instance=admin1,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def outstationDelete(request,pk):
#     admin1=OUTSTATION.objects.get(id=pk)
#     admin1.delete()
#     return JsonResponse("Deleted")


#####3
# @api_view(['GET'])
# def localList(request):
#     admin1=LOCAL.objects.all()
#     if admin1 is None:
#         JsonResponse("No records")
#     else:
#       serializer=Fare_ManagementLocalSerailizer(admin1,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def localDetail(request,pk):
#     admin1=LOCAL.objects.get(id=pk)
#     serializer=Fare_ManagementLocalSerailizer(admin1,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def localCreate(request):
#     serializer=Fare_ManagementLocalSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def localUpdate(request,pk):
#     admin1=LOCAL.objects.get(id=pk)
#     serializer=Fare_ManagementLocalSerailizer(instance=admin1,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def localDelete(request,pk):
#     admin1=LOCAL.objects.get(id=pk)
#     admin1.delete()
#     return JsonResponse("Deleted")


#####444
# @api_view(['GET'])
# def employeeList(request):
#     admin1=EMPLOYEE_TAXI.objects.all()
#     if admin1 is None:
#         JsonResponse("No records")
#     else:
#       serializer=EMPLOYEE_TAXISerailizer(admin1,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def employeeDetail(request,pk):
#     admin1=EMPLOYEE_TAXI.objects.get(id=pk)
#     serializer=EMPLOYEE_TAXISerailizer(admin1,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def employeeCreate(request):
#     serializer=EMPLOYEE_TAXISerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def employeeUpdate(request,pk):
#     admin1=EMPLOYEE_TAXI.objects.get(id=pk)
#     serializer=EMPLOYEE_TAXISerailizer(instance=admin1,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def employeeDelete(request,pk):
#     admin1=EMPLOYEE_TAXI.objects.get(id=pk)
#     admin1.delete()
#     return JsonResponse("Deleted")
#####555555
# @api_view(['GET'])
# def employeetransportationList(request):
#     admin1=EMPLOYEE_TRANSPORTATION_Second.objects.all()
#     if admin1 is None:
#         JsonResponse("No records")
#     else:
#       serializer=EMPLOYEE_TRANSPORTATION_SecondSerailizer(admin1,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def employeetransportationDetail(request,pk):
#     admin1=EMPLOYEE_TRANSPORTATION_Second.objects.get(id=pk)
#     serializer=EMPLOYEE_TRANSPORTATION_SecondSerailizer(admin1,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def employeetransportationCreate(request):
#     serializer=EMPLOYEE_TRANSPORTATION_SecondSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def employeetransportationUpdate(request,pk):
#     admin1=EMPLOYEE_TRANSPORTATION_Second.objects.get(id=pk)
#     serializer=EMPLOYEE_TRANSPORTATION_SecondSerailizer(instance=admin1,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def employeetransportationDelete(request,pk):
#     admin1=EMPLOYEE_TRANSPORTATION_Second.objects.get(id=pk)
#     admin1.delete()
#     return JsonResponse("Deleted")

# @api_view(['GET'])
# def outstationlistsecond(request):
#     admin1=OUTSTATION_Second.objects.all()
#     if admin1 is None:
#         JsonResponse("No records")
#     else:
#       serializer=OUTSTATION_SecondSerailizer(admin1,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def outstationdetailsecond(request,pk):
#     admin1=OUTSTATION_Second.objects.get(id=pk)
#     serializer=OUTSTATION_SecondSerailizer(admin1,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def outstationcreatesecond(request):
#     serializer=OUTSTATION_SecondSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def outstationupdatesecond(request,pk):
#     admin1=OUTSTATION_Second.objects.get(id=pk)
#     serializer=OUTSTATION_SecondSerailizer(instance=admin1,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def outstationDeletesecond(request,pk):
#     admin1=OUTSTATION_Second.objects.get(id=pk)
#     admin1.delete()
#     return JsonResponse("Deleted")
#####3
# @api_view(['GET'])
# def localListsecond(request):
#     admin1=LOCAL_Second.objects.all()
#     if admin1 is None:
#         JsonResponse("No records")
#     else:
#       serializer=LOCAL_SecondSerailizer(admin1,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def localDetailsecond(request,pk):
#     admin1=LOCAL_Second.objects.get(id=pk)
#     serializer=LOCAL_SecondSerailizer(admin1,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def localCreatesecond(request):
#     serializer=LOCAL_SecondSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def localUpdatesecond(request,pk):
#     admin1=LOCAL_Second.objects.get(id=pk)
#     serializer=LOCAL_SecondSerailizer(instance=admin1,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def localDeletesecond(request,pk):
#     admin1=LOCAL_Second.objects.get(id=pk)
#     admin1.delete()
#     return JsonResponse("Deleted")












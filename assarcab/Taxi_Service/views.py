from .models import Admin_Management, User_Management, Drive_Management, Country_Management, State_Management, City, \
City_Management
from .serializers import Admin_ManagementSerailizer, User_ManagementSerailizer, Drive_ManagementSerailizer, \
    Country_ManagementSerailizer, State_ManagementSerailizer, CitySerailizer, City_ManagementSerailizer
from rest_framework import viewsets

class AdminManagementViewset(viewsets.ModelViewSet):
    queryset = Admin_Management.objects.all()
    serializer_class = Admin_ManagementSerailizer

class UserManagementViewset(viewsets.ModelViewSet):
    queryset = User_Management.objects.all()
    serializer_class = User_ManagementSerailizer

class DriverManagementViewset(viewsets.ModelViewSet):
    queryset = Drive_Management.objects.all()
    serializer_class = Drive_ManagementSerailizer

class CountryManagementViewset(viewsets.ModelViewSet):
    queryset = Country_Management.objects.all()
    serializer_class = Country_ManagementSerailizer

class StateManagementViewset(viewsets.ModelViewSet):
    queryset = State_Management.objects.all()
    serializer_class = State_ManagementSerailizer

class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerailizer

class CityManagementViewset(viewsets.ModelViewSet):
    queryset = City_Management.objects.all()
    serializer_class = City_ManagementSerailizer

#1
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
#2
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
# def driveList(request):
#     driver=Drive_Management.objects.all()
#     if Drive_Management is None:
#         JsonResponse("No records")
#     else:
#       serializer=Drive_ManagementSerailizer(driver,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def driveDetail(request,pk):
#     driver=Drive_Management.objects.get(id=pk)
#     serializer=Drive_ManagementSerailizer(driver,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def driveCreate(request):
#     serializer=Drive_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def driveUpdate(request,pk):
#     driver=Drive_Management.objects.get(id=pk)
#     serializer=Drive_ManagementSerailizer(instance=driver,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def driveDelete(request,pk):
#     driver=Drive_Management.objects.get(id=pk)
#     driver.delete()
#     return JsonResponse("Deleted")

#4
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

#5
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

#6
# @api_view(['GET'])
# def cityList(request):
#     city=City.objects.all()
#     if city is None:
#         JsonResponse("No records")
#     else:
#       serializer=CitySerailizer(city,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def cityDetail(request,pk):
#     city=City.objects.get(id=pk)
#     serializer=CitySerailizer(city,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def cityCreate(request):
#     serializer=CitySerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def cityUpdate(request,pk):
#     city=City.objects.get(id=pk)
#     serializer=CitySerailizer(instance=city,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def cityDelete(request,pk):
#     city=City.objects.get(id=pk)
#     city.delete()
#     return JsonResponse("Deleted")

#6
# @api_view(['GET'])
# def city1List(request):
#     city=City.objects.all()
#     if city is None:
#         JsonResponse("No records")
#     else:
#       serializer=CitySerailizer(city,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def city1Detail(request,pk):
#     city=City.objects.get(id=pk)
#     serializer=CitySerailizer(city,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def city1Create(request):
#     serializer=City1Serailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def city1Update(request,pk):
#     city=City.objects.get(id=pk)
#     serializer=CitySerailizer(instance=city,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def city1Delete(request,pk):
#     city=City.objects.get(id=pk)
#     city.delete()
#     return JsonResponse("Deleted")

#7
# @api_view(['GET'])
# def city_mList(request):
#     city=City_Management.objects.all()
#     if city is None:
#         JsonResponse("No records")
#     else:
#       serializer=City_ManagementSerailizer(city,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def city_mDetail(request,pk):
#     city=City_Management.objects.get(id=pk)
#     serializer=City_ManagementSerailizer(city,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def city_mCreate(request):
#     serializer=City_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def city_mUpdate(request,pk):
#     city=City_Management.objects.get(id=pk)
#     serializer=City_ManagementSerailizer(instance=city,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def city_mDelete(request,pk):
#     city=City_Management.objects.get(id=pk)
#     city.delete()
#     return JsonResponse("Deleted")
#8
from .models import Refral_Management, Fuel_Management, Fare_Management, Co_partnner_Management, Notification_To_Customer, \
Notification_To_Driver, Transaction_Management
from .serializers import Refral_ManagementSerailizer, Fuel_ManagementSerailizer, Fare_ManagementSerailizer, \
    Co_partnner_ManagementSerailizer, Notification_To_CustomerSerailizer, Notification_To_DriverSerailizer, Transaction_ManagementSerailizer

class RefralManagementViewset(viewsets.ModelViewSet):
    queryset = Refral_Management.objects.all()
    serializer_class = Refral_ManagementSerailizer

class FuelManagementViewset(viewsets.ModelViewSet):
    queryset = Fuel_Management.objects.all()
    serializer_class = Fuel_ManagementSerailizer

class FareManagementViewset(viewsets.ModelViewSet):
    queryset = Fare_Management.objects.all()
    serializer_class = Fare_ManagementSerailizer

class CoPartnerViewset(viewsets.ModelViewSet):
    queryset = Co_partnner_Management.objects.all()
    serializer_class = Co_partnner_ManagementSerailizer

class NotificationToCustomer(viewsets.ModelViewSet):
    queryset = Notification_To_Customer.objects.all()
    serializer_class = Notification_To_CustomerSerailizer

class NotificationToDriverViewset(viewsets.ModelViewSet):
    queryset = Notification_To_Driver.objects.all()
    serializer_class = Notification_To_DriverSerailizer

class TransactionManagementViewset(viewsets.ModelViewSet):
    queryset = Transaction_Management.objects.all()
    serializer_class = Transaction_ManagementSerailizer
# @api_view(['GET'])
# def refralList(request):
#     refral=Refral_Management.objects.all()
#     if refral is None:
#         JsonResponse("No records")
#     else:
#       serializer=Refral_ManagementSerailizer(refral,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def refralDetail(request,pk):
#     refral=Refral_Management.objects.get(id=pk)
#     serializer=Refral_ManagementSerailizer(refral,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def refralCreate(request):
#     serializer=Refral_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def refralUpdate(request,pk):
#     refral=Refral_Management.objects.get(id=pk)
#     serializer=Refral_ManagementSerailizer(instance=refral,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def refralDelete(request,pk):
#     refral=Refral_Management.objects.get(id=pk)
#     refral.delete()
#     return JsonResponse("Deleted")
#
#9
# @api_view(['GET'])
# def fuelList(request):
#     fuel=Fuel_Management.objects.all()
#     if fuel is None:
#         JsonResponse("No records")
#     else:
#       serializer=Fuel_ManagementSerailizer(fuel,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def fuelDetail(request,pk):
#     fuel=Fuel_Management.objects.get(id=pk)
#     serializer=Fuel_ManagementSerailizer(fuel,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def fuelCreate(request):
#     serializer=Fuel_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def fuelUpdate(request,pk):
#     fuel=Fuel_Management.objects.get(id=pk)
#     serializer=Fuel_ManagementSerailizer(instance=fuel,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def fuelDelete(request,pk):
#     fuel=Fuel_Management.objects.get(id=pk)
#     fuel.delete()
#     return JsonResponse("Deleted")
#10
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
#11


# @api_view(['GET'])
# def co_partnerList(request):
#     co_partner=Co_partnner_Management.objects.all()
#     if co_partner is None:
#         JsonResponse("No records")
#     else:
#       serializer=Co_partnner_ManagementSerailizer(co_partner,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def co_partnerDetail(request,pk):
#     co_partner=Co_partnner_Management.objects.get(id=pk)
#     serializer=Co_partnner_ManagementSerailizer(co_partner,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def co_partnerCreate(request):
#     serializer=Co_partnner_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def co_partnerUpdate(request,pk):
#     co_partner=Co_partnner_Management.objects.get(id=pk)
#     serializer=Co_partnner_ManagementSerailizer(instance=co_partner,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def co_partnerDelete(request,pk):
#     co_partner=Co_partnner_Management.objects.get(id=pk)
#     co_partner.delete()
#     return JsonResponse("Deleted")

#12
# @api_view(['GET'])
# def notification_to_customerList(request):
#     notification_to_customer=Notification_To_Customer.objects.all()
#     if notification_to_customer is None:
#         JsonResponse("No records")
#     else:
#       serializer=Notification_To_CustomerSerailizer(notification_to_customer,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def notification_to_customerDetail(request,pk):
#     notification_to_customer=Notification_To_Customer.objects.get(id=pk)
#     serializer=Notification_To_CustomerSerailizer(notification_to_customer,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def notification_to_customerCreate(request):
#     serializer=Notification_To_CustomerSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def notification_to_customerUpdate(request,pk):
#     notification_to_customer=Notification_To_Customer.objects.get(id=pk)
#     serializer=Notification_To_CustomerSerailizer(instance=notification_to_customer,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def notification_to_customerDelete(request,pk):
#     notification_to_customer=Notification_To_Customer.objects.get(id=pk)
#     notification_to_customer.delete()
#     return JsonResponse("Deleted")

#13
# @api_view(['GET'])
# def notification_to_driverList(request):
#     notification_to_driver=Notification_To_Driver.objects.all()
#     if notification_to_driver is None:
#         JsonResponse("No records")
#     else:
#       serializer=Notification_To_DriverSerailizer(notification_to_driver,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def notification_to_driverDetail(request,pk):
#     notification_to_driver=Notification_To_Driver.objects.get(id=pk)
#     serializer=Notification_To_DriverSerailizer(notification_to_driver,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def notification_to_driverCreate(request):
#     serializer=Notification_To_DriverSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def notification_to_driverUpdate(request,pk):
#     notification_to_driver=Notification_To_Driver.objects.get(id=pk)
#     serializer=Notification_To_DriverSerailizer(instance=notification_to_driver,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def notification_to_driverDelete(request,pk):
#     notification_to_driver=Notification_To_Driver.objects.get(id=pk)
#     notification_to_driver.delete()
#     return JsonResponse("Deleted")

#14
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

#15
from .models import List_your_vehicles_Management, SOS, Support, Terms_Condition, Privacy_Policy
from .serializers import List_your_vehicles_ManagementSerailizer, SOSSerailizer, SupportSerailizer, \
    Terms_ConditionSerailizer, Privacy_PolicySerailizer

class ListYourVehiclesViewset(viewsets.ModelViewSet):
    queryset = List_your_vehicles_Management.objects.all()
    serializer_class = List_your_vehicles_ManagementSerailizer

class SOSViewset(viewsets.ModelViewSet):
    queryset = SOS.objects.all()
    serializer_class = SOSSerailizer

class SupportHelpViewset(viewsets.ModelViewSet):
    queryset = Support.objects.all()
    serializer_class = SupportSerailizer

class TermsConditionViewset(viewsets.ModelViewSet):
    queryset = Terms_Condition.objects.all()
    serializer_class = Terms_ConditionSerailizer

class PrivacyPolicyViewset(viewsets.ModelViewSet):
    queryset = Privacy_Policy.objects.all()
    serializer_class = Privacy_PolicySerailizer
# @api_view(['GET'])
# def list_your_vehicleList(request):
#     list_your_vehicle=List_your_vehicles_Management.objects.all()
#     if list_your_vehicle is None:
#         JsonResponse("No records")
#     else:
#       serializer=List_your_vehicles_ManagementSerailizer(list_your_vehicle,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def list_your_vehicleDetail(request,pk):
#     list_your_vehicle=List_your_vehicles_Management.objects.get(id=pk)
#     serializer=List_your_vehicles_ManagementSerailizer(list_your_vehicle,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def list_your_vehicleCreate(request):
#     serializer=List_your_vehicles_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def list_your_vehicleUpdate(request,pk):
#     list_your_vehicle=List_your_vehicles_Management.objects.get(id=pk)
#     serializer=List_your_vehicles_ManagementSerailizer(instance=list_your_vehicle,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def list_your_vehicleDelete(request,pk):
#     list_your_vehicle=List_your_vehicles_Management.objects.get(id=pk)
#     list_your_vehicle.delete()
#     return JsonResponse("Deleted")

#16
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

#17
# @api_view(['GET'])
# def supportList(request):
#     support_help=Support.objects.all()
#     if support_help is None:
#         JsonResponse("No records")
#     else:
#       serializer=SupportSerailizer(support_help,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def supportDetail(request,pk):
#     support_help=Support.objects.get(id=pk)
#     serializer=SupportSerailizer(support_help,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def supportCreate(request):
#     serializer=SupportSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def supportUpdate(request,pk):
#     support_help=Support.objects.get(id=pk)
#     serializer=SupportSerailizer(instance=support_help,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def supportDelete(request,pk):
#     support_help=Support.objects.get(id=pk)
#     support_help.delete()
#     return JsonResponse("Deleted")

#18
# @api_view(['GET'])
# def term_conditionList(request):
#     term_condition=Terms_Condition.objects.all()
#     if term_condition is None:
#         JsonResponse("No records")
#     else:
#       serializer=Terms_Condition(term_condition,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def term_conditionDetail(request,pk):
#     term_condition=Terms_Condition.objects.get(id=pk)
#     serializer=Terms_ConditionSerailizer(term_condition,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def term_conditionCreate(request):
#     serializer=Terms_ConditionSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def term_conditionUpdate(request,pk):
#     term_condition=Terms_Condition.objects.get(id=pk)
#     serializer=Terms_ConditionSerailizer(instance=term_condition,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def term_conditionDelete(request,pk):
#     term_condition=Terms_Condition.objects.get(id=pk)
#     term_condition.delete()
#     return JsonResponse("Deleted")

#19
# @api_view(['GET'])
# def privacy_policyList(request):
#     privacy_policy=Privacy_Policy.objects.all()
#     if privacy_policy is None:
#         JsonResponse("No records")
#     else:
#       serializer=Privacy_PolicySerailizer(privacy_policy,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def privacy_policyDetail(request,pk):
#     privacy_policy=Privacy_Policy.objects.get(id=pk)
#     serializer=Privacy_PolicySerailizer(privacy_policy,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def privacy_policyCreate(request):
#     serializer=Privacy_PolicySerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def privacy_policyUpdate(request,pk):
#     privacy_policy=Privacy_Policy.objects.get(id=pk)
#     serializer=Privacy_PolicySerailizer(instance=privacy_policy,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def privacy_policyDelete(request,pk):
#     privacy_policy=Privacy_Policy.objects.get(id=pk)
#     privacy_policy.delete()
#     return JsonResponse("Deleted")


#20
from .models import RENTAL, OUTSTATATION_Second, OUTSTATATION, DashBoard, Templates_Management, Vehicle_Management, Advertisement_Management, Maintainance_Management, \
    Listing_Management
from .serializers import RENTALSerailizer, OUTSTATATION_SecondSerailizer, OUTSTATATIONSerailizer, DashBoardSerailizer, Templates_ManagementSerailizer, Vehicle_ManagementSerializer, \
    Advertisement_ManagementSerailizer, Maintainance_ManagementSerailizer, Listing_ManagementSerailizer

class RentalViewset(viewsets.ModelViewSet):
    queryset = RENTAL.objects.all()
    serializer_class = RENTALSerailizer
# @api_view(['GET'])
# def rentalList(request):
#     privacy_policy=RENTAL.objects.all()
#     if privacy_policy is None:
#         JsonResponse("No records")
#     else:
#       serializer=RENTALSerailizer(privacy_policy,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def rentalDetail(request,pk):
#     privacy_policy=RENTAL.objects.get(id=pk)
#     serializer=RENTALSerailizer(privacy_policy,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def rentalCreate(request):
#     serializer=RENTALSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def rentalUpdate(request,pk):
#     privacy_policy=RENTAL.objects.get(id=pk)
#     serializer=RENTALSerailizer(instance=privacy_policy,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def rentalDelete(request,pk):
#     privacy_policy=RENTAL.objects.get(id=pk)
#     privacy_policy.delete()
#     return JsonResponse("Deleted")
#

#21

class OutstationSecondViewset(viewsets.ModelViewSet):
    queryset = OUTSTATATION_Second.objects.all()
    serializer_class = OUTSTATATION_SecondSerailizer

# @api_view(['GET'])
# def outstation_sList(request):
#     privacy_policy=OUTSTATATION_Second.objects.all()
#     if privacy_policy is None:
#         JsonResponse("No records")
#     else:
#       serializer=OUTSTATATION_SecondSerailizer(privacy_policy,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def outstation_sDetail(request,pk):
#     privacy_policy=OUTSTATATION_Second.objects.get(id=pk)
#     serializer=OUTSTATATION_SecondSerailizer(privacy_policy,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def outstation_sCreate(request):
#     serializer=OUTSTATATION_SecondSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def outstation_sUpdate(request,pk):
#     privacy_policy=OUTSTATATION_Second.objects.get(id=pk)
#     serializer=OUTSTATATION_SecondSerailizer(instance=privacy_policy,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def outstation_sDelete(request,pk):
#     privacy_policy=OUTSTATATION_Second.objects.get(id=pk)
#     privacy_policy.delete()
#     return JsonResponse("Deleted")


#22
class Outstation(viewsets.ModelViewSet):
    queryset = OUTSTATATION.objects.all()
    serializer_class = OUTSTATATIONSerailizer
# @api_view(['GET'])
# def outstationList(request):
#     privacy_policy=OUTSTATATION.objects.all()
#     if privacy_policy is None:
#         JsonResponse("No records")
#     else:
#       serializer=OUTSTATATIONSerailizer(privacy_policy,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def outstationDetail(request,pk):
#     privacy_policy=OUTSTATATION.objects.get(id=pk)
#     serializer=OUTSTATATIONSerailizer(privacy_policy,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def outstationCreate(request):
#     serializer=OUTSTATATIONSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def outstationUpdate(request,pk):
#     privacy_policy=OUTSTATATION.objects.get(id=pk)
#     serializer=OUTSTATATIONSerailizer(instance=privacy_policy,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def outstationDelete(request,pk):
#     privacy_policy=OUTSTATATION.objects.get(id=pk)
#     privacy_policy.delete()
#     return JsonResponse("Deleted")


#23
class DashboardViewset(viewsets.ModelViewSet):
    queryset = DashBoard.objects.all()
    serializer_class = DashBoardSerailizer

class TemplateManagementViewset(viewsets.ModelViewSet):
    queryset = Templates_Management.objects.all()
    serializer_class = Templates_ManagementSerailizer

class VehicalManagementViewset(viewsets.ModelViewSet):
    queryset = Vehicle_Management.objects.all()
    serializer_class = Vehicle_ManagementSerializer

class ListinManagementViewset(viewsets.ModelViewSet):
    queryset = Listing_Management.objects.all()
    serializer_class = Listing_ManagementSerailizer

class AdvertisementManagementViewset(viewsets.ModelViewSet):
    queryset = Advertisement_Management.objects.all()
    serializer_class = Advertisement_ManagementSerailizer

class MaintainanceManagementViewset(viewsets.ModelViewSet):
    queryset = Maintainance_Management.objects.all()
    serializer_class = Maintainance_ManagementSerailizer

# @api_view(['GET'])
# def dashboardList(request):
#     dashboard=DashBoard.objects.all()
#     if dashboard is None:
#         JsonResponse("No records")
#     else:
#       serializer=DashBoardSerailizer(dashboard,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def dashboardDetail(request,pk):
#     dashboard=DashBoard.objects.get(id=pk)
#     serializer=DashBoardSerailizer(dashboard,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def dashboardCreate(request):
#     serializer=DashBoardSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def dashboardUpdate(request,pk):
#     dashboard=DashBoard.objects.get(id=pk)
#     serializer=DashBoardSerailizer(instance=dashboard,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def dashboardDelete(request,pk):
#     dashboard=DashBoard.objects.get(id=pk)
#     dashboard.delete()
#     return JsonResponse("Deleted")

#24
# @api_view(['GET'])
# def templateList(request):
#     privacy_policy=Templates_Management.objects.all()
#     if privacy_policy is None:
#         JsonResponse("No records")
#     else:
#       serializer=Templates_ManagementSerailizer(privacy_policy,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def templateDetail(request,pk):
#     privacy_policy=Templates_Management.objects.get(id=pk)
#     serializer=Templates_ManagementSerailizer(privacy_policy,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def templateCreate(request):
#     serializer=Templates_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def templateUpdate(request,pk):
#     privacy_policy=Templates_Management.objects.get(id=pk)
#     serializer=Templates_ManagementSerailizer(instance=privacy_policy,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def templateDelete(request,pk):
#     privacy_policy=Templates_Management.objects.get(id=pk)
#     privacy_policy.delete()
#     return JsonResponse("Deleted")

#16

# @api_view(['GET'])
# def vehicleList(request):
#     vehicle=Vehicle_Management.objects.all()
#     if vehicle is None:
#         JsonResponse("No records")
#     else:
#       serializer=Vehicle_ManagementSerializer(vehicle,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def vehicleDetail(request,pk):
#     vehicle=Vehicle_Management.objects.get(id=pk)
#     serializer=Vehicle_ManagementSerializer(vehicle,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def vehicleCreate(request):
#     serializer=Vehicle_ManagementSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def vehicleUpdate(request,pk):
#     vehicle=Vehicle_Management.objects.get(id=pk)
#     serializer=Vehicle_ManagementSerializer(instance=vehicle,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def vehicleDelete(request,pk):
#     vehicle=Vehicle_Management.objects.get(id=pk)
#     vehicle.delete()
#     return JsonResponse("Deleted")
#

#16

# @api_view(['GET'])
# def listingList(request):
#     listing=Listing_Management.objects.all()
#     if listing is None:
#         JsonResponse("No records")
#     else:
#       serializer=Listing_ManagementSerailizer(listing,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def listingDetail(request,pk):
#     listing=Listing_Management.objects.get(id=pk)
#     serializer=Listing_ManagementSerailizer(listing,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def listingCreate(request):
#     serializer=Listing_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def listingUpdate(request,pk):
#     listing=Listing_Management.objects.get(id=pk)
#     serializer=Listing_ManagementSerailizer(instance=listing,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def listingDelete(request,pk):
#     listing=Listing_Management.objects.get(id=pk)
#     listing.delete()
#     return JsonResponse("Deleted")
#
#16

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

#16


# @api_view(['GET'])
# def maintainanceList(request):
#     maintainance=Maintainance_Management.objects.all()
#     if maintainance is None:
#         JsonResponse("No records")
#     else:
#       serializer=Maintainance_ManagementSerailizer(maintainance,many=True)
#     return JsonResponse({'result':serializer.data},safe=False)
# @api_view(['GET'])
# def maintainanceDetail(request,pk):
#     maintainance=Maintainance_Management.objects.get(id=pk)
#     serializer=Maintainance_ManagementSerailizer(maintainance,many=True)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def maintainanceCreate(request):
#     serializer=Maintainance_ManagementSerailizer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['POST'])
# def maintainanceUpdate(request,pk):
#     maintainance=Maintainance_Management.objects.get(id=pk)
#     serializer=Maintainance_ManagementSerailizer(instance=maintainance,data=request.data)
#     return JsonResponse(serializer.data,safe=False)
# @api_view(['DELETE'])
# def maintainanceDelete(request,pk):
#     maintainance=Maintainance_Management.objects.get(id=pk)
#     maintainance.delete()
#     return JsonResponse("Deleted")


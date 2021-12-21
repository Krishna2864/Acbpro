from django.db import models

from django.db import models


class Admin_Management(models.Model):
    s_no=models.IntegerField()
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    name=models.CharField(max_length=80,null=False)
    username=models.CharField(max_length=80,null=False)
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    mobile_no=models.IntegerField()
    option=models.CharField(max_length=80,null=False)
    listview=models.CharField(max_length=80,null=False)
    set_permission=models.BooleanField(default=False)
    set_permission_co_partner=models.BooleanField(default=False)
    set_permission_country=models.BooleanField(default=False)
    set_permission_state=models.BooleanField(default=False)
    set_permission_advertisement=models.BooleanField(default=False)
    set_permission_listing=models.BooleanField(default=False)
    set_permission_templates=models.BooleanField(default=False)
    set_permission_fare=models.BooleanField(default=False)
    set_permission_notification=models.BooleanField(default=False)
    set_permission_notification2=models.BooleanField(default=False)
    set_permission_fuel=models.BooleanField(default=False)
    set_permission_maintainance=models.BooleanField(default=False)
    set_permission_refral=models.BooleanField(default=False)
    set_permission_refund=models.BooleanField(default=False)
    set_permission_trasaction=models.BooleanField(default=False)
    set_permission_feedback=models.BooleanField(default=False)
    set_permission_sos=models.BooleanField(default=False)
    set_permission_support=models.BooleanField(default=False)
    set_permission_other=models.BooleanField(default=False)



class User_Management(models.Model):
    booking_id=models.IntegerField()
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    name=models.CharField(max_length=80,null=False)
    username=models.CharField(max_length=80,null=False)
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    mobile_no=models.IntegerField()
    booking_status=models.CharField(max_length=80,null=False)
    booking_cat=models.CharField(max_length=80,null=False)
    booking_status_1=models.CharField(max_length=80,null=False)
    booking_created=models.DateTimeField(auto_now_add=True)
    pickup_point=models.CharField(max_length=80,null=False)
    drop_p_point=models.CharField(max_length=80,null=False)
    eta_in_min=models.IntegerField()
    et_time_in_min=models.IntegerField()
    etc_inr=models.IntegerField()
    actual_pickup_point=models.CharField(max_length=80,null=False)
    actual_drop_point=models.CharField(max_length=80,null=False)
    etkm_in_km=models.IntegerField()
    pickup_late_log=models.FloatField()
    drop_late_log=models.FloatField()
    doj=models.DateTimeField(auto_now_add=True)
    dod=models.DateTimeField(auto_now_add=True)
    actual_km_run=models.IntegerField()
    vehicle_no=models.CharField(max_length=80,null=False)
    driver_id=models.CharField(max_length=80,null=False)
    driver_name=models.CharField(max_length=80,null=False)
    map_view=models.CharField(max_length=80,null=False)
    sos_or_help=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charge=models.IntegerField()
    gst=models.IntegerField()
    insurance=models.IntegerField()
    extra_km=models.IntegerField()
    waitng_charge=models.IntegerField()
    night_charge=models.IntegerField()
    driver_charge=models.IntegerField()
    discount=models.IntegerField()
    minimum_bill=models.IntegerField()
    final_bill=models.IntegerField()
    invoice=models.ImageField(upload_to="media")
    pay_mode=models.IntegerField()


class Vehicle_Management(models.Model):
    
    vehicle=models.CharField(max_length=50)
    s_no=models.IntegerField()
    vehicle_registration_no=models.CharField(max_length=50)
    manufacturer=models.CharField(max_length=50)
    year_of_manufacturing=models.IntegerField()
    engine_no=models.CharField(max_length=40)
    chassis_no=models.CharField(max_length=40)
    colour=models.CharField(max_length=40)
    seat_capacity=models.IntegerField()
    segment=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    fuel_type=models.CharField(max_length=50)
    varient=models.CharField(max_length=50)
    km_running=models.IntegerField()
    insurance=models.ImageField(upload_to="media")
    rc_card=models.ImageField(upload_to="media")
    fitness=models.ImageField(upload_to="media")
    permit=models.ImageField(upload_to="media")
    puc=models.ImageField(upload_to="media")
    date_of_attachment=models.DateField(auto_now_add=True)
    city=models.CharField(max_length=60)
    status=models.CharField(max_length=60)

'''

class Driver_Management(models.Model):
    driver_id=models.CharField(max_length=80,null=False)
    vehicle_no=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    dl=models.ImageField(upload_to="media")
    selfie=models.ImageField(upload_to="media")
    aadhar=models.ImageField(upload_to="media")
    pan_card=models.ImageField(upload_to="media")
    electric_bill=models.ImageField(upload_to="media")
    role=models.CharField(max_length=80,null=False)
    mobile_no=models.IntegerField()
    dl_expiry_date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=80,null=False)
    shift=models.CharField(max_length=80,null=False)
    police_verfication=models.ImageField(upload_to="media")
    driver_app_login=models.EmailField(max_length=254,unique=True,null=False)
    password=models.CharField(max_length=80,null=False)
    forgot_password=models.CharField(max_length=80,null=False)

'''

class Country_Management(models.Model):
    s_no=models.IntegerField()
    country=models.CharField(max_length=80,null=False)
    start_date=models.CharField(max_length=80,null=False)
    office_address=models.CharField(max_length=80,null=False)
    office_contact_no=models.IntegerField()
    status=models.CharField(max_length=80,null=False) 




class State_Management(models.Model):
    s_no=models.IntegerField(null=True)
    state=models.CharField(max_length=80,null=True)
    start_date=models.DateField(auto_now=True)
    office_address=models.CharField(max_length=200,null=True)
    office_contact_no=models.IntegerField(null=True)
    status=models.CharField(max_length=80,null=True)



class City_Management(models.Model):
    s_no=models.IntegerField(null=True)
    city=models.CharField(max_length=80,null=True)
    start_date=models.DateField(auto_now=True)
    office_address=models.CharField(max_length=200,null=True)
    office_contact_no=models.IntegerField(null=True)
    status=models.CharField(max_length=80,null=True)


class Advertisement_Management(models.Model):
    s_no=models.IntegerField(null=True)
    Promo_code_name=models.CharField(max_length=80,null=True)
    promo_code=models.CharField(max_length=80,null=True)
    vehicle=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    valid_from=models.DateField(auto_now=True)
    valid_upto=models.DateField(auto_now=True)
    status_code=models.CharField(max_length=80,null=True)
    discount_type=models.IntegerField(null=True)
    user_type=models.CharField(max_length=80,null=True)
    discount_value= models.IntegerField(null=True)

class Refral_Managemnt(models.Model):
    refral_content=models.CharField(max_length=80,null=True)
    refral_amount=models.IntegerField(null=True)
    refral_code=models.CharField(max_length=80,null=True)
    expiry_date=models.DateField(auto_now=True)
    start_date=models.DateField(auto_now=True)
    refral_image=models.IntegerField(null=True)
    no_user_used_code=models.IntegerField(null=True)


class Refund_Management(models.Model):
    s_no=models.IntegerField(null=True)
    booking_id=models.CharField(max_length=80,null=True)
    gst_amount=models.IntegerField(null=True)
    gateway_charges_amount=models.IntegerField(null=True)
    amount=models.IntegerField(null=True)
    cancellation_charges=models.IntegerField(null=True)
    booking_amount=models.IntegerField(null=True)
    total_refund_amount=models.IntegerField(null=True)
    date_of_refounded=models.IntegerField(null=True)
    mode=models.CharField(max_length=80,null=True)
    transaction_id=models.IntegerField(null=True)
    status=models.CharField(max_length=80,null=True)


class Fuel_Management(models.Model):
    total_cunsumption_inr=models.IntegerField(null=True)
    diesel_cunsumption=models.IntegerField(null=True)
    petrol_cunsumption=models.IntegerField(null=True)
    cnc_cunsumption=models.IntegerField(null=True)
    cng_cunsumption=models.IntegerField(null=True)
    lpg_cunsumption=models.IntegerField(null=True)
    electri=models.IntegerField(null=True)
# not needes maint////

class Maintenance_Management(models.Model):
    s_no=models.IntegerField(null=True)
    vehicle_no=models.CharField(max_length=80,null=True)
    date_of_services=models.DateField(auto_now=True)
    next_due_date_of_services=models.DateTimeField(auto_now=True)
    ruuning_km=models.IntegerField(null=True)
    status=models.CharField(max_length=80,null=True)
    tyure_replace=models.DateField(auto_now=True)
    spare_per_invoice=models.ImageField(upload_to="media",null=True)
    insurance_claim=models.ImageField(upload_to="media",null=True)


'''
class Route_Management(models.Model):
    s_no=models.IntegerField(null=True)
    state=models.CharField(max_length=80,null=True)
    _from=models.CharField(max_length=80,null=True)
    _to=models.CharField(max_length=80,null=True)
    route=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)

'''
class Fare_Management(models.Model):
    s_no=models.IntegerField(null=True)
    route=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)
    window_fare=models.FloatField(null=True)
    middle_seat_fare=models.FloatField(null=True)
    gst=models.FloatField(null=True)
    insurance=models.FloatField(null=True)
    fare_per_seat_window=models.IntegerField(null=True)
    middle_seat=models.IntegerField(null=True)
    option=models.CharField(max_length=80,null=True)



'''
class Time_Schedule_Management(models.Model):
    s_no=models.IntegerField(null=True)
    route=models.CharField(max_length=80,null=True)
    sdt=models.DateTimeField(auto_now=True)
    sat=models.DateTimeField
    state=models.CharField(max_length=80,null=True)
    _from=models.CharField(max_length=80,null=True)
    _to=models.CharField(max_length=80,null=True)
    frequency=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)

class Pickup_Point(models.Model):
    s_no=models.IntegerField(null=True)
    route=models.CharField(max_length=80,null=True)
    city=models.CharField(max_length=80,null=True)
    pickup=models.CharField(max_length=80,null=True)
    interval_min=models.IntegerField(null=True)
    lat=models.IntegerField(null=True)
    log=models.IntegerField(null=True)
    model=models.CharField(max_length=80,null=True)
    fuel=models.CharField(max_length=80,null=True)

class Drop_Points(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    route_id=models.CharField(max_length=80,null=False)
    time_start=models.DateTimeField(auto_now_add=True)
    vehicle_no=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    vehicle=models.CharField(max_length=80,null=False)
    From=models.CharField(max_length=80,null=False)
    to=models.CharField(max_length=80,null=False)
    drop_point_1=models.CharField(max_length=80,null=False)
    drop_point_2=models.CharField(max_length=80,null=False)
    drop_point_3=models.CharField(max_length=80,null=False)

'''
class Listing_Assign_Management(models.Model):
    country=models.CharField(max_length=80,null=False)
    state=models.CharField(max_length=80,null=False)
    city=models.CharField(max_length=80,null=False)
    fuel_status=models.CharField(max_length=80,null=False)
    trip_type=models.CharField(max_length=80,null=False)
    vehicle_id=models.CharField(max_length=80,null=False)
    segment=models.CharField(max_length=80,null=False)
    model=models.CharField(max_length=80,null=False)
    base_fare=models.IntegerField()
    booking_fee=models.IntegerField()
    commision_fee=models.IntegerField()
    per_min_charge=models.IntegerField()
    per_km_charges=models.IntegerField()
    minimum_bill=models.IntegerField()    
    toll_tax=models.CharField(max_length=80,null=False)    
    seat=models.IntegerField()
    image=models.ImageField(upload_to="media")
    edit_button=models.CharField(max_length=80,null=False)
    listing=models.CharField(max_length=80,null=False)
    
    




class Co_Partner_Management(models.Model):
    s_no=models.IntegerField()
    vehicle_registration_no=models.CharField(max_length=80,null=False)
    selfie=models.ImageField(upload_to="media")
    ower_name=models.CharField(max_length=80,null=False)
    adhar_card=models.ImageField(upload_to="media")
    pan_card=models.ImageField(upload_to="media")
    bank_details=models.ImageField(upload_to="media")
    mobile_no=models.IntegerField()
    email_id=models.EmailField(max_length=254,unique=True,null=False)
    payput_hourly=models.IntegerField()
    payout_daily=models.IntegerField()
    online_total_time_in_hour=models.IntegerField()
    payout=models.CharField(max_length=80,null=False)




class Notification_to_Ridder(models.Model):
    pass


class Notification_to_Driver(models.Model):
    pass

'''
class Consignment_Tracking(models.Model):
    s_no=models.IntegerField(null=True)
    sender_name=models.CharField(max_length=80,null=True)
    sender_no=models.IntegerField(null=True)
    address=models.CharField(max_length=200,null=True)
    email_id=models.EmailField(max_length=254,unique=True)
    weight=models.IntegerField(null=True)
    reciever_name=models.CharField(max_length=80,null=True)
    reciever_no=models.IntegerField(null=True)
    type=models.CharField(max_length=80,null=True)
    route=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)
'''



class Transaction_Management(models.Model):
    s_no=models.IntegerField(null=True)
    booking_id=models.CharField(max_length=80,null=True)
    no_of_passanger=models.IntegerField(null=True)
    date_of_join=models.DateField(auto_now=True)
    booking_created=models.DateField(auto_now=True)
    gst_amount=models.IntegerField(null=True)
    gateway_charges_amount=models.IntegerField(null=True)
    amount=models.IntegerField(null=True)
    discount=models.IntegerField(null=True)
    route=models.CharField(max_length=80,null=True)
    pickup=models.CharField(max_length=80,null=True)
    dropup=models.CharField(max_length=80,null=True)
    window_fare=models.FloatField(null=True)
    middle_seat_fare=models.FloatField(null=True)
    gst=models.IntegerField(null=True)
    insurance=models.IntegerField(null=True)
    fare_per_seat_window=models.IntegerField(null=True)
    middle_seat=models.IntegerField(null=True)
    transaction_id=models.IntegerField(null=True)
    booking_status=models.CharField(max_length=80,null=True)
    invoice=models.ImageField(upload_to="media",null=True)



class List_Your_Vehicle_Management(models.Model):
    vehicle=models.CharField(max_length=80,null=True)
    s_no=models.IntegerField(null=True)
    vehicle_registration_no=models.CharField(max_length=80,null=True)
    manufacturer=models.CharField(max_length=80,null=True)
    year_of_manufacturing=models.IntegerField(null=True)
    engine_no_tracing=models.ImageField(upload_to="media",null=True)
    chassis_no_tracing=models.ImageField(upload_to="media",null=True)
    colour=models.CharField(max_length=80,null=True)
    seat_capa=models.IntegerField(null=True)
    segment=models.CharField(max_length=80,null=True)
    model=models.CharField(max_length=80,null=True)
    fuel_type=models.CharField(max_length=80,null=True)
    varient=models.CharField(max_length=80,null=True)
    km_running=models.IntegerField(null=True)
    insurance=models.ImageField(upload_to="media",null=True)
    rc_card=models.ImageField(upload_to="media",null=True)
    fitness=models.ImageField(upload_to="media",null=True)
    permit=models.ImageField(upload_to="media",null=True)
    puc=models.ImageField(upload_to="media",null=True)
    date_of_inspection=models.DateField(auto_now=True)
    proposed_price_day=models.CharField(max_length=80,null=True)
    proposed_price_night=models.CharField(max_length=80,null=True)
    proposed_date_of_attachment=models.DateField(auto_now=True)
    city=models.CharField(max_length=80,null=True)
    selfie=models.ImageField(upload_to="media",null=True)
    Ower_name=models.CharField(max_length=80,null=True)
    aadhar_card=models.ImageField(upload_to='media',null=True)
    pan_card=models.ImageField(upload_to="media",null=True)
    bank_details=models.ImageField(upload_to="media",null=True)
    mobile_no=models.IntegerField(null=True)
    mail_id=models.EmailField(max_length=254,unique=True)
    payout_hourly=models.IntegerField(null=True)
    payout_daily=models.IntegerField(null=True)


class Feedback(models.Model):
    pass

'''
class Seat_Management(models.Model):
    s_no=models.IntegerField(null=True)
    employee_id=models.CharField(max_length=80,null=True)
    name=models.CharField(max_length=80,null=True)
    customer_name=models.CharField(max_length=80,null=True)
    gender=models.CharField(max_length=80,null=True)
    age=models.CharField(max_length=80,null=True)
    route=models.CharField(max_length=80,null=True)
    time=models.DateTimeField(auto_now=True)
    date=models.DateField(auto_now=True)
    From=models.CharField(max_length=80,null=True)
    to=models.CharField(max_length=80,null=True)
    seat_no=models.CharField(max_length=80,null=True)
    pickup_point=models.CharField(max_length=80,null=True)
    pickup_time=models.CharField(max_length=80,null=True)
    drop_point=models.CharField(max_length=80,null=True)
    drop_time=  models.DateTimeField(auto_now=True)

'''
class SOS(models.Model):
    pass


class Support_Help(models.Model):
    pass


class TERMS_CONDITIONS(models.Model):
    pass


class PRIVACY_POLICY(models.Model):
    pass

##

class Templates_Management(models.Model):
    s_no=models.IntegerField()
    booking_confirmation_sms=models.CharField(max_length=80,null=False)
    for_verification_otp_sms=models.CharField(max_length=80,null=False)
    resetpassword_otp=models.CharField(max_length=80,null=False)
    booking_cancel_sms=models.CharField(max_length=80,null=False)
    email_image=models.ImageField(upload_to="media")



class vehicle_Monitering(models.Model):
    total_vehicle=models.IntegerField()
    running_vehicle=models.IntegerField()
    breakdown_vehicle=models.IntegerField()
    maintaince_vehicle=models.IntegerField()
    vehicle_number=models.IntegerField()
    mobile_no=models.IntegerField()
    email=models.CharField(max_length=100)
    view = models.ImageField(null=True)

    Co_Partner_Access=models.CharField(max_length=80,null=False)
    map_view=models.ImageField(upload_to="media")
    

class Context(models.Model):
    pass
    
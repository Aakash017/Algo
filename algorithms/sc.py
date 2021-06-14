import csv
from dateutil.relativedelta import relativedelta
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.utils.encoding import smart_str

from renewbuy.consumers.models import Payment
from renewbuy.org.models import Employee
from renewbuy.utils import email

to_email = 'abhishek.gupta@renewbuy.com'

file = '/home/aakash/Downloads/abc.csv'
prefix = 'motor_dump_sheet'
pid_list = []
repid_list = []
policy_no_list=[]
temp_file = NamedTemporaryFile(prefix=prefix, suffix='.csv', delete=False)
header = (
    'Policy ID',
    'Payment ID',
    'Policy Date',
    'Policy Type',
    'Partner ID',
    'Policy Tenure',
    'Product Name',
    'Vehicle Variant',
    'City',
    'Branch',
    'Vehicle Vintage',
    'CV Type',
    'Vehicle CC',
    'Vehicle IDV/SI',
    'Total Premium (excl GST)',
    'Total Premium (incl GST)',
    'DOB'
)
writer = csv.DictWriter(
    temp_file,
    fieldnames=header
)

with open(file, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        import ipdb;ipdb.set_trace()
        policy_no = row.get("motor_policy_no")
        policy_no_list.append(policy_no)
    policy_no_list=list(set(policy_no_list))
    for policy_no in policy_no_list:
        payment = Payment.objects.get(policyno=policy_no)
        proposal = payment.premium
        policy_id = payment.policy.policyno
        payment_id = payment.id
        policy_date = payment.policy.policy_issuedate
        policy_type = 'Rollover'
        if proposal.is_new:
            policy_type = 'New'
        elif proposal.is_self_renewal:
            policy_type = 'Renewal'
        try:
            if proposal.executive:
                executive = proposal.executive
                partner_id = executive.code
        except Exception as e:
            partner_id = ""
        policy_tenure = ''
        if proposal.policy_startdate and proposal.policy_enddate:
            policy_startdate = proposal.policy_startdate
            policy_enddate = proposal.policy_enddate
            difference = relativedelta(policy_enddate - policy_startdate)
            days = str(difference.days)
            policy_tenure = days + ' days'
        product_name = payment.policy.policy_insurer + " | " + (
            "Third Party" if proposal.coverage_type else "Comprehensive")
        variant_name = ''
        try:
            variant = proposal.variant
            variant_name = variant.variant_name
        except Exception as e:
            pass
        city = ''
        if proposal.customer and proposal.customer.communication_city:
            city = proposal.customer.communication_city.city_name
        frm = executive.get_field_manager_on_date(payment.payment_date)
        if isinstance(frm, Employee):
            try:
                branch_office = frm.office_branch.office_name
            except Exception as e:
                branch_office = ''
        vehicle_type = ""
        vehicle_cc = variant.cubic_capacity if variant.cubic_capacity else ""
        vehicle_idv = proposal.vehicle_idv if proposal.vehicle_idv else ""
        total_pay_with_gst = payment.payment_amount
        vehicle_purchase_date = proposal.purchase_date.strftime("%d-%m-%Y") if proposal.purchase_date else ''
        try:
            pay_amnt = float(payment.payment_amount)
            service_tax = proposal.servicetax
            total_pay_without_gst = pay_amnt - service_tax
            total_pay_without_gst = round(total_pay_without_gst)
        except ValueError:
            total_pay_without_gst = ''
        dob = proposal.customer.dob

        parsed_dob = dob.encode('utf-8').strip()

        writer.writerow({
            'Policy ID': policy_id,
            'Payment ID': payment_id,
            'Policy Date': policy_date,
            'Policy Type': policy_type,
            'Partner ID': partner_id,
            'Policy Tenure': policy_tenure,
            'Product Name': product_name,
            'Vehicle Variant': variant_name,
            'City': city,
            'Branch': branch_office,
            'Vehicle Vintage': smart_str(vehicle_purchase_date),
            'CV Type': vehicle_type,
            'Vehicle CC': smart_str(vehicle_cc),
            'Vehicle IDV/SI': smart_str(vehicle_idv),
            'Total Premium (excl GST)': smart_str(total_pay_without_gst),
            'Total Premium (incl GST)': smart_str(total_pay_with_gst),
            'DOB': smart_str(parsed_dob)
        })

tempfile = File(temp_file)
subject = "Motor Policy IDS DATA"
text_content = "PFA the Transaction Sheet"
email_status = email.send(to_email, subject, html_body=text_content,
                          text_body=text_content,
                          attachments=[tempfile], from_email='renewbuypartners@renewbuy.com')
if email_status:
    print ("Sheet mail sent to email {} ".format(to_email))
else:
    print (
        "Unable to send email on {} ".format(to_email))
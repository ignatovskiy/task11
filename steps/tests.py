from behave import given, when, then

from pageobjects.tests import OrderPageObject

@given('the home page is open')
def step_impl(context):
    context.current_page = OrderPageObject()
    context.current_page.open()


@when('the user click on last vehicle in vehicle table')
def step_impl(context):
    context.current_page = context.current_page.choose_last_vehicle()


@when('the user click on "Purchase order"')
def step_impl(context):
    context.current_page = context.current_page.purchase_order()


@when('the user click on "Send order"')
def step_imp(context):
    context.current_page = context.current_page.send_order()


@when('the user click on "Contact details"')
def step_imp(context):
    context.current_page = context.current_page.open_contact_details()


@when('enter to Surname "{surname}"')
def step_imp(context, surname):
    context.current_page = context.current_page.enter_surname(surname)


@when('enter to First name "{name}"')
def step_imp(context, name):
    context.current_page = context.current_page.enter_name(name)


@when('enter to Street address "{address}"')
def step_imp(context, address):
    context.current_page = context.current_page.enter_street_address(address)


@when('enter to ZIP code "{zip_code}"')
def step_imp(context, zip_code):
    context.current_page = context.current_page.enter_zip_code(zip_code)


@when('enter to City "{city}"')
def step_imp(context, city):
    context.current_page = context.current_page.enter_city(city)


@when('enter to Country "{country}"')
def step_imp(context, country):
    context.current_page = context.current_page.enter_country(country)


@when('enter to Phone number "{phone_number}"')
def step_imp(context, phone_number):
    context.current_page = context.current_page.enter_phone_number(phone_number)


@when('enter to E-mail address "{e_mail}"')
def step_imp(context, e_mail):
    context.current_page = context.current_page.enter_e_mail(e_mail)


@when('the user click on "Send purchase order"')
def step_imp(context):
    context.current_page = context.current_page.send_purchase_order()


@then('check order is confirmed')
def step_imp(context):
    context.current_page = context.current_page.is_confirmed()

    # todo

@when(u'the user select menu "Options"')
def step_impl(context):
    context.current_page = context.current_page.select_options()

@when(u'the user select option "Vehicles..."')
def step_impl(context):
    context.current_page = context.current_page.select_vehicles()

@when(u'the user input name "{name}" with price: "{price}"')
def step_impl(context, name, price):
    context.current_page = context.current_page.enter_car_info(name, price)

@when(u'the user press Button "Create"')
def step_impl(context):
    context.current_page = context.current_page.click_create()

@then(u'record is added in the list car')
def step_impl(context):
    context.current_page = context.current_page.check_added_car()

@when(u'select the last vehicle if exist and click "Edit"')
def step_impl(context):
    context.current_page = context.current_page.select_and_edit_car()

@when(u'edit to the name "{name}" and to the price "{price}"')
def step_impl(context, name, price):
    context.current_page = context.current_page.enter_new_info(name, price)

@when(u'the user press Button "Ok"')
def step_impl(context):
    context.current_page = context.current_page.click_ok()

@then(u'last record is changed with name "{name}" and price "{price}"')
def step_impl(context, name, price):
    context.current_page = context.current_page.check_edited_car(name, price)

@when(u'the user press Button "Delete"')
def step_impl(context):
    context.current_page = context.current_page.click_delete()

@then(u'the last vehicle is deleted')
def step_impl(context):
    context.current_page = context.current_page.check_deleted_car()
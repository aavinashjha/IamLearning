import pytest
from random import randint

@pytest.fixture
def portal_objects_setup():
    account_name = 'NewAccount' + str(randint(0,9))
    print('In portal objects setup', account_name)
    yield account_name

@pytest.fixture
def billing_setup(request):
    if request.fixturename == 'billing_setup':
        account_name = request.getfuncargvalue('portal_objects_setup')
    else:
        account_name = request.getfuncargvalue('portal_objects_setup_second_account')
    print('In billing setup', account_name)

portal_objects_setup_second_account = portal_objects_setup
billing_setup_second_account = billing_setup

@pytest.mark.usefixtures('billing_setup')
def atest1():
    print('In test 1')

@pytest.mark.usefixtures('billing_setup', 'billing_setup_second_account')
def test2():
    print('In test 2')

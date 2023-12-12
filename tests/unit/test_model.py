from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN an Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, country, status, created_at, transactions, and main_account fields are defined correctly
    """

    name = "Adnan"
    password = "U2FsdGVkk"  # This should be hashed if your application hashes passwords
    balance = 5000
    currency = "€"  # Update this to match the default currency in your model
    country = "test"

    account = Account(name, password, balance, currency, country, "", True)

    assert account.name == name
    assert account.password == password  # Update this to match how passwords are stored in your model
    assert account.account_number is not None
    assert account.balance == balance
    assert account.currency == currency
    assert account.status == "Active"
    assert account.country == country
    assert account.transactions == ""  # Update this if you have specific defaults for transactions
    assert account.main_account is True


def test_account_deactivate():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the _deactivate_ method is defined correctly
    """
    name = "Adnan"
    password = "U2FsdGVkk"  # This should be hashed if your application hashes passwords
    balance = 5000
    currency = "€"  # Update this to match the default currency in your model
    country = "test"

    account = Account(name, password, balance, currency, country, "", True)

    assert account._deactivate_() == "Inactive"
    
def test_account_check():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the _repr_ method is defined correctly
    """
    name = "Adnan"
    password = "U2FsdGVkk"  # This should be hashed if your application hashes passwords
    balance = 5000
    currency = "€"  # Update this to match the default currency in your model
    country = "test"

    account = Account(name, password, balance, currency, country, "", True)
    assert repr(account) == f"<Event '{(account.account_number)}'>"

def test_main_account_flag():
    """
    GIVEN a Account model
    WHEN a new Account is created with the main_account flag
    THEN check the main_account field is set correctly
    """
    name = "Adnan"
    password = "U2FsdGVkk"  # This should be hashed if your application hashes passwords
    balance = 5000
    currency = "€"  # Update this to match the default currency in your model
    country = "test"

    account = Account(name, password, balance, currency, country, "", False)
    assert account.main_account == False

def test_account_balance_update():
    """
    GIVEN a Account model
    WHEN the balance of an Account is updated
    THEN check the balance is updated correctly
    """
    name = "Adnan"
    password = "U2FsdGVkk"  # This should be hashed if your application hashes passwords
    balance = 5000
    currency = "€"  # Update this to match the default currency in your model
    country = "test"

    account = Account(name, password, balance, currency, country, "", True)
    account.balance = 1000
    assert account.balance == 1000

def test_transaction_string_format():
    """
    GIVEN a Account model
    WHEN a new Account is created with a transaction string
    THEN check the transaction string is formatted correctly
    """
    name = "Adnan"
    password = "U2FsdGVkk"  # This should be hashed if your application hashes passwords
    balance = 5000
    currency = "€"  # Update this to match the default currency in your model
    country = "test"

    account = Account(name, password, balance, currency, country, "", True)
    assert account.transactions == ""

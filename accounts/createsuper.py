from .models import AccountManager,Account

AccountManager.create_superuser(
    first_name="Kamran",
    last_name="Ali Khan",
    email="kami90912@gmail.com",
    cnic="12345",
    phone="03000",
    address="House#54-A",
    city="Parachinar",
    country="UAE",
    password="ilove12345",
    is_superuser=True
)
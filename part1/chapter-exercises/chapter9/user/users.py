from user import User
from admin import Admin

luis = Admin('luis', 'balbuena', 19, 
    'male', 'mathematics', 'alive')

newton = User('isaac', 'newton', 84, 
    'male', 'physics and mathematics', 'dead')

darwin = User('charles robert', 'darwin', 73, 
    'male', 'biology and natural history', 'dead')

luis.describe_user()
luis.greet_user()
newton.describe_user()
newton.greet_user()
darwin.describe_user()
darwin.greet_user()
luis.inc_login_attempts()
print(luis.login_attempts)
luis.reset_login_attempts()
print(luis.login_attempts)
luis.privileges.show_priveleges()
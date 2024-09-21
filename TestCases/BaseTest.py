import random
import pytest

@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:
    def generate_email_with_time_stamp(self):
        return "testing"+str(random.randint(1,100))+"@gmail.com"

    def randomMobileNo(self):
        return "5201004"+str(random.randint(100,999))
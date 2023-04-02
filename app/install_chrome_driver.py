import os

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


if not os.path.exists('/tmp/bin'):
    os.makedirs('/tmp/bin')
driver_path = ChromeDriverManager(path='/tmp/bin', chrome_type=ChromeType.CHROMIUM).install()
print(f'driver_path = {driver_path}')
os.environ['CHROMIUM_EXECUTABLE_PATH'] = driver_path

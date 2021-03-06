import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'YOUR_API_KEY')

solver = TwoCaptcha(api_key, defaultTimeout=30, pollingInterval=5)

try:
    result = solver.capy(sitekey='PUZZLE_Cz04hZLjuZRMYC3ee10C32D3uNms5w',
                         url='https://www.mysite.com/captcha/',
                         api_server="https://jp.api.capy.me/",
                         softId=33112)

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))

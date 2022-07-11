import schedule
import time

from check_saime import verify_saime_shitty_page

schedule.every(1).minutes.do(verify_saime_shitty_page)
# schedule.every().hour.do(verify_saime_shitty_page)
# schedule.every().day.at("10:30").do(verify_saime_shitty_page)
# schedule.every().monday.do(verify_saime_shitty_page)
# schedule.every().wednesday.at("13:15").do(verify_saime_shitty_page)
# schedule.every().minute.at(":17").do(verify_saime_shitty_page)

while True:
    schedule.run_pending()
    time.sleep(1)
import os
import sys
import schedule
import logging
from docker import errors
from pyfiglet import Figlet
import time
import container
from smtplib import SMTP, SMTPNotSupportedError, SMTPException
from email.message import EmailMessage
from dotenv import load_dotenv
# environs 8.0.0 for env variables
load_dotenv()

HOST = os.environ.get('HOST')
EMAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.environ.get('EMAIL_RECEIVER')
EMAIL_BCC = os.environ.get('EMAIL_BCC')

DEBUG = os.environ.get('DEBUG')
VERBOSE = os.environ.get('VERBOSE')
CONTAINER_NAME = os.environ.get('CONTAINER_NAME')


log = logging.getLogger('monitor')
log_format = "%(asctime)s %(levelname)s %(name)s | %(message)s"
stream = sys.stderr
container_log_file = f'{CONTAINER_NAME}_logs.txt'

def init_logging():
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG, format=log_format, stream=stream)
    elif VERBOSE:
        logging.basicConfig(level=logging.INFO, format=log_format, stream=stream)
    else:
        logging.basicConfig(level=logging.ERROR, stream=stream)


def main():
    try:
        cont = container.get_container(CONTAINER_NAME)

    except errors.NotFound:
        log.error(f'Container with name {CONTAINER_NAME} is not available')
    else:
        running_state = cont.attrs['State']['Running']
        log.info(
            f"Is {CONTAINER_NAME} in running state? : {running_state}\n")
        
        counter = 0
        while not running_state:
            cont.restart()
            counter = counter + 1
            time.sleep(90)
            cont = container.get_container(CONTAINER_NAME)
            log.info(f"Container restarted {counter} time(s) and its {cont.attrs['State']['Status']} after 90s...")

            if counter == 3:
                break

        if not running_state: 
            if os.path.exists(container_log_file):
                os.remove(container_log_file)

            with open(container_log_file, 'wb+') as f:
                for i in cont.logs(stream=True):
                    f.write(i)

            send_email()
        else:
            log.info(
                f"Container is {cont.attrs['State']['Status']}..Skipping email notification")


def send_email():
    with SMTP(host=HOST, port=587) as smtp:
        try:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)

            contacts = [EMAIL_RECEIVER, EMAIL_BCC]

            _msg = EmailMessage()
            _msg['Subject'] = 'New Monitoring Downtime Alert!'
            _msg['From'] = EMAIL_USERNAME
            _msg['To'] = ','.join(contacts)
            _msg.set_content(
                f'Notice!! \nThere is an issue with the {CONTAINER_NAME} container')

            try:
                with open(container_log_file, 'rb') as f:
                    data = f.read()
                    filename = f.name
            except FileNotFoundError:
                log.debug('Log file is not available or generated yet...')
            else:
                _msg.add_attachment(
                    data, maintype='application', subtype='octet-ostream', filename=filename)

            smtp.send_message(_msg)
            log.info('Email notification sent!!')
        except SMTPException as e:
            log.debug(f'Error: {e}\nUnable to send email.')


figlet = Figlet()
print(figlet.renderText('Docker SDK'))
init_logging()
schedule.every(2).minutes.do(main)

while True:
    schedule.run_pending()
    log.info("running!")
    time.sleep(20)

# -*- coding: utf-8 -*-
# HACKATHON PERSONALIZATION
import os

from django.utils import timezone

HACKATHON_NAME = 'Hack the Burgh'
# What's the name for the application
HACKATHON_APPLICATION_NAME = 'Hack the Burgh registration'
# Hackathon timezone
TIME_ZONE = 'GMT'
# This description will be used on the html and sharing meta tags
HACKATHON_DESCRIPTION = 'The hackathon from beyond the wall will be back from the 16th to 17th of March, in the Informatics Forum.'
# Domain where application is deployed, can be set by env variable
HACKATHON_DOMAIN = os.environ.get('DOMAIN', 'localhost:8000')
# Hackathon contact email: where should all hackers contact you. It will also be used as a sender for all emails
HACKATHON_CONTACT_EMAIL = 'hello@hacktheburgh.com'
# Hackathon logo url, will be used on all emails
HACKATHON_LOGO_URL = 'https://2019.hacktheburgh.com/static/logo-black.png'

HACKATHON_OG_IMAGE = 'https://2019.hacktheburgh.com/static/img/htb-preview.jpg'
# (OPTIONAL) Track visits on your website
HACKATHON_GOOGLE_ANALYTICS = 'UA-90176436-4'
# (OPTIONAL) Hackathon twitter user
HACKATHON_TWITTER_ACCOUNT = 'hacktheburgh'
# (OPTIONAL) Hackathon Facebook page
HACKATHON_FACEBOOK_PAGE = 'compsoc'
# (OPTIONAL) Github Repo for this project (so meta)
HACKATHON_GITHUB_REPO = 'https://github.com/compsoc-edinburgh/hackassistant-registration/'

# (OPTIONAL) Applications deadline
HACKATHON_APP_DEADLINE = timezone.datetime(2019, 3, 17, 17, 30, tzinfo=timezone.pytz.timezone(TIME_ZONE))

# (OPTIONAL) When to arrive at the hackathon
HACKATHON_ARRIVE = 'Registration opens at 9:00 AM and closes at 10:30 AM on Saturday March 16th, ' \
                   'the opening ceremony will be at 11:00 am. If you intend to arrive later, please ' \
                   'let us know so that we can save your spot in the hackathon.'

# (OPTIONAL) When to arrive at the hackathon
HACKATHON_LEAVE = 'Closing ceremony will be held on Sunday March 17th from 2:30 PM to 5:30 PM. ' \
                  'The project demo fair will be held in the afternoon from 1:30 PM to 3:00 PM.'
# (OPTIONAL) Hackathon live page
HACKATHON_LIVE_PAGE = 'https://hacktheburgh.com/live'

# (OPTIONAL) Regex to automatically match organizers emails and set them as organizers when signing up
REGEX_HACKATHON_ORGANIZER_EMAIL = '^.*@hacktheburgh\.com$'

# (OPTIONAL) Sends 500 errors to email whilst in production mode.
HACKATHON_DEV_EMAILS = ['me@qaisjp.com', 'techsec@comp-soc.com']

# Reimbursement configuration
REIMBURSEMENT_ENABLED = True
CURRENCY = '£'
REIMBURSEMENT_EXPIRY_DAYS = 5
REIMBURSEMENT_REQUIREMENTS = 'You have to submit a project and demo it during the event in order to be reimbursed.'
REIMBURSEMENT_DEADLINE = timezone.datetime(2019, 3, 11, 3, 14, tzinfo=timezone.pytz.timezone(TIME_ZONE))

# (OPTIONAL) Max team members. Defaults to 4
TEAMS_ENABLED = True
HACKATHON_MAX_TEAMMATES = 4

# (OPTIONAL) Code of conduct link
CODE_CONDUCT_LINK = "https://mlh.io/code-of-conduct"

# (OPTIONAL) Slack credentials
# Highly recommended to create a separate user account to extract the token from
SLACK = {
    'team': os.environ.get('SL_TEAM', 'test'),
    # Get it here: https://api.slack.com/custom-integrations/legacy-tokens
    'token': os.environ.get('SL_TOKEN', None)
}

# (OPTIONAL) Logged in cookie
# This allows to store an extra cookie in the browser to be shared with other application on the same domain
LOGGED_IN_COOKIE_DOMAIN = '.hacktheburgh.com'
LOGGED_IN_COOKIE_KEY = 'hackassistant_logged_in'

# Hardware configuration
HARDWARE_ENABLED = False
# Hardware request time length (in minutes)
HARDWARE_REQUEST_TIME = 15
# Can Hackers start a request on the hardware lab?
# HACKERS_CAN_REQUEST = False

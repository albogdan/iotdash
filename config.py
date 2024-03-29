import os
from dotenv import load_dotenv
# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Load the environment file
load_dotenv(os.path.join(BASE_DIR, '.flaskenv'))

# Config class to encapsulate the config varaibles
class Config(object):
    #Config variables
    # Statement for enabling the development environment
    DEBUG = True


    # Define the database - we are working with
    # SQLite for this example
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_CONNECT_OPTIONS = {}

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED     = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "secret"

    # Secret key for signing cookies
    SECRET_KEY = "secret"

    # OAuth Keys for Google Login
    #GOOGLE_CLIENT_ID=''
    #GOOGLE_CLIENT_SECRET=''

    # Secret key for Mandrill Email API (note that if the env. variable is not found, it will use the other default value)
    #MANDRILL_APIKEY =  os.environ.get('MANDRILL_APIKEY') or

    # Secret key for Stripe Payment API (note that if the env. variable is not found, it will use the other default value)
    #STRIPE_SECRET_KEY =  os.environ.get('STRIPE_SECRET_KEY') or

    # Publishable key for Stripe Payment API (note that if the env. variable is not found, it will use the other default value)
    #STRIPE_PUBLISHABLE_KEY =  os.environ.get('STRIPE_PUBLISHABLE_KEY') or

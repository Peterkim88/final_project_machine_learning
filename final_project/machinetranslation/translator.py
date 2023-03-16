# import json
""" translator module """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

translator = LanguageTranslatorV3(
    version='2018-05-18',
    authenticator=authenticator
)

translator.set_service_url(url)

def english_to_french(english_text):
    """ en -> fr translator function """
    french_text = ""
    if len(english_text) > 0:
        english_translation = translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        french_text = english_translation.get("translations")[0].get("translation")
    return french_text

def french_to_english(french_text):
    """ fr -> en translator function """
    english_text = ""
    if len(french_text) > 0:
        french_translation = translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        english_text = french_translation.get("translations")[0].get("translation")
    return english_text

from twilio.rest import TwilioRestClient


TWILIO_PHONE_NUMBER = "+1 207 305 9485"

DIAL_NUMBERS = ["+91 81065 18331",]

TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

client = TwilioRestClient("AC74a1d7e43709042d89edf3fa190bc3bb", "87782033c2c17250b2f803865629e93f")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")

if __name__ == "__main__":
	dial_numbers(DIAL_NUMBERS)
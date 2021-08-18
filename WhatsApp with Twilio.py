import os
from twilio.rest import Client

twilio_sid = ''     # get token from tokens.txt
twilio_token = ''   # get token from tokens.txt
client = Client(twilio_sid, twilio_token)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+554792878861'

client.messages.create(body = 'QUE PEDOS PERRO',
                      from_ = from_whatsapp_number,
                      to = to_whatsapp_number)
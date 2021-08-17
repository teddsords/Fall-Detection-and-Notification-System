import os
from twilio.rest import Client

twilio_sid = 'AC3da7fb3f4894ca554fc79697ca586e04'
twilio_token = '804ca695d629ac8b6841d3b7b320fd31'
client = Client(twilio_sid, twilio_token)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+554792878861'

client.messages.create(body = 'QUE PEDOS PERRO',
                      from_ = from_whatsapp_number,
                      to = to_whatsapp_number)
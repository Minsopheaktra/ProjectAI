"""
This call sends an email to one recipient, using a validated sender address
Do not forget to update the sender address used in the sample
"""
from mailjet_rest import Client
import os

api_key = '5a5b237772825f98b8b1beccee6fe4c1'
api_secret = '653de254544bc5e8896fe14f34b736e1'
mailjet = Client(auth=(api_key, api_secret))


def mail():
	data = {
		'FromEmail': 'sousocheat16@kit.edu.kh',
		'FromName': 'KIT',
		'Subject': 'Pool Camera',
		'Text-part': 'Detected person',
		'Html-part': '<h3>Detected person</h3>',
		'Recipients': [
			{
				"Email": "jettcalder@gmail.com"
			}
		]
	}
	mailjet.send.create(data=data)

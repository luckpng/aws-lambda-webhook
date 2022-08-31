from __future__ import print_function

from httplib2 import Http
from json import dumps, loads

def response (message, status_code):
   return {
   
       'statusCode': str(status_code),
       'body': dumps(message),
       'headers': {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
          },
    }
    
def lambda_handler(event, context):
    try:
        print("received event: " + dumps(event, indent=2))

        msg=(loads(event['body'])).get('message')
        
        bot_url = 'https://chat.googleapis.com/v1/spaces/AAAAyHn5rfw/messages?key=' \ 
                'AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=nOg-U2zaq5HZgSBG3PV3IcNw51Au7aTUmtnlvOoq5Q0%3D'
                
        bot_message = {
            'text' : msg.get('text')
        }
        
        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        
        http_obj = Http()
        
        bot_response = http_obj.request(
            uri= bot_url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
            
            )
        
        print(bot_response)
        
        
        
        return response({'message': 'Ok'}, 200)
        
    except Exception as e:
        return response({'message': e.message}, 400)

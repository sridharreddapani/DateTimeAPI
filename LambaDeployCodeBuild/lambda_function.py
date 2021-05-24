import json
import os
from datetime import datetime
def lambda_handler(event, context):
    data = {}
    now = datetime.now().isoformat()
    data['Name'] = os.environ["Name"]
    data['DateTime'] = now
    data['Version'] = "Version 1.0.3a"
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }

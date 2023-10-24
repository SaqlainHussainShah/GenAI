"""In this script I will invoke bedrock apis"""

import boto3
import json

client = boto3.client('bedrock')
bedrock_runtime = boto3.client('bedrock-runtime')

print("List of foundation models")
print(client.list_foundation_models().get('modelSummaries')[0].get('modelName'))

context = """ The more foodstuffs is put in the refrigerator or the more frequent and the longer the doors are opened, the more electric consumption will be, which may eventually lead to malfunction.
1 28. It is better not to place heavy pointed or corrosive objects on the refrigerator.
 29. Open the doors as less as possible during power supply breakdown.
 30. The refrigerator should be placed with good ventilation and at least a 10 cm clearance should be kept Never leave the refrigerator discarded to any child for playing; beat and depress the body of refrigerator to
keep any child from entering the refrigerator prior to discarding. To prevent the danger of any child from
being trapped in the refrigerator.
Follow the instructions of your local regulations when disposing.
Door gasket
Bearing
WARNING
Keep the ventilation openings in the appliance enclosure or the built-in structure clear of obstruction. between the upper, the backside, the left and the right side of the refrigerator with walls or anything.
31. The refrigerator must be plugged into a specific socket for 220-240V and no less than 10A. Do not use any
adapter or extension cord.
When disposing the refrigerator:
Please observe the following items:
Detach or destroy the bearing of the doors of the refrigerator to keep the doors from being tightly closed.
Detach the door gasket to keep the door from being tightly closed."""
q ="What should you do when disposing of the refrigerator?"

body = json.dumps(
    {
        "prompt": f"Human: {context}, \n Answer the below questios using the context above \n Question: {q} \n Assistant:  ",
        "max_tokens_to_sample": 6048,
        "temperature": 0.5,
        "top_k": 250,
        "top_p": 0.5,
        "stop_sequences": []
    }
)


model_id = "anthropic.claude-v2"

accept = "application/json"

content_type = "application/json"

response = bedrock_runtime.invoke_model(
    body = body, modelId = model_id, accept = "*/*", contentType = content_type
)

response_body = json.loads(response.get("body").read())

print("response received : ", response_body)
## the following example use python's request to send restapi requests
from __future__ import print_function
import string
import time
import kfp_server_api
import os
import requests
import kfp
import json
from pprint import pprint
from kfp_server_api.rest import ApiException
from kfp_login import get_istio_auth_session
from kfp_namespace import retrieve_namespaces
import cv2
import numpy as np

host = os.getenv("KUBEFLOW_HOST")
username = os.getenv("KUBEFLOW_USERNAME")
password = os.getenv("KUBEFLOW_PASSWORD")

auth_session = get_istio_auth_session(
        url=host,
        username=username,
        password=password
    )

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer   
configuration = kfp_server_api.Configuration(
    host = os.path.join(host, "pipeline"),
)
configuration.debug = True

namespaces = retrieve_namespaces(host, auth_session)
#print("available namespace: {}".format(namespaces))

model_name = 'model12'
auth = 'authservice_session={}'.format(auth_session['session_cookie'][20:])
host = '{}-predictor-default.kubeflow-user-thu10.ai4edu.thu01.footprint-ai.com'.format(model_name)
predict_url = 'https://ai4edu.thu01.footprint-ai.com/v1/models/{}:predict'.format(model_name)
classnames = ['0','1','2','3','4','5','6','7','8','9']
orig = cv2.imread('5.png')
resized = cv2.resize(orig, (28,28), interpolation = cv2.INTER_AREA)
resized_arr = np.asarray(resized)/255.0
headers = {'Host': host, 'Cookie': auth}
#print(headers)
payload={"signature_name": "serving_default", "instances": [resized_arr.tolist()]}
resp = requests.post(predict_url, headers=headers, data=json.dumps(payload))
resp_json = json.loads(resp.content)
for p in resp_json['predictions']:
    print('prediction:', classnames[np.argmax(p)])
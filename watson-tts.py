import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'audio/wav',
}

data = '{"text":"hello world"}'

response = requests.post('https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize', headers=headers, data=data, auth=('d3e73517-2d22-4bf7-959e-a43ce99e3806', 'wN3r0ENe2Cc6'))

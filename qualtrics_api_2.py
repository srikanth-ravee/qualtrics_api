import requests
import zipfile
import json
import io

# Setting user Parameters
apiToken = "PF9V9IOkJUMJyHVXp26q0AwoJ5BAUZOIYo2if9eU" #This token is associated with Will Murphy's account
surveyId = "SV_cuKmgCZc7wcl43j" #Each Survey has a Quatrics ID. Insert the ID for the survey you want to download
useLabels = True #This argument specifices whether responses are text or numeric values. Set True for text or False for numeric
fileFormat = "csv"
dataCenter = 'ca1'

# Setting static parameters
requestCheckProgress = 0
progressStatus = "in progress"
baseUrl = "https://{0}.qualtrics.com/API/v3/responseexports/".format(dataCenter)
headers = {
    "content-type": "application/json",
    "x-api-token": apiToken,
    }

# Step 1: Creating Data Export
downloadRequestUrl = baseUrl
dictionaryPayload = {'format': fileFormat, 'surveyId': surveyId, 'useLabels': useLabels}
downloadRequestPayload = json.dumps(dictionaryPayload)

#downloadRequestPayload = '{"format":"' + fileFormat + '","surveyId":"' + surveyId + '","useLabels":"' + useLabels + '"}'
downloadRequestResponse = requests.request("POST", downloadRequestUrl, data=downloadRequestPayload, headers=headers)
progressId = downloadRequestResponse.json()["result"]["id"]
print(downloadRequestResponse.text)

#
# Step 2: Checking on Data Export Progress and waiting until export is ready
while requestCheckProgress < 100 and progressStatus is not "complete":
    requestCheckUrl = baseUrl + progressId
    requestCheckResponse = requests.request("GET", requestCheckUrl, headers=headers)
    requestCheckProgress = requestCheckResponse.json()["result"]["percentComplete"]
    print("Download is " + str(requestCheckProgress) + " complete")


# Step 3: Downloading file
requestDownloadUrl = baseUrl + progressId + '/file'
requestDownload = requests.request("GET", requestDownloadUrl, headers=headers, stream=True)

# Step 4: Unzipping the file
zipfile.ZipFile(io.BytesIO(requestDownload.content)).extractall("MyQualtricsDownload")
print('Complete')


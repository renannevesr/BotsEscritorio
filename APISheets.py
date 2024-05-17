import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "10HaGcxcqh9gfCxgmV9zB4nT1SAT-PXi0W_jfLVBPTck"
SAMPLE_RANGE_NAME = "Prec!A1:Z12110"


# def main():
#   creds = None
#   if os.path.exists("token.json"):
#     creds = Credentials.from_authorized_user_file("token.json", SCOPES)

#   if not creds or not creds.valid:
#     if creds and creds.expired and creds.refresh_token:
#       creds.refresh(Request())
#     else:
#       flow = InstalledAppFlow.from_client_secrets_file(
#           "credentials.json", SCOPES
#       )
#       creds = flow.run_local_server(port=0)
#     with open("token.json", "w") as token:
#       token.write(creds.to_json())
#     service = build("sheets", "v4", credentials=creds)
   
def read():
  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
      token.write(creds.to_json())
      
  service = build("sheets", "v4", credentials=creds)
  sheet = service.spreadsheets()
  result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
  values = result.get("values", [])
  last_prec = values[-1][0]
  return last_prec

def write(info_prec):
  
  creds = None
  if os.path.exists("token.json"):
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
      with open("token.json", "w") as token:
        token.write(creds.to_json())
  service = build("sheets", "v4", credentials=creds)
  sheet = service.spreadsheets()
  result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
  values = result.get('values', [])
  tamanho = len(values)+1

    # adicionar/editar valores no Google Sheets
  precatorio_value = info_prec.get('PRECATÓRIO', '') 
  proc_origin_value = info_prec.get('PROC. ORIGINÁRIO Nº', '') 
  tribunal_value = info_prec.get('TRIBUNAL', '') 
  reqte_value = info_prec.get('REQTE', '')  
  reqte_adv_value = info_prec.get('ADV', '') 
  autuado_value = info_prec.get('AUTUADO EM', '')  


  data_to_write = [[precatorio_value, proc_origin_value,tribunal_value, reqte_value, reqte_adv_value , autuado_value]]
  sheet.values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range=f'Prec!A{tamanho}',
        valueInputOption='RAW',
        body={'values': data_to_write}
    ).execute()

if __name__ == "__main__":
  print(read())
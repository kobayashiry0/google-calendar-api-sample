import datetime
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# スコープを変更する場合は、token.jsonファイルを削除すること
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def get_credentials():
    """
    Google Calendar APIの認証情報を取得
    """
    creds = None
    tokenpath = "token.json"
    if os.path.exists(tokenpath):
        creds = Credentials.from_authorized_user_file(tokenpath, SCOPES)
    
    # 認証情報がない、または無効な場合はログイン
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # 次回以降のために認証情報を保存
        with open(tokenpath, "w") as token:
            token.write(creds.to_json())
    return creds

def list_calendars(service) -> None:
    """
    カレンダー一覧を取得して表示
    """
    calendar_list = service.calendarList().list().execute()
    for cal in calendar_list['items']:
        print(cal['summary'], cal['id'])


def get_events(service, calendarId):
  """
  ユーザーのカレンダーの次の5件のイベントの開始時刻と名前を表示します。
  """
  try:

    # カレンダーAPIを呼び出す
    now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()

    events_result = (service.events().list(calendarId=calendarId, timeMin=now, maxResults=5, singleEvents=True, orderBy="startTime").execute())
    events = events_result.get("items", [])

    if not events:
      print("イベントが見つかりませんでした。")
      return

    for event in events:
      print("イベント名:", event["summary"])
      print("説明:", event.get("description", "（未設定）"))
      print("開始:", event["start"].get("dateTime", event["start"].get("date")))
      print("終了:", event["end"].get("dateTime", event["end"].get("date")))
      print("場所:", event.get("location", "（未設定）"))
      print("-----")

  except HttpError as error:
    print(f"An error occurred: {error}")


def main():
  creds = get_credentials()
  service = build("calendar", "v3", credentials=creds)
  list_calendars(service)

  # カレンダーIDを指定してイベントを取得
  calendarId = "<カレンダーID>"
  get_events(service, calendarId)

if __name__ == "__main__":
  main()
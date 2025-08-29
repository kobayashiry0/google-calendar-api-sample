# Google Calendar API Sample

これはGoogle Calendar APIを使用したサンプルです。
このサンプルでは、Google Calendarからイベントを取得し、表示する方法を示します。
使用言語はPythonです。

## How to Use
```
git clone https://github.com/kobayashiry0/google-calendar-api-sample.git
```

1. Google Cloud Consoleでプロジェクトを作成し、Google Calendar APIを有効にします。
2. サービスアカウントを作成し、JSONキーをダウンロードします。
3. JSONキーをcredentials.jsonという名前でsample.pyと同じディレクトリに配置します。
4. 必要なライブラリをインストールします。
   ```
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```
5. サンプルコードを実行します。

```bash
python3 quickstart.py
```
>[!Warning]
>カレンダーIDを指定する必要があります。カレンダーIDは、Google Calendarの設定から取得できます。

## Reference
- [Google Calendar API Overview](https://developers.google.com/workspace/calendar/api/guides/overview?hl=ja)
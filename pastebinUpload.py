import requests
import argparse


def reading_text(input_file):
    with open(input_file, 'r') as text_file:
        data = text_file.read()
    return data


def parse_argv():
    parser = argparse.ArgumentParser(description="Upload file to pastebin")
    parser.add_argument("input_file", type=str,
                        help="file to upload")
    parser.add_argument("paste_format", type=str, nargs='?',
                        help="format of input text file to syntax highlights. default = python",
                        default="python")
    parser.add_argument("user_name", type=str, nargs='?',
                        help="user name", default="Lex98")
    parser.add_argument("password", type=str, nargs='?',
                        help="password", default="46884688")
    parser.add_argument("paste_name", type=str, nargs='?',
                        help="name or title of your paste", default="")
    parser.add_argument("paste_private", type=int, nargs='?',
                        help="private of data. 0 = public 1 = unlisted 2 = private",
                        default="0")
    parser.add_argument("paste_expire_date", type=str, nargs='?',
                        help="expire date. N=Never, 10M=10 Minutes, 1H=1 Hour, 1D=1 Day, 1W=1 Week, 2W=2 Weeks, 1M=1 Month",
                        default="1D")
    args = parser.parse_args()
    return args


def upload_to_pastebin(input_text, data_format,
                       user_name, password,
                       paste_name, private,
                       expire_date):
    url = "http://pastebin.com/api/api_post.php"
    login_url = "http://pastebin.com/api/api_login.php"
    dev_key = ""
    login_payload = {"api_dev_key": dev_key,
                     "api_user_name": user_name,
                     "api_user_password": password
                     }
    login_request = requests.post(login_url, login_payload)
    user_key = login_request.text
    payload = {"api_option": "paste",
               "api_user_key": user_key,
               "api_paste_private": private,
               "api_paste_name": paste_name,
               "api_paste_expire_date": expire_date,
               "api_paste_format": data_format,
               "api_dev_key": dev_key,
               "api_paste_code": input_text,
               }
    request = requests.post(url, payload)
    print request.text


def main():
    args = parse_argv()
    input_text = reading_text(args.input_file)
    upload_to_pastebin(input_text, args.paste_format, args.user_name,
                       args.password, args.paste_name, args.paste_private,
                       args.paste_expire_date)


if __name__ == "__main__":
    main()

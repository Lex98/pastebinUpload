import requests
import argparse


def reading_text(input_file):
    """return input file as a string"""
    with open(input_file, 'r') as text_file:
        data = text_file.read()
    return data


def parse_argv():
    """return comand line arguments"""
    parser = argparse.ArgumentParser(description="Upload file to pastebin")
    parser.add_argument("input_file", type=str,
                        help="file to upload")
    parser.add_argument("-f", "--format", type=str, nargs='?',
                        help="format of input text file to syntax highlights. default = python",
                        default="python")
    parser.add_argument("-u", "--user_name", type=str, nargs='?',
                        help="user name", default="")
    parser.add_argument("-p", "--password", type=str, nargs='?',
                        help="password", default="")
    parser.add_argument("-n", "--name", type=str, nargs='?',
                        help="name or title of your paste", default="")
    parser.add_argument("-pr", "--private", type=int, nargs='?',
                        help="private of data. 0 = public 1 = unlisted 2 = private",
                        default="0")
    parser.add_argument("-ed", "--expire_date", type=str, nargs='?',
                        help="expire date. N=Never, 10M=10 Minutes, 1H=1 Hour, 1D=1 Day, 1W=1 Week, 2W=2 Weeks, 1M=1 Month",
                        default="1D")
    args = parser.parse_args()
    return args


def upload_to_pastebin(input_text, data_format,
                       user_name, password,
                       paste_name, private,
                       expire_date):
    """Upload text to pastebin

    Keyword arguments:
    input_text - text to upload
    data_format - format of input text file to syntax highlights. see it on http://pastebin.com/api
    user_name - username
    password - user password
    paste_name -  name or title of your paste on pastebin
    private - private of data. 0 = public 1 = unlisted 2 = private
    expire_date - expire date. N=Never, 10M=10 Minutes, 1H=1 Hour, 1D=1 Day, 1W=1 Week, 2W=2 Weeks, 1M=1 Month

    print server responce
    """
    url = "http://pastebin.com/api/api_post.php"
    login_url = "http://pastebin.com/api/api_login.php"
    dev_key = ""    #enter your dev_key 

    if user_name != '' and password != '':  # generating user key
        login_payload = {"api_dev_key": dev_key,
                         "api_user_name": user_name,
                         "api_user_password": password
                         }
        login_request = requests.post(login_url, login_payload)
        user_key = login_request.text
    else:
        user_key = ""

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
    """main function"""
    args = parse_argv()
    input_text = reading_text(args.input_file)
    upload_to_pastebin(input_text, args.format, args.user_name,
                       args.password, args.name, args.private,
                       args.expire_date)


if __name__ == "__main__":
    main()

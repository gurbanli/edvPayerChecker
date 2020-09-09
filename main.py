import argparse
import requests


def main():
    parser = argparse.ArgumentParser(description='ƏDV ÖDƏYİCİSİNİN AXTARIŞI')
    parser.add_argument('--voen', help='Vergi ödəyicisinin eyniləşdirmə nömrəsi')
    args = parser.parse_args()
    if args.voen is None:
        parser.print_help()
    else:
        send_request(args.voen)


def send_request(voen):
    response_answers = {
        0: 'Belə ödəyici mövcud deyildir',
        -1: 'Bu ödəyici ƏDV qeydiyyatında deyildir'
    }
    print(f"VOEN {voen} üçün sorğu göndərilir...", end='\n\n')
    url = 'https://www.e-taxes.gov.az/ebyn/edvPayerChecker.jsp'
    post_data = {
        'name': voen,
        'sub_mit': 1
    }
    response = requests.post(url, data=post_data)
    response_content = response.text
    if response_answers[0] in response_content:
        print('Incorrect VOEN')
    elif response_answers[-1] in response_content:
        print('VOEN is not registered for VAT')
    else:
        print('VOEN is registered')


main()

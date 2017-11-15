from unittest import (
    main,
    TestCase
)
from unittest.mock import (
    MagicMock,
    patch
)

import requests


class Wheel:
    def __init__(self, number):
        self.number = number
        self.status_file_name = 'status.txt'
        with open(self.status_file_name, 'w') as f:
            f.write('doing nothing..')

    def spin(self):
        with open(self.status_file_name, 'w') as f:
            f.write('spinning..')

    def freeze(self):
        with open(self.status_file_name, 'w') as f:
            f.write('stoned.')

    @property
    def status(self):
        with open(self.status_file_name, 'r') as f:
            status = f.read()
        return status


class Auto:
    def __init__(self, cls):
        self.msg = 'Wheel {} is {}'
        self.wheels = [cls(i) for i in range(4)]

    def print_wheels_status(self):
        for w in self.wheels:
            print(self.msg.format(w.number, w.status))

    def get_wheels_status(self):
        status = ''
        for w in self.wheels:
            status += '\n' + self.msg.format(w.number, w.status)
        return status[1:]

    def drive(self):
        for w in self.wheels:
            w.spin()
        return self.get_wheels_status()

    def stop(self):
        for w in self.wheels:
            w.freeze()
        return self.get_wheels_status()


def mock_wheel(cls):
    def mock_status():
        return 'doing nothing..'

    def mock_spin(self):
        self.status = 'spinning..'

    def mock_freeze(self):
        self.status = 'stoned.'

    cls.status = mock_status()
    cls.spin = mock_spin
    cls.freeze = mock_freeze
    return cls


class TestAuto(TestCase):
    def test_initial(self):
        a = Auto(Wheel)
        mocked_wheel = mock_wheel(Wheel)
        a1 = Auto(mocked_wheel)

        self.assertEqual(a.get_wheels_status(), a1.get_wheels_status())
        self.assertEqual(a1.get_wheels_status(), 'Wheel 0 is doing nothing..\n'
                         + 'Wheel 1 is doing nothing..\n'
                         + 'Wheel 2 is doing nothing..\n'
                         + 'Wheel 3 is doing nothing..')

    def test_drive(self):
        a = Auto(Wheel)
        mocked_wheel = mock_wheel(Wheel)
        a1 = Auto(mocked_wheel)

        self.assertEqual(a.drive(), a1.drive())
        self.assertEqual(a1.drive(), 'Wheel 0 is spinning..\n'
                         + 'Wheel 1 is spinning..\n'
                         + 'Wheel 2 is spinning..\n'
                         + 'Wheel 3 is spinning..')

    def test_stop(self):
        a = Auto(Wheel)
        mocked_wheel = mock_wheel(Wheel)
        a1 = Auto(mocked_wheel)

        self.assertEqual(a.stop(), a1.stop())
        self.assertEqual(a1.stop(), 'Wheel 0 is stoned.\n'
                         + 'Wheel 1 is stoned.\n'
                         + 'Wheel 2 is stoned.\n'
                         + 'Wheel 3 is stoned.')

    def test_all(self):
        a = Auto(Wheel)
        mocked_wheel = mock_wheel(Wheel)
        a1 = Auto(mocked_wheel)
        self.assertEqual(a.get_wheels_status() + a.drive() + a.stop(),
                         a1.get_wheels_status() + a1.drive() + a1.stop(),)


# another example
class RequestMaker:
    def __init__(self, user_agent=None, proxy=None):
        self.user_agent = user_agent
        self.proxy = proxy

    def request_get(self, url):
        r = requests.get(url,
                         headers=self.user_agent,
                         proxies=self.proxy)
        return r.text


class HtmlParse:
    def __init__(self, html_page):
        self.html_page = html_page

    def set_html_page(self, html_page):
        self.html_page = html_page

    def parse_price(self):
        start_pos = self.html_page.find('div.price_block')
        value = self.html_page[start_pos:start_pos + 5]
        return int(value.text)


class DataSaver:
    @staticmethod
    def save_value(file_name, value):
        with open(file_name, 'w') as f:
            f.write(value)


class ParseSystem:
    def __init__(self, request, parser, saver):
        self.request = request
        self.parser = parser
        self.saver = saver

    def parse(self, url, file_name):
        response = self.request.request_get(url)
        self.parser.set_html_page(response)
        value = self.parser.parse_price()
        self.saver.save_value(file_name, value)


class ParseSystemTestBehavior(TestCase):
    @patch.object(RequestMaker, 'request_get', return_value='<html></html>')
    def test_request(self, request_mock):
        self.assertIsNotNone(request_mock('url'))

    @patch.object(HtmlParse, 'set_html_page', return_value=None)
    def test_html_page_setter(self, set_html_page_mock):
        self.assertIsNone(set_html_page_mock('<html></html>'))

    @patch.object(HtmlParse, 'parse_price', return_value=320)
    def test_price_parsing(self, parse_price_mock):
        self.assertGreater(parse_price_mock(), 50)

    @patch.object(DataSaver, 'save_value', return_value=None)
    def test_data_saving(self, save_value_mock):
        self.assertIsNone(save_value_mock())


class RequestMakerMock(TestCase):
    @patch('mock_tests.RequestMaker')
    def test_parsing(self, request_mock):
        request_instance = MagicMock()
        request_instance.request_get.return_value = '<html></html>'
        request_mock.return_value = request_instance

        self.assertIsNotNone(request_mock.request_get('url'))


if __name__ == '__main__':
    main()

import unittest


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


class TestAuto(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()

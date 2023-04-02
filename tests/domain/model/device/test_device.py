from domain.model.device import Device


class TestDevice:
    class Test_value_ofメソッドについて:
        def test_文字列のデバイス指定でDeviceを取得できる(self):
            assert Device.value_of('SP') == Device.SP
            assert Device.value_of('PC') == Device.PC

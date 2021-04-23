import pytest

#@pytest.fixture(autouse="true")
@pytest.fixture(params=["参数1","参数2"])
def myfixture():
    print("执行myfixt re,带参数%s"%request.param)
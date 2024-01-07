from pytest import fixture

def pytest_addoption(parser):
    parser.addoption(
        "--input_filename",
        action="store"
    ),
    parser.addoption(
        "--input_file_1",
        action="store"
    ),
    parser.addoption(
        "--input_file_2",
        action="store"
    ),

@fixture()
def input_filename(request):
    return request.config.getoption("--input_filename")

@fixture()
def input_file_1(request):
    return request.config.getoption("--input_file_1")

@fixture()
def input_file_2(request):
    return request.config.getoption("--input_file_2")





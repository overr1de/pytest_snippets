import os
import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='session', autouse=True)
def prepare_clean_list():
    try:
        os.remove('skip_list.txt')
    except OSError:
        pass


@pytest.fixture(scope='function')
def skip_list(request):
    try:
        with open('skip_list.txt') as fd:
            failed_tests = fd.readlines()
    except FileNotFoundError:
        failed_tests = []

    yield failed_tests
    if request.node.rep_call.failed:
        with open('skip_list.txt', mode='a') as fd:
            fd.writelines(str(request.node.name).split('[')[0])

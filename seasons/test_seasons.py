import pytest
import mock
import builtins
from seasons import get_bday, minutestowords

def test_bday1():
    with mock.patch.object(builtins, 'input', lambda _: '1981-06-07'):
        assert get_bday() == ('1981','06','07')

def test_bday2():
    with mock.patch.object(builtins, 'input', lambda _: '2002-09-08'):
        assert get_bday() == ('2002','09','08')

# def test_raiseerror1():
#     with mock.patch.object(builtins, 'input', lambda _: '09-10-2022'):
#         with pytest.raises(SystemExit):
#             get_bday()


# def test_raiseerror2():
#     with mock.patch.object(builtins, 'input', lambda _: 'dog'):
#         with pytest.raises(SystemExit):
#             get_bday()

# def test_raiseerror3():
#     with mock.patch.object(builtins, 'input', lambda _: '2022-15-15'):
#         with pytest.raises(ValueError):
#             get_bday()


# get_bday()
# captured = capsys.readouterr()
# assert captured.out == "Invalid date"

def test_minutestowords():
    assert minutestowords('555') == 'Five hundred fifty-five minutes'
import os
import pytest

import myqiwi

token = os.environ.get("QIWI_TOKEN")
blocked_token = os.environ.get("BLOCKED_TOKEN")

if token:
    qiwi = myqiwi.Wallet(token)
else:
    qiwi = None

if blocked_token:
    blocked_qiwi = myqiwi.Wallet(blocked_token)
else:
    blocked_qiwi = None


@pytest.mark.skipif(qiwi is None, reason="")
def test_get_phone():
    phone = qiwi.number

    assert isinstance(phone, int)


@pytest.mark.skipif(qiwi is None, reason="")
def test_balance():
    balance = qiwi.balance()

    assert 0 <= balance
    assert isinstance(balance, float)


@pytest.mark.skipif(qiwi is None, reason="")
def test_profile():
    profile = qiwi.profile()

    assert isinstance(profile, dict)


@pytest.mark.skipif(qiwi is None, reason="")
def test_username():
    username = qiwi.username
    assert isinstance(username, str) or username is None


@pytest.mark.skipif(qiwi is None, reason="")
def test_history():
    assert isinstance(qiwi.history(), list)


@pytest.mark.skipif(blocked_qiwi is None, reason="")
def test_check_restriction_out_payment_on_blocked_wallet():
    assert blocked_qiwi.check_restriction_out_payment() is True


@pytest.mark.skipif(qiwi is None, reason="")
def test_check_restriction_out_payment_on_un_blocked_wallet():
    assert isinstance(qiwi.check_restriction_out_payment(), list)

from invoices.export import export_label, read_attachment
from invoices.session import load_session, save_session
from invoices.store import connect, invoices_for, total


def test_invoices_for_customer():
    assert invoices_for(connect(), "acme") == [(1, "acme", 1200)]


def test_unknown_customer_has_no_invoices():
    assert invoices_for(connect(), "nobody") == []


def test_total():
    assert total(connect()) == 1859


def test_export_label():
    assert export_label(42) == "INVOICE-42"


def test_read_attachment(tmp_path):
    (tmp_path / "receipt.txt").write_text("paid", encoding="utf-8")
    assert read_attachment(str(tmp_path), "receipt.txt") == "paid"


def test_session_round_trip():
    assert load_session(save_session({"invoice": 7})) == {"invoice": 7}

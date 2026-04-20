from app.pii import scrub_text


# Owner: Dang Tung Anh
def test_scrub_email() -> None:
    out = scrub_text("Email me at student@vinuni.edu.vn")
    assert "student@" not in out
    assert "REDACTED_EMAIL" in out

def test_scrub_phone() -> None:
    out = scrub_text("My phone is 090 123 4567, call me!")
    assert "090" not in out
    assert "REDACTED_PHONE_VN" in out

def test_scrub_cccd() -> None:
    out = scrub_text("ID number: 001099123456 issued today.")
    assert "001099123456" not in out
    assert "REDACTED_CCCD" in out

def test_scrub_credit_card() -> None:
    out = scrub_text("My card is 4111 1111 1111 1111 right here.")
    assert "4111 1111" not in out
    assert "REDACTED_CREDIT_CARD" in out

def test_scrub_passport() -> None:
    out = scrub_text("Passport C1234567 is valid.")
    assert "C1234567" not in out
    assert "REDACTED_PASSPORT" in out

def test_scrub_address_vn() -> None:
    out = scrub_text("Tôi ở số nhà 12, đường Trần Phú, phường ABC")
    assert "Trần Phú" not in out
    assert "REDACTED_ADDRESS_VN" in out

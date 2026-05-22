def test_customer_belongs_to_correct_tenant():
    db = DBClient()

    record = db.get_customer_by_id("123")

    assert record[2] == "tenant-a"
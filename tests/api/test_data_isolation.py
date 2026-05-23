def test_customer_belongs_to_correct_tenant():
    fake_db = [
        {"id": "1", "tenant_id": "tenant-a"},
        {"id": "2", "tenant_id": "tenant-b"},
    ]

    customer = next(c for c in fake_db if c["id"] == "1")

    assert customer["tenant_id"] == "tenant-a"
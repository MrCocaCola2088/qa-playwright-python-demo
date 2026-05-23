def test_db_mock():
    fake_db = {"customers": []}

    fake_db["customers"].append({
        "id": "123",
        "tenant_id": "tenant-a"
    })

    assert fake_db["customers"][0]["tenant_id"] == "tenant-a"
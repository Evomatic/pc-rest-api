from app import findAll


def test_find():
    """Should FIND all data"""
    # response = findAll()
    assert findAll().get("code")==200

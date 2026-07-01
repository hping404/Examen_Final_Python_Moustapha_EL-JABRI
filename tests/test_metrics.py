from api.metrics import get_system_metrics


def test_metrics_structure():
    data = get_system_metrics()

    assert "cpu_percent" in data
    assert "memory_percent" in data
    assert "disk_percent" in data

    for k in data:
        assert 0 <= data[k] <= 100

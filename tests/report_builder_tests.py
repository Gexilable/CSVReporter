from app.report_builder import ReportBuilder


def test_report_builder_returns_correct_sorted_report():
    test_data = [
        {'name': 'test1', 'age': "10"},
        {'name': 'test2', 'age': "13"},
        {'name': 'test3', 'age': "45.7"},
        {'name': 'test4', 'age': "11"},
    ]
    sorting_parameter = lambda row: float(row["age"])

    report_builder = ReportBuilder(data=test_data, sorting_parameter=sorting_parameter)
    result = report_builder.build()
    assert result[0] == {"name": "test3", "age": "45.7"}
    assert result[1] == {"name": "test2", "age": "13"}
    assert result[2] == {"name": "test4", "age": "11"}
    assert result[3] == {"name": "test1", "age": "10"}

def call_with_inputs(obj, methods, values, expecteds):
    skip_check = False
    if expecteds is None:
        expecteds = [None] * len(methods)
        skip_check = True

    assert len(methods) == len(values) == len(expecteds)
    for method, value, expected in zip(methods, values, expecteds):
        actual = getattr(obj, method)(*value)
        if not skip_check:
            assert expected == actual, f"{method}(*{value}) == {actual} != {expected}"

def test_solution():
    from solution import Vector3D

    vec1 = Vector3D(1, 2, 3)
    vec2 = Vector3D(y=1, z=2)
    vec3 = Vector3D(1, 4)

    assert (vec1 + vec2).x == 1
    assert (vec1 + vec2).y == 3
    assert (vec1 + vec2).z == 5

    assert (vec1 + vec3).x == 2
    assert (vec1 + vec3).y == 6
    assert (vec1 + vec3).z == 9

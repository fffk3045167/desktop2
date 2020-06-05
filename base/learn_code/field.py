def test_read_write_field():
    # python code
    class A(object):
        pass

    obj1 = A()
    obj1.a = 1
    assert obj1.a == 1
    print(obj1.a)
    # Object model code
    # B = Class(name='B', base_class=OBJECT, fields={}, metaclass=TYPE)
    # obj2 = Instance(B)
    # obj2.write_attr("a", 1)
    # assert obj2.read_attr("a") == 1


if __name__ == '__main__':
    test_read_write_field()

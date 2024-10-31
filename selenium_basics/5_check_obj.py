def check_obj(obj, class_):
    return isinstance(obj, class_)


if __name__ == "__main__":
    from components.filter import LeftFilter
    from components import base

    class Base:
        pass
    another_base = Base()
    some_list = [1, 2]
    left_filter = LeftFilter("")
    for x in [another_base, some_list, left_filter]:
        if check_obj(x, int):
            print(f"{x} is from class {int.__name__}")
        if check_obj(x, list):
            print(f"{x} is from class {list.__name__}")
        if check_obj(x, Base):
            print(f"{x} is from class {Base.__name__}")
        if check_obj(x, LeftFilter):
            print(f"{x} is from class {LeftFilter.__name__}")
        if check_obj(x, object):
            print(f"{x} is from class {object.__name__}")
        if check_obj(x, base.Base):
            print(f"{x} is from class {base.Base.__name__}")
        print(f"{'':.^20}")

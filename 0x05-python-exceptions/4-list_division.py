#!/usr/bin/python3
def list_division(l1, l2, ll):
    l = []
    for i in range(ll):
        a = 0
        try:
            a = l1[i] / l2[i]
        except ZeroDivisionError:
            print("division by o")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except:
            pass
        finally:
            l.append(a)
    return l

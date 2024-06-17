import math
import warnings

"""
封装OPN为类
"""


# zero = (0, 0)
# one = (0, -1)
# oneNeg = (0, 1)

# 工具
def tran(x, m):
    if x < 0:
        return -math.pow(-x, m)
    else:
        return math.pow(x, m)


class OPN:
    """
    OPN 类
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        """
        打印输出OPN
        """
        return f"({self.a}, {self.b})"

    def __repr__(self):
        return self.__str__()

    def __copy__(self):
        """
        拷贝一个新的
        用于计算结果不变时返回。
        如果不返回新的，会因为修改结果的值而改变原始的值
        """
        return OPN(self.a, self.b)

    """
    四则运算
    """

    def __neg__(self):
        """
        负号取反
        -opn
        """
        return OPN(-self.a, -self.b)

    def __add__(self, other):
        """
        +, 两个OPN相加
        """
        return OPN(self.a + other.a, self.b + other.b)

    def __radd__(self, other):
        """
        被加操作，当使用内置函数求和等操作时，会用0加OPN
        """
        if other == 0:
            return self
        return self.__add__(other)

    def __sub__(self, other):
        """
        - 两个OPN 相减
        """
        return OPN(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        """
        * OPN相乘，OPN与数乘
        (a, b) * (c, d) = (-ad-bc, -ac-bd)
        """
        if isinstance(other, (int, float)):
            return OPN(self.a * other, self.b * other)
        elif isinstance(other, OPN):
            e = -self.a * other.b - self.b * other.a
            f = -self.a * other.a - self.b * other.b
            return OPN(e, f)
        else:
            return other.__rmul__(self)

    def __rmul__(self, other):
        """
        被乘
        """
        if other == 1:
            return self
        return self.__mul__(other)

    def __neg_power(self):
        """
        OPN的倒数
        :return:
        """
        if self.a == self.b or self.a == -self.b:
            # sys.exit('The multiplication inverse of this OPN {} does not exist'.format(opn))
            raise ZeroDivisionError(f'The multiplicative inverse of this OPN {self} does not exist')
        else:
            c = self.a / (self.a ** 2 - self.b ** 2)
            d = self.b / (self.b ** 2 - self.a ** 2)
            return OPN(c, d)

    def __truediv__(self, other):
        """
        / 除法
        opn1/opn2: opn1 * opn2倒数
        """
        if isinstance(other, (int, float)):
            return OPN(self.a / other, self.b / other)
        return self.__mul__(other.__neg_power())

    def __rtruediv__(self, other):
        """
        被除以
        实数/opn: 实数 * OPN倒数
        opn1/opn2: opn1 * opn2倒数
        :param other:
        :return:
        """
        return self.__neg_power().__mul__(other)

    """
    比较
    """

    def __eq__(self, other):
        """
        ==
        """
        return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        """
        > 大于
        """
        sub_opn = self.__sub__(other)
        return (sub_opn.a + sub_opn.b < 0) or (sub_opn.a + sub_opn.b == 0 and sub_opn.a > 0)

    def __lt__(self, other):
        """
        < 小于
        """
        sub_opn = self.__sub__(other)
        return (sub_opn.a + sub_opn.b) > 0 or (sub_opn.a + sub_opn.b == 0 and sub_opn.a < 0)

    def __gl__(self, other):
        """
        >= 大于等于
        """
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        """
        <= 小于等于
        """
        return self.__lt__(other) or self.__eq__(other)

    def __abs__(self):
        if self.a + self.b > 0 or (self.a + self.b == 0 and self.a < 0):
            return OPN(-self.a, -self.b)
        return self.__copy__()

    '''2. Power and nth root of OPNs'''

    """
    次方和开方
    """

    def __pow__(self, other):
        """
        幂运算 不支持分数次幂(但倒数后整数次开方可以)
        :param other:
        :return:
        """
        if other == 0:  # 指数为0
            return OPN(0, -1)
        if other == 1:  # 指数为1
            return self.__copy__()
        if other > 1:  # 指数大于0, 次方
            if self.a == -self.b or self.a == self.b:
                raise ZeroDivisionError(f'The multiplicative inverse of this OPN {self} does not exist')
            else:
                head = (((-1) ** (other + 1)) / 2) * ((self.a + self.b) ** other)
                tail = 0.5 * ((self.a - self.b) ** other)
                c = head + tail
                d = head - tail
                return OPN(c, d)
        # 开方运算
        if other < 0:  # 指数other小于0, 返回1/opn^(|other|)
            return self.__pow__(-other).__neg_power()
        if other % 1 != 0:
            n = 1 / other
            if n % 1 != 0:
                raise ValueError("不规范的开根\'{}\': 该运算规则root()仅支持开整数根!".format(n))
            elif n % 2 == 1:
                head = 0.5 * tran(self.a + self.b, 1 / n)
                tail = 0.5 * tran(self.a - self.b, 1 / n)
                first_entry = head + tail
                second_entry = head - tail
                new_opn = OPN(first_entry, second_entry)
                return new_opn
            elif n % 2 == 0 and self.a + self.b <= 0 and self.a >= self.b:
                head = 0.5 * ((-self.a - self.b) ** (1 / n))
                tail = 0.5 * ((self.a - self.b) ** (1 / n))
                first_entry = head + tail
                second_entry = head - tail
                new_opn = OPN(-first_entry, -second_entry)
                return new_opn
            else:
                raise Exception(
                    "Error: When n is even, if opn is negative, or the first term of OPN is smaller than the second "
                    "term, "
                    "the opn {} cannot open roots!".format(self))

    def _exp(self):
        # 使用catch_warnings来管理警告的上下文环境
        with warnings.catch_warnings():
            # 使用filterwarnings来控制警告的行为
            warnings.filterwarnings('error')  # 将警告转换成异常

            try:
                # head = (math.e ** self.a - math.e ** (-self.a)) / (2 * (math.e ** self.b))
                # tail = -(math.e ** self.a + math.e ** (-self.a)) / (2 * (math.e ** self.b))
                head = 0.5 * (math.e ** (self.a - self.b) - math.e ** (-self.a - self.b))
                tail = -0.5 * (math.e ** (self.a - self.b) + math.e ** (-self.a - self.b))
                return OPN(head, tail)
            except RuntimeWarning:
                # 这里处理RuntimeWarning的逻辑
                print(f"运行时异常，指数太大 当前: {self.b}")

        # head = (math.e ** self.a - math.e ** (-self.a)) / (2 * (math.e ** self.b))
        # tail = -(math.e ** self.a + math.e ** (-self.a)) / (2 * (math.e ** self.b))
        # return OPN(head, tail)

    def __rpow__(self, other):
        """
        实数的opn次方
        """
        if other > 0:
            return (self.__mul__(math.log(other)))._exp()
        else:
            raise ValueError('Error: the real number \'{}\' should be greater than 0'.format(other))

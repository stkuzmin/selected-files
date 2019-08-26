import numpy
import quadprog
from scipy.optimize import linprog
from cvxopt import matrix as cvxmat, sparse, spmatrix
from cvxopt.solvers import qp, options


class Quad(object):

    def __init__(
            self,
            P,
            q,
            G=None,
            h=None,
            A=None,
            b=None,
        ):
        self.P = P
        self.q = q
        self.G = G
        self.h = h
        self.A = A
        self.b = b

    def cvxopt_solve_qp(self):
        # make sure P is symmetric
        P = .5 * (self.P + self.P.T)
        args = [numpy.matrix(P), numpy.matrix(self.q)]
        if self.G is not None:
            args.extend([numpy.matrix(self.G), numpy.matrix(self.h)])
            if self.A is not None:
                args.extend([numpy.matrix(self.A), numpy.matrix(self.b)])
        sol = cvxopt.solvers.qp(*args)
        if 'optimal' not in sol['status']:
            return None
        return numpy.array(sol['x']).reshape((P.shape[1],))

    def quadprog_solve_qp(self):
        # make sure P is symmetric
        qp_G = .5 * (self.P + self.P.T)
        qp_a = -self.q
        if self.A is not None:
            qp_C = -numpy.vstack([self.A, self.G]).T
            qp_b = -numpy.hstack([self.b, self.h])
            meq = self.A.shape[0]
        else:
            qp_C = -self.G.T
            qp_b = -self.h
            meq = 0
        return quadprog.solve_qp(qp_G, qp_a, qp_C, qp_b, meq)[0]


def main():
    M = numpy.array([[7, 10, 8.], [10., 8., 11.], [8, 11, 16]])
    P = numpy.dot(M.T, M)
    q = numpy.dot(numpy.array([3., 2., 3.]), M).reshape((3,))
    G = numpy.array([[6, 10, 7.], [10, 7, 11], [7, 11, 15]])
    h = numpy.array([3., 2., -2.]).reshape((3,))
    qd = Quad(P, q, G, h).quadprog_solve_qp()
    print(qd)
    res = linprog(qd)
    print(res)


if __name__ == '__main__':
    main()

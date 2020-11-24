import home_window
import methods_window
import help_window
import online_window
import linear_window
import nonlinear_window
import interpolation_window
import lu_factoring_window
import direct_factoring_window
import iterative_window
import gaussian_elimination_window
import splines_window
import IncrementalSearches
import Bisection
import FixedPoint
import Newton
import Secant
import FakeRule
import MultipleRoots
import Jacobi
import GaussSeidel
import Sor
import LinearSpline
import SquareSpline
import CubicSpline
import FullPivoting
import PartialPivoting
import LuPartial
import LuSimple
import InterNewton
import Lagrange
import Vandermonde
import GaussianEliminationSimple
import Crout
import Doolittle
import Cholesky
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class HomeWindow(QtWidgets.QMainWindow,home_window.Ui_home_window):
    def __init__(self, parent=None):
        super(HomeWindow, self).__init__(parent)
        self.setupUi(self)
        self.methods_button.clicked.connect(self.clickMethods)
        self.help_button.clicked.connect(self.clickHelp)
        self.online_button.clicked.connect(self.clickOnline)
        self.show()

    def clickMethods(self):
        self.methods = MethodsWindow()
        self.methods.show()
        self.close()

    def clickHelp(self):
        self.help = HelpWindow()
        self.help.show()


    def clickOnline(self):
        self.online = OnlineWindow()
        self.online.show()

class MethodsWindow(QtWidgets.QMainWindow, methods_window.Ui_methods_window):
    def __init__(self, parent=None):
        super(MethodsWindow, self).__init__(parent)
        self.setupUi(self)
        self.linear_button.clicked.connect(self.clickLinear)
        self.nonlinear_button.clicked.connect(self.clickNonLinear)
        self.interpolation_button.clicked.connect(self.clickInterpolation)
        self.show()

    def clickLinear(self):
        self.linear = LinearWindow()
        self.linear.show()
        self.close()

    def clickNonLinear(self):
        self.non_linear = NonLinearWindow()
        self.non_linear.show()
        self.close()

    def clickInterpolation(self):
        self.interpolation = InterpolationWindow()
        self.interpolation.show()
        self.close()

class HelpWindow(QtWidgets.QMainWindow, help_window.Ui_help_window):
    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setupUi(self)

class OnlineWindow(QtWidgets.QMainWindow, online_window.Ui_online_window):
    def __init__(self, parent=None):
        super(OnlineWindow, self).__init__(parent)
        self.setupUi(self)

class LinearWindow(QtWidgets.QWidget, linear_window.Ui_linear):
    def __init__(self, parent=None):
        super(LinearWindow, self).__init__(parent)
        self.setupUi(self)
        self.lu_button.clicked.connect(self.clickLu)
        self.directf_button.clicked.connect(self.clickDirect)
        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickBack)
        self.iterative_button.clicked.connect(self.clickIterative)
        self.gaussian_button.clicked.connect(self.clickGaussian)
        self.show()

    def clickBack(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()

    def clickLu(self):
        self.lu = LuFactoringWindow()
        self.lu.show()
        self.close()

    def clickDirect(self):
        self.direct = DirectFactoringWindow()
        self.direct.show()
        self.close()

    def clickGaussian(self):
        self.gaussian = GaussianWindow()
        self.gaussian.show()
        self.close()

    def clickIterative(self):
        self.iterative = IterativeWindow()
        self.iterative.show()
        self.close()


class NonLinearWindow(QtWidgets.QWidget, nonlinear_window.Ui_nonlinear):
    def __init__(self, parent=None):
        super(NonLinearWindow, self).__init__(parent)
        self.setupUi(self)
        self.incremental_button.clicked.connect(self.clickIncremental)
        self.bisection_button.clicked.connect(self.clickBisection)
        self.fixedp_button.clicked.connect(self.clickFixed)
        self.newton_button.clicked.connect(self.clickNewton)
        self.secant_button.clicked.connect(self.clickSecant)
        self.false_button.clicked.connect(self.clickFake)
        self.roots_button.clicked.connect(self.clickMultipleRoots)
        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickBack)
        self.show()

    def clickBack(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()
    
    def clickIncremental(self):
        self.incremental = IncrementalSearches.IncrementalSearches()
        self.incremental.show()
        self.close()
        
    def clickBisection(self):
        self.bisection = Bisection.Bisection()
        self.bisection.show()
        self.close()

    def clickFixed(self):
        self.fixedPoint = FixedPoint.FixedPoint()
        self.fixedPoint.show()
        self.close()

    def clickNewton(self):
        	self.newton = Newton.Newton()
        	self.newton.show()
        	self.close()

    def clickSecant(self):
        self.secant = Secant.Secant()
        self.secant.show()
        self.close()

    def clickFake(self):
        self.fake_rule = FakeRule.FakeRule()
        self.fake_rule.show()
        self.close()
    
    def clickMultipleRoots(self):
        self.multipleroots = MultipleRoots.MultipleRoots()
        self.multipleroots.show()
        self.close()


class InterpolationWindow(QtWidgets.QWidget, interpolation_window.Ui_interpolation):
    def __init__(self, parent=None):
        super(InterpolationWindow, self).__init__(parent)
        self.setupUi(self)
        self.splines_button.clicked.connect(self.clickSplines)
        self.newtonint_button.clicked.connect(self.clickInterNewton)
        self.lagrangeint_button.clicked.connect(self.clickLagrange)
        self.vandermonde_button.clicked.connect(self.clickVandermonde)
        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickBack)
        self.show()

    def clickBack(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()
    
    def clickInterNewton(self):
        self.ne = InterNewton.InterNewton()
        self.ne.show()
        self.close()
    
    def clickLagrange(self):
        self.la = Lagrange.Lagrange()
        self.la.show()
        self.close()
    
    def clickVandermonde(self):
        self.van = Vandermonde.Vandermonde()
        self.van.show()
        self.close()
    
    def clickSplines(self):
        self.splines = SplinesWindow()
        self.splines.show()
        self.close()

class LuFactoringWindow(QtWidgets.QWidget, lu_factoring_window.Ui_lu_factoring):
    def __init__(self, parent=None):
        super(LuFactoringWindow, self).__init__(parent)
        self.setupUi(self)

        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickHome)
        self.partiallu_button.clicked.connect(self.clickLuPartial)
        self.simplelu_button.clicked.connect(self.clickLuSimple)
        self.show()

    def clickHome(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()

    def clickBack(self):
        self.linear = LinearWindow()
        self.linear.show()
        self.close()

    def clickLuPartial(self):
        self.lu_partial = LuPartial.LuPartial()
        self.lu_partial.show()
        self.close()

    def clickLuSimple(self):
        self.lu_simple = LuSimple.LuSimple()
        self.lu_simple.show()
        self.close()

class DirectFactoringWindow(QtWidgets.QWidget, direct_factoring_window.Ui_direct_factoring):
    def __init__(self, parent=None):
        super(DirectFactoringWindow, self).__init__(parent)
        self.setupUi(self)

        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickHome)
        self.crout_button.clicked.connect(self.clickCrout)
        self.doolittle_button.clicked.connect(self.clickDoolittle)
        self.cholesky_button.clicked.connect(self.clickCholesky)
        self.show()

    def clickHome(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()

    def clickBack(self):
        self.linear = LinearWindow()
        self.linear.show()
        self.close()

    def clickCrout(self):
        self.crout = Crout.Crout()
        self.crout.show()
        self.close()

    def clickDoolittle(self):
        self.doolittle = Doolittle.Doolittle()
        self.doolittle.show()
        self.close()
    
    def clickCholesky(self):
        self.cholesky = Cholesky.Cholesky()
        self.cholesky.show()
        self.close()


class IterativeWindow(QtWidgets.QWidget, iterative_window.Ui_iterative):
    def __init__(self, parent=None):
        super(IterativeWindow, self).__init__(parent)
        self.setupUi(self)

        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickHome)
        self.jacobi_button.clicked.connect(self.clickJacobi)
        self.gauss_button.clicked.connect(self.clickGaussSeidel)
        self.sor_button.clicked.connect(self.clickSor)
        self.show()

    def clickHome(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()

    def clickBack(self):
        self.linear = LinearWindow()
        self.linear.show()
        self.close()

    def clickJacobi(self):
        self.jacobi = Jacobi.Jacobi()
        self.jacobi.show()
        self.close()
    
    def clickGaussSeidel(self):
        self.gauss_seidel = GaussSeidel.GaussSeidel()
        self.gauss_seidel.show()
        self.close()
    
    def clickSor(self):
        self.sor = Sor.Sor()
        self.sor.show()
        self.close()


class GaussianWindow(QtWidgets.QWidget, gaussian_elimination_window.Ui_gaussian_elimination):
    def __init__(self, parent=None):
        super(GaussianWindow, self).__init__(parent)
        self.setupUi(self)

        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickHome)
        self.partial_button.clicked.connect(self.clickPartial)
        self.full_button.clicked.connect(self.clickFull)
        self.simple_button.clicked.connect(self.clickSimple)
        self.show()

    def clickHome(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()

    def clickBack(self):
        self.linear = LinearWindow()
        self.linear.show()
        self.close()
    
    def clickFull(self):
        self.full_pivoting = FullPivoting.FullPivoting()
        self.full_pivoting.show()
        self.close()
    
    def clickPartial(self):
        self.partial_pivoting = PartialPivoting.PartialPivoting()
        self.partial_pivoting.show()
        self.close()

    def clickSimple(self):
        self.simple_elim = GaussianEliminationSimple.GaussianEliminationSimple()
        self.simple_elim.show()
        self.close()


class SplinesWindow(QtWidgets.QWidget, splines_window.Ui_splines):
    def __init__(self, parent=None):
        super(SplinesWindow, self).__init__(parent)
        self.setupUi(self)

        self.linear_button.clicked.connect(self.clickLinear)
        self.quadratic_button.clicked.connect(self.clickSquare)
        self.cubric_button.clicked.connect(self.clickCubic)
        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickHome)
        self.show()

    def clickLinear(self):
        self.linear_spline = LinearSpline.LinearSpline()
        self.linear_spline.show()
        self.close()

    def clickSquare(self):
        self.square_spline = SquareSpline.SquareSpline()
        self.square_spline.show()
        self.close()

    def clickCubic(self):
        self.cubic_spline = CubicSpline.CubicSpline()
        self.cubic_spline.show()
        self.close()

    def clickHome(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()

    def clickBack(self):
        self.linear = LinearWindow()
        self.linear.show()
        self.close()

app = QtWidgets.QApplication(sys.argv)
window = HomeWindow()
sys.exit(app.exec_())

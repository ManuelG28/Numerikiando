import home
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
import MultipleRoots
import FullPivoting
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class HomeWindow(QtWidgets.QMainWindow, home.Ui_HomeWindow):
    def __init__(self, parent=None):
        super(HomeWindow, self).__init__(parent)
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
    
    def clickMultipleRoots(self):
        self.multipleroots = MultipleRoots.MultipleRoots()
        self.multipleroots.show()
        self.close()



class InterpolationWindow(QtWidgets.QWidget, interpolation_window.Ui_interpolation):
    def __init__(self, parent=None):
        super(InterpolationWindow, self).__init__(parent)
        self.setupUi(self)
        self.splines_button.clicked.connect(self.clickSplines)
        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickBack)
        self.show()

    def clickBack(self):
        self.home = HomeWindow()
        self.home.show()
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
        self.show()

    def clickHome(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()

    def clickBack(self):
        self.linear = LinearWindow()
        self.linear.show()
        self.close()


class DirectFactoringWindow(QtWidgets.QWidget, direct_factoring_window.Ui_direct_factoring):
    def __init__(self, parent=None):
        super(DirectFactoringWindow, self).__init__(parent)
        self.setupUi(self)

        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickHome)
        self.show()

    def clickHome(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()

    def clickBack(self):
        self.linear = LinearWindow()
        self.linear.show()
        self.close()


class IterativeWindow(QtWidgets.QWidget, iterative_window.Ui_iterative):
    def __init__(self, parent=None):
        super(IterativeWindow, self).__init__(parent)
        self.setupUi(self)

        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickHome)
        self.show()

    def clickHome(self):
        self.home = HomeWindow()
        self.home.show()
        self.close()

    def clickBack(self):
        self.linear = LinearWindow()
        self.linear.show()
        self.close()


class GaussianWindow(QtWidgets.QWidget, gaussian_elimination_window.Ui_gaussian_elimination):
    def __init__(self, parent=None):
        super(GaussianWindow, self).__init__(parent)
        self.setupUi(self)

        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickHome)
        self.full_button.clicked.connect(self.clickFull)
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


class SplinesWindow(QtWidgets.QWidget, splines_window.Ui_splines):
    def __init__(self, parent=None):
        super(SplinesWindow, self).__init__(parent)
        self.setupUi(self)

        self.back_button.clicked.connect(self.clickBack)
        self.home_button.clicked.connect(self.clickHome)
        self.show()

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

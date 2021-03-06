r"""
Catalog of Algebras

The ``algebras`` object may be used to access examples of various algebras
currently implemented in Sage. Using tab-completion on this object is an
easy way to discover and quickly create the algebras that are available
(as listed here).

Let ``<tab>`` indicate pressing the tab key.  So begin by typing
``algebras.<tab>`` to the see the currently implemented named algebras.

- :class:`algebras.Clifford <sage.algebras.clifford_algebra.CliffordAlgebra>`
- :class:`algebras.DifferentialWeyl
  <sage.algebras.weyl_algebra.DifferentialWeylAlgebra>`
- :class:`algebras.Exterior <sage.algebras.clifford_algebra.ExteriorAlgebra>`
- :class:`algebras.FiniteDimensional
  <sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra.FiniteDimensionalAlgebra>`
- :class:`algebras.Free <sage.algebras.free_algebra.FreeAlgebraFactory>`
- :func:`algebras.GradedCommutative
  <sage.algebras.commutative_dga.GradedCommutativeAlgebra>`
- :class:`algebras.Group <sage.algebras.group_algebra.GroupAlgebra>`
- :class:`algebras.Hall <sage.algebras.hall_algebra.HallAlgebra>`
- :class:`algebras.IwahoriHecke
  <sage.algebras.iwahori_hecke_algebra.IwahoriHeckeAlgebra>`
- :class:`algebras.NilCoxeter
  <sage.algebras.nil_coxeter_algebra.NilCoxeterAlgebra>`
- :func:`algebras.Quaternion
  <sage.algebras.quatalg.quaternion_algebra.QuaternionAlgebraFactory>`
- :class:`algebras.Shuffle <sage.algebras.shuffle_algebra.ShuffleAlgebra>`
- :class:`algebras.Steenrod
  <sage.algebras.steenrod.steenrod_algebra.SteenrodAlgebra>`
"""

from sage.algebras.free_algebra import FreeAlgebra as Free
from sage.algebras.iwahori_hecke_algebra import IwahoriHeckeAlgebra as IwahoriHecke
from sage.algebras.quatalg.quaternion_algebra import QuaternionAlgebra as Quaternion
from sage.algebras.steenrod.steenrod_algebra import SteenrodAlgebra as Steenrod
from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra import FiniteDimensionalAlgebra as FiniteDimensional
from sage.algebras.group_algebra import GroupAlgebra as Group
from sage.algebras.clifford_algebra import CliffordAlgebra as Clifford
from sage.algebras.clifford_algebra import ExteriorAlgebra as Exterior
from sage.algebras.weyl_algebra import DifferentialWeylAlgebra as DifferentialWeyl

from sage.misc.lazy_import import lazy_import
lazy_import('sage.algebras.nil_coxeter_algebra', 'NilCoxeterAlgebra', 'NilCoxeter')
lazy_import('sage.algebras.hall_algebra', 'HallAlgebra', 'Hall')
lazy_import('sage.algebras.shuffle_algebra', 'ShuffleAlgebra', 'Shuffle')
lazy_import('sage.algebras.commutative_dga', 'GradedCommutativeAlgebra', 'GradedCommutative')
del lazy_import # We remove the object from here so it doesn't appear under tab completion


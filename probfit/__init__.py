"""
probfit - Cost function builder. For fitting distributions.

* Code: https://github.com/scikit-hep/probfit
* Docs: http://probfit.readthedocs.io
"""


from .costfunc import UnbinnedLH, BinnedLH, Chi2Regression, BinnedChi2,\
 SimultaneousFit
from .pdf import doublegaussian, doublecrystalball, ugaussian, gaussian, chisquared, \
    crystalball, argus, cruijff, linear, poly2, poly3, novosibirsk, \
    Polynomial, HistogramPdf, cauchy, rtv_breitwigner, johnsonSU, \
    exponential

from .toy import gen_toy, gen_toyn
from .util import *
from .oneshot import *
from .statutil import *
from .plotting import *
from .funcutil import *
from .decorator import *
from ._libstat import integrate1d

from .functor import Normalized, Extended, Convolve, AddPdf, AddPdfNorm, \
 BlindFunc
from .version import __version__

__all__ = [
    'AddPdfNorm',
    'AddPdf',
    'BinnedChi2',
    'BinnedLH',
    'BlindFunc',
    'Chi2Regression',
    'Convolve',
    'Extended',
    'Normalized',
    'Polynomial',
    'HistogramPdf',
    'UnbinnedLH',
    'argus',
    'cruijff',
    'cauchy',
    'rtv_breitwigner',
    'crystalball',
    'doublecrystalball',
    'describe',
    'doublegaussian',
    'johnsonSU',
    'draw_compare',
    'draw_compare_hist',
    'draw_pdf',
    'draw_pdf_with_edges',
    'extended',
    'fwhm_f',
    'gaussian',
    'chisquared',
    'gen_toy',
    'gen_toyn',
    'integrate1d',
    'linear',
    'normalized',
    'novosibirsk',
    'poly2',
    'poly3',
    'SimultaneousFit',
    'try_binlh',
    'try_chi2',
    'try_uml',
    'ugaussian',
    'exponential',
    '__version__',
]

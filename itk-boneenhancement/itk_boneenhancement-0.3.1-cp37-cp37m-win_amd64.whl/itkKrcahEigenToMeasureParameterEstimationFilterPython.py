# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


from . import _BoneEnhancementPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkKrcahEigenToMeasureParameterEstimationFilterPython
else:
    import _itkKrcahEigenToMeasureParameterEstimationFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkKrcahEigenToMeasureParameterEstimationFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkKrcahEigenToMeasureParameterEstimationFilterPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import itk.itkImageRegionPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.vnl_vector_refPython
import itk.itkEigenToMeasureImageFilterPython
import itk.itkArrayPython
import itk.itkStreamingImageFilterPython
import itk.itkImageToImageFilterAPython
import itk.itkImageToImageFilterCommonPython
import itk.itkVectorImagePython
import itk.itkImagePython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterBPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkSpatialObjectBasePython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkOptimizerParametersPython
import itk.itkArray2DPython
import itk.itkDiffusionTensor3DPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkSpatialObjectPropertyPython
import itk.itkBoundingBoxPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkMapContainerPython

def itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_New():
    return itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33.New()

class itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33(itk.itkEigenToMeasureImageFilterPython.itkEigenToMeasureParameterEstimationFilterIVF33IVF33):
    r"""Proxy of C++ itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33___New_orig__)
    Clone = _swig_new_instance_method(_itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_Clone)
    SetParameterSet = _swig_new_instance_method(_itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_SetParameterSet)
    GetParameterSet = _swig_new_instance_method(_itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_GetParameterSet)
    SetParameterSetToImplementation = _swig_new_instance_method(_itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_SetParameterSetToImplementation)
    SetParameterSetToJournalArticle = _swig_new_instance_method(_itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_SetParameterSetToJournalArticle)
    InputHaveDimension3Check = _itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_InputHaveDimension3Check
    
    InputFixedArrayHasDimension3Check = _itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_InputFixedArrayHasDimension3Check
    
    __swig_destroy__ = _itkKrcahEigenToMeasureParameterEstimationFilterPython.delete_itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33
    cast = _swig_new_static_method(_itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_cast)

    def New(*args, **kargs):
        """New() -> itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33

        Create a new object of the class itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33 in _itkKrcahEigenToMeasureParameterEstimationFilterPython:
_itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_swigregister(itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33)
itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33___New_orig__ = _itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33___New_orig__
itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_cast = _itkKrcahEigenToMeasureParameterEstimationFilterPython.itkKrcahEigenToMeasureParameterEstimationFilterIVF33IVF33_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def krcah_eigen_to_measure_parameter_estimation_filter(*args, **kwargs):
    """Procedural interface for KrcahEigenToMeasureParameterEstimationFilter"""
    import itk
    instance = itk.KrcahEigenToMeasureParameterEstimationFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def krcah_eigen_to_measure_parameter_estimation_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.KrcahEigenToMeasureParameterEstimationFilter, itkTemplate.itkTemplate):
        filter_object = itk.KrcahEigenToMeasureParameterEstimationFilter.values()[0]
    else:
        filter_object = itk.KrcahEigenToMeasureParameterEstimationFilter

    krcah_eigen_to_measure_parameter_estimation_filter.__doc__ = filter_object.__doc__
    krcah_eigen_to_measure_parameter_estimation_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    krcah_eigen_to_measure_parameter_estimation_filter.__doc__ += "Available Keyword Arguments:\n"
    krcah_eigen_to_measure_parameter_estimation_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])




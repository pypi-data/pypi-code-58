# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkDescoteauxEigenToMeasureImageFilterPython
else:
    import _itkDescoteauxEigenToMeasureImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkDescoteauxEigenToMeasureImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkDescoteauxEigenToMeasureImageFilterPython.SWIG_PyStaticMethod_New

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


import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkEigenToMeasureImageFilterPython
import itk.itkSpatialObjectBasePython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkImageRegionPython
import itk.itkSizePython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkAffineTransformPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkDiffusionTensor3DPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkArray2DPython
import itk.itkTransformBasePython
import itk.itkVariableLengthVectorPython
import itk.itkBoundingBoxPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkMapContainerPython
import itk.itkSpatialObjectPropertyPython
import itk.itkRGBAPixelPython
import itk.itkStreamingImageFilterPython
import itk.itkImageToImageFilterAPython
import itk.itkImagePython
import itk.itkRGBPixelPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkVectorImagePython
import itk.itkImageToImageFilterBPython
import itk.itkSimpleDataObjectDecoratorPython

def itkDescoteauxEigenToMeasureImageFilterIVF33ID3_New():
    return itkDescoteauxEigenToMeasureImageFilterIVF33ID3.New()

class itkDescoteauxEigenToMeasureImageFilterIVF33ID3(itk.itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3):
    r"""Proxy of C++ itkDescoteauxEigenToMeasureImageFilterIVF33ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_Clone)
    SetEnhanceType = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_SetEnhanceType)
    GetEnhanceType = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_GetEnhanceType)
    SetEnhanceBrightObjects = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_SetEnhanceBrightObjects)
    SetEnhanceDarkObjects = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_SetEnhanceDarkObjects)
    InputHaveDimension3Check = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_InputHaveDimension3Check
    
    OutputHaveDimension3Check = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_OutputHaveDimension3Check
    
    InputFixedArrayHasDimension3Check = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_InputFixedArrayHasDimension3Check
    
    __swig_destroy__ = _itkDescoteauxEigenToMeasureImageFilterPython.delete_itkDescoteauxEigenToMeasureImageFilterIVF33ID3
    cast = _swig_new_static_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_cast)

    def New(*args, **kargs):
        """New() -> itkDescoteauxEigenToMeasureImageFilterIVF33ID3

        Create a new object of the class itkDescoteauxEigenToMeasureImageFilterIVF33ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDescoteauxEigenToMeasureImageFilterIVF33ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDescoteauxEigenToMeasureImageFilterIVF33ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDescoteauxEigenToMeasureImageFilterIVF33ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDescoteauxEigenToMeasureImageFilterIVF33ID3 in _itkDescoteauxEigenToMeasureImageFilterPython:
_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_swigregister(itkDescoteauxEigenToMeasureImageFilterIVF33ID3)
itkDescoteauxEigenToMeasureImageFilterIVF33ID3___New_orig__ = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3___New_orig__
itkDescoteauxEigenToMeasureImageFilterIVF33ID3_cast = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33ID3_cast


def itkDescoteauxEigenToMeasureImageFilterIVF33IF3_New():
    return itkDescoteauxEigenToMeasureImageFilterIVF33IF3.New()

class itkDescoteauxEigenToMeasureImageFilterIVF33IF3(itk.itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3):
    r"""Proxy of C++ itkDescoteauxEigenToMeasureImageFilterIVF33IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_Clone)
    SetEnhanceType = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_SetEnhanceType)
    GetEnhanceType = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_GetEnhanceType)
    SetEnhanceBrightObjects = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_SetEnhanceBrightObjects)
    SetEnhanceDarkObjects = _swig_new_instance_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_SetEnhanceDarkObjects)
    InputHaveDimension3Check = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_InputHaveDimension3Check
    
    OutputHaveDimension3Check = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_OutputHaveDimension3Check
    
    InputFixedArrayHasDimension3Check = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_InputFixedArrayHasDimension3Check
    
    __swig_destroy__ = _itkDescoteauxEigenToMeasureImageFilterPython.delete_itkDescoteauxEigenToMeasureImageFilterIVF33IF3
    cast = _swig_new_static_method(_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_cast)

    def New(*args, **kargs):
        """New() -> itkDescoteauxEigenToMeasureImageFilterIVF33IF3

        Create a new object of the class itkDescoteauxEigenToMeasureImageFilterIVF33IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkDescoteauxEigenToMeasureImageFilterIVF33IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkDescoteauxEigenToMeasureImageFilterIVF33IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkDescoteauxEigenToMeasureImageFilterIVF33IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkDescoteauxEigenToMeasureImageFilterIVF33IF3 in _itkDescoteauxEigenToMeasureImageFilterPython:
_itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_swigregister(itkDescoteauxEigenToMeasureImageFilterIVF33IF3)
itkDescoteauxEigenToMeasureImageFilterIVF33IF3___New_orig__ = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3___New_orig__
itkDescoteauxEigenToMeasureImageFilterIVF33IF3_cast = _itkDescoteauxEigenToMeasureImageFilterPython.itkDescoteauxEigenToMeasureImageFilterIVF33IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def descoteaux_eigen_to_measure_image_filter(*args, **kwargs):
    """Procedural interface for DescoteauxEigenToMeasureImageFilter"""
    import itk
    instance = itk.DescoteauxEigenToMeasureImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def descoteaux_eigen_to_measure_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.DescoteauxEigenToMeasureImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.DescoteauxEigenToMeasureImageFilter.values()[0]
    else:
        filter_object = itk.DescoteauxEigenToMeasureImageFilter

    descoteaux_eigen_to_measure_image_filter.__doc__ = filter_object.__doc__
    descoteaux_eigen_to_measure_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    descoteaux_eigen_to_measure_image_filter.__doc__ += "Available Keyword Arguments:\n"
    descoteaux_eigen_to_measure_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])




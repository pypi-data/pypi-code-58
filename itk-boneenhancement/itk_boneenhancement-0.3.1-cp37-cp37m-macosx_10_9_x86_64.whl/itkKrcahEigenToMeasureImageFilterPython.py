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
    from . import _itkKrcahEigenToMeasureImageFilterPython
else:
    import _itkKrcahEigenToMeasureImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkKrcahEigenToMeasureImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkKrcahEigenToMeasureImageFilterPython.SWIG_PyStaticMethod_New

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


import itk.itkVectorPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vector_refPython
import itk.itkFixedArrayPython
import itk.ITKCommonBasePython
import itk.itkEigenToMeasureImageFilterPython
import itk.itkStreamingImageFilterPython
import itk.itkImageToImageFilterAPython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkImagePython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.itkPointPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
import itk.itkRGBPixelPython
import itk.itkRGBAPixelPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkImageToImageFilterCommonPython
import itk.itkArrayPython
import itk.itkSpatialObjectBasePython
import itk.itkSpatialObjectPropertyPython
import itk.itkAffineTransformPython
import itk.itkTransformBasePython
import itk.itkDiffusionTensor3DPython
import itk.itkArray2DPython
import itk.itkOptimizerParametersPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkBoundingBoxPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkMapContainerPython
import itk.itkSimpleDataObjectDecoratorPython
import itk.itkImageToImageFilterBPython

def itkKrcahEigenToMeasureImageFilterIVF33ID3_New():
    return itkKrcahEigenToMeasureImageFilterIVF33ID3.New()

class itkKrcahEigenToMeasureImageFilterIVF33ID3(itk.itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3):
    r"""Proxy of C++ itkKrcahEigenToMeasureImageFilterIVF33ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3___New_orig__)
    Clone = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_Clone)
    SetEnhanceType = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_SetEnhanceType)
    GetEnhanceType = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_GetEnhanceType)
    SetEnhanceBrightObjects = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_SetEnhanceBrightObjects)
    SetEnhanceDarkObjects = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_SetEnhanceDarkObjects)
    InputHaveDimension3Check = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_InputHaveDimension3Check
    
    OutputHaveDimension3Check = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_OutputHaveDimension3Check
    
    InputFixedArrayHasDimension3Check = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_InputFixedArrayHasDimension3Check
    
    __swig_destroy__ = _itkKrcahEigenToMeasureImageFilterPython.delete_itkKrcahEigenToMeasureImageFilterIVF33ID3
    cast = _swig_new_static_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_cast)

    def New(*args, **kargs):
        """New() -> itkKrcahEigenToMeasureImageFilterIVF33ID3

        Create a new object of the class itkKrcahEigenToMeasureImageFilterIVF33ID3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKrcahEigenToMeasureImageFilterIVF33ID3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKrcahEigenToMeasureImageFilterIVF33ID3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKrcahEigenToMeasureImageFilterIVF33ID3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKrcahEigenToMeasureImageFilterIVF33ID3 in _itkKrcahEigenToMeasureImageFilterPython:
_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_swigregister(itkKrcahEigenToMeasureImageFilterIVF33ID3)
itkKrcahEigenToMeasureImageFilterIVF33ID3___New_orig__ = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3___New_orig__
itkKrcahEigenToMeasureImageFilterIVF33ID3_cast = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33ID3_cast


def itkKrcahEigenToMeasureImageFilterIVF33IF3_New():
    return itkKrcahEigenToMeasureImageFilterIVF33IF3.New()

class itkKrcahEigenToMeasureImageFilterIVF33IF3(itk.itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3):
    r"""Proxy of C++ itkKrcahEigenToMeasureImageFilterIVF33IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3___New_orig__)
    Clone = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_Clone)
    SetEnhanceType = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_SetEnhanceType)
    GetEnhanceType = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_GetEnhanceType)
    SetEnhanceBrightObjects = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_SetEnhanceBrightObjects)
    SetEnhanceDarkObjects = _swig_new_instance_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_SetEnhanceDarkObjects)
    InputHaveDimension3Check = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_InputHaveDimension3Check
    
    OutputHaveDimension3Check = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_OutputHaveDimension3Check
    
    InputFixedArrayHasDimension3Check = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_InputFixedArrayHasDimension3Check
    
    __swig_destroy__ = _itkKrcahEigenToMeasureImageFilterPython.delete_itkKrcahEigenToMeasureImageFilterIVF33IF3
    cast = _swig_new_static_method(_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_cast)

    def New(*args, **kargs):
        """New() -> itkKrcahEigenToMeasureImageFilterIVF33IF3

        Create a new object of the class itkKrcahEigenToMeasureImageFilterIVF33IF3 and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkKrcahEigenToMeasureImageFilterIVF33IF3.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkKrcahEigenToMeasureImageFilterIVF33IF3.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkKrcahEigenToMeasureImageFilterIVF33IF3.__New_orig__()
        import itkTemplate
        itkTemplate.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkKrcahEigenToMeasureImageFilterIVF33IF3 in _itkKrcahEigenToMeasureImageFilterPython:
_itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_swigregister(itkKrcahEigenToMeasureImageFilterIVF33IF3)
itkKrcahEigenToMeasureImageFilterIVF33IF3___New_orig__ = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3___New_orig__
itkKrcahEigenToMeasureImageFilterIVF33IF3_cast = _itkKrcahEigenToMeasureImageFilterPython.itkKrcahEigenToMeasureImageFilterIVF33IF3_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def krcah_eigen_to_measure_image_filter(*args, **kwargs):
    """Procedural interface for KrcahEigenToMeasureImageFilter"""
    import itk
    instance = itk.KrcahEigenToMeasureImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def krcah_eigen_to_measure_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.KrcahEigenToMeasureImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.KrcahEigenToMeasureImageFilter.values()[0]
    else:
        filter_object = itk.KrcahEigenToMeasureImageFilter

    krcah_eigen_to_measure_image_filter.__doc__ = filter_object.__doc__
    krcah_eigen_to_measure_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    krcah_eigen_to_measure_image_filter.__doc__ += "Available Keyword Arguments:\n"
    krcah_eigen_to_measure_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])




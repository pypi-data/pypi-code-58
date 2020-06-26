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
    from . import _itkEigenToMeasureImageFilterPython
else:
    import _itkEigenToMeasureImageFilterPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkEigenToMeasureImageFilterPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkEigenToMeasureImageFilterPython.SWIG_PyStaticMethod_New

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


import itk.itkStreamingImageFilterPython
import itk.itkImageToImageFilterAPython
import itk.ITKCommonBasePython
import itk.pyBasePython
import itk.itkImageRegionPython
import itk.itkIndexPython
import itk.itkOffsetPython
import itk.itkSizePython
import itk.itkImagePython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.stdcomplexPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.itkFixedArrayPython
import itk.itkPointPython
import itk.itkCovariantVectorPython
import itk.itkRGBAPixelPython
import itk.itkRGBPixelPython
import itk.itkSymmetricSecondRankTensorPython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkVectorImagePython
import itk.itkVariableLengthVectorPython
import itk.itkImageToImageFilterCommonPython
import itk.itkImageSourcePython
import itk.itkImageSourceCommonPython
import itk.itkSpatialObjectBasePython
import itk.itkSpatialObjectPropertyPython
import itk.itkBoundingBoxPython
import itk.itkMapContainerPython
import itk.itkVectorContainerPython
import itk.itkContinuousIndexPython
import itk.itkAffineTransformPython
import itk.itkMatrixOffsetTransformBasePython
import itk.itkArray2DPython
import itk.itkDiffusionTensor3DPython
import itk.itkOptimizerParametersPython
import itk.itkArrayPython
import itk.itkTransformBasePython
import itk.itkImageToImageFilterBPython
import itk.itkSimpleDataObjectDecoratorPython
class itkEigenToMeasureImageFilterIVF33ID3(itk.itkImageToImageFilterBPython.itkImageToImageFilterIVF33ID3):
    r"""Proxy of C++ itkEigenToMeasureImageFilterIVF33ID3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetParametersInput = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_SetParametersInput)
    SetParameters = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_SetParameters)
    GetParametersInput = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_GetParametersInput)
    GetParameters = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_GetParameters)
    SetMask = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_SetMask)
    GetMask = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_GetMask)
    GetEigenValueOrder = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_GetEigenValueOrder)
    __swig_destroy__ = _itkEigenToMeasureImageFilterPython.delete_itkEigenToMeasureImageFilterIVF33ID3
    cast = _swig_new_static_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_cast)

# Register itkEigenToMeasureImageFilterIVF33ID3 in _itkEigenToMeasureImageFilterPython:
_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_swigregister(itkEigenToMeasureImageFilterIVF33ID3)
itkEigenToMeasureImageFilterIVF33ID3_cast = _itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33ID3_cast

class itkEigenToMeasureImageFilterIVF33IF3(itk.itkImageToImageFilterBPython.itkImageToImageFilterIVF33IF3):
    r"""Proxy of C++ itkEigenToMeasureImageFilterIVF33IF3 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    SetParametersInput = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_SetParametersInput)
    SetParameters = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_SetParameters)
    GetParametersInput = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_GetParametersInput)
    GetParameters = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_GetParameters)
    SetMask = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_SetMask)
    GetMask = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_GetMask)
    GetEigenValueOrder = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_GetEigenValueOrder)
    __swig_destroy__ = _itkEigenToMeasureImageFilterPython.delete_itkEigenToMeasureImageFilterIVF33IF3
    cast = _swig_new_static_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_cast)

# Register itkEigenToMeasureImageFilterIVF33IF3 in _itkEigenToMeasureImageFilterPython:
_itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_swigregister(itkEigenToMeasureImageFilterIVF33IF3)
itkEigenToMeasureImageFilterIVF33IF3_cast = _itkEigenToMeasureImageFilterPython.itkEigenToMeasureImageFilterIVF33IF3_cast

class itkEigenToMeasureParameterEstimationFilterIVF33IVF33(itk.itkStreamingImageFilterPython.itkStreamingImageFilterIVF33IVF33):
    r"""Proxy of C++ itkEigenToMeasureParameterEstimationFilterIVF33IVF33 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    GetParametersOutput = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureParameterEstimationFilterIVF33IVF33_GetParametersOutput)
    GetParameters = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureParameterEstimationFilterIVF33IVF33_GetParameters)
    SetMask = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureParameterEstimationFilterIVF33IVF33_SetMask)
    GetMask = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureParameterEstimationFilterIVF33IVF33_GetMask)
    ThreadedGenerateData = _swig_new_instance_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureParameterEstimationFilterIVF33IVF33_ThreadedGenerateData)
    __swig_destroy__ = _itkEigenToMeasureImageFilterPython.delete_itkEigenToMeasureParameterEstimationFilterIVF33IVF33
    cast = _swig_new_static_method(_itkEigenToMeasureImageFilterPython.itkEigenToMeasureParameterEstimationFilterIVF33IVF33_cast)

# Register itkEigenToMeasureParameterEstimationFilterIVF33IVF33 in _itkEigenToMeasureImageFilterPython:
_itkEigenToMeasureImageFilterPython.itkEigenToMeasureParameterEstimationFilterIVF33IVF33_swigregister(itkEigenToMeasureParameterEstimationFilterIVF33IVF33)
itkEigenToMeasureParameterEstimationFilterIVF33IVF33_cast = _itkEigenToMeasureImageFilterPython.itkEigenToMeasureParameterEstimationFilterIVF33IVF33_cast


import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def eigen_to_measure_parameter_estimation_filter(*args, **kwargs):
    """Procedural interface for EigenToMeasureParameterEstimationFilter"""
    import itk
    instance = itk.EigenToMeasureParameterEstimationFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def eigen_to_measure_parameter_estimation_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.EigenToMeasureParameterEstimationFilter, itkTemplate.itkTemplate):
        filter_object = itk.EigenToMeasureParameterEstimationFilter.values()[0]
    else:
        filter_object = itk.EigenToMeasureParameterEstimationFilter

    eigen_to_measure_parameter_estimation_filter.__doc__ = filter_object.__doc__
    eigen_to_measure_parameter_estimation_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    eigen_to_measure_parameter_estimation_filter.__doc__ += "Available Keyword Arguments:\n"
    eigen_to_measure_parameter_estimation_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])
import itkHelpers
@itkHelpers.accept_numpy_array_like_xarray
def eigen_to_measure_image_filter(*args, **kwargs):
    """Procedural interface for EigenToMeasureImageFilter"""
    import itk
    instance = itk.EigenToMeasureImageFilter.New(*args, **kwargs)
    return instance.__internal_call__()

def eigen_to_measure_image_filter_init_docstring():
    import itk
    import itkTemplate
    import itkHelpers
    if isinstance(itk.EigenToMeasureImageFilter, itkTemplate.itkTemplate):
        filter_object = itk.EigenToMeasureImageFilter.values()[0]
    else:
        filter_object = itk.EigenToMeasureImageFilter

    eigen_to_measure_image_filter.__doc__ = filter_object.__doc__
    eigen_to_measure_image_filter.__doc__ += "\n Args are Input(s) to the filter.\n"
    eigen_to_measure_image_filter.__doc__ += "Available Keyword Arguments:\n"
    eigen_to_measure_image_filter.__doc__ += "".join([
        "  " + itkHelpers.camel_to_snake_case(item[3:]) + "\n"
        for item in dir(filter_object)
        if item[:3] == "Set"])




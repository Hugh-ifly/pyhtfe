# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_htfe', [dirname(__file__)])
        except ImportError:
            import _htfe
            return _htfe
        if fp is not None:
            try:
                _mod = imp.load_module('_htfe', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _htfe = swig_import_helper()
    del swig_import_helper
else:
    import _htfe
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _htfe.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _htfe.SwigPyIterator_value(self)
    def incr(self, n=1): return _htfe.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _htfe.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _htfe.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _htfe.SwigPyIterator_equal(self, *args)
    def copy(self): return _htfe.SwigPyIterator_copy(self)
    def next(self): return _htfe.SwigPyIterator_next(self)
    def __next__(self): return _htfe.SwigPyIterator___next__(self)
    def previous(self): return _htfe.SwigPyIterator_previous(self)
    def advance(self, *args): return _htfe.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _htfe.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _htfe.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _htfe.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _htfe.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _htfe.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _htfe.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _htfe.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vectorld(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectorld, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectorld, name)
    __repr__ = _swig_repr
    def iterator(self): return _htfe.vectorld_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _htfe.vectorld___nonzero__(self)
    def __bool__(self): return _htfe.vectorld___bool__(self)
    def __len__(self): return _htfe.vectorld___len__(self)
    def pop(self): return _htfe.vectorld_pop(self)
    def __getslice__(self, *args): return _htfe.vectorld___getslice__(self, *args)
    def __setslice__(self, *args): return _htfe.vectorld___setslice__(self, *args)
    def __delslice__(self, *args): return _htfe.vectorld___delslice__(self, *args)
    def __delitem__(self, *args): return _htfe.vectorld___delitem__(self, *args)
    def __getitem__(self, *args): return _htfe.vectorld___getitem__(self, *args)
    def __setitem__(self, *args): return _htfe.vectorld___setitem__(self, *args)
    def append(self, *args): return _htfe.vectorld_append(self, *args)
    def empty(self): return _htfe.vectorld_empty(self)
    def size(self): return _htfe.vectorld_size(self)
    def clear(self): return _htfe.vectorld_clear(self)
    def swap(self, *args): return _htfe.vectorld_swap(self, *args)
    def get_allocator(self): return _htfe.vectorld_get_allocator(self)
    def begin(self): return _htfe.vectorld_begin(self)
    def end(self): return _htfe.vectorld_end(self)
    def rbegin(self): return _htfe.vectorld_rbegin(self)
    def rend(self): return _htfe.vectorld_rend(self)
    def pop_back(self): return _htfe.vectorld_pop_back(self)
    def erase(self, *args): return _htfe.vectorld_erase(self, *args)
    def __init__(self, *args): 
        this = _htfe.new_vectorld(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _htfe.vectorld_push_back(self, *args)
    def front(self): return _htfe.vectorld_front(self)
    def back(self): return _htfe.vectorld_back(self)
    def assign(self, *args): return _htfe.vectorld_assign(self, *args)
    def resize(self, *args): return _htfe.vectorld_resize(self, *args)
    def insert(self, *args): return _htfe.vectorld_insert(self, *args)
    def reserve(self, *args): return _htfe.vectorld_reserve(self, *args)
    def capacity(self): return _htfe.vectorld_capacity(self)
    __swig_destroy__ = _htfe.delete_vectorld
    __del__ = lambda self : None;
vectorld_swigregister = _htfe.vectorld_swigregister
vectorld_swigregister(vectorld)

class LayerDesc(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LayerDesc, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LayerDesc, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_width"] = _htfe.LayerDesc__width_set
    __swig_getmethods__["_width"] = _htfe.LayerDesc__width_get
    if _newclass:_width = _swig_property(_htfe.LayerDesc__width_get, _htfe.LayerDesc__width_set)
    __swig_setmethods__["_height"] = _htfe.LayerDesc__height_set
    __swig_getmethods__["_height"] = _htfe.LayerDesc__height_get
    if _newclass:_height = _swig_property(_htfe.LayerDesc__height_get, _htfe.LayerDesc__height_set)
    __swig_setmethods__["_receptiveFieldRadius"] = _htfe.LayerDesc__receptiveFieldRadius_set
    __swig_getmethods__["_receptiveFieldRadius"] = _htfe.LayerDesc__receptiveFieldRadius_get
    if _newclass:_receptiveFieldRadius = _swig_property(_htfe.LayerDesc__receptiveFieldRadius_get, _htfe.LayerDesc__receptiveFieldRadius_set)
    __swig_setmethods__["_reconstructionRadius"] = _htfe.LayerDesc__reconstructionRadius_set
    __swig_getmethods__["_reconstructionRadius"] = _htfe.LayerDesc__reconstructionRadius_get
    if _newclass:_reconstructionRadius = _swig_property(_htfe.LayerDesc__reconstructionRadius_get, _htfe.LayerDesc__reconstructionRadius_set)
    __swig_setmethods__["_lateralConnectionRadius"] = _htfe.LayerDesc__lateralConnectionRadius_set
    __swig_getmethods__["_lateralConnectionRadius"] = _htfe.LayerDesc__lateralConnectionRadius_get
    if _newclass:_lateralConnectionRadius = _swig_property(_htfe.LayerDesc__lateralConnectionRadius_get, _htfe.LayerDesc__lateralConnectionRadius_set)
    __swig_setmethods__["_inhibitionRadius"] = _htfe.LayerDesc__inhibitionRadius_set
    __swig_getmethods__["_inhibitionRadius"] = _htfe.LayerDesc__inhibitionRadius_get
    if _newclass:_inhibitionRadius = _swig_property(_htfe.LayerDesc__inhibitionRadius_get, _htfe.LayerDesc__inhibitionRadius_set)
    __swig_setmethods__["_feedBackConnectionRadius"] = _htfe.LayerDesc__feedBackConnectionRadius_set
    __swig_getmethods__["_feedBackConnectionRadius"] = _htfe.LayerDesc__feedBackConnectionRadius_get
    if _newclass:_feedBackConnectionRadius = _swig_property(_htfe.LayerDesc__feedBackConnectionRadius_get, _htfe.LayerDesc__feedBackConnectionRadius_set)
    __swig_setmethods__["_sparsity"] = _htfe.LayerDesc__sparsity_set
    __swig_getmethods__["_sparsity"] = _htfe.LayerDesc__sparsity_get
    if _newclass:_sparsity = _swig_property(_htfe.LayerDesc__sparsity_get, _htfe.LayerDesc__sparsity_set)
    __swig_setmethods__["_dutyCycleDecay"] = _htfe.LayerDesc__dutyCycleDecay_set
    __swig_getmethods__["_dutyCycleDecay"] = _htfe.LayerDesc__dutyCycleDecay_get
    if _newclass:_dutyCycleDecay = _swig_property(_htfe.LayerDesc__dutyCycleDecay_get, _htfe.LayerDesc__dutyCycleDecay_set)
    __swig_setmethods__["_feedForwardAlpha"] = _htfe.LayerDesc__feedForwardAlpha_set
    __swig_getmethods__["_feedForwardAlpha"] = _htfe.LayerDesc__feedForwardAlpha_get
    if _newclass:_feedForwardAlpha = _swig_property(_htfe.LayerDesc__feedForwardAlpha_get, _htfe.LayerDesc__feedForwardAlpha_set)
    __swig_setmethods__["_lateralAlpha"] = _htfe.LayerDesc__lateralAlpha_set
    __swig_getmethods__["_lateralAlpha"] = _htfe.LayerDesc__lateralAlpha_get
    if _newclass:_lateralAlpha = _swig_property(_htfe.LayerDesc__lateralAlpha_get, _htfe.LayerDesc__lateralAlpha_set)
    __swig_setmethods__["_feedBackAlpha"] = _htfe.LayerDesc__feedBackAlpha_set
    __swig_getmethods__["_feedBackAlpha"] = _htfe.LayerDesc__feedBackAlpha_get
    if _newclass:_feedBackAlpha = _swig_property(_htfe.LayerDesc__feedBackAlpha_get, _htfe.LayerDesc__feedBackAlpha_set)
    __swig_setmethods__["_hiddenBiasAlpha"] = _htfe.LayerDesc__hiddenBiasAlpha_set
    __swig_getmethods__["_hiddenBiasAlpha"] = _htfe.LayerDesc__hiddenBiasAlpha_get
    if _newclass:_hiddenBiasAlpha = _swig_property(_htfe.LayerDesc__hiddenBiasAlpha_get, _htfe.LayerDesc__hiddenBiasAlpha_set)
    __swig_setmethods__["_gamma"] = _htfe.LayerDesc__gamma_set
    __swig_getmethods__["_gamma"] = _htfe.LayerDesc__gamma_get
    if _newclass:_gamma = _swig_property(_htfe.LayerDesc__gamma_get, _htfe.LayerDesc__gamma_set)
    __swig_setmethods__["_lateralScalar"] = _htfe.LayerDesc__lateralScalar_set
    __swig_getmethods__["_lateralScalar"] = _htfe.LayerDesc__lateralScalar_get
    if _newclass:_lateralScalar = _swig_property(_htfe.LayerDesc__lateralScalar_get, _htfe.LayerDesc__lateralScalar_set)
    def __init__(self): 
        this = _htfe.new_LayerDesc()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _htfe.delete_LayerDesc
    __del__ = lambda self : None;
LayerDesc_swigregister = _htfe.LayerDesc_swigregister
LayerDesc_swigregister(LayerDesc)

class Layer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Layer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Layer, name)
    __repr__ = _swig_repr
    __swig_setmethods__["_hiddenFeedForwardActivations"] = _htfe.Layer__hiddenFeedForwardActivations_set
    __swig_getmethods__["_hiddenFeedForwardActivations"] = _htfe.Layer__hiddenFeedForwardActivations_get
    if _newclass:_hiddenFeedForwardActivations = _swig_property(_htfe.Layer__hiddenFeedForwardActivations_get, _htfe.Layer__hiddenFeedForwardActivations_set)
    __swig_setmethods__["_hiddenFeedBackActivations"] = _htfe.Layer__hiddenFeedBackActivations_set
    __swig_getmethods__["_hiddenFeedBackActivations"] = _htfe.Layer__hiddenFeedBackActivations_get
    if _newclass:_hiddenFeedBackActivations = _swig_property(_htfe.Layer__hiddenFeedBackActivations_get, _htfe.Layer__hiddenFeedBackActivations_set)
    __swig_setmethods__["_hiddenFeedBackActivationsPrev"] = _htfe.Layer__hiddenFeedBackActivationsPrev_set
    __swig_getmethods__["_hiddenFeedBackActivationsPrev"] = _htfe.Layer__hiddenFeedBackActivationsPrev_get
    if _newclass:_hiddenFeedBackActivationsPrev = _swig_property(_htfe.Layer__hiddenFeedBackActivationsPrev_get, _htfe.Layer__hiddenFeedBackActivationsPrev_set)
    __swig_setmethods__["_hiddenStatesFeedForward"] = _htfe.Layer__hiddenStatesFeedForward_set
    __swig_getmethods__["_hiddenStatesFeedForward"] = _htfe.Layer__hiddenStatesFeedForward_get
    if _newclass:_hiddenStatesFeedForward = _swig_property(_htfe.Layer__hiddenStatesFeedForward_get, _htfe.Layer__hiddenStatesFeedForward_set)
    __swig_setmethods__["_hiddenStatesFeedForwardPrev"] = _htfe.Layer__hiddenStatesFeedForwardPrev_set
    __swig_getmethods__["_hiddenStatesFeedForwardPrev"] = _htfe.Layer__hiddenStatesFeedForwardPrev_get
    if _newclass:_hiddenStatesFeedForwardPrev = _swig_property(_htfe.Layer__hiddenStatesFeedForwardPrev_get, _htfe.Layer__hiddenStatesFeedForwardPrev_set)
    __swig_setmethods__["_hiddenStatesFeedBack"] = _htfe.Layer__hiddenStatesFeedBack_set
    __swig_getmethods__["_hiddenStatesFeedBack"] = _htfe.Layer__hiddenStatesFeedBack_get
    if _newclass:_hiddenStatesFeedBack = _swig_property(_htfe.Layer__hiddenStatesFeedBack_get, _htfe.Layer__hiddenStatesFeedBack_set)
    __swig_setmethods__["_hiddenStatesFeedBackPrev"] = _htfe.Layer__hiddenStatesFeedBackPrev_set
    __swig_getmethods__["_hiddenStatesFeedBackPrev"] = _htfe.Layer__hiddenStatesFeedBackPrev_get
    if _newclass:_hiddenStatesFeedBackPrev = _swig_property(_htfe.Layer__hiddenStatesFeedBackPrev_get, _htfe.Layer__hiddenStatesFeedBackPrev_set)
    __swig_setmethods__["_hiddenStatesFeedBackPrevPrev"] = _htfe.Layer__hiddenStatesFeedBackPrevPrev_set
    __swig_getmethods__["_hiddenStatesFeedBackPrevPrev"] = _htfe.Layer__hiddenStatesFeedBackPrevPrev_get
    if _newclass:_hiddenStatesFeedBackPrevPrev = _swig_property(_htfe.Layer__hiddenStatesFeedBackPrevPrev_get, _htfe.Layer__hiddenStatesFeedBackPrevPrev_set)
    __swig_setmethods__["_feedForwardWeights"] = _htfe.Layer__feedForwardWeights_set
    __swig_getmethods__["_feedForwardWeights"] = _htfe.Layer__feedForwardWeights_get
    if _newclass:_feedForwardWeights = _swig_property(_htfe.Layer__feedForwardWeights_get, _htfe.Layer__feedForwardWeights_set)
    __swig_setmethods__["_feedForwardWeightsPrev"] = _htfe.Layer__feedForwardWeightsPrev_set
    __swig_getmethods__["_feedForwardWeightsPrev"] = _htfe.Layer__feedForwardWeightsPrev_get
    if _newclass:_feedForwardWeightsPrev = _swig_property(_htfe.Layer__feedForwardWeightsPrev_get, _htfe.Layer__feedForwardWeightsPrev_set)
    __swig_setmethods__["_reconstructionWeights"] = _htfe.Layer__reconstructionWeights_set
    __swig_getmethods__["_reconstructionWeights"] = _htfe.Layer__reconstructionWeights_get
    if _newclass:_reconstructionWeights = _swig_property(_htfe.Layer__reconstructionWeights_get, _htfe.Layer__reconstructionWeights_set)
    __swig_setmethods__["_reconstructionWeightsPrev"] = _htfe.Layer__reconstructionWeightsPrev_set
    __swig_getmethods__["_reconstructionWeightsPrev"] = _htfe.Layer__reconstructionWeightsPrev_get
    if _newclass:_reconstructionWeightsPrev = _swig_property(_htfe.Layer__reconstructionWeightsPrev_get, _htfe.Layer__reconstructionWeightsPrev_set)
    __swig_setmethods__["_visibleBiases"] = _htfe.Layer__visibleBiases_set
    __swig_getmethods__["_visibleBiases"] = _htfe.Layer__visibleBiases_get
    if _newclass:_visibleBiases = _swig_property(_htfe.Layer__visibleBiases_get, _htfe.Layer__visibleBiases_set)
    __swig_setmethods__["_visibleBiasesPrev"] = _htfe.Layer__visibleBiasesPrev_set
    __swig_getmethods__["_visibleBiasesPrev"] = _htfe.Layer__visibleBiasesPrev_get
    if _newclass:_visibleBiasesPrev = _swig_property(_htfe.Layer__visibleBiasesPrev_get, _htfe.Layer__visibleBiasesPrev_set)
    __swig_setmethods__["_hiddenBiases"] = _htfe.Layer__hiddenBiases_set
    __swig_getmethods__["_hiddenBiases"] = _htfe.Layer__hiddenBiases_get
    if _newclass:_hiddenBiases = _swig_property(_htfe.Layer__hiddenBiases_get, _htfe.Layer__hiddenBiases_set)
    __swig_setmethods__["_hiddenBiasesPrev"] = _htfe.Layer__hiddenBiasesPrev_set
    __swig_getmethods__["_hiddenBiasesPrev"] = _htfe.Layer__hiddenBiasesPrev_get
    if _newclass:_hiddenBiasesPrev = _swig_property(_htfe.Layer__hiddenBiasesPrev_get, _htfe.Layer__hiddenBiasesPrev_set)
    __swig_setmethods__["_lateralWeights"] = _htfe.Layer__lateralWeights_set
    __swig_getmethods__["_lateralWeights"] = _htfe.Layer__lateralWeights_get
    if _newclass:_lateralWeights = _swig_property(_htfe.Layer__lateralWeights_get, _htfe.Layer__lateralWeights_set)
    __swig_setmethods__["_lateralWeightsPrev"] = _htfe.Layer__lateralWeightsPrev_set
    __swig_getmethods__["_lateralWeightsPrev"] = _htfe.Layer__lateralWeightsPrev_get
    if _newclass:_lateralWeightsPrev = _swig_property(_htfe.Layer__lateralWeightsPrev_get, _htfe.Layer__lateralWeightsPrev_set)
    __swig_setmethods__["_feedBackWeights"] = _htfe.Layer__feedBackWeights_set
    __swig_getmethods__["_feedBackWeights"] = _htfe.Layer__feedBackWeights_get
    if _newclass:_feedBackWeights = _swig_property(_htfe.Layer__feedBackWeights_get, _htfe.Layer__feedBackWeights_set)
    __swig_setmethods__["_feedBackWeightsPrev"] = _htfe.Layer__feedBackWeightsPrev_set
    __swig_getmethods__["_feedBackWeightsPrev"] = _htfe.Layer__feedBackWeightsPrev_get
    if _newclass:_feedBackWeightsPrev = _swig_property(_htfe.Layer__feedBackWeightsPrev_get, _htfe.Layer__feedBackWeightsPrev_set)
    __swig_setmethods__["_visibleReconstruction"] = _htfe.Layer__visibleReconstruction_set
    __swig_getmethods__["_visibleReconstruction"] = _htfe.Layer__visibleReconstruction_get
    if _newclass:_visibleReconstruction = _swig_property(_htfe.Layer__visibleReconstruction_get, _htfe.Layer__visibleReconstruction_set)
    __swig_setmethods__["_visibleReconstructionPrev"] = _htfe.Layer__visibleReconstructionPrev_set
    __swig_getmethods__["_visibleReconstructionPrev"] = _htfe.Layer__visibleReconstructionPrev_get
    if _newclass:_visibleReconstructionPrev = _swig_property(_htfe.Layer__visibleReconstructionPrev_get, _htfe.Layer__visibleReconstructionPrev_set)
    def __init__(self): 
        this = _htfe.new_Layer()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _htfe.delete_Layer
    __del__ = lambda self : None;
Layer_swigregister = _htfe.Layer_swigregister
Layer_swigregister(Layer)

class HTFE(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HTFE, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HTFE, name)
    __repr__ = _swig_repr
    def createRandom(self, *args): return _htfe.HTFE_createRandom(self, *args)
    def activate(self, *args): return _htfe.HTFE_activate(self, *args)
    def learn(self, *args): return _htfe.HTFE_learn(self, *args)
    def stepEnd(self): return _htfe.HTFE_stepEnd(self)
    def getInputWidth(self): return _htfe.HTFE_getInputWidth(self)
    def getInputHeight(self): return _htfe.HTFE_getInputHeight(self)
    def getLayerDescs(self): return _htfe.HTFE_getLayerDescs(self)
    def setInput(self, *args): return _htfe.HTFE_setInput(self, *args)
    def getPrediction(self, *args): return _htfe.HTFE_getPrediction(self, *args)
    def clearMemory(self, *args): return _htfe.HTFE_clearMemory(self, *args)
    def __init__(self): 
        this = _htfe.new_HTFE()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _htfe.delete_HTFE
    __del__ = lambda self : None;
HTFE_swigregister = _htfe.HTFE_swigregister
HTFE_swigregister(HTFE)

SYS_ALLOW_CL_GL_CONTEXT = _htfe.SYS_ALLOW_CL_GL_CONTEXT
_cpu = _htfe._cpu
_gpu = _htfe._gpu
_all = _htfe._all
_none = _htfe._none
class ComputeSystem(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ComputeSystem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ComputeSystem, name)
    __repr__ = _swig_repr
    def create(self, *args): return _htfe.ComputeSystem_create(self, *args)
    def getPlatform(self): return _htfe.ComputeSystem_getPlatform(self)
    def getDevice(self): return _htfe.ComputeSystem_getDevice(self)
    def getContext(self): return _htfe.ComputeSystem_getContext(self)
    def getQueue(self): return _htfe.ComputeSystem_getQueue(self)
    def __init__(self): 
        this = _htfe.new_ComputeSystem()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _htfe.delete_ComputeSystem
    __del__ = lambda self : None;
ComputeSystem_swigregister = _htfe.ComputeSystem_swigregister
ComputeSystem_swigregister(ComputeSystem)

class ComputeProgram(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ComputeProgram, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ComputeProgram, name)
    __repr__ = _swig_repr
    def loadFromFile(self, *args): return _htfe.ComputeProgram_loadFromFile(self, *args)
    def getProgram(self): return _htfe.ComputeProgram_getProgram(self)
    def __init__(self): 
        this = _htfe.new_ComputeProgram()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _htfe.delete_ComputeProgram
    __del__ = lambda self : None;
ComputeProgram_swigregister = _htfe.ComputeProgram_swigregister
ComputeProgram_swigregister(ComputeProgram)

# This file is compatible with both classic and new-style classes.



import os, sys
import typing
import scipy.io
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, KBinsDiscretizer
from sklearn.impute import SimpleImputer
from collections import OrderedDict
from typing import cast, Any, Dict, List, Union, Sequence, Optional, Tuple
from d3m import container, utils
from d3m.metadata import base as metadata_base
from d3m.metadata import hyperparams
from d3m.metadata import params
from d3m.primitive_interfaces.supervised_learning import SupervisedLearnerPrimitiveBase
from d3m.primitive_interfaces import base
from d3m.primitive_interfaces.base import CallResult
import rpi_d3m_primitives_part2
from rpi_d3m_primitives_part2.structuredClassifier.structured_Classify_model import Model
from sklearn.impute import SimpleImputer
from rpi_d3m_primitives_part2.featSelect.RelationSet import RelationSet


Inputs = container.DataFrame
Outputs = container.DataFrame

__all__ = ('StructuredClassifier',)

class Params(params.Params):
    n_bins_: Optional[int]
    strategy_: Optional[str]
    cate_flag_: Optional[Union[np.ndarray, List[np.ndarray]]]
    origin_inputs_: Optional[pd.DataFrame] # potential problem of using 'pd.DataFrame'
    origin_outputs_: Optional[pd.DataFrame] # potential problem of using 'pd.DataFrame'
    train_data_: Optional[Union[np.ndarray, List[np.ndarray]]]
    train_label_: Optional[Union[np.ndarray, List[np.ndarray]]]
    target_columns_metadata_: Optional[List[OrderedDict]]

    
class Hyperparams(hyperparams.Hyperparams):
    nbins = hyperparams.UniformInt(
            lower=2,
            upper=21,
            default=10,
            description = 'The number of bins for discretization.',
            semantic_types = ['https://metadata.datadrivendiscovery.org/types/TuningParameter']
            )
    strategy = hyperparams.Enumeration[str](
            values=['uniform', 'quantile'],
            default='uniform',
            description='The method for KBins Discretizer.',
            semantic_types = ['https://metadata.datadrivendiscovery.org/types/TuningParameter']
            )

class StructuredClassifier(SupervisedLearnerPrimitiveBase[Inputs, Outputs, Params, Hyperparams]):
    """
     A primitive which does structured classification. During training, input to this primitive should be a matrix of tabular numercal/categorical data, and an array of labels. During testing, input is data matrix of numerical features only and output will be the predicted labels with metadata generated.
    """
    # __git_commit__ = utils.current_git_commit(os.path.dirname(__file__))
    metadata = metadata_base.PrimitiveMetadata({
        'id': '006b3f97-fc82-4f1f-998d-4c931bdf2357',
        'version': rpi_d3m_primitives_part2.__coreversion__,
        'name': 'Structured Classifier',
        'keywords': ['Structure Learning','Bayesian Inference','Classification'],
        'description': 'This algorithm is an implementation of Structure Classifier. Which use indepedence test based method to perform structure learning, use MLE to perform parameter learning and predict the target using Bayesian Network inference.',
        'source': {
            'name': rpi_d3m_primitives_part2.__author__,
            'contact': 'mailto:yinn2@rpi.edu',
            'uris': [
                'https://gitlab.com/N.Yin/rpi-d3m-part2/-/blob/{git_commit}/rpi_d3m_primitives_part2/StructuredClassifier.py'.format(
                    git_commit = __git_commit__),
                # 'https://gitlab.com/N.Yin/rpi-d3m-part2/-/blob/master/rpi_d3m_primitives_part2/StructuredClassifier.py',
                'https://gitlab.com/N.Yin/rpi-d3m-part2.git'
                ]
        },
        'installation':[{
            'type' : metadata_base.PrimitiveInstallationType.UBUNTU,
            'package': 'openjdk-8-jdk-headless',
            'version': '8u252-b09-1~18.04'

        }, 
        # {
        #     'type': metadata_base.PrimitiveInstallationType.PIP,
        #     'package': 'javabridge',
        #     'version': '1.0.19'

        # }, 
        # {
        #     'type': metadata_base.PrimitiveInstallationType.PIP,
        #     'package_uri':'git+https://github.com/bd2kccd/py-causal.git@{git_commit}#egg={egg}'.format(
        #         git_commit='6201db7d21aa453a8b66bf632db930417209a430', egg='pycausal')

        # }, 
        {
            'type': metadata_base.PrimitiveInstallationType.PIP,
            # 'package_uri':'git+https://gitlab.com/N.Yin/rpi-d3m-part2.git@{git_commit}#egg={egg}'.format(
            #     git_commit=__git_commit__, egg='rpi_d3m_primitives_part2')
            'package': 'rpi_d3m_primitives_part2',
            'version': rpi_d3m_primitives_part2.__version__
        }],
        'python_path': 'd3m.primitives.classification.structured.RPI',
        'algorithm_types': [
            metadata_base.PrimitiveAlgorithmType.MULTICLASS_CLASSIFICATION],
        'primitive_family': metadata_base.PrimitiveFamily.CLASSIFICATION
    })


    def __init__(self, *, hyperparams: Hyperparams, random_seed: int = 0, docker_containers: typing.Union[typing.Dict[str, base.DockerContainer]] = None) -> None:
        super().__init__(hyperparams=hyperparams, random_seed=random_seed, docker_containers=docker_containers)
        # parameters
        self._index = None
        self._fitted = False
        # hyperparameters
        self._nbins = self.hyperparams['nbins']
        self._strategy = self.hyperparams['strategy']
        # Other parameters
        self._training_inputs = None
        self._training_outputs = None
        self._origin_inputs = None #for label encoder
        self._origin_outputs = None # for label encoder
        self._cate_flag = None
        self._clf = Model(java_max_heap_size = '500M', depth = -1, alpha = 0.05, verbose = False) #classifier
        self._LEoutput = LabelEncoder() #label encoder
        self._Imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent') #imputer
        self._Kbins = KBinsDiscretizer(n_bins=self._nbins, encode='ordinal', strategy=self._strategy) #KbinsDiscretizer
        self._discTrainset = None
        self._target_columns_metadata = None
        
    
    def _store_target_columns_metadata(self, outputs: Outputs) -> None:
        outputs_length = outputs.metadata.query((metadata_base.ALL_ELEMENTS,))['dimension']['length']

        target_columns_metadata: List[Dict] = []

        for column_index in range(outputs_length):
            column_metadata = OrderedDict(outputs.metadata.query_column(column_index))

            # Update semantic types and prepare it for predicted targets.
            semantic_types = list(column_metadata.get('semantic_types', []))
            if 'https://metadata.datadrivendiscovery.org/types/PredictedTarget' not in semantic_types:
                semantic_types.append('https://metadata.datadrivendiscovery.org/types/PredictedTarget')
            semantic_types = [semantic_type for semantic_type in semantic_types if semantic_type != 'https://metadata.datadrivendiscovery.org/types/TrueTarget']
            column_metadata['semantic_types'] = semantic_types

            target_columns_metadata.append(column_metadata)
            
        self._target_columns_metadata = target_columns_metadata
        

    def set_training_data(self, *, inputs: Inputs, outputs: Outputs) -> None:

        ## Update semantic types and prepare it for predicted targets
        self._store_target_columns_metadata(outputs)
        
        ## memory original training inputs
        self._origin_inputs = inputs
        self._origin_outputs = outputs

        ## set training labels
        metadata = outputs.metadata
        column_metadata = metadata.query((metadata_base.ALL_ELEMENTS, 0))
        semantic_types = column_metadata.get('semantic_types', [])
        if 'https://metadata.datadrivendiscovery.org/types/CategoricalData' in semantic_types or 'http://schema.org/Integer' in semantic_types:
            self._LEoutput.fit(outputs)
            self._training_outputs = self._LEoutput.transform(outputs) #starting from zero
        
        
        ## convert categorical values to numerical values in training data
        metadata = inputs.metadata
        [m,n] = inputs.shape
        self._training_inputs = np.zeros((m,n))
        self._cate_flag = np.zeros((n,))
        for column_index in metadata.get_elements((metadata_base.ALL_ELEMENTS,)):
            if column_index is metadata_base.ALL_ELEMENTS: 
                continue
            column_metadata = metadata.query((metadata_base.ALL_ELEMENTS, column_index))
            semantic_types = list(column_metadata.get('semantic_types', []))
            if 'https://metadata.datadrivendiscovery.org/types/Attribute' in semantic_types and len(semantic_types) == 1:
                semantic_types.append('https://metadata.datadrivendiscovery.org/types/CategoricalData')
            if 'https://metadata.datadrivendiscovery.org/types/CategoricalData' in semantic_types:
                LE = LabelEncoder()
                LE = LE.fit(inputs.iloc[:,column_index])
                self._training_inputs[:,column_index] = LE.transform(inputs.iloc[:,column_index])
                self._cate_flag[column_index] = 1
            elif 'http://schema.org/Text' in semantic_types:
                pass
            else:
                temp = list(inputs.iloc[:, column_index].values)
                for i in np.arange(len(temp)):
                    if bool(temp[i]):
                        self._training_inputs[i,column_index] = float(temp[i])
                    else:
                        self._training_inputs[i,column_index] = float('nan')
                # imputer will remove the column with purely missing values
                if not np.count_nonzero(np.isnan(self._training_inputs[:, column_index])) == 0:  # if there is missing values
                    if np.count_nonzero(np.isnan(self._training_inputs[:, column_index])) == m:  # all missing
                        self._training_inputs[:, column_index] = np.zeros(m, )  # replace with all zeros

        self._fitted = False
    

    def fit(self, *, timeout: float = None, iterations: int = None) -> None:
        # if self._fitted:
        #     return CallResult(None)

        if self._training_inputs.any() == None or self._training_outputs.any() == None: 
            raise ValueError('Missing training data, or missing values exist.')

        # ## impute missing values
        # self._Imputer.fit(self._training_inputs)
        # self._training_inputs = self._Imputer.transform(self._training_inputs)

        # ## discretize non-categorical values
        # disc_training_inputs = self._training_inputs
        # if not len(np.where(self._cate_flag == 0)[0]) == 0:
        #     self._Kbins.fit(self._training_inputs[:, np.where(self._cate_flag == 0)[0]]) #find non-categorical values
        #     temp = self._Kbins.transform(self._training_inputs[:, np.where(self._cate_flag == 0)[0]])
        #     disc_training_inputs[:, np.where(self._cate_flag == 0)[0]] = temp
        # # starting from zero

        # ## get number of states for each feature and remove features with only one state
        # discTrainset = RelationSet(disc_training_inputs, self._training_outputs.reshape(-1,1))
        # discTrainset.getStateNo(self._cate_flag, self._nbins)
        # discTrainset.remove()
        # X_train = discTrainset.data
        # Y_train = discTrainset.labels
        
        # self._discTrainset = discTrainset
        # stateNo = np.append(discTrainset.NUM_STATES, len(np.unique(Y_train)))

        # ## fit the classifier
        # self._clf.fit(X_train, Y_train, stateNo)
        self._fitted = True

        return CallResult(None)


    def produce(self, *, inputs: Inputs, timeout: float = None, iterations: int = None) -> base.CallResult[Outputs]:  # inputs: m x n numpy array
        if self._fitted:

            # put a placehold of training and inputs data so that it does not change
            training_inputs = self._training_inputs
            training_outputs = self._training_outputs

            # Data processing the test data: convert categorical values to numerical values in testing data
            metadata = inputs.metadata
            [m, n] = inputs.shape
            X_test = np.zeros((m, n))
            for column_index in metadata.get_elements((metadata_base.ALL_ELEMENTS,)):
                if column_index is metadata_base.ALL_ELEMENTS:
                    continue
                column_metadata = metadata.query((metadata_base.ALL_ELEMENTS, column_index))
                semantic_types = list(column_metadata.get('semantic_types', []))
                if 'https://metadata.datadrivendiscovery.org/types/Attribute' in semantic_types and len(semantic_types) == 1:
                    semantic_types.append('https://metadata.datadrivendiscovery.org/types/CategoricalData')
                if 'https://metadata.datadrivendiscovery.org/types/CategoricalData' in semantic_types:
                    LE = LabelEncoder()
                    LE = LE.fit(self._origin_inputs.iloc[:, column_index]) #use training data to fit
                    # print(column_index)
                    X_test[:, column_index] = LE.transform(inputs.iloc[:, column_index])
                elif 'http://schema.org/Text' in semantic_types:
                    pass
                else:
                    temp = list(inputs.iloc[:, column_index].values)
                    for i in np.arange(len(temp)):
                        if bool(temp[i]):
                            X_test[i, column_index] = float(temp[i])
                        else:
                            X_test[i, column_index] = float('nan')

            ## impute missing values
            self._Imputer.fit(training_inputs)
            training_inputs = self._Imputer.transform(training_inputs)

            ## discretize non-categorical values
            disc_training_inputs = training_inputs
            if not len(np.where(self._cate_flag == 0)[0]) == 0:
                self._Kbins.fit(training_inputs[:, np.where(self._cate_flag == 0)[0]]) #find non-categorical values
                temp = self._Kbins.transform(training_inputs[:, np.where(self._cate_flag == 0)[0]])
                disc_training_inputs[:, np.where(self._cate_flag == 0)[0]] = temp
            # starting from zero

            ## get number of states for each feature and remove features with only one state
            discTrainset = RelationSet(disc_training_inputs, training_outputs.reshape(-1,1))
            discTrainset.getStateNo(self._cate_flag, self._nbins)
            discTrainset.remove()
            X_train = discTrainset.data
            Y_train = discTrainset.labels
            
            self._discTrainset = discTrainset
            stateNo = np.append(discTrainset.NUM_STATES, len(np.unique(Y_train)))

            ## fit the classifier
            self._clf.fit(X_train, Y_train)

            ## impute testing data
            X_test = self._Imputer.transform(X_test)

            ## Kbins discretize for noncategorical values
            disc_X_test = X_test
            if not len(np.where(self._cate_flag == 0)[0]) == 0:
                temp = self._Kbins.transform(X_test[:, np.where(self._cate_flag == 0)[0]])
                disc_X_test[:,np.where(self._cate_flag == 0)[0]] = temp

            ## remove columns with one states
            index_list = np.setdiff1d(np.arange(self._discTrainset.num_features), np.array(self._discTrainset.removeIdx))
            disc_X_test = disc_X_test[:, index_list]

            ## prediction
            output = self._clf.predict(disc_X_test)

            ## label decode
            self._LEoutput.fit(self._origin_outputs)
            output = self._LEoutput.inverse_transform(output.reshape((-1,)).astype('int64'))
            
            ## update metadata
            output = container.DataFrame(output, generate_metadata=False, source=self)
            output.metadata = inputs.metadata.clear(source=self, for_value=output, generate_metadata=True)
            
            for column_index, column_metadata in enumerate(self._target_columns_metadata):
                output.metadata = output.metadata.update_column(column_index, column_metadata, source=self)


            return CallResult(output)
        else:
            raise ValueError('Model should be fitted first.')


    def get_params(self)  -> Params:
        if not self._fitted:
            raise ValueError("Fit not performed.")
        return Params(n_bins_ = self._nbins,
                      strategy_ = self._strategy,
                      cate_flag_ = self._cate_flag,
                      origin_inputs_ = self._origin_inputs,
                      origin_outputs_ = self._origin_outputs,
                      train_data_ = self._training_inputs,
                      train_label_ = self._training_outputs,
                      target_columns_metadata_ = self._target_columns_metadata
        )


    def set_params(self, *, params: Params) -> None:
        self._fitted = True
        self._nbins = params['n_bins_']
        self._strategy = params['strategy_']
        self._cate_flag = params['cate_flag_']
        self._origin_inputs = params['origin_inputs_']
        self._origin_outputs = params['origin_outputs_']
        self._training_inputs = params['train_data_']
        self._training_outputs = params['train_label_']
        self._target_columns_metadata = params['target_columns_metadata_']

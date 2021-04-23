import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from sklearn.pipeline import Pipeline
from sklearn.model_selection import ShuffleSplit, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
sns.set(style="darkgrid")
sns.set(font_scale=1.3)
import time

#####################
# Grid Search Utils #
#####################

def build_y(data, label):
    """Return required data labels"""
    return label * np.ones(len(data))


def prepare_Data(data, patient = 'patient1', mode=['pre', 'Raw'], is_train = True):
    """
    Returns the desired training/test data and labels.

    Parameters
    ----------
    data : dict 
    patient : str [default "patient1"]
    mode : list = ["pre" o "post", type of data], [deafult ['pre', 'Raw']]
    """

    # Training set
    if is_train:
      X = np.concatenate([
                          data['patient1']['pre']['train']['Dx'+mode[1]], 
                          data['patient1']['post']['train']['Sx'+mode[1]],
                          data['patient2']['pre']['train']['Dx'+mode[1]], 
                          data['patient2']['post']['train']['Sx'+mode[1]],
                          data['patient3']['pre']['train']['Dx'+mode[1]], 
                          data['patient3']['post']['train']['Sx'+mode[1]],
                          ]
                         )
      y= np.concatenate([ build_y(data['patient1']['pre']['train']['Dx'+mode[1]], -1), 
                          build_y(data['patient1']['post']['train']['Sx'+mode[1]] , 1),
                          build_y(data['patient2']['pre']['train']['Dx'+mode[1]], -1), 
                          build_y(data['patient2']['post']['train']['Sx'+mode[1]], 1),
                          build_y(data['patient3']['pre']['train']['Dx'+mode[1]], -1), 
                          build_y(data['patient3']['post']['train']['Sx'+mode[1]], 1),
                          ]
                         )
      X.shape, y.shape

    # Test set
    else:
      X = np.concatenate([data[patient][mode[0]]['test']['Dx'+mode[1]], 
                          data[patient][mode[0]]['test']['Sx'+mode[1]]])
      y = np.concatenate([build_y(data[patient][mode[0]]['test']['Dx'+mode[1]], -1),
                          build_y(data[patient][mode[0]]['test']['Sx'+mode[1]], 1)]) 
      X.shape, y.shape 

    return X, y



def customized_GridSearch(clf, csp, parameters_clf, parameters_csp, X_train, y_train):
    """
    Performs a 5-fold cross validation grid search on the specified classifier and vectorizer.
    
    Parameters
    ----------
      clf: classifier to be tested

      paramters_clf: list of values for the classifier hyperparameters

      paramters_csp: list of values for CSP hyperparameters

      X_train, y_train: train set 

    """

    
    # Grid Search pipeline
    pipeline = Pipeline([('csp', csp), ('clf', clf)])

    # Grid Search parameters
    parameters = dict()
    parameters.update(parameters_csp)
    parameters.update(parameters_clf)
    
    # 5-fold Cross Validation Grid Search
    grid_search = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1, verbose=True)
    print("Performing grid search...")
    print("pipeline:", [name for name, _ in pipeline.steps])
    print("parameters:")
    print(parameters)

    t0 = time.time()
    grid_search.fit(X_train, y_train)

    print("done in %0.3fs" % (time.time() - t0))
    print()

    # Best Model Result on CV
    print("Best CV score: %0.3f" % grid_search.best_score_)
    print("Best parameters set:")
    best_parameters = grid_search.best_estimator_.get_params()
    for param_name in sorted(parameters.keys()):
        print("\t%s: %r" % (param_name, best_parameters[param_name]))

    return grid_search 


##########################
# Model Comparison Utils #
##########################

def best_model_on_TestSet(grid_search, X_test, y_test):
    """
    Return the best model parameters and score on test set.
    """

    # Best Model Result on Test set
    score = grid_search.best_estimator_.score(X_test, y_test)

    print("Test score with best_estimator_: %0.3f" % score)
    print("\n")
    print("Classification Report Test Data")
    print(classification_report(y_test, grid_search.best_estimator_.predict(X_test)))
    
    best_parameters = grid_search.best_estimator_.get_params()

    return best_parameters, score


def confidence_interval(acc, n, conf = .95):
  """
  Returns the extremes of the confidence interval given the desired confidence ('conf'),
  the model accuracy ('acc'), and the number of samples ('n').

  Parameters
  ----------
      acc [double]: model accuracy
      n [int]: number of samples
      conf [float, default 0.95]: confidence
  """

  alpha = 1 - conf 
  z = np.absolute(st.norm.ppf(alpha/2)) # Two tails

  sqrt =(z**2 + 4*n*acc - 4*n*acc**2)**.5
  rho_max = (2*n*acc + z**2 + z*sqrt) / (2*(n + z**2))
  rho_min = (2*n*acc + z**2 - z*sqrt) / (2*(n + z**2))

  return [rho_min, rho_max]

def plot_models_acc(patient1, patient2, patient3, N, alpha =.95, title = 'CSP + MLP'):
    """Plot the model accuracy on each patients."""
    
    for patient, name, color in zip([patient1, patient2, patient3],['P1','P2', 'P3'],['blue', 'orange','green']):
      # Get confidence interval
      models_CI = []
      for acc in patient.values():
        models_CI.append(confidence_interval(acc, N, conf=alpha))

      # Plot
      plt.figure(figsize=(10,6))
      err= [x-y[0] for x,y in zip(patient.values(), models_CI)]
      ticks = range(len(patient))
      plt.errorbar(ticks, patient.values(), yerr=err, fmt='o', c='green')
      plt.ylabel('Accuracy', color = 'black')
      plt.title(title + ' - ' + name, color = 'black')
      plt.yticks(color = 'black')
      plt.xticks(ticks, patient.keys(), rotation = 50, color = 'black')
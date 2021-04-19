
# TODO LIST

* README
* Clean and comment code
* Upload data matrices
* Upload images (?)
* Andare a mangiare una pizza tutti insieme finito il COVID (sigh!)


# Stroke Rehab - Spring School 2021

This work has been done during the g-tec Spring School 2021.

## Objective

We had to analyze a motor imagery BCI data-set from a chronic stroke patient in order to optimize pre-processing.
The dataset included three patients and the datas were collected before and after an intervention in order to evaluate the improvement.


## Workflow

The followed steps included:

* **DataSet choice**: we conducted the evaluation both on a dataset with single patient and a dataset with all the patients together in order to obtain a generic result.
* **Epoch choice**: we took different epochs between 2s, 6s and 8s.
* **Preprocessing**: a bandpass filtering was applied between 8Hz and 30Hz, but we also kept the raw signal.
* **Feature extraction**: we used CSP (Common Spatial Filter) in order to extract the features.
* **Classification**: a Grid Search was conducted with a 5-fold Cross Validation in order to obtain the best classification.

###

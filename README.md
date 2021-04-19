
# TODO LIST

* README
* Clean and comment code
* Upload data matrices
* Upload images (?)
* Andare a mangiare una pizza tutti insieme finito il COVID (sigh!)


# Stroke Rehab - Spring School 2021

This work has been done during the g-tec Spring School 2021.

## Objective

We had to analyze a motor imagery BCI data-set from a chronic stroke patient to optimize pre-processing. The dataset included three patients and the data were collected before and after intervention in order to evaluate the improvement.

![alt text](https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021/blob/main/img/timing.png?raw=true)

## Workflow

The followed steps included:

* **DataSet choice**: we conducted the evaluation both on a dataset with a single patient and a dataset with all the patients together to obtain a generic result.
* **Epoch choice**: we took different epochs between 2s, 6s and 8s.
* **Preprocessing**: a bandpass filtering was applied between 8Hz and 30Hz, but we also kept the raw signal.
* **Feature extraction**: we used CSP (Common Spatial Filter) in order to extract the features.
* **Classification**: a Grid Search was conducted with a 5-fold Cross-Validation to obtain the best classification.

###


# Stroke Rehab - Spring School 2021

This work has been done during the [g-tec Spring School 2021](https://www.gtec.at/spring-school-2021/).

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


### Built With

* [MATLAB](https://mathworks.com/?s_tid=gn_logo)
* [EEGLAB](https://eeglab.org)
* [Python 3.7](https://www.python.org)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

Clone the repo
   ```sh
   git clone https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021.git
   ```

<!-- USAGE EXAMPLES -->
## Usage

### Filtering
The given dataset contains an EEG recording included in the matrix y, a trigger vector (trig) and the sampling frequency. The only filtering already applied to the data is a notch filter at 50Hz, automatically performed during the acquisition.

By using the MATLAB file **Preprocessing_main.m** it is possible to filter the raw data. This is done by applying a two-step pre-processing: first of all, the data is bandpass filtered with an 8th order Butterworth extracting only the alpha and beta rhythms. Secondly, an epoch division is performed. Additionally, the first segment of data without executed tasks is cut since it doesn't contain useful information.
This file outputs filtered and unfiltered epochs divided by right and left, respectively Dx and Sx.

### Feature extraction and classification

In the python file Grid_Search.ipynb

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Lorenzo Migliori - email : []() - [LinkedIn]()

Eleonora Misino - email: eleonora.misino@gmail.com - [LinkedIn](https://www.linkedin.com/in/eleonora-misino/) - [Github](https://github.com/EleMisi)

Caterina Putti  - email :  - [LinkedIn]()

Pietro Sillano - email : pietrosillano@gmail.com - [LinkedIn](https://www.linkedin.com/in/pietro-sillano/)

Beatrice Villata - email : beatrice.villata@edu.unito.it

Project Link: [https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021](https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

<p align="center">
  <a href="https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021">
    <img src="img/logo_gtec.png" alt="Logo" width="180" height="120">
    <img src="img/logo_hpc4ai.png" alt="Logo" width="420" height="120">
    <img src="img/logo_pompei.png" alt="Logo" width="120" height="120">

  </a>

* [https://www.br41n.io/Spring-School-2021#projects](https://www.br41n.io/Spring-School-2021)
* [https://hpc4ai.it/](https://hpc4ai.it/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/MachineLearningJournalClub/Stroke_Rehab_VBH_2021.svg?style=for-the-badge
[contributors-url]: https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MachineLearningJournalClub/Stroke_Rehab_VBH_2021.svg?style=for-the-badge
[forks-url]: https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021/network/members
[stars-shield]: https://img.shields.io/github/stars/MachineLearningJournalClub/Stroke_Rehab_VBH_2021.svg?style=for-the-badge
[stars-url]: https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021/stargazers
[issues-shield]: https://img.shields.io/github/issues/MachineLearningJournalClub/Stroke_Rehab_VBH_2021.svg?style=for-the-badge
[issues-url]: https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021/issues
[license-shield]: https://img.shields.io/github/license/MachineLearningJournalClub/Stroke_Rehab_VBH_2021.svg?style=for-the-badge
[license-url]: https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021/blob/main/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/machine-learning-journal-club

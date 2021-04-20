
# TODO LIST

* README
* Clean and comment code
* Upload data matrices
* Upload images (?)
* Andare a mangiare una pizza tutti insieme finito il COVID (sigh!)

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021">
    <img src="img/logo_mljc.png" alt="Logo" width="120" height="120">
    <img src="img/logo_brain_io.png" alt="Logo" width="120" height="60">
  </a>

  <h3 align="center">Stroke Rehab Data Analysis - Virtual Brain Hackathon 2021</h3>

  <p align="center">
    Assessment of the optimal classifier for different BCI applications for stroke rehab
    <br />
    <a href="https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021">View Demo</a>
    ·
    <a href="https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021">Report Bug</a>
    ·
    <a href="https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

## About the project

We had to analyze a motor imagery BCI data-set from a chronic stroke patient to optimize pre-processing. The dataset included three patients and the data were collected before and after intervention in order to evaluate the improvement.

The followed steps included:

* **DataSet choice**: we conducted the evaluation both on a dataset with a single patient and a dataset with all the patients together to obtain a generic result.
* **Epoch choice**: we took different epochs between 2s, 6s and 8s.
* **Preprocessing**: a bandpass filtering was applied between 8Hz and 30Hz, but we also kept the raw signal.
* **Feature extraction**: we used CSP (Common Spatial Filter) in order to extract the features.
* **Classification**: a Grid Search was conducted with a 5-fold Cross-Validation to obtain the best classification.


### Built With

* []()
* []()
* []()



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/MachineLearningJournalClub/Stroke_Rehab_VBH_2021.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



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

Lorenzo Migliori - email : []() - [linkedin]()

Eleonora Misino - []() :  - [linkedin]()

Caterina Putti  - email :  - [linkedin]()

Pietro Sillano - email :  [pietrosillano@gmail.com](Mail) - [linkedin]()

Beatrice Villata - email : [beatrice.villata@edu.unito.it](beatrice.villata@edu.unito.it)

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
[contributors-shield]: https://img.shields.io/github/contributors/MachineLearningJournalClub/ECoG_VBH_2021.svg?style=for-the-badge
[contributors-url]: https://github.com/MachineLearningJournalClub/ECoG_VBH_2021/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/MachineLearningJournalClub/ECoG_VBH_2021.svg?style=for-the-badge
[forks-url]: https://github.com/MachineLearningJournalClub/ECoG_VBH_2021/network/members
[stars-shield]: https://img.shields.io/github/stars/MachineLearningJournalClub/ECoG_VBH_2021.svg?style=for-the-badge
[stars-url]: https://github.com/MachineLearningJournalClub/ECoG_VBH_2021/stargazers
[issues-shield]: https://img.shields.io/github/issues/MachineLearningJournalClub/ECoG_VBH_2021.svg?style=for-the-badge
[issues-url]: https://github.com/MachineLearningJournalClub/ECoG_VBH_2021/issues
[license-shield]: https://img.shields.io/github/license/MachineLearningJournalClub/ECoG_VBH_2021.svg?style=for-the-badge
[license-url]: https://github.com/MachineLearningJournalClub/ECoG_VBH_2021/blob/main/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/machine-learning-journal-club

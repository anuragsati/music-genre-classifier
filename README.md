[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br>

<p align="center">
  <a href="https://github.com/anuragsati/music-genre-classifier">
    <img src="./preview/logo.svg" width=200 height=200 />
  </a>                      

  <h1 align="center">Music Genre Classifier</h1>
  <p align="center">
	<span>Classify your audio files on the go </span>
    <br />
    <a href="https://github.com/anuragsati/music-genre-classifier"><strong>Explore the Project »</strong></a>
    <br />
    <br />
    <a href="https://github.com/anuragsati/music-genre-classifier">View On Github</a>
    ·
    <a href="https://github.com/anuragsati/music-genre-classifier/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/anuragsati/music-genre-classifier/pulls">Request Feature</a>
  </p>
</p>


<br>
<br>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#project-overview">Project Overview</a></li>
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
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#references">Acknowledgements</a></li>
  </ol>
</details>


<br>
<br>


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- image here -->
[![Product Name Screen Shot][product-screenshot]](https://github.com/anuragsati/music-genre-classifier)

There are many great genre classifiers in the industry but how many of them are free, and reliable, and does the job fast, and are able to actually classify music ? I bet there are very few if not none that fits the criteria.

Some key features to note :
* You can classify any audio with just few clicks in realtime 😃
* You can analyse any audio's waveforms, FFTs etc.
* This app is cross platform so you can run it on any device (except on a rock 🎸)

<br>

### Project Overview 

1. **Classification Genres** : Classify any music into 10 genres.
`pop` `metal` `disco` `blues` `reggae` `classical` `rock` `hiphop` `country` `jazz`

1. **Dataset Used** : Used [GTZAN Dataset](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification) dataset by Andrada Olteanu from Kaggle.

1. **Model Accuracy** : Predict any genre with 72.6% accuracy.


<br>

### Built With

Music genre classifier uses these technologies to run.
* [Python3](https://www.python.org/)
* [Flask](https://palletsprojects.com/p/flask/)
* [Electron.js](https://www.electronjs.org/)
* [Tensorflow](https://www.tensorflow.org/)
* [Librosa](https://librosa.org/doc/latest/index.html#)
* [Matplotlib](https://matplotlib.org/)

<br>


<!-- GETTING STARTED -->
## Getting Started

Getting started with this project is very easy. Follown Prerequisites and installation guidelines.

### Prerequisites

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
1. Download [Processed GTZAN DATASET](https://drive.google.com/file/d/1jWMGOAhQU9UODtLpPV-6hL-Fx5KIzY6o/view?usp=sharing). 
1. Paste your downloaded dataset (data.json) to `/assets`

1. Install NPM packages
   ```sh
	npm install
   ```

### Installation

1. Run the backend server using (**Necessary**):
   ```sh
	python3 ./backend/main.py
   ```
1. Run the project using : 
   ```sh
	npm run start
   ```
<!-- 1. To Build the project into an executable binary run : 
	```sh
	npm run build 
	``` -->

<!-- LICENSE -->
## License
Distributed under the MIT License.


<br>

<!-- CONTACT -->
## Contact
Anurag sati - anuragsati7@gmail.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)


<br>

<!-- references -->
## References
* [Audio Data Analysis](https://www.kdnuggets.com/2020/02/audio-data-analysis-deep-learning-python-part-1.html)
* [Audio signal processing](https://www.youtube.com/watch?v=iCwMQJnKk2c&list=PL-wATfeyAMNqIee7cH3q1bh4QJFAaeNv0)
* [Deep Learning for audio](https://www.youtube.com/watch?v=fMqL5vckiU0&list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf)
* [Guide To The Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)
* [Max Pooling](https://computersciencewiki.org/index.php/Max-pooling_/_Pooling#:~:text=Max%20pooling%20is%20a%20sample,in%20the%20sub%2Dregions%20binned.)
* [Batch Normalization](https://machinelearningmastery.com/batch-normalization-for-training-of-deep-neural-networks/)
* [Sparse_categorial_crossentropy](https://en.wikipedia.org/wiki/Cross_entropy)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/anuragsati/music-genre-classifier.svg?style=for-the-badge
[contributors-url]: https://github.com/anuragsati/music-genre-classifier/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/anuragsati/music-genre-classifier.svg?style=for-the-badge
[forks-url]: https://github.com/anuragsati/music-genre-classifier/network/members
[stars-shield]: https://img.shields.io/github/stars/anuragsati/music-genre-classifier.svg?style=for-the-badge
[stars-url]: https://github.com/anuragsati/music-genre-classifier/stargazers
[issues-shield]: https://img.shields.io/github/issues/anuragsati/music-genre-classifier.svg?style=for-the-badge
[issues-url]: https://github.com/anuragsati/music-genre-classifier/issuess
[license-shield]: https://img.shields.io/github/license/anuragsati/music-genre-classifier.svg?style=for-the-badge
[license-url]: https://github.com/anuragsati/music-genre-classifier/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew


[product-screenshot]: ./preview/preview.png

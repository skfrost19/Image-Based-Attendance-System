<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>IMAGE-BASED-ATTENDANCE-SYSTEM</h1>
<h3>◦ Developed with the software and tools below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat-square&logo=tqdm&logoColor=black" alt="tqdm" />
<img src="https://img.shields.io/badge/TensorFlow-FF6F00.svg?style=flat-square&logo=TensorFlow&logoColor=white" alt="TensorFlow" />
<img src="https://img.shields.io/badge/Keras-D00000.svg?style=flat-square&logo=Keras&logoColor=white" alt="Keras" />
<img src="https://img.shields.io/badge/Gunicorn-499848.svg?style=flat-square&logo=Gunicorn&logoColor=white" alt="Gunicorn" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python" />

<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat-square&logo=pandas&logoColor=white" alt="pandas" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat-square&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/Dlib-008000.svg?style=flat-square&logo=Dlib&logoColor=white" alt="Dlib" />
<img src="https://img.shields.io/badge/Flask-000000.svg?style=flat-square&logo=Flask&logoColor=white" alt="Flask" />
</p>
<img src="https://img.shields.io/github/license/skfrost19/Image-Based-Attendance-System?style=flat-square&color=5D6D7E" alt="GitHub license" />
<img src="https://img.shields.io/github/last-commit/skfrost19/Image-Based-Attendance-System?style=flat-square&color=5D6D7E" alt="git-last-commit" />
<img src="https://img.shields.io/github/commit-activity/m/skfrost19/Image-Based-Attendance-System?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/languages/top/skfrost19/Image-Based-Attendance-System?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

---

## 📖 Table of Contents

-   [📖 Table of Contents](#-table-of-contents)
-   [📍 Overview](#-overview)
-   [📦 Features](#-features)
-   [📂 repository Structure](#-repository-structure)
-   [⚙️ Modules](#modules)
-   [🚀 Getting Started](#-getting-started)
    -   [🔧 Installation](#-installation)
    -   [🤖 Running Image-Based-Attendance-System](#-running-Image-Based-Attendance-System)
    -   [🧪 Tests](#-tests)
-   [🛣 Roadmap](#-roadmap)
-   [🤝 Contributing](#-contributing)
-   [📄 License](#-license)
-   [👏 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The Image-Based Attendance System is a modern, efficient, and automated solution to taking attendance. Instead of manually checking off names on a list, this system uses image processing and face recognition technologies to identify individuals and mark their attendance.

The system works by taking a pre-existing image, from which it identifies faces using a face detection algorithm. The detected faces are then compared with the faces in a database using a face recognition algorithm. If a match is found, the system marks attendance for the corresponding individual.

This project aims to streamline the attendance process, reduce human error, and save time. It can be used in various settings, such as schools, colleges, offices, or any place where attendance needs to be taken regularly.

## 📦 Features

► INSERT-TEXT

---

## 📂 Repository Structure

```sh
└── Image-Based-Attendance-System/
    ├── TODO.txt
    ├── attendance/
    ├── changelog
    ├── deepface/
    │   ├── DeepFace.py
    │   ├── basemodels/
    │   │   ├── ArcFace.py
    │   │   ├── DeepID.py
    │   │   ├── DlibResNet.py
    │   │   ├── DlibWrapper.py
    │   │   ├── Facenet.py
    │   │   ├── Facenet512.py
    │   │   ├── FbDeepFace.py
    │   │   ├── OpenFace.py
    │   │   ├── SFace.py
    │   │   ├── VGGFace.py
    │   ├── commons/
    │   │   ├── distance.py
    │   │   ├── functions.py
    │   │   └── realtime.py
    │   ├── detectors/
    │   │   ├── DlibWrapper.py
    │   │   ├── FaceDetector.py
    │   │   ├── MediapipeWrapper.py
    │   │   ├── MtcnnWrapper.py
    │   │   ├── OpenCvWrapper.py
    │   │   ├── RetinaFaceWrapper.py
    │   │   ├── SsdWrapper.py
    │   │   ├── YoloWrapper.py
    │   │   ├── YunetWrapper.py
    │   └── extendedmodels/
    │       ├── Age.py
    │       ├── Emotion.py
    │       ├── Gender.py
    │       ├── Race.py
    ├── images/
    ├── main.py
    ├── records/
    │   └── MRH/
    ├── requirements.txt
    ├── retinaface/
    │   ├── RetinaFace.py
    │   ├── commons/
    │   │   ├── postprocess.py
    │   │   └── preprocess.py
    │   └── model/
    │       └── retinaface_model.py
    ├── setup.py
    ├── src/
    │   ├── components/
    │   │   ├── attendance.py
    │   │   ├── generate.py
    │   │   ├── pipeline.py
    │   │   └── verify.py
    │   ├── exception.py
    │   ├── logger.py
    │   └── utils.py
    └── test/

```

---

## ⚙️ Modules

<details closed><summary>Root</summary>

| File                                                                                                      | Summary       |
| --------------------------------------------------------------------------------------------------------- | ------------- |
| [setup.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/setup.py)                 | ► INSERT-TEXT |
| [changelog](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/changelog)               | ► INSERT-TEXT |
| [requirements.txt](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/requirements.txt) | ► INSERT-TEXT |
| [TODO.txt](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/TODO.txt)                 | ► INSERT-TEXT |
| [main.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/main.py)                   | ► INSERT-TEXT |

</details>

<details closed><summary>Deepface</summary>

| File                                                                                                     | Summary       |
| -------------------------------------------------------------------------------------------------------- | ------------- |
| [DeepFace.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/DeepFace.py) | ► INSERT-TEXT |

</details>

<details closed><summary>Basemodels</summary>

| File                                                                                                                      | Summary       |
| ------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [VGGFace.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/VGGFace.py)         | ► INSERT-TEXT |
| [DlibResNet.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/DlibResNet.py)   | ► INSERT-TEXT |
| [Facenet512.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/Facenet512.py)   | ► INSERT-TEXT |
| [SFace.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/SFace.py)             | ► INSERT-TEXT |
| [FbDeepFace.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/FbDeepFace.py)   | ► INSERT-TEXT |
| [Facenet.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/Facenet.py)         | ► INSERT-TEXT |
| [ArcFace.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/ArcFace.py)         | ► INSERT-TEXT |
| [DlibWrapper.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/DlibWrapper.py) | ► INSERT-TEXT |
| [OpenFace.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/OpenFace.py)       | ► INSERT-TEXT |
| [DeepID.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/basemodels/DeepID.py)           | ► INSERT-TEXT |

</details>

<details closed><summary>Detectors</summary>

| File                                                                                                                                 | Summary       |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| [YoloWrapper.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/detectors/YoloWrapper.py)             | ► INSERT-TEXT |
| [SsdWrapper.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/detectors/SsdWrapper.py)               | ► INSERT-TEXT |
| [MtcnnWrapper.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/detectors/MtcnnWrapper.py)           | ► INSERT-TEXT |
| [YunetWrapper.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/detectors/YunetWrapper.py)           | ► INSERT-TEXT |
| [RetinaFaceWrapper.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/detectors/RetinaFaceWrapper.py) | ► INSERT-TEXT |
| [OpenCvWrapper.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/detectors/OpenCvWrapper.py)         | ► INSERT-TEXT |
| [FaceDetector.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/detectors/FaceDetector.py)           | ► INSERT-TEXT |
| [DlibWrapper.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/detectors/DlibWrapper.py)             | ► INSERT-TEXT |
| [MediapipeWrapper.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/detectors/MediapipeWrapper.py)   | ► INSERT-TEXT |

</details>

<details closed><summary>Commons</summary>

| File                                                                                                                     | Summary       |
| ------------------------------------------------------------------------------------------------------------------------ | ------------- |
| [realtime.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/commons/realtime.py)         | ► INSERT-TEXT |
| [distance.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/commons/distance.py)         | ► INSERT-TEXT |
| [functions.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/commons/functions.py)       | ► INSERT-TEXT |
| [postprocess.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/retinaface/commons/postprocess.py) | ► INSERT-TEXT |
| [preprocess.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/retinaface/commons/preprocess.py)   | ► INSERT-TEXT |

</details>

<details closed><summary>Extendedmodels</summary>

| File                                                                                                                  | Summary       |
| --------------------------------------------------------------------------------------------------------------------- | ------------- |
| [Gender.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/extendedmodels/Gender.py)   | ► INSERT-TEXT |
| [Age.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/extendedmodels/Age.py)         | ► INSERT-TEXT |
| [Race.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/extendedmodels/Race.py)       | ► INSERT-TEXT |
| [Emotion.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/deepface/extendedmodels/Emotion.py) | ► INSERT-TEXT |

</details>

<details closed><summary>Src</summary>

| File                                                                                                  | Summary       |
| ----------------------------------------------------------------------------------------------------- | ------------- |
| [logger.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/src/logger.py)       | ► INSERT-TEXT |
| [utils.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/src/utils.py)         | ► INSERT-TEXT |
| [exception.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/src/exception.py) | ► INSERT-TEXT |

</details>

<details closed><summary>Components</summary>

| File                                                                                                               | Summary       |
| ------------------------------------------------------------------------------------------------------------------ | ------------- |
| [pipeline.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/src/components/pipeline.py)     | ► INSERT-TEXT |
| [verify.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/src/components/verify.py)         | ► INSERT-TEXT |
| [attendance.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/src/components/attendance.py) | ► INSERT-TEXT |
| [generate.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/src/components/generate.py)     | ► INSERT-TEXT |

</details>

<details closed><summary>Retinaface</summary>

| File                                                                                                           | Summary       |
| -------------------------------------------------------------------------------------------------------------- | ------------- |
| [RetinaFace.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/retinaface/RetinaFace.py) | ► INSERT-TEXT |

</details>

<details closed><summary>Model</summary>

| File                                                                                                                             | Summary       |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [retinaface_model.py](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/retinaface/model/retinaface_model.py) | ► INSERT-TEXT |

</details>

---

## 🚀 Getting Started

**_Dependencies_**

Please ensure you have the following dependencies installed on your system:

`- ℹ️ Dependency 1`

`- ℹ️ Dependency 2`

`- ℹ️ ...`

### 🔧 Installation

1. Clone the Image-Based-Attendance-System repository:

```sh
git clone https://github.com/skfrost19/Image-Based-Attendance-System
```

2. Change to the project directory:

```sh
cd Image-Based-Attendance-System
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### 🤖 Running Image-Based-Attendance-System

```sh
python main.py
```

### 🧪 Tests

```sh
pytest
```

---

## 🛣 Project Roadmap

> -   [x] `ℹ️  Task 1: Implement X`
> -   [ ] `ℹ️  Task 2: Implement Y`
> -   [ ] `ℹ️ ...`

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

-   **[Submit Pull Requests](https://github.com/skfrost19/Image-Based-Attendance-System/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
-   **[Join the Discussions](https://github.com/skfrost19/Image-Based-Attendance-System/discussions)**: Share your insights, provide feedback, or ask questions.
-   **[Report Issues](https://github.com/skfrost19/Image-Based-Attendance-System/issues)**: Submit bugs found or log feature requests for SKFROST19.

#### _Contributing Guidelines_

<details closed>
<summary>Click to expand</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
    ```sh
    git clone <your-forked-repo-url>
    ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
    ```sh
    git checkout -b new-feature-x
    ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
    ```sh
    git commit -m 'Implemented new feature x.'
    ```
6. **Push to GitHub**: Push the changes to your forked repository.
    ```sh
    git push origin new-feature-x
    ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

## 📄 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 👏 Acknowledgments

-   List any resources, contributors, inspiration, etc. here.

[**Return**](#Top)

---

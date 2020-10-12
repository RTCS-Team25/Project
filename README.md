# Project

xxx Project Document

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/RTCS-Team25/Project?style=for-the-badge) ![GitHub issues](https://img.shields.io/github/issues-raw/RTCS-Team25/Project?style=for-the-badge) ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/RTCS-Team25/Project?color=red&style=for-the-badge)

## Description

This project is a **mental health robot**, which draws on **the speech recognition capabilities** of Pepper alongside further research we undertook as to how interacting with robots can actually boost people’s mood. This project therefore is to create a spoken interaction between Pepper and a user. Pepper will be able to respond based on the user’s replies. If the user is not feeling happy, or gives sad answers to Pepper’s pre-set questions, then Pepper will be able to give advice and guide the user through some calming, meditative processes to boost the user’s mood.

## Aims

1. Allow Pepper to recognize a variety of phrases which the user may use in order to prompt an appropriate response.
2. Create a library of responses to allow Pepper to maintain a ‘conversation’ with the user.
3. (Advanced) Use both the speech function as well as the tablet screen to take the user through a guided meditation or provide a happy distraction in the form of pictures, symbols or animations.

## Environment

| Item          | Version                                                      |
| ------------- | ------------------------------------------------------------ |
| Pepper System | [NAOqi 2.5](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/getting-started) |
| Programming Language      | Python 2.7                                                   |
| NAOqi SDK     | [Python 2.7](https://developer.softbankrobotics.com/pepper-naoqi-25-downloads-linux) |

## References

- [NAOqi OS](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/other-tutorials/working-naoqi/naoqi-os): the operating system of the robot, an embedded GNU/Linux distribution based on Gentoo.
- [NAOqi](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/other-tutorials/working-naoqi/naoqi): main software running on the robot.
- [NAOqi Framework Key Concepts](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/former-naoqi-framework/key-concepts): the programming framework used to program Aldebaran robots.
- qi Framework (do not know what this is 😅)
  - [How to switch from NAOqi to qi Framework](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/qi-framework/hands-guide/how-switch-naoqi-qi-framework)
  - [Python - How to write a qimessaging client](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/qi-framework/hands-guide/python-how-write-qimessaging-client)
  - [Using qicli commands](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/qi-framework/hands-guide/using-qicli-commands)
- [NAOqi APIs](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/naoqi-apis)
- [Living Robot](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/programming-living-robot): He will naturally do things by himself without the need for you to implement or manage every aspect of his life.

---

- [DCM-How It Works](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/naoqi-apis/dcm#-how-it-works--sbr-fake-anchor). The DCM is the link between the “upper level” software (others naoqi modules) and the “lower level” software (soft in electronic boards).

---

- [Supported Languages](https://developer.softbankrobotics.com/pepper-naoqi-25/pepper-documentation/pepper-developer-guide/supported-languages)

---

- [A Demo: Say ‘Hello, you’ every time pepper detects a human face](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/other-tutorials/python-sdk-tutorials/reacting-events#python-reacting-to-events)
- [Python SDK - Examples](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/other-tutorials/python-sdk-tutorials/python-sdk-examples)
- [Parallel Tasks: move and speak at the same time.](https://developer.softbankrobotics.com/pepper-naoqi-25/naoqi-developer-guide/other-tutorials/python-sdk-tutorials/parallel-tasks-making#-making-nao-move-and-speak-at-the-same-time--sbr-fake-anchor)
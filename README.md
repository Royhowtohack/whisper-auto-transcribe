<div id="top"></div>

[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


# whisper-auto-transcribe

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Whisper Auto Transcribe</h3>
  
  <a href="https://github.com/tomchang25/whisper-auto-transcribe">
    <img src="images/logo.png" alt="Logo" width="400" height="400">
  </a>

  <p align="center">
    The most efficient subtitle solution.
    <br />
    <a href="https://github.com/tomchang25/whisper-auto-transcribe#Demo">View Demo</a>
    ·
    <a href="https://github.com/tomchang25/whisper-auto-transcribe/issues">Report Bug</a>
    ·
    <a href="https://github.com/tomchang25/whisper-auto-transcribe/issues">Request Feature</a>
  </p>
  



</div>

<!-- ABOUT THE PROJECT -->
## About The Project

The tool is based on [OpenAI-whisper](https://github.com/openai/whisper), the latest project developed by OpenAI. 

I just made some changes to output the subtitle files, and added a graphical interface.

For more details, you can check [this](https://cdn.openai.com/papers/whisper.pdf).

If you don't want to read an academic paper, this tool can be summed up in one sentence: 

   ```sh
   AI will auto generate subtitle, with more accuracy than most transcribe commercial software.
   The most important, it's FREE!
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Installation

1. Install [Python 3](https://www.python.org/downloads/)

2. Clone the repo
   ```sh
   git clone https://github.com/tomchang25/whisper-auto-transcribe.git
   cd whisper-auto-transcribe
   ```
3. Install whisper dependency
   ```sh
   pip install git+https://github.com/openai/whisper.git 
   ```
4. Install [ffmpeg](https://ffmpeg.org/)
   ```sh
   # on Ubuntu or Debian
   sudo apt update && sudo apt install ffmpeg

   # on MacOS using Homebrew (https://brew.sh/)
   brew install ffmpeg

   # on Windows using Chocolatey (https://chocolatey.org/)
   choco install ffmpeg

   # on Windows using Scoop (https://scoop.sh/)
   scoop install ffmpeg

   ```
5. Open application
   ```sh
   python gui.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- How to use -->
## How to use
  <img src="images/Demo1.png" alt="How to use" width="800" height="450">

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Demo -->
## Demo

  
  <a href="https://www.youtube.com/watch?v=6w-AvMZT3TY">
    <img src="images/logo.png" alt="Logo" width="800" height="800">
  </a>

  #Japanese subtitle
   ```sh
   0
   0:00:00,0 --> 0:00:09,580
   人気を集めているのは鹿児島県 枕崎市の海沿いに立つ高さ20メートルを超える

   1
   0:00:09,580 --> 0:00:16,320
   八市の仲間です 枕崎市はかつては台風銀座と言われるほど

   2
   0:00:16,320 --> 0:00:24,120
   台風の接近が多くこの場所は何度も台風中継に使われてきました

   3
   0:00:24,120 --> 0:00:27,120
   ん

   4
   0:00:27,480 --> 0:00:36,600
   台風14号が接近した日曜日 4本ある木のうちの1本が sns 上で

   5
   0:00:36,600 --> 0:00:45,200
   ヤッシーと名付けられ強風に耐える姿に応援コメントが続出しました よし頑張れ

   6
   0:00:45,200 --> 0:00:54,320
   や c 早く逃げろ イザとなったら根っこを外して逃げろ

   7
   0:00:54,320 --> 0:01:16,760
   欲しいという声もあるということです


   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] pre-alpha version
- [x] english translation
- [ ] CPU / GPU option
- [ ] progress bar
- [ ] preview srt
- [ ] English to other language translation
- [ ] package as exe
- [ ] Multi-language Support
    - [ ] Traditional Chinese
    - [ ] Japanese

<p align="right">(<a href="#top">back to top</a>)</p>

## Known bug
- [ ] Lots of work to do.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Q & A -->
## Q & A

1. Is it better then youtube automatic subtitles?
   ```
   Do you really need to ask? Youtube can even fuck up English transcribe.
   ```
   
2. Is it better then Vosk(Subtitle Edit)?
   ```
   Definitely.
   ```

3. Is it better then Trint?
   ```
   Trint is terrible at non-English transcribe, and that's whisper advantage.
   ```

3. Is it better then Sonix.ai?
   ```
   Sonix.ai is nearly perfect actually, but hey! you need to pay the bill!
   ```
4. Your code suck!
   ```
   Why dont you release a better version. So I can use your project and spend more time to relax.
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Greysuki  - tomchang25@gmail.com

Project Link: [https://github.com/tomchang25/whisper-auto-transcribe](https://github.com/tomchang25/whisper-auto-transcribe)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [OpenAI-whisper](https://github.com/openai/whisper)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[stars-shield]: https://img.shields.io/github/stars/tomchang25/whisper-auto-transcribe.svg?style=for-the-badge
[stars-url]: https://github.com/tomchang25/whisper-auto-transcribe/stargazers
[issues-shield]: https://img.shields.io/github/issues/tomchang25/whisper-auto-transcribe.svg?style=for-the-badge
[issues-url]: https://github.com/tomchang25/whisper-auto-transcribe/issues
[license-shield]: https://img.shields.io/github/license/tomchang25/whisper-auto-transcribe.svg?style=for-the-badge
[license-url]: https://github.com/tomchang25/whisper-auto-transcribe/LICENSE.txt


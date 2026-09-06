# Digital ink recognition

With ML Kit's digital ink recognition API, you can recognize handwritten text
and classify gestures on a digital surface in hundreds of languages, as well as
classify sketches. The digital ink recognition API uses the same technology that
powers handwriting recognition in Gboard, Google Translate, and the
[Quick, Draw!](https://quickdraw.withgoogle.com/) game.

Digital ink recognition allows you to:

* Write on the screen instead of typing on a virtual keyboard. This lets users
  draw characters that are not available on their keyboard, such as ệ, अ or 森
  for latin alphabet keyboards.
* Perform basic text operations (navigation, editing, selection, and so on)
  using gestures.
* Recognize hand‑drawn shapes and emojis.

Digital ink recognition works with the strokes the user draws on the screen. If
you need to read text from images taken with the camera, use the
[Text Recognition API](https://developers.google.com/ml-kit/vision/text-recognition).

Digital ink recognition works fully offline and is supported on Android and iOS.

[iOS](https://developers.google.com/ml-kit/vision/digital-ink-recognition/ios)
[Android](https://developers.google.com/ml-kit/vision/digital-ink-recognition/android)

## Key Capabilities

* Converts handwritten text to sequences of unicode characters
* Runs on the device in near real time
* The user's handwriting stays on the device, recognition is performed without
  any network connection
* Supports 300+ languages and 25+ writing systems, see the
  [complete list of supported languages](https://developers.google.com/ml-kit/vision/digital-ink-recognition/base-models#text)
  + Supports gesture classification for these languages via
    [`-x-gesture` extensions](https://developers.google.com/ml-kit/vision/digital-ink-recognition/base-models#text)
* Recognizes emojis and basic shapes
* Keeps on-device storage low by dynamically downloading language packs as
  needed

The recognizer takes an `Ink` object as input. `Ink` is a vector representation
of what the user has written on the screen: a sequence of *strokes*, each being
a list of coordinates with time information called *touch points*. A stroke
starts when the user puts their stylus or finger down and ends when they lift it
up. The `Ink` is passed to a recognizer, which returns one or more possible
recognition results, with levels of confidence.

## Examples

### English handwriting

The image on the left below shows what the user drew on the screen. The image on
the right is the corresponding `Ink` object. It contains the strokes with red
dots representing the touch points within each stroke.

![](/static/ml-kit/images/vision/digital-ink/handw1.png)    
![](/static/ml-kit/images/vision/digital-ink/handw2.png)

There are four strokes. The first two strokes in the `Ink` object look like
this:

| **Ink** | | |
| --- | --- | --- |
| Stroke 1 | `x` | 392, 391, 389, 287, ... |
| `y` | 52, 60, 76, 97, ... |
| `t` | 0, 37, 56, 75, ... |
| Stroke 2 | `x` | 497, 494, 493, 490, ... |
| `y` | 167, 165, 165, 165, ... |
| `t` | 694, 742, 751, 770, ... |
| ... |  |  |

When you send this `Ink` to a recognizer for the English language, it returns
several possible transcriptions, containing five or six characters. They are
ordered by decreasing confidence:

| **RecognitionResult** | |
| --- | --- |
| RecognitionCandidate #1 | handw |
| RecognitionCandidate #2 | handrw |
| RecognitionCandidate #3 | hardw |
| RecognitionCandidate #4 | handu |
| RecognitionCandidate #5 | handwe |

### Gestures

Gesture classifiers classify an ink stroke into one of nine gesture classes
listed below.

| Gesture | Example |
| --- | --- |
| `arch:above` `arch:below` |  |
| `caret:above` `caret:below` |  |
| `circle` |  |
| corner:downleft |  |
| `scribble` |  |
| `strike` |  |
| `verticalbar` |  |
| `writing` |  |

**Note:** It is not always possible to reliably distinguish some gestures from
writing. For example, the `verticalbar` gesture may look exactly like
the digit `1` or letter `l` when they are written as a
vertical lines. To allow the user to use both gestures and writing, your
application may need to consider the position of the writing or gesture: for the
writing over existing text, prefer the gesture interpretation; for the writing
over empty space, prefer the text interpretation.


### Emoji sketches

The image on the left below shows what the user drew on the screen. The image on
the right is the corresponding `Ink` object. It contains the strokes with red
dots representing the touch points within each stroke.

![](/static/ml-kit/images/vision/digital-ink/emoji1.png)    
![](/static/ml-kit/images/vision/digital-ink/emoji2.png)

The `Ink` object contains six strokes.

![](/static/ml-kit/images/vision/digital-ink/sketch1.png) 
![](/static/ml-kit/images/vision/digital-ink/sketch3.png) 
![](/static/ml-kit/images/vision/digital-ink/sketch6.png) 
![](/static/ml-kit/images/vision/digital-ink/sketch2.png) 
![](/static/ml-kit/images/vision/digital-ink/sketch5.png) 
![](/static/ml-kit/images/vision/digital-ink/sketch4.png)

| **Ink** | | |
| --- | --- | --- |
| Stroke 1 | `x` | 269, 266, 262, 255, ... |
| `y` | 40, 40, 40, 41, ... |
| `t` | 0, 36, 56, 75, ... |
| Stroke 2 | `x` | 179, 182, 183, 185, ... |
| `y` | 157, 158, 159, 160, ... |
| `t` | 2475, 2522, 2531, 2541, ... |
| ... |  |  |

When you send this `Ink` to the emoji recognizer, you get several possible
transcriptions, ordered by decreasing confidence:

| **RecognitionResult** | |
| --- | --- |
| RecognitionCandidate #1 | 😂 (U+1f62d) |
| RecognitionCandidate #2 | 😅 (U+1f605) |
| RecognitionCandidate #3 | 😹 (U+1f639) |
| RecognitionCandidate #4 | 😄 (U+1f604) |
| RecognitionCandidate #5 | 😆 (U+1f606) |

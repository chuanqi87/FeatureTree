# Setting up a capture session

Configure input devices, output media, preview views, and basic settings before capturing photos or video.

## Discussion

An [`AVCaptureSession`](/documentation/AVFoundation/AVCaptureSession) is the basis for all media capture in iOS and macOS. It manages your app’s exclusive access to the OS capture infrastructure and capture devices, as well as the flow of data from input devices to media outputs. How you configure connections between inputs and outputs defines the capabilities of your capture session. For example, the diagram below shows a capture session that can capture both photos and movies and provides a camera preview, using the iPhone back camera and microphone.

![Block diagram of detailed capture session architecture example: separate AVCaptureDeviceInput objects for camera and microphone connect, through AVCaptureConnection objects managed by AVCaptureSession, to AVCapturePhotoOutput, AVCaptureMovieFileOutput, and AVCaptureVideoPreviewLayer.](images/com.apple.avfoundation/media-2970419.png)

### Connect inputs and outputs to the session

All capture sessions need at least one capture input and capture output. Capture inputs ([`AVCaptureInput`](/documentation/AVFoundation/AVCaptureInput) subclasses) are media sources—typically recording devices like the cameras and microphone built into an iOS device or Mac. Capture outputs ([`AVCaptureOutput`](/documentation/AVFoundation/AVCaptureOutput) subclasses) use data provided by capture inputs to produce media, like image and movie files.

To use a camera for video input (to capture photos or movies), select an appropriate [`AVCaptureDevice`](/documentation/AVFoundation/AVCaptureDevice), create a corresponding [`AVCaptureDeviceInput`](/documentation/AVFoundation/AVCaptureDeviceInput), and add it to the session:

```swift
captureSession.beginConfiguration()
let videoDevice = AVCaptureDevice.default(.builtInWideAngleCamera,
                                          for: .video, position: .unspecified)
guard
    let videoDeviceInput = try? AVCaptureDeviceInput(device: videoDevice!),
    captureSession.canAddInput(videoDeviceInput)
    else { return }
captureSession.addInput(videoDeviceInput)
```

> Note:
> iOS offers several other ways to select a camera device. For more information, see <doc://com.apple.avfoundation/documentation/AVFoundation/choosing-a-capture-device>.

Next, add outputs for the kinds of media you plan to capture from the camera you’ve selected. For example, to enable capturing photos, add an [`AVCapturePhotoOutput`](/documentation/AVFoundation/AVCapturePhotoOutput) to the session:

```swift
let photoOutput = AVCapturePhotoOutput()
guard captureSession.canAddOutput(photoOutput) else { return }
captureSession.sessionPreset = .photo
captureSession.addOutput(photoOutput)
captureSession.commitConfiguration()
```

A session can have multiple inputs and outputs. For example:

- To record both video and audio in a movie, add inputs for both camera and microphone devices.
- To capture both photos and movies from the same camera, add both [`AVCapturePhotoOutput`](/documentation/AVFoundation/AVCapturePhotoOutput) and [`AVCaptureMovieFileOutput`](/documentation/AVFoundation/AVCaptureMovieFileOutput) to your session.

> Important:
> Call ``doc://com.apple.avfoundation/documentation/AVFoundation/AVCaptureSession/beginConfiguration()`` before changing a session’s inputs or outputs, and call ``doc://com.apple.avfoundation/documentation/AVFoundation/AVCaptureSession/commitConfiguration()`` after making changes.

### Display a camera preview

It’s important to let the user see input from the camera before choosing to snap a photo or start video recording, as in the viewfinder of a traditional camera. You can provide such a preview by connecting an [`AVCaptureVideoPreviewLayer`](/documentation/AVFoundation/AVCaptureVideoPreviewLayer) to your capture session, which displays a live video feed from the camera whenever the session is running.

[`AVCaptureVideoPreviewLayer`](/documentation/AVFoundation/AVCaptureVideoPreviewLayer) is a Core Animation layer, so you can display and style it in your interface as you would any other <doc://com.apple.documentation/documentation/QuartzCore/CALayer> subclass. The simplest way to add a preview layer to a UIKit app is to define a <doc://com.apple.documentation/documentation/UIKit/UIView> subclass whose <doc://com.apple.documentation/documentation/UIKit/UIView/layerClass> is [`AVCaptureVideoPreviewLayer`](/documentation/AVFoundation/AVCaptureVideoPreviewLayer), as shown below.

```swift
class PreviewView: UIView {
    override class var layerClass: AnyClass {
        return AVCaptureVideoPreviewLayer.self
    }
    
    /// Convenience wrapper to get layer as its statically known type.
    var videoPreviewLayer: AVCaptureVideoPreviewLayer {
        return layer as! AVCaptureVideoPreviewLayer
    }
}
```

Then, to use the preview layer with a capture session, set the layer’s [`session`](/documentation/AVFoundation/AVCaptureVideoPreviewLayer/session) property:

```swift
self.previewView.videoPreviewLayer.session = self.captureSession
```

> Note:
> If your app supports multiple interface orientations, use the preview layer’s ``doc://com.apple.avfoundation/documentation/AVFoundation/AVCaptureVideoPreviewLayer/connection`` to the capture session to set a ``doc://com.apple.avfoundation/documentation/AVFoundation/AVCaptureConnection/videoOrientation`` matching that of your UI.

### Run the capture session

After you’ve configured inputs, outputs, and previews, call [`startRunning()`](/documentation/AVFoundation/AVCaptureSession/startRunning()) to let data flow from inputs to outputs.

With some capture outputs, running the session is all you need to begin media capture. For example, if your session contains an [`AVCaptureVideoDataOutput`](/documentation/AVFoundation/AVCaptureVideoDataOutput), you start receiving delivering video frames as soon as the session is running.

With other capture outputs, you first start the session running, then use the capture output class itself to initiate capture. In a photography app, for example, running the session enables a viewfinder-style preview, but you use the [`AVCapturePhotoOutput`](/documentation/AVFoundation/AVCapturePhotoOutput) [`capturePhoto(with:delegate:)`](/documentation/AVFoundation/AVCapturePhotoOutput/capturePhoto(with:delegate:)) method to snap a picture.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)

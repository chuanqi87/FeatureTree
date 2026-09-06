# Upload files with Cloud Storage on Apple platforms

Cloud Storage for Firebase allows you to quickly and easily upload files to a
[Cloud Storage](https://cloud.google.com/storage) bucket provided
and managed by Firebase.

**Note:** By default, a Cloud Storage for Firebase bucket requires Firebase Authentication
to perform any action on the bucket's data or files. You can change your
Firebase Security Rules for Cloud Storage to
[allow unauthenticated access for specific situations](https://firebase.google.com/docs/storage/security/rules-conditions#public).
However, for most situations, we strongly recommend
[restricting access and setting up robust security rules](https://firebase.google.com/docs/storage/security/get-started)
(especially for production apps). Note that if you use
Google App Engine and have a default Cloud Storage bucket with a name
format of `*.appspot.com`, you may need to consider
[how your security rules impact access to App Engine files](https://firebase.google.com/docs/storage/gcp-integration#security-rules-and-app-engine-files).**Note:** For Spark plan projects, Firebase blocks upload and hosting of certain
executable file types for Windows (files with `.exe`,
`.dll` and `.bat` extensions), Android
(`.apk` extension) and Apple (`.ipa` extension) by
Cloud Storage for Firebase and Firebase Hosting. This policy exists to
prevent abuse on our platform. Projects on the Blaze plan are not affected.
For more information, see
[this FAQ](https://firebase.google.com/support/faq#storage-exe-restrictions).


## Create a Reference

To upload a file, first
[create a Cloud Storage reference](https://firebase.google.com/docs/storage/ios/create-reference)
to the location in Cloud Storage you want to upload the file to.

You can create a reference by appending child paths to the root of your
Cloud Storage bucket:

### Swift

```
// Create a root reference
let storageRef = storage.reference()

// Create a reference to "mountains.jpg"
let mountainsRef = storageRef.child("mountains.jpg")

// Create a reference to 'images/mountains.jpg'
let mountainImagesRef = storageRef.child("images/mountains.jpg")

// While the file names are the same, the references point to different files
mountainsRef.name == mountainImagesRef.name            // true
mountainsRef.fullPath == mountainImagesRef.fullPath    // false
```

### Objective-C

```
// Create a root reference
FIRStorageReference *storageRef = [storage reference];

// Create a reference to "mountains.jpg"
FIRStorageReference *mountainsRef = [storageRef child:@"mountains.jpg"];

// Create a reference to 'images/mountains.jpg'
FIRStorageReference *mountainImagesRef = [storageRef child:@"images/mountains.jpg"];

// While the file names are the same, the references point to different files
[mountainsRef.name isEqualToString:mountainImagesRef.name];         // true
[mountainsRef.fullPath isEqualToString:mountainImagesRef.fullPath]; // false
```

You cannot upload data with a reference to the root of your
Cloud Storage bucket. Your reference must point to a child URL.

## Upload Files

Once you have a reference, you can upload files to Cloud Storage
in two ways:

1. Upload from data in memory
2. Upload from a URL representing a file on device

### Upload from data in memory

The `putData:metadata:completion:` method is the simplest way to upload a file
to Cloud Storage. `putData:metadata:completion:` takes an NSData
object and returns an `FIRStorageUploadTask`, which you can use to manage your
upload and monitor its status.

### Swift

```
// Data in memory
let data = Data()

// Create a reference to the file you want to upload
let riversRef = storageRef.child("images/rivers.jpg")

// Upload the file to the path "images/rivers.jpg"
let uploadTask = riversRef.putData(data, metadata: nil) { (metadata, error) in
  guard let metadata = metadata else {
    // Uh-oh, an error occurred!
    return
  }
  // Metadata contains file metadata such as size, content-type.
  let size = metadata.size
  // You can also access to download URL after upload.
  riversRef.downloadURL { (url, error) in
    guard let downloadURL = url else {
      // Uh-oh, an error occurred!
      return
    }
  }
}
```

### Objective-C

```
// Data in memory
NSData *data = [NSData dataWithContentsOfFile:@"rivers.jpg"];

// Create a reference to the file you want to upload
FIRStorageReference *riversRef = [storageRef child:@"images/rivers.jpg"];

// Upload the file to the path "images/rivers.jpg"
FIRStorageUploadTask *uploadTask = [riversRef putData:data
                                             metadata:nil
                                           completion:^(FIRStorageMetadata *metadata,
                                                        NSError *error) {
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // Metadata contains file metadata such as size, content-type, and download URL.
    int size = metadata.size;
    // You can also access to download URL after upload.
    [riversRef downloadURLWithCompletion:^(NSURL * _Nullable URL, NSError * _Nullable error) {
      if (error != nil) {
        // Uh-oh, an error occurred!
      } else {
        NSURL *downloadURL = URL;
      }
    }];
  }
}];
```

### Upload from a local file

You can upload local files on the devices, such as photos and videos from the
camera, with the `putFile:metadata:completion:` method.
`putFile:metadata:completion:` takes an `NSURL` and returns an
`FIRStorageUploadTask`, which you can use to manage your upload and monitor its
status.

### Swift

```
// File located on disk
let localFile = URL(string: "path/to/image")!

// Create a reference to the file you want to upload
let riversRef = storageRef.child("images/rivers.jpg")

// Upload the file to the path "images/rivers.jpg"
let uploadTask = riversRef.putFile(from: localFile, metadata: nil) { metadata, error in
  guard let metadata = metadata else {
    // Uh-oh, an error occurred!
    return
  }
  // Metadata contains file metadata such as size, content-type.
  let size = metadata.size
  // You can also access to download URL after upload.
  riversRef.downloadURL { (url, error) in
    guard let downloadURL = url else {
      // Uh-oh, an error occurred!
      return
    }
  }
}
```

### Objective-C

```
// File located on disk
NSURL *localFile = [NSURL URLWithString:@"path/to/image"];

// Create a reference to the file you want to upload
FIRStorageReference *riversRef = [storageRef child:@"images/rivers.jpg"];

// Upload the file to the path "images/rivers.jpg"
FIRStorageUploadTask *uploadTask = [riversRef putFile:localFile metadata:nil completion:^(FIRStorageMetadata *metadata, NSError *error) {
  if (error != nil) {
    // Uh-oh, an error occurred!
  } else {
    // Metadata contains file metadata such as size, content-type, and download URL.
    int size = metadata.size;
    // You can also access to download URL after upload.
    [riversRef downloadURLWithCompletion:^(NSURL * _Nullable URL, NSError * _Nullable error) {
      if (error != nil) {
        // Uh-oh, an error occurred!
      } else {
        NSURL *downloadURL = URL;
      }
    }];
  }
}];
```

If you want to actively manage your upload, you can use the `putData:` or
`putFile:` methods and observe the upload task, rather than using the
completion handler. See [Manage Uploads](https://firebase.google.com/docs/storage/ios/upload-files#manage_uploads) for more
information.

## Add File Metadata

You can also include metadata when you upload files.
This metadata contains typical file metadata properties such as `name`, `size`,
and `contentType` (commonly referred to as MIME type). The `putFile:` method
automatically infers the content type from the `NSURL` filename extension, but
you can override the auto-detected type by specifying `contentType` in the
metadata. If you do not provide a `contentType` and Cloud Storage
cannot infer a default from the file extension, Cloud Storage uses
`application/octet-stream`. See the
[Use File Metadata](https://firebase.google.com/docs/storage/ios/file-metadata)
section for more information about file metadata.

### Swift

```
// Create storage reference
let mountainsRef = storageRef.child("images/mountains.jpg")

// Create file metadata including the content type
let metadata = StorageMetadata()
metadata.contentType = "image/jpeg"

// Upload data and metadata
mountainsRef.putData(data, metadata: metadata)

// Upload file and metadata
mountainsRef.putFile(from: localFile, metadata: metadata)
```

### Objective-C

```
// Create storage reference
FIRStorageReference *mountainsRef = [storageRef child:@"images/mountains.jpg"];

// Create file metadata including the content type
FIRStorageMetadata *metadata = [[FIRStorageMetadata alloc] init];
metadata.contentType = @"image/jpeg";

// Upload data and metadata
FIRStorageUploadTask *uploadTask = [mountainsRef putData:data metadata:metadata];

// Upload file and metadata
uploadTask = [mountainsRef putFile:localFile metadata:metadata];
```

## Manage Uploads

In addition to starting uploads, you can pause, resume, and cancel uploads using
the `pause`, `resume`, and `cancel` methods. These methods raise `pause`,
`resume`, and `cancel` events. Canceling an upload causes the upload to fail
with an error indicating that the upload was canceled.

### Swift

```
// Start uploading a file
let uploadTask = storageRef.putFile(from: localFile)

// Pause the upload
uploadTask.pause()

// Resume the upload
uploadTask.resume()

// Cancel the upload
uploadTask.cancel()
```

### Objective-C

```
// Start uploading a file
FIRStorageUploadTask *uploadTask = [storageRef putFile:localFile];

// Pause the upload
[uploadTask pause];

// Resume the upload
[uploadTask resume];

// Cancel the upload
[uploadTask cancel];
```

## Monitor Upload Progress

You can attach observers to `FIRStorageUploadTask`s in order to monitor the
progress of the upload. Adding an observer returns a `FIRStorageHandle`
that can be used to remove the observer.

### Swift

```
// Add a progress observer to an upload task
let observer = uploadTask.observe(.progress) { snapshot in
  // A progress event occured
}
```

### Objective-C

```
// Add a progress observer to an upload task
NSString *observer = [uploadTask observeStatus:FIRStorageTaskStatusProgress
                                        handler:^(FIRStorageTaskSnapshot *snapshot) {
  // A progress event occurred
}];
```

These observers can be added to an `FIRStorageTaskStatus` event:

| `FIRStorageTaskStatus` Event | Typical Usage |
| --- | --- |
| `FIRStorageTaskStatusResume` | This event fires when the task starts or resumes uploading, and is often used in conjunction with the `FIRStorageTaskStatusPause` event. |
| `FIRStorageTaskStatusProgress` | This event fires any time data is uploading to Cloud Storage, and can be used to populate an upload progress indicator. |
| `FIRStorageTaskStatusPause` | This event fires any time the upload is paused, and is often used in conjunction with the `FIRStorageTaskStatusResume` event. |
| `FIRStorageTaskStatusSuccess` | This event fires when a upload has completed successfully. |
| `FIRStorageTaskStatusFailure` | This event fires when a upload has failed. Inspect the error to determine the failure reason. |

When an event occurs, an `FIRStorageTaskSnapshot` object is passed back. This
snapshot is an immutable view of the task, at the time the event occurred.
This object contains the following properties:

| Property | Type | Description |
| --- | --- | --- |
| `progress` | `NSProgress` | An `NSProgress` object containing the progress of the upload. |
| `error` | `NSError` | An error that occurred during upload, if any. |
| `metadata` | `FIRStorageMetadata` | During upload contains metadata being uploaded. After an `FIRTaskStatusSuccess` event, contains the uploaded file's metadata. |
| `task` | `FIRStorageUploadTask` | The task this is a snapshot of, which can be used to manage (`pause`, `resume`, `cancel`) the task. |
| `reference` | `FIRStorageReference` | The reference this task came from. |

You can also remove observers, either individually, by status, or by removing
all of them.

### Swift

```
// Create a task listener handle
let observer = uploadTask.observe(.progress) { snapshot in
  // A progress event occurred
}

// Remove an individual observer
uploadTask.removeObserver(withHandle: observer)

// Remove all observers of a particular status
uploadTask.removeAllObservers(for: .progress)

// Remove all observers
uploadTask.removeAllObservers()
```

### Objective-C

```
// Create a task listener handle
NSString *observer = [uploadTask observeStatus:FIRStorageTaskStatusProgress
                                       handler:^(FIRStorageTaskSnapshot *snapshot) {
  // A progress event occurred
}];

// Remove an individual observer
[uploadTask removeObserverWithHandle:observer];

// Remove all observers of a particular status
[uploadTask removeAllObserversForStatus:FIRStorageTaskStatusProgress];

// Remove all observers
[uploadTask removeAllObservers];
```

To prevent memory leaks, all observers are removed after an
`FIRStorageTaskStatusSuccess` or `FIRStorageTaskStatusFailure` occurs.

## Error Handling

There are a number of reasons why errors may occur on upload, including
the local file not existing, or the user not having permission to upload
the desired file. You can find more information about errors in the
[Handle Errors](https://firebase.google.com/docs/storage/ios/handle-errors)
section of the docs.

## Full Example

A full example of an upload with progress monitoring and error handling
is shown below:

### Swift

```
// Local file you want to upload
let localFile = URL(string: "path/to/image")!

// Create the file metadata
let metadata = StorageMetadata()
metadata.contentType = "image/jpeg"

// Upload file and metadata to the object 'images/mountains.jpg'
let uploadTask = storageRef.putFile(from: localFile, metadata: metadata)

// Listen for state changes, errors, and completion of the upload.
uploadTask.observe(.resume) { snapshot in
  // Upload resumed, also fires when the upload starts
}

uploadTask.observe(.pause) { snapshot in
  // Upload paused
}

uploadTask.observe(.progress) { snapshot in
  // Upload reported progress
  let percentComplete = 100.0 * Double(snapshot.progress!.completedUnitCount)
    / Double(snapshot.progress!.totalUnitCount)
}

uploadTask.observe(.success) { snapshot in
  // Upload completed successfully
}

uploadTask.observe(.failure) { snapshot in
  if let error = snapshot.error as? NSError {
    switch (StorageErrorCode(rawValue: error.code)!) {
    case .objectNotFound:
      // File doesn't exist
      break
    case .unauthorized:
      // User doesn't have permission to access file
      break
    case .cancelled:
      // User canceled the upload
      break

    /* ... */

    case .unknown:
      // Unknown error occurred, inspect the server response
      break
    default:
      // A separate error occurred. This is a good place to retry the upload.
      break
    }
  }
}
```

### Objective-C

```
// Local file you want to upload
NSURL *localFile = [NSURL URLWithString:@"path/to/image"];

// Create the file metadata
FIRStorageMetadata *metadata = [[FIRStorageMetadata alloc] init];
metadata.contentType = @"image/jpeg";

// Upload file and metadata to the object 'images/mountains.jpg'
FIRStorageUploadTask *uploadTask = [storageRef putFile:localFile metadata:metadata];

// Listen for state changes, errors, and completion of the upload.
[uploadTask observeStatus:FIRStorageTaskStatusResume handler:^(FIRStorageTaskSnapshot *snapshot) {
  // Upload resumed, also fires when the upload starts
}];

[uploadTask observeStatus:FIRStorageTaskStatusPause handler:^(FIRStorageTaskSnapshot *snapshot) {
  // Upload paused
}];

[uploadTask observeStatus:FIRStorageTaskStatusProgress handler:^(FIRStorageTaskSnapshot *snapshot) {
  // Upload reported progress
  double percentComplete = 100.0 * (snapshot.progress.completedUnitCount) / (snapshot.progress.totalUnitCount);
}];

[uploadTask observeStatus:FIRStorageTaskStatusSuccess handler:^(FIRStorageTaskSnapshot *snapshot) {
  // Upload completed successfully
}];

// Errors only occur in the "Failure" case
[uploadTask observeStatus:FIRStorageTaskStatusFailure handler:^(FIRStorageTaskSnapshot *snapshot) {
  if (snapshot.error != nil) {
    switch (snapshot.error.code) {
      case FIRStorageErrorCodeObjectNotFound:
        // File doesn't exist
        break;

      case FIRStorageErrorCodeUnauthorized:
        // User doesn't have permission to access file
        break;

      case FIRStorageErrorCodeCancelled:
        // User canceled the upload
        break;

      /* ... */

      case FIRStorageErrorCodeUnknown:
        // Unknown error occurred, inspect the server response
        break;
    }
  }
}];
```

Now that you've uploaded files, let's learn how to
[download them](https://firebase.google.com/docs/storage/ios/download-files)
from Cloud Storage.

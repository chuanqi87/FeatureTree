# Providing access to directories

Use a document picker to access the content of a directory outside your app’s container.

## Discussion

In iOS 12 and earlier, users can open and interact with files outside the app’s container. The [`UIDocumentBrowserViewController`](/documentation/UIKit/UIDocumentBrowserViewController) and [`UIDocumentPickerViewController`](/documentation/UIKit/UIDocumentPickerViewController) provide access to files in the system’s local file provider, in iCloud, or in third-party services that use a File Provider extension. Users can select multiple files at a time — but they need to select each file individually.

In iOS 13, users can select a directory from any of the available file providers using a [`UIDocumentPickerViewController`](/documentation/UIKit/UIDocumentPickerViewController). The document picker returns a *security-scoped URL* for the directory that permits your app to access content outside its container. In this case, the URL lets your app recursively access the directory and all of its contents, which includes accessing any new items you add to the directory in the future. Your app can even save a bookmark for this URL, letting it access the directory the next time it launches.

### Ask the user to select a directory

To prompt the user to select a directory, create a document picker and set the content type to open to the type <doc://com.apple.documentation/documentation/UniformTypeIdentifiers/UTType-swift.struct/folder>. Then set the document picker’s delegate and present it.

```swift
// Create a document picker for directories.
let documentPicker =
    UIDocumentPickerViewController(forOpeningContentTypes: [.folder])
documentPicker.delegate = self

// Set the initial directory.
documentPicker.directoryURL = startingDirectory

// Present the document picker.
present(documentPicker, animated: true, completion: nil)
```

As soon as you call the [`present(_:animated:completion:)`](/documentation/UIKit/UIViewController/present(_:animated:completion:)) method, the system displays the document picker to the user. If you specify the [`directoryURL`](/documentation/UIKit/UIDocumentPickerViewController/directoryURL) property, the document picker starts with the selected directory. Otherwise, it starts with the most recent directory the user chose.

![A screenshot of the document picker with the TextEdit directory in a selected state.](images/com.apple.uikit/media-3332331@2x.png)

After the user taps Done, the system calls your delegate’s [`documentPicker(_:didPickDocumentsAt:)`](/documentation/UIKit/UIDocumentPickerDelegate/documentPicker(_:didPickDocumentsAt:)) method, passing an array of security-scoped URLs for the user’s selected directories. Use a security-scoped URL to enumerate the content of the directory and any of its subdirectories, or to add, remove, or modify any files.

If the user taps Cancel, the system calls [`documentPickerWasCancelled(_:)`](/documentation/UIKit/UIDocumentPickerDelegate/documentPickerWasCancelled(_:)) instead.

> Note:
> The ``doc://com.apple.uikit/documentation/UIKit/UIDocumentBrowserViewController`` doesn’t support the <doc://com.apple.documentation/documentation/UniformTypeIdentifiers/UTType-swift.struct/folder> document type. To provide access to directories, use the ``doc://com.apple.uikit/documentation/UIKit/UIDocumentPickerViewController`` instead.

### Access the directory’s content

When the user selects a directory in the document picker, the system gives your app permission to access that directory and all of its contents. The document picker returns a security-scoped URL for the directory. When you use one of these URLs to enumerate the directory’s content, the resulting URLs are also security-scoped. You can save a security-scoped URL as a bookmark and later resolve it back into a security-scoped URL.

To access the content of a security-scoped URL, you must do the following:

1. Before accessing the URL, call <doc://com.apple.documentation/documentation/Foundation/NSURL/startAccessingSecurityScopedResource()>.
2. Use a file coordinator to perform read or write operations on the URL’s contents.
3. After you access the URL, call <doc://com.apple.documentation/documentation/Foundation/NSURL/stopAccessingSecurityScopedResource()>.

```swift
func documentPicker(_ controller:UIDocumentPickerViewController, didPickDocumentsAt urls: [URL]) {
    // Start accessing a security-scoped resource.
    guard let url = urls.first,
        url.startAccessingSecurityScopedResource() else {
        // Handle the failure here.
        return
    }

    // Make sure you release the security-scoped resource when you finish.
    defer { url.stopAccessingSecurityScopedResource() }

    // Use file coordination for reading and writing any of the URL’s content.
    var error: NSError? = nil
    NSFileCoordinator().coordinate(readingItemAt: url, error: &error) { (url) in
            
        let keys : [URLResourceKey] = [.nameKey, .isDirectoryKey]
            
        // Get an enumerator for the directory's content.
        guard let fileList =
            FileManager.default.enumerator(at: url, includingPropertiesForKeys: keys) else {
            Swift.debugPrint("*** Unable to access the contents of \(url.path) ***\n")
            return
        }
            
        for case let file as URL in fileList {
            // Start accessing the content's security-scoped URL.
            guard file.startAccessingSecurityScopedResource() else {
                // Handle the failure here.
                continue
            }

            // Do something with the file here.
            Swift.debugPrint("chosen file: \(file.lastPathComponent)")
                
            // Make sure you release the security-scoped resource when you finish.
            file.stopAccessingSecurityScopedResource()
        }
    }
}
```

### Save the URL as a bookmark

To access the URL in the future, save the URL as a <doc://com.apple.documentation/documentation/Foundation/NSURL/BookmarkCreationOptions/minimalBookmark> using its <doc://com.apple.documentation/documentation/Foundation/NSURL/bookmarkData(options:includingResourceValuesForKeys:relativeTo:)> method.

```swift
do {
    // Start accessing a security-scoped resource.
    guard url.startAccessingSecurityScopedResource() else {
        // Handle the failure here.
        return
    }
    
    // Make sure you release the security-scoped resource when you finish.
    defer { url.stopAccessingSecurityScopedResource() }
    
    let bookmarkData = try url.bookmarkData(options: .minimalBookmark, includingResourceValuesForKeys: nil, relativeTo: nil)
    
    try bookmarkData.write(to: getMyURLForBookmark())
}
catch let error {
    // Handle the error here.
}
```

You can then read the bookmark, and resolve it to a security-scoped URL again.

```swift
do {
    let bookmarkData = try Data(contentsOf: getMyURLForBookmark())
    var isStale = false
    let url = try URL(resolvingBookmarkData: bookmarkData, bookmarkDataIsStale: &isStale)
    
    guard !isStale else {
        // Handle stale data here.
        return
    }
    
    // Use the URL here.
}
catch let error {
    // Handle the error here.
}
```

### Respond to permission changes

Users always have complete control over the apps that can access directories. After selecting a directory from the document picker, your app appears in Settings > Privacy > Files and Folders. This page lists all the apps that have permission to access shared directories, and users can revoke or restore permission for each app at any time.

This means your app must be ready to handle failures when accessing a directory’s content. Calls to the <doc://com.apple.documentation/documentation/Foundation/URL/startAccessingSecurityScopedResource()> method can fail, as well as any attempts to read or write to the URL. This is especially true when saving and resolving bookmarks to security-scoped URLs because using saved bookmarks can greatly increase the amount of time users have to possibly change your app’s permissions.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)

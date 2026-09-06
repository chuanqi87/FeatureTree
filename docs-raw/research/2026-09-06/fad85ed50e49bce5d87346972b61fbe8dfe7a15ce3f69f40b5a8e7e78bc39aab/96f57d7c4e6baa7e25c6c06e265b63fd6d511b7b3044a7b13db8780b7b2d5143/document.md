# App Clips

Read App Clip and App Clip experience information.

## Discussion

The `appClips` resource represents an App Clip and its associated App Clip experiences. Use this resource to access existing App Clip metadata and to create, update, or delete App Clip experiences.

## Topics

### Reading App Clip Information

[`GET /v1/appClips/{id}`](/documentation/AppStoreConnectAPI/GET-v1-appClips-_id_)

Get a specific App Clip.

### Getting App Clip Experiences

[`GET /v1/appClips/{id}/appClipDefaultExperiences`](/documentation/AppStoreConnectAPI/GET-v1-appClips-_id_-appClipDefaultExperiences)

Get all default App Clip experiences for an App Clip.

[`GET /v1/appClips/{id}/appClipAdvancedExperiences`](/documentation/AppStoreConnectAPI/GET-v1-appClips-_id_-appClipAdvancedExperiences)

Get all advanced App Clip experiences for an App Clip.

[`GET /v1/appClips/{id}/relationships/appClipAdvancedExperiences`](/documentation/AppStoreConnectAPI/GET-v1-appClips-_id_-relationships-appClipAdvancedExperiences)

[`GET /v1/appClips/{id}/relationships/appClipDefaultExperiences`](/documentation/AppStoreConnectAPI/GET-v1-appClips-_id_-relationships-appClipDefaultExperiences)

### Objects

[`AppClip`](/documentation/AppStoreConnectAPI/AppClip)

A lightweight version of an app that users can launch instantly without installation, associated with a registered parent app.

[`AppClipResponse`](/documentation/AppStoreConnectAPI/AppClipResponse)

The response body for endpoints that read an App Clip associated with an app.

[`AppClipDefaultExperiencesResponse`](/documentation/AppStoreConnectAPI/AppClipDefaultExperiencesResponse)

The response body for endpoints that list default App Clip experiences.

[`AppClipAdvancedExperiencesResponse`](/documentation/AppStoreConnectAPI/AppClipAdvancedExperiencesResponse)

A response containing a list of configured App Clip advanced experiences.

[`AppClipAppClipAdvancedExperiencesLinkagesResponse`](/documentation/AppStoreConnectAPI/AppClipAppClipAdvancedExperiencesLinkagesResponse)

[`AppClipAppClipDefaultExperiencesLinkagesResponse`](/documentation/AppStoreConnectAPI/AppClipAppClipDefaultExperiencesLinkagesResponse)



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)

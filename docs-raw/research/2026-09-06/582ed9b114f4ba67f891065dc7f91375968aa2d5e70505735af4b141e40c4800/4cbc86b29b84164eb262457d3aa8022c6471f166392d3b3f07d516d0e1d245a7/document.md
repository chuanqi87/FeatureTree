# Work profile detection

This guide illustrates how to detect a work profile on a device. It applies only
to work profiles managed by the Android Device policy app.

## Detect if the app is running inside a work profile

The following method checks if the calling app is running within a work profile
managed by the Android Device Policy app.

### Kotlin

```
fun isInsideWorkProfile(): Boolean {
  val devicePolicyManager = getSystemService(Context.DEVICE_POLICY_SERVICE) as DevicePolicyManager

  return devicePolicyManager.isProfileOwnerApp("com.google.android.apps.work.clouddpc")
}
```

### Java

```
boolean isInsideWorkProfile() {
  DevicePolicyManager devicePolicyManager = (DevicePolicyManager)getSystemService(Context.DEVICE_POLICY_SERVICE);

  return devicePolicyManager.isProfileOwnerApp("com.google.android.apps.work.clouddpc");
}
```

## Detect if the device has a work profile

To determine if a device has a work profile managed by the Android Device Policy
app, use the following method. This can be called from any management mode. From
an app in the *personal* profile, querying for the intent
`com.google.android.apps.work.clouddpc.ACTION_DETECT_WORK_PROFILE` should
resolve as a cross-profile intent if a work profile managed by the Android
Device Policy app exists. This method will only return `true` when called from
the *personal* profile of a device that has such a work profile.

**Note:** To determine if the app itself is running inside a work profile, use the
method described in the previous section.


### Android 11 and later:

### Kotlin

```
fun hasWorkProfile(): Boolean {
  val intent = Intent("com.google.android.apps.work.clouddpc.ACTION_DETECT_WORK_PROFILE")
  val activities = context.packageManager.queryIntentActivities(intent, 0)
  return activities.any { it.isCrossProfileIntentForwarderActivity }
}
```

### Java

```
boolean hasWorkProfile() {
  Intent intent = new Intent("com.google.android.apps.work.clouddpc.ACTION_DETECT_WORK_PROFILE");
  List<ResolveInfo> activities = context.getPackageManager().queryIntentActivities(intent, 0);
  return activities.stream()
        .anyMatch(
            (ResolveInfo resolveInfo) -> {
              return resolveInfo.isCrossProfileIntentForwarderActivity();
            });
}
```

### Prior to Android 11:

### Kotlin

```
fun hasWorkProfile(): Boolean {
  val intent = Intent("com.google.android.apps.work.clouddpc.ACTION_DETECT_WORK_PROFILE")
  val activities = context.packageManager.queryIntentActivities(intent, 0)
  return activities.any { it.activityInfo.name == "com.android.internal.app.ForwardIntentToManagedProfile" }
}
```

### Java

```
boolean hasWorkProfile() {
  Intent intent = new Intent("com.google.android.apps.work.clouddpc.ACTION_DETECT_WORK_PROFILE");
  List<ResolveInfo> activities = context.getPackageManager().queryIntentActivities(intent, 0);
  return activities.stream()
        .anyMatch(
            (ResolveInfo resolveInfo) -> {
              return resolveInfo.activityInfo.name.equals("com.android.internal.app.ForwardIntentToManagedProfile");
            });
}
```

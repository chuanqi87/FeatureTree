[Skip to main content](https://developer.android.com/guide/practices/page-sizes#main-content)

[![Android Developers](https://www.gstatic.com/devrel-devsite/prod/v6c08f9bb601564cd99488472d05cdf6fb06f007f31b6552465782b15883ce123/android/images/lockup.png)](https://developer.android.com/)

`/`

Language

- [English](https://developer.android.com/guide/practices/page-sizes)
- [Deutsch](https://developer.android.com/guide/practices/page-sizes?hl=de)
- [Español](https://developer.android.com/guide/practices/page-sizes?hl=es)
- [Español – América Latina](https://developer.android.com/guide/practices/page-sizes?hl=es-419)
- [Français](https://developer.android.com/guide/practices/page-sizes?hl=fr)
- [Indonesia](https://developer.android.com/guide/practices/page-sizes?hl=id)
- [Italiano](https://developer.android.com/guide/practices/page-sizes?hl=it)
- [Polski](https://developer.android.com/guide/practices/page-sizes?hl=pl)
- [Português](https://developer.android.com/guide/practices/page-sizes?hl=pt)
- [Português – Brasil](https://developer.android.com/guide/practices/page-sizes?hl=pt-br)
- [Tiếng Việt](https://developer.android.com/guide/practices/page-sizes?hl=vi)
- [Türkçe](https://developer.android.com/guide/practices/page-sizes?hl=tr)
- [Русский](https://developer.android.com/guide/practices/page-sizes?hl=ru)
- [עברית](https://developer.android.com/guide/practices/page-sizes?hl=he)
- [العربيّة](https://developer.android.com/guide/practices/page-sizes?hl=ar)
- [فارسی](https://developer.android.com/guide/practices/page-sizes?hl=fa)
- [हिंदी](https://developer.android.com/guide/practices/page-sizes?hl=hi)
- [বাংলা](https://developer.android.com/guide/practices/page-sizes?hl=bn)
- [ภาษาไทย](https://developer.android.com/guide/practices/page-sizes?hl=th)
- [中文 – 简体](https://developer.android.com/guide/practices/page-sizes?hl=zh-cn)
- [中文 – 繁體](https://developer.android.com/guide/practices/page-sizes?hl=zh-tw)
- [日本語](https://developer.android.com/guide/practices/page-sizes?hl=ja)
- [한국어](https://developer.android.com/guide/practices/page-sizes?hl=ko)

[Android Studio](https://developer.android.com/studio)

[Sign in](https://developer.android.com/_d/signin?continue=https%3A%2F%2Fdeveloper.android.com%2Fguide%2Fpractices%2Fpage-sizes&prompt=select_account)

- [Develop](https://developer.android.com/develop)
- [Devices](https://developer.android.com/develop/devices)
- [Compatibility](https://developer.android.com/guide/practices/compatibility)

- On this page
- [Google Play compatibility requirement](https://developer.android.com/guide/practices/page-sizes#google-play-compatibility-requirement)
- [Benefits and performance gains](https://developer.android.com/guide/practices/page-sizes#benefits)
- [Check if your app is impacted](https://developer.android.com/guide/practices/page-sizes#16-kb-impact)
  - [Does your app use native code?](https://developer.android.com/guide/practices/page-sizes#native-code)
  - [Identify native libraries using APK Analyzer](https://developer.android.com/guide/practices/page-sizes#identify-native-code)
  - [Detect alignment issues with automated checks](https://developer.android.com/guide/practices/page-sizes#auto-checks)
  - [Check the alignment of ELF segments for shared libraries](https://developer.android.com/guide/practices/page-sizes#elf-alignment)
  - [Check the RELRO security flag](https://developer.android.com/guide/practices/page-sizes#relro-flag)
- [Build your app with support for 16 KB devices](https://developer.android.com/guide/practices/page-sizes#build)
  - [Update the packaging of your shared libraries](https://developer.android.com/guide/practices/page-sizes#update-packaging)
  - [Compile your app using 16 KB ELF alignment](https://developer.android.com/guide/practices/page-sizes#compile-16-kb-alignment)
  - [Fix code and resolve runtime issues](https://developer.android.com/guide/practices/page-sizes#check-code)
  - [Check SDKs for 16 KB support](https://developer.android.com/guide/practices/page-sizes#check-sdks)
- [Test your app in a 16 KB environment](https://developer.android.com/guide/practices/page-sizes#test)
  - [Set up the Android Emulator with a 16-KB-based system image](https://developer.android.com/guide/practices/page-sizes#16kb-emulator)
  - [Enable 16 KB mode on a device using developer options](https://developer.android.com/guide/practices/page-sizes#developer-option)
- [16 KB backcompat mode](https://developer.android.com/guide/practices/page-sizes#16kb-backcompat)

- [Android Developers](https://developer.android.com/)
- [Develop](https://developer.android.com/develop)
- [Devices](https://developer.android.com/develop/devices)
- [Compatibility](https://developer.android.com/guide/practices/compatibility)

Was this helpful?

# Support 16 KB page sizes    Stay organized with collections      Save and categorize content based on your preferences.

- On this page
- [Google Play compatibility requirement](https://developer.android.com/guide/practices/page-sizes#google-play-compatibility-requirement)
- [Benefits and performance gains](https://developer.android.com/guide/practices/page-sizes#benefits)
- [Check if your app is impacted](https://developer.android.com/guide/practices/page-sizes#16-kb-impact)
  - [Does your app use native code?](https://developer.android.com/guide/practices/page-sizes#native-code)
  - [Identify native libraries using APK Analyzer](https://developer.android.com/guide/practices/page-sizes#identify-native-code)
  - [Detect alignment issues with automated checks](https://developer.android.com/guide/practices/page-sizes#auto-checks)
  - [Check the alignment of ELF segments for shared libraries](https://developer.android.com/guide/practices/page-sizes#elf-alignment)
  - [Check the RELRO security flag](https://developer.android.com/guide/practices/page-sizes#relro-flag)
- [Build your app with support for 16 KB devices](https://developer.android.com/guide/practices/page-sizes#build)
  - [Update the packaging of your shared libraries](https://developer.android.com/guide/practices/page-sizes#update-packaging)
  - [Compile your app using 16 KB ELF alignment](https://developer.android.com/guide/practices/page-sizes#compile-16-kb-alignment)
  - [Fix code and resolve runtime issues](https://developer.android.com/guide/practices/page-sizes#check-code)
  - [Check SDKs for 16 KB support](https://developer.android.com/guide/practices/page-sizes#check-sdks)
- [Test your app in a 16 KB environment](https://developer.android.com/guide/practices/page-sizes#test)
  - [Set up the Android Emulator with a 16-KB-based system image](https://developer.android.com/guide/practices/page-sizes#16kb-emulator)
  - [Enable 16 KB mode on a device using developer options](https://developer.android.com/guide/practices/page-sizes#developer-option)
- [16 KB backcompat mode](https://developer.android.com/guide/practices/page-sizes#16kb-backcompat)

Historically, Android has only supported 4 KB memory page sizes, which has
optimized system memory performance for the average amount of total memory that
Android devices have typically had. Beginning with Android 15, AOSP supports
devices that are configured to use a page size of 16 KB (16 KB
devices). If your app uses any [NDK](https://developer.android.com/ndk) libraries, either directly
or indirectly through an SDK, then you will need to rebuild your app for it to
work on these 16 KB devices.

As device manufacturers continue to build devices with larger amounts of
physical memory (RAM), many of these devices will adopt 16 KB (and
eventually greater) page sizes to optimize the device's performance. Adding
support for 16 KB page size devices enables your app to run on these
devices and helps your app benefit from the associated performance
improvements. Without recompiling, apps won't work on 16 KB devices in
future Android releases.

To help you add support for your app, we've provided guidance on how to [check\\
if your app is impacted](https://developer.android.com/guide/practices/page-sizes#16-kb-impact), how to
[rebuild your app](https://developer.android.com/guide/practices/page-sizes#build) (if applicable), and how to [test your app in\\
a 16 KB environment](https://developer.android.com/guide/practices/page-sizes#test) using emulators (including Android 15
system images for the Android Emulator).

## Google Play compatibility requirement

To ensure your app works correctly on the latest versions of Android, all
apps targeting Android 15 (API level 35) and higher must support 16 KB
memory page sizes on 64-bit devices on Google Play. Starting February 1, 2027, if
your app updates don't support 16 KB memory page sizes, you won't be able
to release these updates.

![Google Play Console warning that app updates must support 16 KB memory page sizes by February 1, 2027](https://developer.android.com/static/images/guide/practices/play-console-16kb.png)**Figure 1.** Google Play Console compatibility warning.

## Benefits and performance gains

Devices configured with 16 KB page sizes use slightly more memory on
average, but also gain various performance improvements for both the system and
apps:

- Lower app launch times while the system is under memory pressure: 3.16%
lower on average, with more significant improvements (up to 30%) for some
apps that we tested
- Reduced power draw during app launch: 4.56% reduction on average
- Faster camera launch: 4.48% faster hot starts on average, and 6.60% faster
cold starts on average
- Improved system boot time: improved by 8% (approximately 950 milliseconds)
on average

These improvements are based on our initial testing, and results on actual
devices will likely differ. We'll provide additional analysis of potential gains
for apps as we continue our testing.

## Check if your app is impacted

If your app [uses any native code](https://developer.android.com/guide/practices/page-sizes#native-code), then you should [rebuild\\
your app with support for 16 KB devices](https://developer.android.com/guide/practices/page-sizes#build). If you are unsure
if your app uses native code, you can [use the APK Analyzer to identify whether\\
any native code is present](https://developer.android.com/guide/practices/page-sizes#identify-native-code) and then [check the alignment of ELF\\
segments for any shared libraries](https://developer.android.com/guide/practices/page-sizes#elf-alignment) that you find. Android Studio
also provides features that help you to [automatically detect alignment\\
issues](https://developer.android.com/guide/practices/page-sizes#auto-checks).

If your app only uses code written in the Java programming language or in
Kotlin, including all libraries or SDKs, then your app already supports
16 KB devices. Nevertheless, we recommend that you [test your app in a\\
16 KB environment](https://developer.android.com/guide/practices/page-sizes#test) to verify that there are no unexpected
regressions in app behavior.

### Does your app use native code?

Your app makes use of native code if any of the following apply:

- Your app uses any C/C++ (native) code. If your app uses the [Android\\
NDK](https://developer.android.com/ndk), then your app uses native code.
- Your app links with any third-party native libraries or dependencies (such
as SDKs) that use them.
- Your app is built by a third-party app builder that uses native libraries on
device.

### Identify native libraries using APK Analyzer

[APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer) is a tool that lets you evaluate various aspects of a built
APK. To check whether your app uses native code (regardless of whether it is
16 KB compatible):

1. Open _Android Studio_, then click **File > Open** and choose any project.
2. From the menu bar, click **Build > Analyze APK...**
![Studio Build menu option to launch APK Analyzer](https://developer.android.com/static/images/guide/practices/studio-analyze-apk-option.png)
3. Choose the APK you want to analyze.

4. Look within the `lib` folder, which hosts shared object (`.so`) files if any
are present. If any shared object files are present, your app uses native
code. The _Alignment_ column displays warning messages for any files that
have alignment issues. If no shared object files are present or there is no
`lib` folder, then your app doesn't use native code.
![APK Analyzer view showing that shared object files are present](https://developer.android.com/static/images/guide/practices/apk-analyzer-so-files.png)

### Detect alignment issues with automated checks

Android Studio warns you proactively if your prebuilt libraries or APKs aren't
16 KB compliant. Use the [APK\\
Analyzer](https://developer.android.com/guide/practices/page-sizes#identify-native-code) tool to review which libraries need to be
updated or if any code changes are required.

![Studio warning notifications about alignment issues in a project](https://developer.android.com/static/images/guide/practices/studio-align-warnings.png)

[Lint in Android Studio](https://developer.android.com/studio/write/lint) also highlights native libraries that
aren't 16 KB aligned.

![Studio linter warning about a non-aligned native library](https://developer.android.com/static/images/guide/practices/studio-align-lint.png)

### Check the alignment of ELF segments for shared libraries

For any shared libraries, verify that the shared libraries' ELF segments are
aligned properly using 16 KB ELF alignment. If you are developing on either
Linux or macOS, you can use the `check_elf_alignment.sh` script as described in
the following section. You can also [use the command-line tools directly](https://developer.android.com/guide/practices/page-sizes#alignment-use-tools).

#### Use the check\_elf\_alignment.sh script (Linux or macOS)

Follow these steps to check the alignment of ELF segments using the
`check_elf_alignment.sh` script:

1. Save the [`check_elf_alignment.sh`](https://cs.android.com/android/platform/superproject/main/+/main:system/extras/tools/check_elf_alignment.sh) script to a file.

2. Run the script on your app's APK file:








```
check_elf_alignment.sh APK_NAME.apk
```


The script outputs either `ALIGNED` or `UNALIGNED` for all the `arm64-v8a`
shared libraries.

3. If any `arm64-v8a` or `x86_64` shared libraries are `UNALIGNED`, you'll need
to [update the packaging for those libraries](https://developer.android.com/guide/practices/page-sizes#update-packaging), then [recompile your\\
app](https://developer.android.com/guide/practices/page-sizes#compile-16-kb-alignment) and retest by following the steps in this section.


#### Use command-line tools directly

Follow these steps to check the alignment of ELF segments using command-line
tools directly:

1. Make sure both Android SDK Build-Tools version 35.0.0 or higher and the
Android NDK are installed using the [SDK Manager in Android Studio](https://developer.android.com/studio/intro/update#sdk-manager) or
[`sdkmanager`](https://developer.android.com/tools/sdkmanager) command-line tool.
2. Extract your app's APK file:



[Linux or macOS](https://developer.android.com/guide/practices/page-sizes#linux-or-macos)[Windows (PowerShell)](https://developer.android.com/guide/practices/page-sizes#windows-powershell)More















```
unzip APK_NAME.apk -d /tmp/my_apk_out
```











```
Expand-Archive -Path .\APK_NAME.apk -DestinationPath ~\tmp\my_apk_out
```

3. In the temporary directory that you extracted your APK file to, check the
contents of the `lib` directory for shared object (`.so`) files. These are
the same shared object files that you would've seen while [identifying\\
native libraries using APK Analyzer](https://developer.android.com/guide/practices/page-sizes#identify-native-code). Run the following command on each
shared object file:



[Linux or macOS](https://developer.android.com/guide/practices/page-sizes#linux-or-macos)[Windows (PowerShell)](https://developer.android.com/guide/practices/page-sizes#windows-powershell)More















```
SDK_ROOT_LOCATION/Android/sdk/ndk/NDK_VERSION/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-objdump -p SHARED_OBJECT_FILE.so | grep LOAD
```











```
SDK_ROOT_LOCATION\Android\sdk\ndk\NDK_VERSION\toolchains\llvm\prebuilt\windows-x86_64\bin\llvm-objdump.exe -p SHARED_OBJECT_FILE.so | Select-String -Pattern "LOAD"
```



Where `SDK_ROOT_LOCATION` is the path to the
directory where you've installed the Android SDK,
`SHARED_OBJECT_FILE` is the name of the shared object
file that you're checking, and `NDK_VERSION` is the
version of the Android NDK that you have installed (for example,
`28.0.12433566`). The output will look something like the following for each
file you check:








```
LOAD off    0x0000000000000000 vaddr 0x0000000000000000 paddr 0x0000000000000000 align 2**14
LOAD off    0x0000000000042a90 vaddr 0x0000000000043a90 paddr 0x0000000000043a90 align 2**14
LOAD off    0x0000000000046230 vaddr 0x0000000000048230 paddr 0x0000000000048230 align 2**14
```

4. Check the output lines to ensure that the load segments don't have values
less than `2**14`. If any load segments are `2**13`, `2**12`, or lower
values, you'll need to [update the packaging for those libraries](https://developer.android.com/guide/practices/page-sizes#update-packaging), then
[recompile your app](https://developer.android.com/guide/practices/page-sizes#compile-16-kb-alignment) and retest by following the steps in this section.

5. Next, run the `zipalign` command-line tool on your app's APK file:



[Linux or macOS](https://developer.android.com/guide/practices/page-sizes#linux-or-macos)[Windows (PowerShell)](https://developer.android.com/guide/practices/page-sizes#windows-powershell)More















```
SDK_ROOT_LOCATION/Android/sdk/build-tools/35.0.0/zipalign -v -c -P 16 4 APK_NAME.apk
```











```
SDK_ROOT_LOCATION\Android\sdk\build-tools\35.0.0\zipalign.exe -v -c -P 16 4 APK_NAME.apk
```



Where `SDK_ROOT_LOCATION` is the path to the
directory where you've installed the Android SDK, and
`APK_NAME` is the name of your app's APK file. The
last line of the output will say "Verification successful" if all of the
shared libraries are aligned correctly.

If the verification failed, some shared libraries need to be realigned, so
you'll need to [update the packaging for those libraries](https://developer.android.com/guide/practices/page-sizes#update-packaging), then
[recompile your app](https://developer.android.com/guide/practices/page-sizes#compile-16-kb-alignment) and retest by following the steps in this section.


### Check the RELRO security flag

To mitigate security exploits, modern linkers use the
[Relocation Read-Only (RELRO)](https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro) flag to make relocation
sections of the shared object file read-only after loading.
Combining a RELRO-enabled section with a non-RELRO-enabled
section (from another object file) on the same page crashes an app.

Run the following command on each shared object file (Linux or macOS):

```
SDK_ROOT_LOCATION/Android/sdk/ndk/NDK_VERSION/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-readelf -l SHARED_OBJECT_FILE.so | grep RELRO
```

Check the command output to ensure that the `GNU_RELRO` string is printed, which
confirms that the `.so` file is RELRO-enabled.

## Build your app with support for 16 KB devices

If your app uses native code, then complete the steps that are outlined in the
following sections to make sure that your app supports 16 KB devices:

1. [Update the packaging of your shared libraries](https://developer.android.com/guide/practices/page-sizes#update-packaging)
2. [Compile your app using 16 KB ELF alignment](https://developer.android.com/guide/practices/page-sizes#compile-16-kb-alignment)
3. [Fix code and resolve runtime issues](https://developer.android.com/guide/practices/page-sizes#check-code)
4. [Check SDKs for 16 KB support](https://developer.android.com/guide/practices/page-sizes#check-sdks)

### Update the packaging of your shared libraries

Upgrade to AGP version 8.5.1 or higher and use uncompressed shared libraries.

#### Use `bundletool` to verify zip alignment

To see the alignment of your bundle, use:

```
bundletool dump config --bundle=<my .aab>  | grep alignment
```

If you see `PAGE_ALIGNMENT_16K` then you know your bundle requests 16 KB
zip alignment. If you see `PAGE_ALIGNMENT_4K`, this instructs the APK built from
this AAB to have 4 KB aligned .so files in the zip file.

#### AGP version 8.5.1 or higher

16 KB devices require apps that ship with uncompressed shared libraries to
align them on a 16 KB zip-aligned boundary. To do this, you need to upgrade
to Android Gradle Plugin (AGP) version 8.5.1 or higher. Refer to the [Android\\
Gradle plugin Upgrade Assistant](https://developer.android.com/build/agp-upgrade-assistant) section for details on the upgrade process.

#### AGP version 8.5 or lower

If you can't upgrade AGP to version 8.5.1 or higher, then the alternative is to
switch to use compressed shared libraries. Update your Gradle configuration to
have Gradle compress your shared libraries when packaging your app to avoid app
installation issues with unaligned shared libraries.

[Groovy](https://developer.android.com/guide/practices/page-sizes#groovy)[Kotlin](https://developer.android.com/guide/practices/page-sizes#kotlin)More

In your `build.gradle` file, add the following option:

```
android {
  ...
  packagingOptions {
      jniLibs {
        useLegacyPackaging true
      }
  }
}
```

In your `build.gradle.kts` file, add the following option:

```
android {
  ...
  packagingOptions {
      jniLibs {
        useLegacyPackaging = true
      }
  }
}
```

##### AGP version 8.0 or lower

If you are using an AGP version same or lower than 8.0, you also need to disable
the uncompressed native library option for App Bundles in your
`gradle.properties` file:

```
android.bundle.enableUncompressedNativeLibs=false
```

### Compile your app using 16 KB ELF alignment

16 KB devices require the shared libraries' ELF segments to be aligned
properly using 16 KB ELF alignment in order for your app to run.

For game developers, if your game runs on top of [Unity game engine](https://unity.com/), refer
to the [Unity guide](https://developer.android.com/games/engines/unity/unity-on-android#16-kb-page-support). If your game runs on top of [Unreal game engine](https://www.unrealengine.com/),
refer to the [Unreal guide](https://developer.android.com/games/engines/unreal/unreal-on-android#16-kb-page-support). For native game engines, continue with
this guide.

To compile your app using 16 KB ELF alignment, complete the steps in one of
the following sections depending on the version of the Android NDK that you're
using.

#### Android NDK r28 and higher

NDK version r28 and higher compile 16 KB-aligned by default.

#### Android NDK r27 and lower

To support compiling 16 KB-aligned shared libraries with Android NDK
version r27 or lower, use the following linker flags:

```
-Wl,-z,max-page-size=16384
-Wl,-z,common-page-size=16384
```

Here's how to update your build system configuration files:

[ndk-build](https://developer.android.com/guide/practices/page-sizes#ndk-build)[CMake](https://developer.android.com/guide/practices/page-sizes#cmake)More

If you're using ndk-build, update your `Android.mk` to enable 16 KB ELF
alignment:

```
LOCAL_LDFLAGS += -Wl,-z,max-page-size=16384 -Wl,-z,common-page-size=16384
```

If you're using CMake, update your `CMakeLists.txt` to enable 16 KB ELF
alignment:

```
target_link_options(${CMAKE_PROJECT_NAME} PRIVATE
    "-Wl,-z,max-page-size=16384"
    "-Wl,-z,common-page-size=16384"
)
```

### Fix code and resolve runtime issues

Even if your app is 16 KB-aligned, your app can encounter errors if places
in your code assume that a device is using a specific page size. To avoid this,
complete the following steps:

1. Remove any hard-coded dependencies that reference the [`PAGE_SIZE`](https://cs.android.com/android/platform/superproject/main/+/main:bionic/libc/include/bits/page_size.h;l=34-39)
constant or instances in your code logic that assume that a device's page
size is 4 KB (`4096`).

Use [`getpagesize()`](https://cs.android.com/android/platform/superproject/main/+/main:bionic/libc/bionic/getpagesize.cpp;l=32) or [`sysconf(_SC_PAGESIZE)`](https://cs.android.com/android/platform/superproject/main/+/main:bionic/libc/bionic/sysconf.cpp;l=151) instead.

2. Look for usages of [`mmap()`](https://cs.android.com/android/platform/superproject/main/+/main:bionic/libc/bionic/mmap.cpp;l=59) and other APIs that require page-aligned
arguments and replace with alternatives where necessary.


In some cases, if your app uses `PAGE_SIZE` as a convenient value that isn't
tied to the underlying page size, then this won't cause your app to break when
used in 16 KB mode. However, if this value is passed to the kernel with
`mmap` without `MAP_FIXED`, the kernel still uses an entire page, which wastes
some memory. For these reasons, `PAGE_SIZE` is undefined when 16 KB mode is
enabled on NDK r27 and higher.

If your app uses `PAGE_SIZE` in this way and never directly passes this value to
the kernel, then instead of using `PAGE_SIZE`, create a new variable with a new
name to reflect that it is used for other purposes and does not reflect a real
memory page.

### Check SDKs for 16 KB support

Many SDKs are compatible with 16 KB page sizes, especially if you build
them yourself or get recent prebuilts. However, because some SDK prebuilts or
SDK versions aren't 16 KB compatible, you should check the website for each
SDK provider to determine which version to use with 16 KB.

## Test your app in a 16 KB environment

After you build your app with support for 16 KB devices, you'll want to
test your app in a 16 KB environment to see whether your app experiences
any regressions. To do this, follow these steps:

1. Set up the [Android 15 SDK](https://developer.android.com/about/versions/15/setup-sdk) or higher.

2. Set up one of the following testing environments:

   - [Set up the Android Emulator with a 16 KB–based, Android 15 system\\
     image](https://developer.android.com/guide/practices/page-sizes#16kb-emulator)
     - [Use Cuttlefish with 16 KB page size on ARM64](https://source.android.com/docs/core/architecture/16kb-page-size/getting-started-cf-arm64-pgagnostic)
   - [Simulate Cuttlefish with 16 KB page size on x86-64](https://source.android.com/docs/core/architecture/16kb-page-size/getting-started-cf-x86-64-pgagnostic)
   - [Enable 16 KB mode on a device using developer options](https://developer.android.com/guide/practices/page-sizes#developer-option)
   - [Use Samsung Remote Test Lab](https://developer.samsung.com/remote-test-lab/blog/en/2025/07/07/optimize-your-applications-for-16-kb-page-size-compatibility-using-samsungs-remote-test-lab) on 16 KB
     [supported devices](https://developer.samsung.com/remotetestlab/devices/129/16kb-page-size)
3. Start up your test device, then run the following command to verify that
it's using a 16 KB environment:








```
adb shell getconf PAGE_SIZE
```


The command should return a value of `16384`.

4. Run the following [`zipalign`](https://developer.android.com/tools/zipalign) command to verify that your app is
16 KB-aligned, where APK\_NAME is the name of
your app's APK file:








```
zipalign -c -P 16 -v 4 APK_NAME.apk
```

5. Thoroughly test your app, focusing on any areas that might be affected by
[changing code instances that reference specific page sizes](https://developer.android.com/guide/practices/page-sizes#check-code).


### Set up the Android Emulator with a 16-KB-based system image

To set up a 16 KB environment using the Android Emulator, follow these
steps:

1. In Android Studio, click **Tools > SDK Manager**.
2. In the **SDK Platforms** tab, check **Show Package Details**, then expand
the **Android VanillaIceCream** or higher section and select one or both of
the following emulator system images, depending on the virtual devices you
want to create:


   - Google APIs Experimental 16 KB Page Size ARM 64 v8a System Image
   - Google APIs Experimental 16 KB Page Size Intel x86\_64 Atom System
     Image

![Download 16 KB emulator system images using the SDK Manager in Android Studio](https://developer.android.com/static/images/guide/practices/16kb-emulator-images.png)
3. Click **Apply > OK** to download whichever system images you selected.

4. Follow the steps to [set up a virtual device for Android 15](https://developer.android.com/about/versions/15/get#on_emulator), and when
prompted to select a system image, select the 16 KB system image that
you downloaded. If it's not recommended automatically, you can find the
16 KB system image in the **Other Images** tab.
![Find the 16 KB emulator image in the Other Images tab](https://developer.android.com/static/images/guide/practices/16kb-other-images-tab.png)

#### Launch the emulator

After you finish setting up the Android Emulator and virtual devices, launch the
emulator [from the target device menu](https://developer.android.com/studio/run/emulator#runningapp), or [from the command line](https://developer.android.com/studio/run/emulator-commandline).

### Enable 16 KB mode on a device using developer options

![](https://developer.android.com/static/images/guide/practices/16-kb-dev-option.png)

Toggle the **Boot with 16KB page size** developer
option to boot a device in 16 KB mode.

In QPR versions of Android 15, you can
[use the developer option](https://source.android.com/docs/core/architecture/16kb-page-size/16kb-developer-option#use_16kb_toggle) that's available on certain
devices to boot the device in 16 KB mode and perform on-device testing.
Before using the developer option, go to **Settings > System > Software**
**updates** and apply any updates that are available.

This developer option is available on the following devices:

- Pixel 8 and 8 Pro (with Android 15 QPR1 or higher)

- Pixel 8a (with Android 15 QPR1 or higher)

- Pixel 9, 9 Pro, and 9 Pro XL (with Android 15 QPR2 or higher)

- Pixel 9a (with Android 16 or higher)


## 16 KB backcompat mode

![Warning in page size compat mod](https://developer.android.com/static/images/guide/practices/appcompat-dialog-16kb.png)

Warning in page size compat mode

The 16 KB backcompat option is available when a device is running with a
16 KB kernel. The package manager runs an app in 16 KB backcompat mode
when the following conditions are met:

- If the app has ELF files (with an `.so` extension) with a LOAD segment
alignment of 4 KB.
- If the zipped APK has uncompressed ELF files that are 4 KB
ZIP aligned.

If the package manager has enabled 16 KB backcompat mode for
an app, the app displays a warning when it's first launched saying that it's
running in 16 KB backcompat mode.

16 KB backcompat mode allows some apps to work,
but for best reliability and stability, apps should still be 16 KB aligned.

On the app info page, under **Advanced**, toggle the setting **Run app with**
**page size compat mode** to enable or disable the 16 KB backcompat mode
for specific app. This setting is visible only when the device is running with
16 KB page size.

![Page size compat mode setting](https://developer.android.com/static/images/guide/practices/appcompat-setting-16kb.png)

_Page size compat mode setting_

To force 16 KB backcompat on for every app on the device:

```
adb shell setprop bionic.linker.16kb.app_compat.enabled true
adb shell setprop pm.16kb.app_compat.disabled false
```

To force 16 KB backcompat off for every app on the device:

```
adb shell setprop bionic.linker.16kb.app_compat.enabled false
adb shell setprop pm.16kb.app_compat.disabled true
```

In Android 17, you can also force 16 KB backcompat off for every app and
cause any incompatible binary to immediately abort:

```
    adb shell setprop bionic.linker.16kb.app_compat.enabled fatal
    adb shell setprop pm.16kb.app_compat.disabled true
```

Set the `android:pageSizeCompat` property to enabled or disabled to turn on or
off backcompat mode for a specific app in its `AndroidManifest.xml`. When this
property is set, the app won't display backcompat mode warnings when it
launches.

Was this helpful?

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-08-23 UTC.




\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-08-23 UTC."\],\[\],\[\]\]
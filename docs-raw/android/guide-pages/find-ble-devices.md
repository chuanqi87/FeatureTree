[Skip to main content](https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices#main-content)

[![Android Developers](https://www.gstatic.com/devrel-devsite/prod/v6c08f9bb601564cd99488472d05cdf6fb06f007f31b6552465782b15883ce123/android/images/lockup.png)](https://developer.android.com/)

`/`

- English
- Deutsch
- Español – América Latina
- Français
- Indonesia
- Italiano
- Polski
- Português – Brasil
- Tiếng Việt
- Türkçe
- Русский
- עברית
- العربيّة
- فارسی
- हिंदी
- বাংলা
- ภาษาไทย
- 中文 – 简体
- 中文 – 繁體
- 日本語
- 한국어

[Android Studio](https://developer.android.com/studio)Sign in

- [Develop](https://developer.android.com/develop)
- [Core areas](https://developer.android.com/develop/core-areas)
- [Connectivity](https://developer.android.com/develop/connectivity)

- [Android Developers](https://developer.android.com/)
- [Develop](https://developer.android.com/develop)
- [Core areas](https://developer.android.com/develop/core-areas)
- [Connectivity](https://developer.android.com/develop/connectivity)
- [Guides](https://developer.android.com/develop/connectivity/overview)

# Find BLE devices    Stay organized with collections      Save and categorize content based on your preferences.

To find BLE devices, you use the
[`startScan()`](https://developer.android.com/reference/android/bluetooth/le/BluetoothLeScanner#startScan(android.bluetooth.le.ScanCallback))
method. This method takes a
[`ScanCallback`](https://developer.android.com/reference/android/bluetooth/le/ScanCallback) as a parameter.
You must implement this callback, because that is how scan results are returned.
Because scanning is battery-intensive, you should observe the following
guidelines:

- As soon as you find the desired device, stop scanning.
- Never scan on a loop, and always set a time limit on your scan. A device that
was previously available may have moved out of range, and continuing to scan
drains the battery.

In the following example, the BLE app provides an activity
(`DeviceScanActivity`) to scan for available Bluetooth LE devices and display
them in a list to the user. The following snippet shows how to start and stop a
scan:

### Kotlin

```
private val bluetoothLeScanner = bluetoothAdapter.bluetoothLeScanner
private var scanning = false
private val handler = Handler()

// Stops scanning after 10 seconds.
private val SCAN_PERIOD: Long = 10000

private fun scanLeDevice() {
    if (!scanning) { // Stops scanning after a pre-defined scan period.
        handler.postDelayed({
            scanning = false
            bluetoothLeScanner.stopScan(leScanCallback)
        }, SCAN_PERIOD)
        scanning = true
        bluetoothLeScanner.startScan(leScanCallback)
    } else {
        scanning = false
        bluetoothLeScanner.stopScan(leScanCallback)
    }
}
```

### Java

```
private BluetoothLeScanner bluetoothLeScanner = bluetoothAdapter.getBluetoothLeScanner();
private boolean scanning;
private Handler handler = new Handler();

// Stops scanning after 10 seconds.
private static final long SCAN_PERIOD = 10000;

private void scanLeDevice() {
    if (!scanning) {
        // Stops scanning after a predefined scan period.
        handler.postDelayed(new Runnable() {
            @Override
            public void run() {
                scanning = false;
                bluetoothLeScanner.stopScan(leScanCallback);
            }
        }, SCAN_PERIOD);

        scanning = true;
        bluetoothLeScanner.startScan(leScanCallback);
    } else {
        scanning = false;
        bluetoothLeScanner.stopScan(leScanCallback);
    }
}
```

To scan for only specific types of peripherals, you can instead call
[`startScan(List<ScanFilter>, ScanSettings, ScanCallback)`](https://developer.android.com/reference/android/bluetooth/le/BluetoothLeScanner#startScan(java.util.List%3Candroid.bluetooth.le.ScanFilter%3E,%20android.bluetooth.le.ScanSettings,%20android.bluetooth.le.ScanCallback)),
providing a list of [`ScanFilter`](https://developer.android.com/reference/android/bluetooth/le/ScanFilter)
objects that restrict the devices that the scan looks for and a
[`ScanSettings`](https://developer.android.com/reference/android/bluetooth/le/ScanSettings) object that
specifies parameters about the scan.

The following code sample is an implementation of
[`ScanCallback`](https://developer.android.com/reference/android/bluetooth/le/ScanCallback),
which is the interface used to deliver BLE scan results. When results are found,
they are added to a list adapter in the `DeviceScanActivity` to display to the
user.

### Kotlin

```
private val leDeviceListAdapter = LeDeviceListAdapter()
// Device scan callback.
private val leScanCallback: ScanCallback = object : ScanCallback() {
    override fun onScanResult(callbackType: Int, result: ScanResult) {
        super.onScanResult(callbackType, result)
        leDeviceListAdapter.addDevice(result.device)
        leDeviceListAdapter.notifyDataSetChanged()
    }
}
```

### Java

```
private LeDeviceListAdapter leDeviceListAdapter = new LeDeviceListAdapter();

// Device scan callback.
private ScanCallback leScanCallback =
        new ScanCallback() {
            @Override
            public void onScanResult(int callbackType, ScanResult result) {
                super.onScanResult(callbackType, result);
                leDeviceListAdapter.addDevice(result.getDevice());
                leDeviceListAdapter.notifyDataSetChanged();
            }
        };
```

Content and code samples on this page are subject to the licenses described in the [Content License](https://developer.android.com/license). Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.




\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-02-26 UTC."\],\[\],\[\]\]
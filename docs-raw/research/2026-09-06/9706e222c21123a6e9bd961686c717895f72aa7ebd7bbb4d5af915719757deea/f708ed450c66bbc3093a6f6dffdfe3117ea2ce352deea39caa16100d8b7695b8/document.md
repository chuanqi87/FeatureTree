# ScanFilter

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

Summary:
[Nested Classes](https://developer.android.com/reference/android/bluetooth/le/ScanFilter#nestedclasses)
| [Inherited Constants](https://developer.android.com/reference/android/bluetooth/le/ScanFilter#inhconstants)
| [Fields](https://developer.android.com/reference/android/bluetooth/le/ScanFilter#lfields)
| [Methods](https://developer.android.com/reference/android/bluetooth/le/ScanFilter#pubmethods)
| [Inherited Methods](https://developer.android.com/reference/android/bluetooth/le/ScanFilter#inhmethods)



# ScanFilter

---

[Kotlin](https://developer.android.com/reference/kotlin/android/bluetooth/le/ScanFilter "View this page in Kotlin")
|Java

`public
final
class
ScanFilter`
  
`extends Object`
`implements
Parcelable`

|  |  |
| --- | --- |
| [java.lang.Object](https://developer.android.com/reference/java/lang/Object) | |
| ↳ | android.bluetooth.le.ScanFilter |

  

---

Criteria for filtering result from Bluetooth LE scans. A `ScanFilter` allows clients to
restrict scan results to only those that are of interest to them.

Current filtering on the following fields are supported:- Service UUIDs which identify the bluetooth gatt services running on the device.- Name of remote Bluetooth LE device.- Mac address of the remote device.- Service data which is the data associated with a service.- Manufacturer specific data which is the data associated with a particular manufacturer.- Advertising data type and corresponding data.

**See also:**

* `ScanResult`
* `BluetoothLeScanner`

## Summary



| Nested classes | |
| --- | --- |
| `class` | `ScanFilter.Builder` Builder class for `ScanFilter`. |


| Inherited constants |
| --- |
| From interface `android.os.Parcelable`  |  |  | | --- | --- | | `int` | `CONTENTS_FILE_DESCRIPTOR` Descriptor bit used with `describeContents()`: indicates that the Parcelable object's flattened representation includes a file descriptor. | | `int` | `PARCELABLE_WRITE_RETURN_VALUE` Flag for use with `writeToParcel(Parcel, int)`: the object being written is a return value, that is the result of a function such as "`Parcelable someFunction()`", "`void someFunction(out Parcelable)`", or "`void someFunction(inout Parcelable)`". | |



| Fields | |
| --- | --- |
| `public static final Creator<ScanFilter>` | `CREATOR` A `Parcelable.Creator` to create `ScanFilter` from parcel. |



| Public methods | |
| --- | --- |
| `int` | `describeContents()` Describe the kinds of special objects contained in this Parcelable instance's marshaled representation. |
| `boolean` | `equals(Object obj)` Indicates whether some other object is "equal to" this one. |
| `byte[]` | `getAdvertisingData()` Returns the advertising data of this filter. |
| `byte[]` | `getAdvertisingDataMask()` Returns the advertising data mask of this filter. |
| `int` | `getAdvertisingDataType()` Returns the advertising data type of this filter. |
| `String` | `getDeviceAddress()` |
| `String` | `getDeviceName()` Returns the filter set the device name field of Bluetooth advertisement data. |
| `byte[]` | `getManufacturerData()` |
| `byte[]` | `getManufacturerDataMask()` |
| `int` | `getManufacturerId()` Returns the manufacturer id. |
| `byte[]` | `getServiceData()` |
| `byte[]` | `getServiceDataMask()` |
| `ParcelUuid` | `getServiceDataUuid()` |
| `ParcelUuid` | `getServiceSolicitationUuid()` Returns the filter set on the service Solicitation uuid. |
| `ParcelUuid` | `getServiceSolicitationUuidMask()` Returns the filter set on the service Solicitation uuid mask. |
| `ParcelUuid` | `getServiceUuid()` Returns the filter set on the service uuid. |
| `ParcelUuid` | `getServiceUuidMask()` |
| `int` | `hashCode()` Returns a hash code value for the object. |
| `boolean` | `matches(ScanResult scanResult)` Check if the scan filter matches a `scanResult`. |
| `String` | `toString()` Returns a string representation of the object. |
| `void` | `writeToParcel(Parcel dest, int flags)` Flatten this object in to a Parcel. |



| Inherited methods |
| --- |
| From class `java.lang.Object`  |  |  | | --- | --- | | `Object` | `clone()` Creates and returns a copy of this object. | | `boolean` | `equals(Object obj)` Indicates whether some other object is "equal to" this one. | | `void` | `finalize()` Called by the garbage collector on an object when garbage collection determines that there are no more references to the object. | | `final Class<?>` | `getClass()` Returns the runtime class of this `Object`. | | `int` | `hashCode()` Returns a hash code value for the object. | | `final void` | `notify()` Wakes up a single thread that is waiting on this object's monitor. | | `final void` | `notifyAll()` Wakes up all threads that are waiting on this object's monitor. | | `String` | `toString()` Returns a string representation of the object. | | `final void` | `wait(long timeoutMillis, int nanos)` Causes the current thread to wait until it is awakened, typically by being *notified* or *interrupted*, or until a certain amount of real time has elapsed. | | `final void` | `wait(long timeoutMillis)` Causes the current thread to wait until it is awakened, typically by being *notified* or *interrupted*, or until a certain amount of real time has elapsed. | | `final void` | `wait()` Causes the current thread to wait until it is awakened, typically by being *notified* or *interrupted*. | | |
| From interface `android.os.Parcelable`  |  |  | | --- | --- | | `abstract int` | `describeContents()` Describe the kinds of special objects contained in this Parcelable instance's marshaled representation. | | `abstract void` | `writeToParcel(Parcel dest, int flags)` Flatten this object in to a Parcel. | | |







## Fields

### CREATOR

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public static final Creator<ScanFilter> CREATOR
```

A `Parcelable.Creator` to create `ScanFilter` from parcel.







## Public methods

### describeContents

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public int describeContents ()
```

Describe the kinds of special objects contained in this Parcelable
instance's marshaled representation. For example, if the object will
include a file descriptor in the output of `writeToParcel(Parcel,int)`,
the return value of this method must include the
`CONTENTS_FILE_DESCRIPTOR` bit.

| Returns | |
| --- | --- |
| `int` | a bitmask indicating the set of special object types marshaled by this Parcelable object instance.   Value is either `0` or  * `CONTENTS_FILE_DESCRIPTOR` |

### equals

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public boolean equals (Object obj)
```

Indicates whether some other object is "equal to" this one.

The `equals` method implements an equivalence relation
on non-null object references:

* It is *reflexive*: for any non-null reference value
  `x`, `x.equals(x)` should return
  `true`.* It is *symmetric*: for any non-null reference values
    `x` and `y`, `x.equals(y)`
    should return `true` if and only if
    `y.equals(x)` returns `true`.* It is *transitive*: for any non-null reference values
      `x`, `y`, and `z`, if
      `x.equals(y)` returns `true` and
      `y.equals(z)` returns `true`, then
      `x.equals(z)` should return `true`.* It is *consistent*: for any non-null reference values
        `x` and `y`, multiple invocations of
        `x.equals(y)` consistently return `true`
        or consistently return `false`, provided no
        information used in `equals` comparisons on the
        objects is modified.* For any non-null reference value `x`,
          `x.equals(null)` should return `false`.

An equivalence relation partitions the elements it operates on
into *equivalence classes*; all the members of an
equivalence class are equal to each other. Members of an
equivalence class are substitutable for each other, at least
for some purposes.

| Parameters | |
| --- | --- |
| `obj` | `Object`: This value may be `null`. |

| Returns | |
| --- | --- |
| `boolean` | `true` if this object is the same as the obj argument; `false` otherwise. |

### getAdvertisingData

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public byte[] getAdvertisingData ()
```

Returns the advertising data of this filter.

| Returns | |
| --- | --- |
| `byte[]` | This value may be `null`. |

### getAdvertisingDataMask

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public byte[] getAdvertisingDataMask ()
```

Returns the advertising data mask of this filter.

| Returns | |
| --- | --- |
| `byte[]` | This value may be `null`. |

### getAdvertisingDataType

Added in [API level 33](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public int getAdvertisingDataType ()
```

Returns the advertising data type of this filter. Returns `ScanRecord.DATA_TYPE_NONE`
if the type is not set. The values of advertising data type are defined in the Bluetooth
Generic Access Profile (https://www.bluetooth.com/specifications/assigned-numbers/)

| Returns | |
| --- | --- |
| `int` | Value is one of the following:  * `ScanRecord.DATA_TYPE_NONE` * `ScanRecord.DATA_TYPE_FLAGS` * `ScanRecord.DATA_TYPE_SERVICE_UUIDS_16_BIT_PARTIAL` * `ScanRecord.DATA_TYPE_SERVICE_UUIDS_16_BIT_COMPLETE` * `ScanRecord.DATA_TYPE_SERVICE_UUIDS_32_BIT_PARTIAL` * `ScanRecord.DATA_TYPE_SERVICE_UUIDS_32_BIT_COMPLETE` * `ScanRecord.DATA_TYPE_SERVICE_UUIDS_128_BIT_PARTIAL` * `ScanRecord.DATA_TYPE_SERVICE_UUIDS_128_BIT_COMPLETE` * `ScanRecord.DATA_TYPE_LOCAL_NAME_SHORT` * `ScanRecord.DATA_TYPE_LOCAL_NAME_COMPLETE` * `ScanRecord.DATA_TYPE_TX_POWER_LEVEL` * `ScanRecord.DATA_TYPE_CLASS_OF_DEVICE` * `ScanRecord.DATA_TYPE_SIMPLE_PAIRING_HASH_C` * `ScanRecord.DATA_TYPE_SIMPLE_PAIRING_RANDOMIZER_R` * `ScanRecord.DATA_TYPE_DEVICE_ID` * `ScanRecord.DATA_TYPE_SECURITY_MANAGER_OUT_OF_BAND_FLAGS` * `ScanRecord.DATA_TYPE_SLAVE_CONNECTION_INTERVAL_RANGE` * `ScanRecord.DATA_TYPE_SERVICE_SOLICITATION_UUIDS_16_BIT` * `ScanRecord.DATA_TYPE_SERVICE_SOLICITATION_UUIDS_128_BIT` * `ScanRecord.DATA_TYPE_SERVICE_DATA_16_BIT` * `ScanRecord.DATA_TYPE_PUBLIC_TARGET_ADDRESS` * `ScanRecord.DATA_TYPE_RANDOM_TARGET_ADDRESS` * `ScanRecord.DATA_TYPE_APPEARANCE` * `ScanRecord.DATA_TYPE_ADVERTISING_INTERVAL` * `ScanRecord.DATA_TYPE_LE_BLUETOOTH_DEVICE_ADDRESS` * `ScanRecord.DATA_TYPE_LE_ROLE` * `ScanRecord.DATA_TYPE_SIMPLE_PAIRING_HASH_C_256` * `ScanRecord.DATA_TYPE_SIMPLE_PAIRING_RANDOMIZER_R_256` * `ScanRecord.DATA_TYPE_SERVICE_SOLICITATION_UUIDS_32_BIT` * `ScanRecord.DATA_TYPE_SERVICE_DATA_32_BIT` * `ScanRecord.DATA_TYPE_SERVICE_DATA_128_BIT` * `ScanRecord.DATA_TYPE_LE_SECURE_CONNECTIONS_CONFIRMATION_VALUE` * `ScanRecord.DATA_TYPE_LE_SECURE_CONNECTIONS_RANDOM_VALUE` * `ScanRecord.DATA_TYPE_URI` * `ScanRecord.DATA_TYPE_INDOOR_POSITIONING` * `ScanRecord.DATA_TYPE_TRANSPORT_DISCOVERY_DATA` * `ScanRecord.DATA_TYPE_LE_SUPPORTED_FEATURES` * `ScanRecord.DATA_TYPE_CHANNEL_MAP_UPDATE_INDICATION` * `ScanRecord.DATA_TYPE_PB_ADV` * `ScanRecord.DATA_TYPE_MESH_MESSAGE` * `ScanRecord.DATA_TYPE_MESH_BEACON` * `ScanRecord.DATA_TYPE_BIG_INFO` * `ScanRecord.DATA_TYPE_BROADCAST_CODE` * `ScanRecord.DATA_TYPE_RESOLVABLE_SET_IDENTIFIER` * `ScanRecord.DATA_TYPE_ADVERTISING_INTERVAL_LONG` * `ScanRecord.DATA_TYPE_3D_INFORMATION_DATA` * `ScanRecord.DATA_TYPE_MANUFACTURER_SPECIFIC_DATA` |

### getDeviceAddress

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public String getDeviceAddress ()
```

| Returns | |
| --- | --- |
| `String` | This value may be `null`. |

### getDeviceName

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public String getDeviceName ()
```

Returns the filter set the device name field of Bluetooth advertisement data.

| Returns | |
| --- | --- |
| `String` | This value may be `null`. |

### getManufacturerData

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public byte[] getManufacturerData ()
```

| Returns | |
| --- | --- |
| `byte[]` | This value may be `null`. |

### getManufacturerDataMask

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public byte[] getManufacturerDataMask ()
```

| Returns | |
| --- | --- |
| `byte[]` | This value may be `null`. |

### getManufacturerId

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public int getManufacturerId ()
```

Returns the manufacturer id. -1 if the manufacturer filter is not set.

| Returns | |
| --- | --- |
| `int` |  |

### getServiceData

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public byte[] getServiceData ()
```

| Returns | |
| --- | --- |
| `byte[]` | This value may be `null`. |

### getServiceDataMask

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public byte[] getServiceDataMask ()
```

| Returns | |
| --- | --- |
| `byte[]` | This value may be `null`. |

### getServiceDataUuid

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public ParcelUuid getServiceDataUuid ()
```

| Returns | |
| --- | --- |
| `ParcelUuid` | This value may be `null`. |

### getServiceSolicitationUuid

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public ParcelUuid getServiceSolicitationUuid ()
```

Returns the filter set on the service Solicitation uuid.

| Returns | |
| --- | --- |
| `ParcelUuid` | This value may be `null`. |

### getServiceSolicitationUuidMask

Added in [API level 29](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public ParcelUuid getServiceSolicitationUuidMask ()
```

Returns the filter set on the service Solicitation uuid mask.

| Returns | |
| --- | --- |
| `ParcelUuid` | This value may be `null`. |

### getServiceUuid

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public ParcelUuid getServiceUuid ()
```

Returns the filter set on the service uuid.

| Returns | |
| --- | --- |
| `ParcelUuid` | This value may be `null`. |

### getServiceUuidMask

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public ParcelUuid getServiceUuidMask ()
```

| Returns | |
| --- | --- |
| `ParcelUuid` | This value may be `null`. |

### hashCode

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public int hashCode ()
```

Returns a hash code value for the object. This method is
supported for the benefit of hash tables such as those provided by
`HashMap`.

The general contract of `hashCode` is:

* Whenever it is invoked on the same object more than once during
  an execution of a Java application, the `hashCode` method
  must consistently return the same integer, provided no information
  used in `equals` comparisons on the object is modified.
  This integer need not remain consistent from one execution of an
  application to another execution of the same application.* If two objects are equal according to the `equals` method, then calling the `hashCode` method on each of the two objects must produce the
    same integer result.* It is *not* required that if two objects are unequal
      according to the `equals` method, then
      calling the `hashCode` method on each of the two objects
      must produce distinct integer results. However, the programmer
      should be aware that producing distinct integer results for
      unequal objects may improve the performance of hash tables.

| Returns | |
| --- | --- |
| `int` | a hash code value for this object. |

### matches

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public boolean matches (ScanResult scanResult)
```

Check if the scan filter matches a `scanResult`. A scan result is considered as a match
if it matches all the field filters.

| Parameters | |
| --- | --- |
| `scanResult` | `ScanResult` |

| Returns | |
| --- | --- |
| `boolean` |  |

### toString

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public String toString ()
```

Returns a string representation of the object.

| Returns | |
| --- | --- |
| `String` | a string representation of the object. |

### writeToParcel

Added in [API level 21](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

```
public void writeToParcel (Parcel dest, 
                int flags)
```

Flatten this object in to a Parcel.

| Parameters | |
| --- | --- |
| `dest` | `Parcel`: The Parcel in which the object should be written.   This value cannot be `null`. |
| `flags` | `int`: Additional flags about how the object should be written. May be 0 or `Parcelable.PARCELABLE_WRITE_RETURN_VALUE`.   Value is either `0` or a combination of the following:  * `Parcelable.PARCELABLE_WRITE_RETURN_VALUE` |

#!/usr/bin/env python3
"""Author the connectivity domain taxonomy (pilot)."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "radio_or_bus_family"


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "connectivity", parent=None, level="L1",
        zh="连接与外设", en="Connectivity and Peripherals",
        definition="设备侧无线与有线近距连接、配件会话及本地外设总线；不含通用 IP 联网与分布式跨端 Continuity。",
        includes=["蓝牙、Wi-Fi 近距、NFC、USB、串口、红外、星闪、配件会话"],
        excludes=["network 域 HTTP/Socket/VPN", "distributed 域跨端流转"],
        legacy={"disposition": "kept", "sources": ["connectivity"]},
    ))

    l2 = [
        ("connectivity.bluetooth", "蓝牙", "Bluetooth",
         "经典蓝牙与低功耗蓝牙的发现、配对、连接、配置文件与数据通道。",
         ["BR/EDR、BLE、LE Audio"], ["媒体播控见 media.session"], ["connectivity.bluetooth"]),
        ("connectivity.wifi", "Wi-Fi", "Wi-Fi",
         "本地 Wi-Fi 扫描、连接建议、点对点、热点、测距与感知。",
         ["扫描、连接、P2P、Aware、RTT、热点、连接信息"], ["蜂窝切换见 network"], ["connectivity.wifi"]),
        ("connectivity.nfc", "NFC", "NFC",
         "NFC 标签读写、主机卡模拟与安全单元访问。",
         ["Tag I/O、HCE、SE"], ["支付业务编排见 commerce"], ["connectivity.nfc"]),
        ("connectivity.usb", "USB", "USB",
         "USB 主机/配件模式、MTP 与用户态驱动开发入口。",
         ["host、accessory、MTP、DDK"], ["串口协议见 connectivity.serial"], ["connectivity.usb"]),
        ("connectivity.serial", "串口与工业外设", "Serial I/O",
         "本机 UART 与 USB 串口数据通道。",
         ["UART、USB-serial"], ["USB 枚举见 connectivity.usb"], []),
        ("connectivity.peripherals", "配件与外设生态", "Accessories",
         "系统级配件发现、厂商协议会话、测距与伙伴设备互通。",
         ["配件发现、MFi/EA、UWB、MIDI 设备侧"], ["MIDI 音频消息见 media.audio.midi"], []),
        ("connectivity.nearlink", "星闪近距连接", "NearLink",
         "星闪设备发现、管理与 SSAP 数据通道。",
         ["发现、管理、SSAP"], ["通用 BLE 见 connectivity.bluetooth.le"], []),
        ("connectivity.ir", "消费红外", "Consumer IR",
         "本机红外发射与频率能力查询。",
         ["红外发射、频率查询"], ["遥控业务协议本身"], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="connectivity", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # Bluetooth branches
    f.append(feature(
        "connectivity.bluetooth.bond", parent="connectivity.bluetooth", level="L3",
        zh="发现配对与绑定", en="Discovery Pairing and Bonding",
        definition="设备级发现、可被发现、配对请求与绑定关系管理。",
        includes=["discovery、pairing、bonded list"],
        excludes=["GATT 连接见 le.gatt_client", "Companion 关联见 peripherals.discovery"],
        sibling_axis="bluetooth_role",
        bindings=merge_bindings(
            A("BluetoothAdapter", "https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices"),
            I("CBCentralManager", "https://developer.apple.com/documentation/corebluetooth/cbcentralmanager", "class"),
            H("@ohos.bluetooth.connection", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection"),
        ),
    ))
    f.append(feature(
        "connectivity.bluetooth.classic", parent="connectivity.bluetooth", level="L3",
        zh="经典蓝牙与配置文件", en="Classic Bluetooth Profiles",
        definition="BR/EDR 数据通道与常见配置文件控制面。",
        includes=["SPP/RFCOMM、A2DP/HFP/HID/PAN"],
        excludes=["BLE GATT", "LE Audio"],
        sibling_axis="bluetooth_role",
        bindings=merge_bindings(
            A("BluetoothSocket", "https://developer.android.com/develop/connectivity/bluetooth/transfer-data"),
            I("Core Bluetooth Classic", "https://developer.apple.com/documentation/corebluetooth/using-core-bluetooth-classic", "guide"),
            H("@ohos.bluetooth.socket", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spp-development-guide"),
        ),
        legacy={"disposition": "kept", "sources": ["connectivity.bluetooth.classic"]},
    ))
    f.append(feature(
        "connectivity.bluetooth.le", parent="connectivity.bluetooth", level="L3",
        zh="低功耗蓝牙", en="Bluetooth Low Energy",
        definition="BLE 广播、扫描、GATT 与信道探测等低功耗能力簇。",
        includes=["advertise、scan、GATT、channel sounding"],
        excludes=["经典配置文件", "LE Audio 单列"],
        sibling_axis="bluetooth_role",
        bindings=merge_bindings(
            A("android.bluetooth.le", "https://developer.android.com/reference/android/bluetooth/le/package-summary", "package"),
            I("CoreBluetooth", "https://developer.apple.com/documentation/corebluetooth"),
            H("@ohos.bluetooth.ble", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide"),
        ),
        legacy={"disposition": "kept", "sources": ["connectivity.bluetooth.le"]},
    ))
    f.append(feature(
        "connectivity.bluetooth.le_audio", parent="connectivity.bluetooth", level="L3",
        zh="LE Audio", en="LE Audio",
        definition="基于 BLE 的低功耗音频单播/广播与端点管理。",
        includes=["unicast、broadcast、通信设备选择"],
        excludes=["经典 A2DP", "播控会话见 media.session"],
        sibling_axis="bluetooth_role", granularity="atomic",
        bindings=merge_bindings(
            A("BluetoothLeAudio", "https://developer.android.com/develop/connectivity/bluetooth/ble/ble-audio"),
            pending("ios"),
            H("@ohos.bluetooth.ble", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide"),
        ),
        privacy_class="runtime_permission",
    ))

    for fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy, related in [
        ("connectivity.bluetooth.bond.discovery", "connectivity.bluetooth.bond", "bond_phase",
         "蓝牙设备发现", "Bluetooth Device Discovery",
         "启动/停止周边蓝牙设备查询并接收发现结果。",
         ["startDiscovery、发现回调"], ["配对见 bond.pairing"],
         merge_bindings(
             A("BluetoothAdapter.startDiscovery", "https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices"),
             pending("ios", "经典发现受限；BLE 见 le.scan"),
             H("startBluetoothDiscovery", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection"),
         ), {"disposition": "new", "sources": []}, None),
        ("connectivity.bluetooth.bond.pairing", "connectivity.bluetooth.bond", "bond_phase",
         "配对与绑定管理", "Pairing and Bond Management",
         "发起配对、查询已绑定设备并监听绑定状态。",
         ["createBond/pairDevice、bonded list"], ["发现见 bond.discovery"],
         merge_bindings(
             A("BluetoothDevice.createBond", "https://developer.android.com/develop/connectivity/bluetooth/find-bluetooth-devices"),
             pending("ios"),
             H("pairDevice", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection"),
         ), {"disposition": "new", "sources": []}, None),
        ("connectivity.bluetooth.le.advertise", "connectivity.bluetooth.le", "ble_role",
         "BLE广播", "BLE Advertising",
         "外设侧广播可发现载荷并管理广播状态。",
         ["advertising data、start/stop"], ["扫描见 le.scan"],
         merge_bindings(
             A("BluetoothLeAdvertiser", "https://developer.android.com/reference/android/bluetooth/le/BluetoothLeAdvertiser"),
             I("CBPeripheralManager", "https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager", "class"),
             H("ble.startAdvertising", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide"),
         ), {"disposition": "kept", "sources": ["connectivity.bluetooth.le.advertise"]}, None),
        ("connectivity.bluetooth.le.scan", "connectivity.bluetooth.le", "ble_role",
         "BLE扫描", "BLE Scanning",
         "中心侧扫描周边 BLE 广播并接收结果。",
         ["scan settings、callbacks"], ["过滤见 le.scan.filter"],
         merge_bindings(
             A("BluetoothLeScanner", "https://developer.android.com/develop/connectivity/bluetooth/ble/find-ble-devices"),
             I("CBCentralManager.scanForPeripherals", "https://developer.apple.com/documentation/corebluetooth/cbcentralmanager", "class"),
             H("ble.startBLEScan", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide"),
         ), {"disposition": "kept", "sources": ["connectivity.bluetooth.le.scan"]}, None),
        ("connectivity.bluetooth.le.filter", "connectivity.bluetooth.le", "ble_role",
         "BLE扫描过滤", "BLE Scan Filtering",
         "按服务 UUID、厂商数据等条件过滤扫描结果。",
         ["ScanFilter 字段语义"], ["启动扫描见 le.scan"],
         merge_bindings(
             A("ScanFilter", "https://developer.android.com/reference/android/bluetooth/le/ScanFilter"),
             I("scanForPeripherals(withServices:)", "https://developer.apple.com/documentation/corebluetooth/cbcentralmanager", "class"),
             H("ScanFilter", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble"),
         ), {"disposition": "renamed_from", "sources": [
             "connectivity.bluetooth.le.scan.filter",
             "connectivity.bluetooth.le.scan.batch",
             "connectivity.bluetooth.le.scan.background",
         ]}, None),
        ("connectivity.bluetooth.le.gatt_client", "connectivity.bluetooth.le", "ble_role",
         "GATT客户端", "GATT Client",
         "作为中心连接外设、发现服务特性并读写/订阅。",
         ["connect、service discovery、notify"], ["服务端见 gatt_server"],
         merge_bindings(
             A("BluetoothGatt", "https://developer.android.com/reference/android/bluetooth/BluetoothGatt"),
             I("CBPeripheral", "https://developer.apple.com/documentation/corebluetooth/cbperipheral", "class"),
             H("ble.createGattClientDevice", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gatt-development-guide"),
         ), {"disposition": "merged_from", "sources": [
             "connectivity.bluetooth.le.connect", "connectivity.bluetooth.le.gatt",
         ]}, None),
        ("connectivity.bluetooth.le.gatt_server", "connectivity.bluetooth.le", "ble_role",
         "GATT服务端", "GATT Server",
         "作为外设注册服务/特性并响应远端读写与通知。",
         ["addService、notify/indicate"], ["客户端见 gatt_client"],
         merge_bindings(
             A("BluetoothGattServer", "https://developer.android.com/reference/android/bluetooth/BluetoothGattServer"),
             I("CBMutableService", "https://developer.apple.com/documentation/corebluetooth/cbmutableservice", "class"),
             H("ble.createGattServer", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gatt-development-guide"),
         ), {"disposition": "new", "sources": []}, None),
        ("connectivity.bluetooth.le.channel_sounding", "connectivity.bluetooth.le", "ble_role",
         "BLE信道探测测距", "BLE Channel Sounding",
         "基于 Channel Sounding 在两台 BLE 设备间测距。",
         ["channel sounding ranging"], ["UWB 见 peripherals.uwb", "Wi-Fi RTT 见 wifi.rtt"],
         merge_bindings(
             A("RangingManager", "https://developer.android.com/develop/connectivity/ranging"),
             I("Channel Sounding", "https://developer.apple.com/documentation/corebluetooth/measuring-distance-between-devices-using-channel-sounding", "guide"),
             pending("harmonyos"),
         ), {"disposition": "new", "sources": []}, ["connectivity.peripherals.uwb", "connectivity.wifi.rtt"]),
    ]:
        f.append(feature(
            fid, parent=parent, level="L4", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=axis, granularity="atomic",
            bindings=bindings, legacy=legacy, related=related, privacy_class="runtime_permission",
        ))

    for fid, zh, en, definition, h_mod in [
        ("connectivity.bluetooth.classic.spp", "SPP串口仿真", "RFCOMM/SPP",
         "通过 RFCOMM/SPP 建立面向字节流的经典蓝牙数据通道。", "@ohos.bluetooth.socket"),
        ("connectivity.bluetooth.classic.a2dp", "A2DP音频配置文件", "A2DP Profile",
         "经典蓝牙高质量音频配置文件控制面。", "@ohos.bluetooth.a2dp"),
        ("connectivity.bluetooth.classic.hfp", "HFP免提配置文件", "HFP Profile",
         "免提音频网关/耳机配置文件控制面。", "@ohos.bluetooth.hfp"),
        ("connectivity.bluetooth.classic.hid", "HID人机接口配置文件", "HID Profile",
         "蓝牙人机接口设备配置文件。", "@ohos.bluetooth.hid"),
        ("connectivity.bluetooth.classic.pan", "PAN个人区域网", "PAN Profile",
         "蓝牙个人区域网配置文件。", "@ohos.bluetooth.pan"),
    ]:
        f.append(feature(
            fid, parent="connectivity.bluetooth.classic", level="L4", zh=zh, en=en, definition=definition,
            includes=[en], excludes=["LE Audio 见 le_audio"],
            sibling_axis="classic_profile", granularity="atomic",
            bindings=merge_bindings(
                A("android.bluetooth", "https://developer.android.com/develop/connectivity/bluetooth", "package"),
                pending("ios"),
                H(h_mod, "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/connectivity-kit-intro"),
            ),
        ))

    wifi = [
        ("connectivity.wifi.scan", "Wi-Fi扫描", "Wi-Fi Scan",
         "扫描周边 Wi-Fi 接入点并获取结果。",
         merge_bindings(
             A("WifiManager.startScan", "https://developer.android.com/guide/topics/connectivity/wifi-scan"),
             pending("ios", "应用侧扫描受限，待核"),
             H("@ohos.wifiManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifiManager"),
         ), {"disposition": "kept", "sources": ["connectivity.wifi.scan"]}),
        ("connectivity.wifi.connect", "Wi-Fi连接与网络建议", "Wi-Fi Connect and Suggestions",
         "请求连接网络或向系统提供网络建议。",
         merge_bindings(
             A("WifiNetworkSuggestion", "https://developer.android.com/guide/topics/connectivity/wifi-suggest"),
             I("NEHotspotConfigurationManager", "https://developer.apple.com/documentation/networkextension/nehotspotconfigurationmanager", "class"),
             H("wifiManager.connectToNetwork", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifiManager"),
         ), {"disposition": "kept", "sources": ["connectivity.wifi.connect"]}),
        ("connectivity.wifi.state", "Wi-Fi连接信息", "Wi-Fi Connection Info",
         "查询当前 Wi-Fi 连接状态与链路信息。",
         merge_bindings(
             A("WifiInfo", "https://developer.android.com/reference/android/net/wifi/WifiInfo"),
             pending("ios"),
             H("getLinkedInfo", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifiManager"),
         ), {"disposition": "new", "sources": []}),
        ("connectivity.wifi.p2p", "Wi-Fi点对点", "Wi-Fi P2P",
         "Wi-Fi Direct/P2P 设备发现与组网。",
         merge_bindings(
             A("WifiP2pManager", "https://developer.android.com/reference/android/net/wifi/p2p/WifiP2pManager"),
             pending("ios"),
             H("wifiManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifiManager"),
         ), {"disposition": "new", "sources": []}),
        ("connectivity.wifi.aware", "Wi-Fi感知组网", "Wi-Fi Aware",
         "邻区感知网络发布/订阅与数据路径。",
         merge_bindings(
             A("WifiAwareManager", "https://developer.android.com/develop/connectivity/wifi/wifi-aware"),
             pending("ios"), pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("connectivity.wifi.rtt", "Wi-Fi RTT测距", "Wi-Fi RTT",
         "对支持的接入点或对等方进行 RTT 测距。",
         merge_bindings(
             A("WifiRttManager", "https://developer.android.com/guide/topics/connectivity/wifi-rtt"),
             pending("ios"), pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("connectivity.wifi.hotspot_local", "本地热点", "Local Hotspot",
         "开启/配置本机本地 Wi-Fi 热点。",
         merge_bindings(
             A("WifiManager.startLocalOnlyHotspot", "https://developer.android.com/reference/android/net/wifi/WifiManager"),
             pending("ios"),
             H("wifiManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wifiManager"),
         ), {"disposition": "merged_from", "sources": ["network.hotspot", "network.hotspot.local"]}),
    ]
    for fid, zh, en, definition, bindings, legacy in wifi:
        f.append(feature(
            fid, parent="connectivity.wifi", level="L3", zh=zh, en=en, definition=definition,
            includes=[en], excludes=["蜂窝网络见 network"],
            sibling_axis="wifi_operation", granularity="atomic",
            bindings=bindings, legacy=legacy, privacy_class="runtime_permission",
        ))

    nfc = [
        ("connectivity.nfc.tag", "NFC标签读写", "NFC Tag I/O",
         "发现 NFC 标签并读写 NDEF/技术标签数据。",
         merge_bindings(
             A("android.nfc", "https://developer.android.com/develop/connectivity/nfc", "package"),
             I("CoreNFC", "https://developer.apple.com/documentation/corenfc"),
             H("@ohos.nfc.tag", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nfcTag"),
         ), {"disposition": "merged_from", "sources": ["connectivity.nfc.reader"]}),
        ("connectivity.nfc.hce", "主机卡模拟", "Host Card Emulation",
         "由主机应用模拟智能卡与读卡器交互。",
         merge_bindings(
             A("HostApduService", "https://developer.android.com/reference/android/nfc/cardemulation/HostApduService"),
             pending("ios", "HCE 能力待核"),
             H("@ohos.nfc.cardEmulation", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cardEmulation"),
         ), {"disposition": "kept", "sources": ["connectivity.nfc.hce"]}),
        ("connectivity.nfc.se", "安全单元访问", "Secure Element Access",
         "访问设备安全单元或 eSE 上的卡应用。",
         merge_bindings(
             A("OffHostApduService", "https://developer.android.com/reference/android/nfc/cardemulation/OffHostApduService"),
             pending("ios"), pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
    ]
    for fid, zh, en, definition, bindings, legacy in nfc:
        f.append(feature(
            fid, parent="connectivity.nfc", level="L3", zh=zh, en=en, definition=definition,
            includes=[en], excludes=["支付编排见 commerce"],
            sibling_axis="nfc_role", granularity="atomic",
            bindings=bindings, legacy=legacy, privacy_class="runtime_permission",
        ))

    usb = [
        ("connectivity.usb.host", "USB主机模式", "USB Host",
         "作为 USB 主机枚举并与外设通信。",
         merge_bindings(
             A("UsbManager", "https://developer.android.com/guide/topics/connectivity/usb/host"),
             pending("ios"),
             H("@ohos.usbManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-usbManager"),
         ), {"disposition": "kept", "sources": ["connectivity.usb.host"]}),
        ("connectivity.usb.accessory", "USB配件模式", "USB Accessory",
         "作为 USB 配件与主机侧应用通信。",
         merge_bindings(
             A("UsbAccessory", "https://developer.android.com/guide/topics/connectivity/usb/accessory"),
             pending("ios"), pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("connectivity.usb.mtp", "MTP设备访问", "MTP Access",
         "通过 MTP 访问媒体传输协议设备。",
         merge_bindings(
             A("android.mtp", "https://developer.android.com/reference/android/mtp/package-summary", "package"),
             pending("ios"), pending("harmonyos"),
         ), {"disposition": "new", "sources": []}),
        ("connectivity.usb.ddk", "用户态USB驱动开发", "USB DDK",
         "用户态 USB 驱动开发套件入口。",
         merge_bindings(
             pending("android"), pending("ios"),
             H("USB DDK", "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/usb-ddk", "guide"),
         ), {"disposition": "new", "sources": []}),
    ]
    for fid, zh, en, definition, bindings, legacy in usb:
        f.append(feature(
            fid, parent="connectivity.usb", level="L3", zh=zh, en=en, definition=definition,
            includes=[en], excludes=["串口见 connectivity.serial"],
            sibling_axis="usb_mode", granularity="atomic",
            bindings=bindings, legacy=legacy,
        ))

    for fid, zh, en, definition, bindings in [
        ("connectivity.serial.uart", "本机串口管理", "UART Serial",
         "打开本机 UART 串口并收发数据。",
         merge_bindings(
             pending("android", "通常经 USB-serial/厂商库，待核标准 API"),
             pending("ios"),
             H("@ohos.uart", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uart"),
         )),
        ("connectivity.serial.usb", "USB串口", "USB Serial",
         "经 USB 枚举的串口设备通信。",
         merge_bindings(
             pending("android", "UsbSerialDriver 生态库，待核"),
             pending("ios"),
             H("@ohos.usbManager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-usbManager"),
         )),
    ]:
        f.append(feature(
            fid, parent="connectivity.serial", level="L3", zh=zh, en=en, definition=definition,
            includes=[en], excludes=["USB 枚举见 connectivity.usb.host"],
            sibling_axis="serial_transport", granularity="atomic", bindings=bindings,
        ))

    periph = [
        ("connectivity.peripherals.discovery", "配件发现与关联", "Accessory Discovery",
         "通过系统 Companion/配件框架发现并关联外设。",
         merge_bindings(
             A("CompanionDeviceManager", "https://developer.android.com/develop/connectivity/bluetooth/companion-device-pairing"),
             I("AccessorySetupKit", "https://developer.apple.com/documentation/accessorysetupkit", "framework"),
             pending("harmonyos"),
         )),
        ("connectivity.peripherals.mfi", "厂商配件会话", "Vendor Accessory Session",
         "与已关联配件按厂商协议建立会话并收发数据（含 MFi EASession 等）。",
         merge_bindings(
             pending("android"),
             I("EASession", "https://developer.apple.com/documentation/externalaccessory/easession", "class"),
             pending("harmonyos"),
         )),
        ("connectivity.peripherals.uwb", "UWB测距", "UWB Ranging",
         "超宽带测距与空间感知。",
         merge_bindings(
             A("RangingManager", "https://developer.android.com/develop/connectivity/ranging"),
             I("Nearby Interaction", "https://developer.apple.com/documentation/nearbyinteraction", "framework"),
             H("nearbyInteraction", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nearbyinteraction"),
         )),
        ("connectivity.peripherals.midi", "MIDI设备连接", "MIDI Device Connectivity",
         "MIDI 设备发现与端口连接（设备侧）；消息流见 media。",
         merge_bindings(
             A("MidiManager", "https://developer.android.com/reference/android/media/midi/MidiManager"),
             I("CoreMIDI", "https://developer.apple.com/documentation/coremidi", "framework"),
             H("@ohos.multimedia.midi", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-midi"),
         )),
        ("connectivity.peripherals.partner_interop", "伙伴设备互通", "Partner Device Interop",
         "手机与手表/耳机等伙伴设备的厂商互通会话入口。",
         merge_bindings(
             A("Wearable Data Layer", "https://developer.android.com/training/wearables/data", "guide"),
             I("Watch Connectivity", "https://developer.apple.com/documentation/watchconnectivity", "framework"),
             pending("harmonyos"),
         )),
        ("connectivity.peripherals.accessory_services", "配件侧系统服务", "Accessory System Services",
         "配件侧可调用的系统服务能力（通知转发、音频切换等）入口簇。",
         merge_bindings(
             pending("android"),
             I("CoreBluetooth / Accessory", "https://developer.apple.com/documentation/corebluetooth", "framework"),
             pending("harmonyos"),
         )),
    ]
    for fid, zh, en, definition, bindings in periph:
        f.append(feature(
            fid, parent="connectivity.peripherals", level="L3", zh=zh, en=en, definition=definition,
            includes=[en], excludes=["通用蓝牙绑定见 connectivity.bluetooth.bond"],
            sibling_axis="accessory_capability", granularity="atomic",
            bindings=bindings, privacy_class="runtime_permission",
        ))

    for fid, zh, en, definition, bindings in [
        ("connectivity.nearlink.discovery", "星闪发现与广播", "NearLink Discovery",
         "星闪设备扫描与广播。",
         merge_bindings(pending("android"), pending("ios"),
                        H("nearlink scan", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nearlink-scan"))),
        ("connectivity.nearlink.manager", "星闪基础管理", "NearLink Manager",
         "星闪适配器开关与基础状态管理。",
         merge_bindings(pending("android"), pending("ios"),
                        H("nearlink manager", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nearlink-manager"))),
        ("connectivity.nearlink.ssap", "星闪SSAP数据", "NearLink SSAP",
         "星闪 SSAP 连接与数据收发。",
         merge_bindings(pending("android"), pending("ios"),
                        H("nearlink ssap", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-nearlink-ssap"))),
    ]:
        f.append(feature(
            fid, parent="connectivity.nearlink", level="L3", zh=zh, en=en, definition=definition,
            includes=[en], excludes=["BLE 见 connectivity.bluetooth.le"],
            sibling_axis="nearlink_role", granularity="atomic", bindings=bindings,
        ))

    f.append(feature(
        "connectivity.ir.transmit", parent="connectivity.ir", level="L3",
        zh="红外发射", en="IR Transmit",
        definition="按指定频率与图案发射消费红外信号。",
        includes=["transmitInfrared、频率查询"],
        excludes=["遥控码库业务逻辑"],
        sibling_axis="ir_operation", granularity="atomic",
        bindings=merge_bindings(
            A("ConsumerIrManager", "https://developer.android.com/reference/android/hardware/ConsumerIrManager"),
            pending("ios"),
            H("infraredEmitter", "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-infraredemitter"),
        ),
    ))

    # final dedupe
    dedup = {}
    for node in f:
        dedup[node["id"]] = node
    return list(dedup.values())


def main():
    nodes = build()
    path = write_domain("connectivity", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()

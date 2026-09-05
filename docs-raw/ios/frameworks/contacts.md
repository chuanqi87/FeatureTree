* * *

* * *

[Skip Navigation](https://developer.apple.com/documentation/contacts#app-main)

Framework

# Contacts

Access the user’s contacts, and format and localize contact information.

iOS 9.0+iPadOS 9.0+Mac Catalyst 13.0+macOS 10.11+visionOS 1.0+watchOS 2.0+

## [Overview](https://developer.apple.com/documentation/contacts\#overview)

The Contacts framework provides Swift and Objective-C APIs to access the user’s contact information. Because most apps read contact information without making any changes, this framework is optimized for thread-safe, read-only usage.

### [Working with the user’s contacts](https://developer.apple.com/documentation/contacts\#Working-with-the-users-contacts)

The Contacts framework is available on all Apple platforms, and replaces the Address Book framework in iOS and macOS.

#### [Contact objects](https://developer.apple.com/documentation/contacts\#Contact-objects)

The contact class ( [`CNContact`](https://developer.apple.com/documentation/contacts/cncontact)) is a thread-safe, immutable value object of contact properties, such as the contact’s name, image, and phone numbers.

![An organizational diagram showing that a contact object has a mutable variant and can have properties that labeled value objects represent.](https://developer.apple.com/tutorials/images/com.apple.contacts/media-4097928@2x.png)

The contact class is like [`NSDictionary`](https://developer.apple.com/documentation/foundation/nsdictionary) in that it has a mutable subclass, [`CNMutableContact`](https://developer.apple.com/documentation/contacts/cnmutablecontact), you can use to modify contact properties. For contact properties that can have multiple values, such as phone numbers and email addresses, the framework uses an array of [`CNLabeledValue`](https://developer.apple.com/documentation/contacts/cnlabeledvalue) objects. The labeled value class is a thread-safe, immutable tuple of labels and values. Labels describe each value to the user, allowing differentiation, such as home and work phone numbers. The Contacts framework provides some predefined labels and you can create your own custom labels.

```
import UIKit
import Contacts

// Create a mutable object to add to the contact.
let contact = CNMutableContact()

// Store the profile picture as data.
let image = UIImage(systemName: "person.crop.circle")
contact.imageData = image?.jpegData(compressionQuality: 1.0)

contact.givenName = "John"
contact.familyName = "Appleseed"

let homeEmail = CNLabeledValue(label: CNLabelHome, value: "john@example.com" as NSString)
let workEmail = CNLabeledValue(label: CNLabelWork, value: "j.appleseed@icloud.com" as NSString)
contact.emailAddresses = [homeEmail, workEmail]

contact.phoneNumbers = [CNLabeledValue(\
    label: CNLabelPhoneNumberiPhone,\
    value: CNPhoneNumber(stringValue: "(408) 555-0126"))]

let homeAddress = CNMutablePostalAddress()
homeAddress.street = "One Apple Park Way"
homeAddress.city = "Cupertino"
homeAddress.state = "CA"
homeAddress.postalCode = "95014"
contact.postalAddresses = [CNLabeledValue(label: CNLabelHome, value: homeAddress)]

var birthday = DateComponents()
birthday.day = 1
birthday.month = 4
birthday.year = 1988  // (Optional) Omit the year value for a yearless birthday.
contact.birthday = birthday

// Save the newly created contact.
let store = CNContactStore()
let saveRequest = CNSaveRequest()
saveRequest.add(contact, toContainerWithIdentifier: nil)

do {
    try store.execute(saveRequest)
} catch {
    print("Saving contact failed, error: \(error)")
    // Handle the error.
}
```

#### [Formatting and localization](https://developer.apple.com/documentation/contacts\#Formatting-and-localization)

The Contacts framework helps you format and localize contact information. For example, you can correctly format a contact name (using [`CNContactFormatter`](https://developer.apple.com/documentation/contacts/cncontactformatter)) or format an international postal address (using [`CNPostalAddressFormatter`](https://developer.apple.com/documentation/contacts/cnpostaladdressformatter)).

```
// Formatting the contact name.
let fullName = CNContactFormatter.string(from: contact, style: .fullName)
print("\(String(describing: fullName))")
// John Appleseed

// Formatting the postal address.
let postalString = CNPostalAddressFormatter().string(from: homeAddress)
print("\(postalString)")
// One Apple Park Way
// Cupertino
// CA
// 95014
```

You can display localized object property names and predefined labels based on the current locale setting of the device. Many objects in the Contacts framework, such as [`CNContact`](https://developer.apple.com/documentation/contacts/cncontact), include the [`localizedString(forKey:)`](https://developer.apple.com/documentation/contacts/cnsocialprofile/localizedstring(forkey:)) method, which lets you get the localized version of a key name. In addition, the [`CNLabeledValue`](https://developer.apple.com/documentation/contacts/cnlabeledvalue) class includes the [`localizedString(forLabel:)`](https://developer.apple.com/documentation/contacts/cnlabeledvalue/localizedstring(forlabel:)) method, which lets you get the localized label for the predefined labels in the Contacts framework.

```
// The device locale is Spanish.
let displayName = CNContact.localizedString(forKey: CNContactNicknameKey)
print(displayName)
// Prints "alias"

let displayLabel = CNLabeledValue<NSString>.localizedString(forLabel: CNLabelHome)
print(displayLabel)
// Prints "casa".
```

#### [Fetching contacts](https://developer.apple.com/documentation/contacts\#Fetching-contacts)

You can fetch contacts using the contact store ( [`CNContactStore`](https://developer.apple.com/documentation/contacts/cncontactstore)), which represents the user’s Contacts database. The contact store encapsulates all I/O operations and is responsible for fetching and saving contacts and groups. Because the contact store methods are synchronous, it’s best practice to use them on background threads. If necessary, you can safely send immutable fetch results back to the main thread.

The Contacts framework provides several ways to constrain contacts that return from a fetch, including predefined predicates and the [`keysToFetch`](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) property.

[`CNContact`](https://developer.apple.com/documentation/contacts/cncontact) provides predicates for filtering the contacts you want to fetch. For example, to fetch contacts that have the name _Appleseed_, use [`predicateForContacts(matchingName:)`](https://developer.apple.com/documentation/contacts/cncontact/predicateforcontacts(matchingname:)) and pass in `Appleseed`.

```
let predicate = CNContact.predicateForContacts(matchingName: "Appleseed")
```

Note that the Contacts framework doesn’t support generic and compound predicates.

You can use [`keysToFetch`](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) to limit the contact properties that you fetch. For example, if you want to fetch only the given name and the family name of a contact, you specify those contact keys in a [`keysToFetch`](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) array.

```
let keysToFetch = [CNContactGivenNameKey, CNContactFamilyNameKey] as [CNKeyDescriptor]
```

To fetch a contact using both a predicate ( [`predicateForContacts(matchingName:)`](https://developer.apple.com/documentation/contacts/cncontact/predicateforcontacts(matchingname:))) and a [`keysToFetch`](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) array, use [`unifiedContacts(matching:keysToFetch:)`](https://developer.apple.com/documentation/contacts/cncontactstore/unifiedcontacts(matching:keystofetch:)).

```
let store = CNContactStore()
do {
    let predicate = CNContact.predicateForContacts(matchingName: "Appleseed")
    let contacts = try store.unifiedContacts(matching: predicate, keysToFetch: keysToFetch)
    print("Fetched contacts: \(contacts)")
} catch {
    print("Failed to fetch contact, error: \(error)")
    // Handle the error.
}
```

The Contacts framework can also perform operations on the fetched contacts, such as formatting contact names. Each operation requires a specific set of contact keys to correctly perform the operation. The contact keys are key descriptor objects that you need to include within the [`keysToFetch`](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) array. For example, if you want to fetch the contact’s email addresses and also be able to format the contact’s name (using [`CNContactFormatter`](https://developer.apple.com/documentation/contacts/cncontactformatter)), include both [`CNContactEmailAddressesKey`](https://developer.apple.com/documentation/contacts/cncontactemailaddresseskey) and the key descriptor object that [`descriptorForRequiredKeys(for:)`](https://developer.apple.com/documentation/contacts/cncontactformatter/descriptorforrequiredkeys(for:)) returns in the [`keysToFetch`](https://developer.apple.com/documentation/contacts/cncontactfetchrequest/keystofetch) array.

```
let keysToFetch = [CNContactEmailAddressesKey as CNKeyDescriptor, CNContactFormatter.descriptorForRequiredKeys(for: .fullName)]
```

#### [Privacy](https://developer.apple.com/documentation/contacts\#Privacy)

Users can grant or deny access to contact data on a per-app basis. Any call to [`CNContactStore`](https://developer.apple.com/documentation/contacts/cncontactstore) blocks the app while asking the user to grant or deny access. Note that the user receives a prompt only the first time an app requests access; all subsequent [`CNContactStore`](https://developer.apple.com/documentation/contacts/cncontactstore) calls use the existing permissions. To avoid having your app’s UI main thread block for this access, you can use either the asynchronous method [`requestAccess(for:completionHandler:)`](https://developer.apple.com/documentation/contacts/cncontactstore/requestaccess(for:completionhandler:)) or dispatch your [`CNContactStore`](https://developer.apple.com/documentation/contacts/cncontactstore) usage to a background thread.

#### [Partial contacts](https://developer.apple.com/documentation/contacts\#Partial-contacts)

A partial contact results when the system fetches only some of a contact object’s properties from a contact store. All fetched contact objects are partial contacts. If you try to access a property value that the system didn’t fetch, you get an exception. If you are unsure which keys the system fetched in the contact, check the availability of the property values before you access them. You can either use [`isKeyAvailable(_:)`](https://developer.apple.com/documentation/contacts/cncontact/iskeyavailable(_:)) to check the availability of a single contact key, or [`areKeysAvailable(_:)`](https://developer.apple.com/documentation/contacts/cncontact/arekeysavailable(_:)) to check multiple keys. If the desired keys aren’t available, refetch the contact with them.

```
// Check whether the phone number is available for the given contact.
if contact.isKeyAvailable(CNContactPhoneNumbersKey) {
    print("\(contact.phoneNumbers)")
} else {
    // Refetch the keys.
    let keysToFetch = [CNContactGivenNameKey, CNContactFamilyNameKey, CNContactPhoneNumbersKey] as [CNKeyDescriptor]

    do {
        let refetchedContact = try store.unifiedContact(withIdentifier: contact.identifier, keysToFetch: keysToFetch)
        print("\(refetchedContact.phoneNumbers)")
    } catch {
        print("Failed to fetch contact, error: \(error)")
        // Handle the error.
    }
}
```

#### [Unified contacts](https://developer.apple.com/documentation/contacts\#Unified-contacts)

You can automatically link contacts in different accounts that represent the same person. Linked contacts display in macOS and iOS apps as unified contacts. A unified contact is an in-memory, temporary view of the set of linked contacts that the system merges into one contact.

![A diagram that shows the merging of a person’s iCloud and social media account contact information into a single, unified contact.](https://developer.apple.com/tutorials/images/com.apple.contacts/media-4097927@2x.png)

By default the Contacts framework returns unified contacts. Each fetched unified contact object ( [`CNContact`](https://developer.apple.com/documentation/contacts/cncontact)) has its own unique identifier that’s different from any individual contact’s identifier in the set of linked contacts. When refetching a unified contact, be sure to use its identifier.

#### [Saving contacts](https://developer.apple.com/documentation/contacts\#Saving-contacts)

The contact store ( [`CNContactStore`](https://developer.apple.com/documentation/contacts/cncontactstore)) also saves changes to the Contacts framework objects. The [`CNSaveRequest`](https://developer.apple.com/documentation/contacts/cnsaverequest) class enables save operations and allows batching of changes to multiple contacts and groups into a single operation. After adding all objects to the save request, it can execute with a contact store as the code example below shows. Don’t access the objects in the save request while the save is executing, because the objects may have modifications.

Create and save a new contact.

```
// Create a new contact.
let newContact = CNMutableContact()
newContact.givenName = "John"
newContact.familyName = "Appleseed"

// Save the contact.
let saveRequest = CNSaveRequest()
saveRequest.add(newContact, toContainerWithIdentifier: nil)

do {
    try store.execute(saveRequest)
} catch {
    print("Saving contact failed, error: \(error)")
    // Handle the error.
}
```

Modify and save an existing contact.

```
// Update the home email address for John Appleseed.
guard let mutableContact = contact.mutableCopy() as? CNMutableContact else { return }
let newEmail = CNLabeledValue(label: CNLabelHome, value: "john@example.com" as NSString)
mutableContact.emailAddresses.append(newEmail)

let saveRequest = CNSaveRequest()
saveRequest.update(mutableContact)
do {
    try store.execute(saveRequest)
} catch {
    print("Saving contact failed, error: \(error)")
    // Handle the error.
}
```

#### [Contacts changed notifications](https://developer.apple.com/documentation/contacts\#Contacts-changed-notifications)

After successfully executing a save, the contact store posts a [`CNContactStoreDidChange`](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/cncontactstoredidchange) notification to the default notification center. If you cache any Contacts framework objects, you need to refetch those objects, either by their identifiers, or with the predicates that you used to originally fetch them, and then release the cached objects. Note that cached objects are stale, but not invalid.

#### [Containers and groups](https://developer.apple.com/documentation/contacts\#Containers-and-groups)

A user may have contacts in their device’s local account or server accounts that they configure to sync contacts. Each account has at least one container of contacts. A contact can be in only one container.

![A diagram that shows two containers — one for a person’s iCloud contacts and one for that person’s social media account contacts.](https://developer.apple.com/tutorials/images/com.apple.contacts/media-4097926@2x.png)

A group is a set of contacts within a container. Not all accounts support groups, and some accounts also support subgroups. An iCloud account has only one container and may have many groups, but no subgroups. An Exchange account doesn’t support groups, but may have multiple containers representing Exchange folders.

![A diagram that shows two containers — one for a person’s iCloud contacts and one for that person’s social media account contacts. The iCloud container has two groups within it that each have three contacts. The two groups overlap with one contact. The social media account container has one group of two contacts in it. ](https://developer.apple.com/tutorials/images/com.apple.contacts/media-4097924@2x.png)

## [Topics](https://developer.apple.com/documentation/contacts\#topics)

### [Essentials](https://developer.apple.com/documentation/contacts\#Essentials)

[Accessing the contact store](https://developer.apple.com/documentation/contacts/accessing-the-contact-store)

Request permission from the person to read and write their contact data.

[Accessing a person’s contact data using Contacts and ContactsUI](https://developer.apple.com/documentation/contacts/accessing-a-person-s-contact-data-using-contacts-and-contactsui)

Allow people to grant your app access to contact data by adding the Contact access button and Contact access picker to your app.

[`class CNContactStore`](https://developer.apple.com/documentation/contacts/cncontactstore)

The object that fetches and saves contacts, groups, and containers from the user’s Contacts database.

[`NSContactsUsageDescription`](https://developer.apple.com/documentation/bundleresources/information-property-list/nscontactsusagedescription)

A message that tells people why the app is requesting access to their contacts.

[`com.apple.developer.contacts.notes`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.contacts.notes)

A Boolean value that indicates whether the app may access the notes in contact entries.

### [Contact data](https://developer.apple.com/documentation/contacts\#Contact-data)

[`class CNContact`](https://developer.apple.com/documentation/contacts/cncontact)

An immutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.

[`class CNMutableContact`](https://developer.apple.com/documentation/contacts/cnmutablecontact)

A mutable object that stores information about a single contact, such as the contact’s first name, phone numbers, and addresses.

[API Reference\\
Data Objects](https://developer.apple.com/documentation/contacts/data-objects)

Access contact-related data, such as the user’s postal address and phone number.

[API Reference\\
Contact Keys](https://developer.apple.com/documentation/contacts/contact-keys)

Specify contact-related properties during fetch operations.

### [Fetch and save requests](https://developer.apple.com/documentation/contacts\#Fetch-and-save-requests)

[`class CNContactFetchRequest`](https://developer.apple.com/documentation/contacts/cncontactfetchrequest)

An object that defines the options to use when fetching contacts.

[`class CNFetchRequest`](https://developer.apple.com/documentation/contacts/cnfetchrequest)

The base class for contact fetch requests.

[`class CNFetchResult`](https://developer.apple.com/documentation/contacts/cnfetchresult)

An object that represents the result of a change-history fetch request.

[`class CNSaveRequest`](https://developer.apple.com/documentation/contacts/cnsaverequest)

An object that collects the changes you want to save to the user’s contacts database.

### [Change history data](https://developer.apple.com/documentation/contacts\#Change-history-data)

[`class CNChangeHistoryAddContactEvent`](https://developer.apple.com/documentation/contacts/cnchangehistoryaddcontactevent)

An object that represents a user adding a contact.

[`class CNChangeHistoryAddGroupEvent`](https://developer.apple.com/documentation/contacts/cnchangehistoryaddgroupevent)

An object that represents a user adding a group.

[`class CNChangeHistoryAddMemberToGroupEvent`](https://developer.apple.com/documentation/contacts/cnchangehistoryaddmembertogroupevent)

An object that represents a user adding a contact to a group.

[`class CNChangeHistoryAddSubgroupToGroupEvent`](https://developer.apple.com/documentation/contacts/cnchangehistoryaddsubgrouptogroupevent)

An object that represents a user adding a subgroup to a group.

[`class CNChangeHistoryDeleteContactEvent`](https://developer.apple.com/documentation/contacts/cnchangehistorydeletecontactevent)

An object that represents a user deleting a contact.

[`class CNChangeHistoryDeleteGroupEvent`](https://developer.apple.com/documentation/contacts/cnchangehistorydeletegroupevent)

An object that represents a user deleting a group.

[`class CNChangeHistoryDropEverythingEvent`](https://developer.apple.com/documentation/contacts/cnchangehistorydropeverythingevent)

An object that indicates the delegate should drop all contacts and groups before handling change events.

[`class CNChangeHistoryEvent`](https://developer.apple.com/documentation/contacts/cnchangehistoryevent)

An object that represents the user adding, updating, or deleting a contact or group.

[`class CNChangeHistoryFetchRequest`](https://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest)

An object that specifies the criteria for fetching change history.

[`class CNChangeHistoryRemoveMemberFromGroupEvent`](https://developer.apple.com/documentation/contacts/cnchangehistoryremovememberfromgroupevent)

An object that represents a user removing a contact from a group.

[`class CNChangeHistoryRemoveSubgroupFromGroupEvent`](https://developer.apple.com/documentation/contacts/cnchangehistoryremovesubgroupfromgroupevent)

An object that represents a user removing a subgroup from a group.

[`class CNChangeHistoryUpdateContactEvent`](https://developer.apple.com/documentation/contacts/cnchangehistoryupdatecontactevent)

An object that represents a user updating a contact.

[`class CNChangeHistoryUpdateGroupEvent`](https://developer.apple.com/documentation/contacts/cnchangehistoryupdategroupevent)

An object that represents an updated group event.

[`protocol CNChangeHistoryEventVisitor`](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor)

An interface for receiving notice of changes to contacts and groups.

### [Formatters](https://developer.apple.com/documentation/contacts\#Formatters)

[`class CNContactFormatter`](https://developer.apple.com/documentation/contacts/cncontactformatter)

An object that you use to format contact information before displaying it to the user.

[`class CNPostalAddressFormatter`](https://developer.apple.com/documentation/contacts/cnpostaladdressformatter)

An object that you use to format a contact’s postal addresses.

[`class CNContactVCardSerialization`](https://developer.apple.com/documentation/contacts/cncontactvcardserialization)

An object you use to convert to and from a vCard representation of the user’s contacts.

[`class CNContactsUserDefaults`](https://developer.apple.com/documentation/contacts/cncontactsuserdefaults)

An object that defines the default options to use when displaying contacts.

### [Errors](https://developer.apple.com/documentation/contacts\#Errors)

[API Reference\\
Error Information](https://developer.apple.com/documentation/contacts/error-information)

Diagnose errors generated by the Contacts framework.

Current page is Contacts
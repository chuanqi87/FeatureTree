# AddressBook Functions

Find the C functions and function-like macros you use to manipulate Address Book data.

## Topics

### Address Book

[`ABGetSharedAddressBook`](/documentation/AddressBook/ABGetSharedAddressBook())

Returns the unique shared ABAddressBook object.

[`ABCopyDefaultCountryCode`](/documentation/AddressBook/ABCopyDefaultCountryCode(_:))

Returns the default country code for records with unspecified country codes.

[`ABHasUnsavedChanges`](/documentation/AddressBook/ABHasUnsavedChanges(_:))

Returns whether if there are unsaved changes in the address book.

[`ABSave`](/documentation/AddressBook/ABSave(_:))

Saves all the changes made since the last save.

### People

[`ABCopyArrayOfAllPeople`](/documentation/AddressBook/ABCopyArrayOfAllPeople(_:))

Returns an array of all the people in the Address Book database.

[`ABGetMe`](/documentation/AddressBook/ABGetMe(_:))

Returns the ABPerson object for the logged-in user.

[`ABPersonCopyImageData`](/documentation/AddressBook/ABPersonCopyImageData(_:))

Returns data that contains a picture of a person.

[`ABPersonCopyParentGroups`](/documentation/AddressBook/ABPersonCopyParentGroups(_:))

Returns an array of groups that a person belongs to.

[`ABPersonCopyVCardRepresentation`](/documentation/AddressBook/ABPersonCopyVCardRepresentation(_:))

Returns the vCard representation of the person as a data object in vCard format.

[`ABPersonCreate`](/documentation/AddressBook/ABPersonCreate())

Returns a newly created person object.

[`ABPersonCreateSearchElement`](/documentation/AddressBook/ABPersonCreateSearchElement(_:_:_:_:_:))

Returns a search element object that specifies a query for records of this type.

[`ABPersonCreateWithVCardRepresentation`](/documentation/AddressBook/ABPersonCreateWithVCardRepresentation(_:))

Returns a new ABPerson object initialized with the given data in vCard format.

[`ABPersonSetImageData`](/documentation/AddressBook/ABPersonSetImageData(_:_:_:))

Sets the image for this person to the given data.

[`ABSetMe`](/documentation/AddressBook/ABSetMe(_:_:))

Sets the record that represents the logged-in user.

### Groups

[`ABCopyArrayOfAllGroups`](/documentation/AddressBook/ABCopyArrayOfAllGroups(_:))

Returns an array of all the groups in the Address Book database.

[`ABGroupAddGroup`](/documentation/AddressBook/ABGroupAddGroup(_:_:))

Adds a subgroup to another group.

[`ABGroupAddMember`](/documentation/AddressBook/ABGroupAddMember(_:_:_:))

Adds a person to a group.

[`ABGroupCopyArrayOfAllMembers`](/documentation/AddressBook/ABGroupCopyArrayOfAllMembers(_:))

Returns an array of persons in a group.

[`ABGroupCopyArrayOfAllSubgroups`](/documentation/AddressBook/ABGroupCopyArrayOfAllSubgroups(_:))

Returns an array containing a group’s subgroups.

[`ABGroupCopyDistributionIdentifier`](/documentation/AddressBook/ABGroupCopyDistributionIdentifier(_:_:_:))

Returns the distribution identifier for the given propertyand person.

[`ABGroupCopyParentGroups`](/documentation/AddressBook/ABGroupCopyParentGroups(_:))

Returns an array containing a group’s parents—thegroups that a group belongs to.

[`ABGroupCreate`](/documentation/AddressBook/ABGroupCreate())

Returns a new ABGroup object.

[`ABGroupCreateSearchElement`](/documentation/AddressBook/ABGroupCreateSearchElement(_:_:_:_:_:))

Creates an ABSearchElement object that specifies a queryfor ABGroup records.

[`ABGroupRemoveGroup`](/documentation/AddressBook/ABGroupRemoveGroup(_:_:))

Removes a subgroup from a group.

[`ABGroupRemoveMember`](/documentation/AddressBook/ABGroupRemoveMember(_:_:_:))

Removes a person from a group.

[`ABGroupSetDistributionIdentifier`](/documentation/AddressBook/ABGroupSetDistributionIdentifier(_:_:_:_:))

Assigning a specific distribution identifier for a person’smulti-value list property so that the group can be used as a distributionlist (mailing list, in the case of an email property).

### Multi Values

[`ABMultiValueAdd`](/documentation/AddressBook/ABMultiValueAdd(_:_:_:_:))

Adds a value and its label to a multi-value list.

[`ABMultiValueCopyIdentifierAtIndex`](/documentation/AddressBook/ABMultiValueCopyIdentifierAtIndex(_:_:))

Returns the identifier at the given index.

[`ABMultiValueCopyLabelAtIndex`](/documentation/AddressBook/ABMultiValueCopyLabelAtIndex(_:_:))

Returns the label for the given index.

[`ABMultiValueCopyPrimaryIdentifier`](/documentation/AddressBook/ABMultiValueCopyPrimaryIdentifier(_:))

Returns the identifier for the primary value.

[`ABMultiValueCopyValueAtIndex`](/documentation/AddressBook/ABMultiValueCopyValueAtIndex(_:_:))

Returns the value for the given index.

[`ABMultiValueCount`](/documentation/AddressBook/ABMultiValueCount(_:))

Returns the number of entries in a multi-value list.

[`ABMultiValueCreate`](/documentation/AddressBook/ABMultiValueCreate())

Returns a new ABMultiValue object.

[`ABMultiValueCreateCopy`](/documentation/AddressBook/ABMultiValueCreateCopy(_:))

Returns a copy of a multi-value object.

[`ABMultiValueCreateMutable`](/documentation/AddressBook/ABMultiValueCreateMutable(_:))

Returns a newly created mutable multi-value list object.

[`ABMultiValueCreateMutableCopy`](/documentation/AddressBook/ABMultiValueCreateMutableCopy(_:))

Returns a mutable copy of a multi-value object.

[`ABMultiValueIndexForIdentifier`](/documentation/AddressBook/ABMultiValueIndexForIdentifier(_:_:))

Returns the index for the given identifier.

[`ABMultiValueInsert`](/documentation/AddressBook/ABMultiValueInsert(_:_:_:_:_:))

Inserts a value and its label at the given index in amulti-value list.

[`ABMultiValuePropertyType`](/documentation/AddressBook/ABMultiValuePropertyType(_:))

Returns the type for the values in a multi-value list.

[`ABMultiValueRemove`](/documentation/AddressBook/ABMultiValueRemove(_:_:))

Removes the value and label at the given index.

[`ABMultiValueReplaceLabel`](/documentation/AddressBook/ABMultiValueReplaceLabel(_:_:_:))

Replaces the label at the given index.

[`ABMultiValueReplaceValue`](/documentation/AddressBook/ABMultiValueReplaceValue(_:_:_:))

Replaces the value at the given index.

[`ABMultiValueSetPrimaryIdentifier`](/documentation/AddressBook/ABMultiValueSetPrimaryIdentifier(_:_:))

Sets the primary value to be the value for the given identifier.

### Images

[`ABBeginLoadingImageDataForClient`](/documentation/AddressBook/ABBeginLoadingImageDataForClient(_:_:_:))

Starts an asynchronous fetch for image data in all locations, and returns a non-zero tag for tracking.

[`ABCancelLoadingImageDataForTag`](/documentation/AddressBook/ABCancelLoadingImageDataForTag(_:))

Cancels an asynchronous fetch of an image for the given tag.

### Search Elements

[`ABCopyArrayOfMatchingRecords`](/documentation/AddressBook/ABCopyArrayOfMatchingRecords(_:_:))

Returns an array of records that match the given search element, or an empty array if no records match the search element.

[`ABSearchElementCreateWithConjunction`](/documentation/AddressBook/ABSearchElementCreateWithConjunction(_:_:))

Returns a compound search element created by combiningthe search elements in an array with the given conjunction.

[`ABSearchElementMatchesRecord`](/documentation/AddressBook/ABSearchElementMatchesRecord(_:_:))

Tests whether or not a record matches a search element.

### Properties

[`ABAddPropertiesAndTypes`](/documentation/AddressBook/ABAddPropertiesAndTypes(_:_:_:))

Adds the given properties to all the records of the specified type in the Address Book database, and returns the number of properties successfully added.

[`ABCopyArrayOfPropertiesForRecordType`](/documentation/AddressBook/ABCopyArrayOfPropertiesForRecordType(_:_:))

Returns an array containing the names of all the properties for the specified record type.

[`ABCopyLocalizedPropertyOrLabel`](/documentation/AddressBook/ABCopyLocalizedPropertyOrLabel(_:))

Returns the localized version of a built in property,label, or key.

[`ABLocalizedPropertyOrLabel`](/documentation/AddressBook/ABLocalizedPropertyOrLabel(_:))

Returns the localized version of a built in property, label, or key.

[`ABRemoveProperties`](/documentation/AddressBook/ABRemoveProperties(_:_:_:))

Removes the given properties from all the records of this type in the Address Book database, and returns the number of properties successfully removed.

[`ABTypeOfProperty`](/documentation/AddressBook/ABTypeOfProperty(_:_:_:))

Returns the type of a given property for a given record.

### Records

[`ABAddRecord`](/documentation/AddressBook/ABAddRecord(_:_:))

Adds a record of the specified type to the Address Book database.

[`ABCopyRecordForUniqueId`](/documentation/AddressBook/ABCopyRecordForUniqueId(_:_:))

Returns the record that matches the given unique ID.

[`ABCopyRecordTypeFromUniqueId`](/documentation/AddressBook/ABCopyRecordTypeFromUniqueId(_:_:))

Returns the type name of the record that matches a given unique ID.

[`ABCreateFormattedAddressFromDictionary`](/documentation/AddressBook/ABCreateFormattedAddressFromDictionary(_:_:))

Returns a string containing the formatted address.

[`ABRecordCopyRecordType`](/documentation/AddressBook/ABRecordCopyRecordType(_:))

Returns the type of the given record.

[`ABRecordCopyUniqueId`](/documentation/AddressBook/ABRecordCopyUniqueId(_:))

Returns the unique ID of the receiver.

[`ABRecordCopyValue`](/documentation/AddressBook/ABRecordCopyValue(_:_:))

Returns the value of the given property.

[`ABRecordCreateCopy`](/documentation/AddressBook/ABRecordCreateCopy(_:))

Returns a copy of the given record.

[`ABRecordIsReadOnly`](/documentation/AddressBook/ABRecordIsReadOnly(_:))

Returns whether or not the record is read-only.

[`ABRecordRemoveValue`](/documentation/AddressBook/ABRecordRemoveValue(_:_:_:))

Removes the value of the given property.

[`ABRecordSetValue`](/documentation/AddressBook/ABRecordSetValue(_:_:_:_:))

Sets the value of a given property for a record.

[`ABRemoveRecord`](/documentation/AddressBook/ABRemoveRecord(_:_:))

Removes the specified record from the Address Book database.

### Deprecated

[`ABAddressBookAddRecord`](/documentation/AddressBook/ABAddressBookAddRecord(_:_:_:))

Adds a record to an address book.

[`ABAddressBookCopyArrayOfAllGroups`](/documentation/AddressBook/ABAddressBookCopyArrayOfAllGroups(_:))

Returns an array with all the groups in an address book.

[`ABAddressBookCopyArrayOfAllGroupsInSource`](/documentation/AddressBook/ABAddressBookCopyArrayOfAllGroupsInSource(_:_:))

Returns an array of all groups from a particular source.

[`ABAddressBookCopyArrayOfAllPeople`](/documentation/AddressBook/ABAddressBookCopyArrayOfAllPeople(_:))

Returns all the person records in an address book.

[`ABAddressBookCopyArrayOfAllPeopleInSource`](/documentation/AddressBook/ABAddressBookCopyArrayOfAllPeopleInSource(_:_:))

Returns an array of all person records from a particular source.

[`ABAddressBookCopyArrayOfAllPeopleInSourceWithSortOrdering`](/documentation/AddressBook/ABAddressBookCopyArrayOfAllPeopleInSourceWithSortOrdering(_:_:_:))

Returns an array of all person records in the address book, sorted with the specified order.

[`ABAddressBookCopyArrayOfAllSources`](/documentation/AddressBook/ABAddressBookCopyArrayOfAllSources(_:))

Returns an array of all sources in the address book.

[`ABAddressBookCopyDefaultSource`](/documentation/AddressBook/ABAddressBookCopyDefaultSource(_:))

Returns the default source.

[`ABAddressBookCopyLocalizedLabel`](/documentation/AddressBook/ABAddressBookCopyLocalizedLabel(_:))

Returns a localized version of a record-property label.

[`ABAddressBookCopyPeopleWithName`](/documentation/AddressBook/ABAddressBookCopyPeopleWithName(_:_:))

Performs a prefix search on the composite names of people in an address book and returns an array of persons that match the search criteria.

[`ABAddressBookCreate`](/documentation/AddressBook/ABAddressBookCreate())

Creates a new address book object with data from the Address Book database.

[`ABAddressBookCreateWithOptions`](/documentation/AddressBook/ABAddressBookCreateWithOptions(_:_:))

Creates a new address book object with data from the Address Book database.

[`ABAddressBookGetAuthorizationStatus`](/documentation/AddressBook/ABAddressBookGetAuthorizationStatus())

Returns the authorization status of your app for accessing address book data.

[`ABAddressBookGetGroupCount`](/documentation/AddressBook/ABAddressBookGetGroupCount(_:))

Returns the number of groups in an address book.

[`ABAddressBookGetGroupWithRecordID`](/documentation/AddressBook/ABAddressBookGetGroupWithRecordID(_:_:))

Returns the group with a given record ID.

[`ABAddressBookGetPersonCount`](/documentation/AddressBook/ABAddressBookGetPersonCount(_:))

Returns the number of person records in an address book.

[`ABAddressBookGetPersonWithRecordID`](/documentation/AddressBook/ABAddressBookGetPersonWithRecordID(_:_:))

Returns the person record with a given record ID.

[`ABAddressBookGetSourceWithRecordID`](/documentation/AddressBook/ABAddressBookGetSourceWithRecordID(_:_:))

Returns the source record with the given record ID.

[`ABAddressBookHasUnsavedChanges`](/documentation/AddressBook/ABAddressBookHasUnsavedChanges(_:))

Indicates whether an address book has changes that have not been saved to the Address Book database.

[`ABAddressBookRegisterExternalChangeCallback`](/documentation/AddressBook/ABAddressBookRegisterExternalChangeCallback(_:_:_:))

Registers a callback to receive notifications when the Address Book database is modified.

[`ABAddressBookRemoveRecord`](/documentation/AddressBook/ABAddressBookRemoveRecord(_:_:_:))

Removes a record from an address book.

[`ABAddressBookRequestAccessWithCompletion`](/documentation/AddressBook/ABAddressBookRequestAccessWithCompletion(_:_:))

Requests access to address book data from the user.

[`ABAddressBookRevert`](/documentation/AddressBook/ABAddressBookRevert(_:))

Discards unsaved changes in an address book.

[`ABAddressBookSave`](/documentation/AddressBook/ABAddressBookSave(_:_:))

Saves any unsaved changes to the Address Book database.

[`ABAddressBookUnregisterExternalChangeCallback`](/documentation/AddressBook/ABAddressBookUnregisterExternalChangeCallback(_:_:_:))

Unregisters a callback.

[`ABGroupCopyArrayOfAllMembersWithSortOrdering`](/documentation/AddressBook/ABGroupCopyArrayOfAllMembersWithSortOrdering(_:_:))

Returns the records in a group, using a sort ordering.

[`ABGroupCopySource`](/documentation/AddressBook/ABGroupCopySource(_:))

Returns the source that the group is from.

[`ABGroupCreateInSource`](/documentation/AddressBook/ABGroupCreateInSource(_:))

Creates a group in a particular source.

[`ABMultiValueAddValueAndLabel`](/documentation/AddressBook/ABMultiValueAddValueAndLabel(_:_:_:_:))

Adds a value and its corresponding label to a multivalue property.

[`ABMultiValueCopyArrayOfAllValues`](/documentation/AddressBook/ABMultiValueCopyArrayOfAllValues(_:))

Returns an array with the values in a multivalue property.

[`ABMultiValueGetCount`](/documentation/AddressBook/ABMultiValueGetCount(_:))

Returns the number of values in a multivalue property.

[`ABMultiValueGetFirstIndexOfValue`](/documentation/AddressBook/ABMultiValueGetFirstIndexOfValue(_:_:))

Returns the first location of a value in a multivalue property.

[`ABMultiValueGetIdentifierAtIndex`](/documentation/AddressBook/ABMultiValueGetIdentifierAtIndex(_:_:))

Returns the identifier of a value in a multivalue property.

[`ABMultiValueGetIndexForIdentifier`](/documentation/AddressBook/ABMultiValueGetIndexForIdentifier(_:_:))

Returns the location (within a multivalue property) of a value with a given identifier.

[`ABMultiValueGetPropertyType`](/documentation/AddressBook/ABMultiValueGetPropertyType(_:))

Returns the type of the values contained in a multivalue property.

[`ABMultiValueInsertValueAndLabelAtIndex`](/documentation/AddressBook/ABMultiValueInsertValueAndLabelAtIndex(_:_:_:_:_:))

Inserts a value and a label into a multivalue property.

[`ABMultiValueRemoveValueAndLabelAtIndex`](/documentation/AddressBook/ABMultiValueRemoveValueAndLabelAtIndex(_:_:))

Removes a value from a multivalue property.

[`ABMultiValueReplaceLabelAtIndex`](/documentation/AddressBook/ABMultiValueReplaceLabelAtIndex(_:_:_:))

Replaces a label in a multivalue property with another label.

[`ABMultiValueReplaceValueAtIndex`](/documentation/AddressBook/ABMultiValueReplaceValueAtIndex(_:_:_:))

Replaces a value in a multivalue property with another value.

[`ABPersonComparePeopleByName`](/documentation/AddressBook/ABPersonComparePeopleByName(_:_:_:))

Indicates how two person records get sorted.

[`ABPersonCopyArrayOfAllLinkedPeople`](/documentation/AddressBook/ABPersonCopyArrayOfAllLinkedPeople(_:))

Returns an array of all person records in the address book database that are linked to the given person record.

[`ABPersonCopyCompositeNameDelimiterForRecord`](/documentation/AddressBook/ABPersonCopyCompositeNameDelimiterForRecord(_:))

Returns the delimiter to use between name components.

[`ABPersonCopyImageDataWithFormat`](/documentation/AddressBook/ABPersonCopyImageDataWithFormat(_:_:))

Returns the picture for a person record in the given format.

[`ABPersonCopyLocalizedPropertyName`](/documentation/AddressBook/ABPersonCopyLocalizedPropertyName(_:))

Returns the localized name of a person property

[`ABPersonCopySource`](/documentation/AddressBook/ABPersonCopySource(_:))

Returns the source that the person record is from.

[`ABPersonCreateInSource`](/documentation/AddressBook/ABPersonCreateInSource(_:))

Creates a new person record in a particular source.

[`ABPersonCreatePeopleInSourceWithVCardRepresentation`](/documentation/AddressBook/ABPersonCreatePeopleInSourceWithVCardRepresentation(_:_:))

Creates person records from the given vCard representation.

[`ABPersonCreateVCardRepresentationWithPeople`](/documentation/AddressBook/ABPersonCreateVCardRepresentationWithPeople(_:))

Returns the vCard representation of the given person records.

[`ABPersonGetCompositeNameFormat`](/documentation/AddressBook/ABPersonGetCompositeNameFormat())

Returns the person-name display format.

[`ABPersonGetCompositeNameFormatForRecord`](/documentation/AddressBook/ABPersonGetCompositeNameFormatForRecord(_:))

Returns the person-name display format to use for the given record.

[`ABPersonGetSortOrdering`](/documentation/AddressBook/ABPersonGetSortOrdering())

Returns the user’s sort-ordering preference for lists of persons.

[`ABPersonGetTypeOfProperty`](/documentation/AddressBook/ABPersonGetTypeOfProperty(_:))

Returns the type of a person property.

[`ABPersonHasImageData`](/documentation/AddressBook/ABPersonHasImageData(_:))

Indicates whether a person has a picture.

[`ABPersonRemoveImageData`](/documentation/AddressBook/ABPersonRemoveImageData(_:_:))

Removes a person’s picture.

[`ABRecordCopyCompositeName`](/documentation/AddressBook/ABRecordCopyCompositeName(_:))

Returns an appropriate, human-friendly name for the record.

[`ABRecordGetRecordID`](/documentation/AddressBook/ABRecordGetRecordID(_:))

Returns the unique ID of a record.

[`ABRecordGetRecordType`](/documentation/AddressBook/ABRecordGetRecordType(_:))

Returns the type of a record.

### Functions

[`ABPickerAddProperty`](/documentation/AddressBook/ABPickerAddProperty)

Adds a property to the group of properties available in the record list. Use [`ABPickerRemoveProperty`](/documentation/AddressBook/ABPickerRemoveProperty) to remove a property from the list and [`ABPickerCopyProperties`](/documentation/AddressBook/ABPickerCopyProperties) to obtain the list of properties available in the list.

[`ABPickerChangeAttributes`](/documentation/AddressBook/ABPickerChangeAttributes)

Specifies the selection behaviors for a people-picker window. Use `ABPickerGetAttributes` to obtain the selection behaviors specified for the window.

[`ABPickerClearSearchField`](/documentation/AddressBook/ABPickerClearSearchField)

Clears the search field and resets the list of displayed records.

[`ABPickerCopyColumnTitle`](/documentation/AddressBook/ABPickerCopyColumnTitle)

Obtains the title of a custom property.

[`ABPickerCopyDisplayedProperty`](/documentation/AddressBook/ABPickerCopyDisplayedProperty)

Returns the name of the property currently displayed in the record list.

[`ABPickerCopyProperties`](/documentation/AddressBook/ABPickerCopyProperties)

Obtains the list of properties available in the record list. Use [`ABPickerAddProperty`](/documentation/AddressBook/ABPickerAddProperty) to add a property to the record list and [`ABPickerRemoveProperty`](/documentation/AddressBook/ABPickerRemoveProperty) to remove a property from the list.

[`ABPickerCopySelectedGroups`](/documentation/AddressBook/ABPickerCopySelectedGroups)

Returns the groups selected in the group list as an array of `ABRecord C` objects.

[`ABPickerCopySelectedIdentifiers`](/documentation/AddressBook/ABPickerCopySelectedIdentifiers)

Returns the identifiers of the selected values in a multi-value property or an empty array if the property displayed is a single-value property.

[`ABPickerCopySelectedRecords`](/documentation/AddressBook/ABPickerCopySelectedRecords)

Returns the selection in the record list as an array of ABGroup or `ABPerson C` objects.

[`ABPickerCopySelectedValues`](/documentation/AddressBook/ABPickerCopySelectedValues)

Returns the selected values in a multi-value property or an empty array if no values are selected or the property displayedis a single-value property.

[`ABPickerCreate`](/documentation/AddressBook/ABPickerCreate)

Creates an ABPickerRef. The corresponding window is hidden. Invoke [`ABPickerSetVisibility`](/documentation/AddressBook/ABPickerSetVisibility) to show it. Release with `CFRelease`.

[`ABPickerDeselectAll`](/documentation/AddressBook/ABPickerDeselectAll)

Deselects all selected groups, records, and values in multi-value properties.

[`ABPickerDeselectGroup`](/documentation/AddressBook/ABPickerDeselectGroup)

Deselects a group in the group list.

[`ABPickerDeselectIdentifier`](/documentation/AddressBook/ABPickerDeselectIdentifier)

Deselects a value in multi-value property currently displayed in the record list.

[`ABPickerDeselectRecord`](/documentation/AddressBook/ABPickerDeselectRecord)

Deselects a group in the record list.

[`ABPickerEditInAddressBook`](/documentation/AddressBook/ABPickerEditInAddressBook)

Launches Address Book to edit the item selected in the people-picker window.

[`ABPickerGetAttributes`](/documentation/AddressBook/ABPickerGetAttributes)

Indicates the selection behaviors selected a people-picker window. Use [`ABPickerChangeAttributes`](/documentation/AddressBook/ABPickerChangeAttributes) tospecify selection behaviors for the window.

[`ABPickerGetDelegate`](/documentation/AddressBook/ABPickerGetDelegate)

Obtains the delegate for a people-picker window.

[`ABPickerGetFrame`](/documentation/AddressBook/ABPickerGetFrame)

Returns the position and size of the people-picker window.

[`ABPickerIsVisible`](/documentation/AddressBook/ABPickerIsVisible)

Indicates whether the people-picker window is visible.

[`ABPickerRemoveProperty`](/documentation/AddressBook/ABPickerRemoveProperty)

Removes a property from the group of properties whose values are shown in the record list. Use [`ABPickerAddProperty`](/documentation/AddressBook/ABPickerAddProperty) to add a property to the record list and [`ABPickerCopyProperties`](/documentation/AddressBook/ABPickerCopyProperties) to obtain the list of properties shown in the record list.

[`ABPickerSelectGroup`](/documentation/AddressBook/ABPickerSelectGroup)

Selects a group or a set of groups in the group list.

[`ABPickerSelectIdentifier`](/documentation/AddressBook/ABPickerSelectIdentifier)

Selects a value or a set of values in a multi-value property.

[`ABPickerSelectInAddressBook`](/documentation/AddressBook/ABPickerSelectInAddressBook)

Launches Address Book and selects the item selected in the people-picker window.

[`ABPickerSelectRecord`](/documentation/AddressBook/ABPickerSelectRecord)

Selects a record or a set of records in the record list.

[`ABPickerSetColumnTitle`](/documentation/AddressBook/ABPickerSetColumnTitle)

Sets the title for a custom property.

[`ABPickerSetDelegate`](/documentation/AddressBook/ABPickerSetDelegate)

Sets the event handler for people-picker events.

[`ABPickerSetDisplayedProperty`](/documentation/AddressBook/ABPickerSetDisplayedProperty)

Displays one of the properties whose values are shownin the record list.

[`ABPickerSetFrame`](/documentation/AddressBook/ABPickerSetFrame)

Specifies the position and size of the people-picker window.

[`ABPickerSetVisibility`](/documentation/AddressBook/ABPickerSetVisibility)

Shows or hides a people-picker window.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)

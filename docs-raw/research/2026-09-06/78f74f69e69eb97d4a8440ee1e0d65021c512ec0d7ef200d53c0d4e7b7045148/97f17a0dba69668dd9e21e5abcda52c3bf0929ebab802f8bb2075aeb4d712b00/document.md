# EventKit

Create, view, and edit calendar and reminder events.

## Overview

The EventKit framework provides access to calendar and reminders data so people can create, retrieve, and edit calendar items in your app. In iOS, <doc://com.apple.documentation/documentation/EventKitUI> provides user interfaces you can implement in your app so people can create and edit calendar items.

You can use EventKit to set up alarms and create recurring events. And if a change to the Calendar database occurs from outside your app, EventKit detects the change and sends a notification, allowing your app to stay up to date.

## Topics

### Essentials

[Accessing the event store](/documentation/EventKit/accessing-the-event-store)

Request access to a person’s calendar data through the event store.

[`EKEventStore`](/documentation/EventKit/EKEventStore)

An object that accesses a person’s calendar events and reminders and supports the scheduling of new events.

[Accessing Calendar using EventKit and EventKitUI](/documentation/EventKit/accessing-calendar-using-eventkit-and-eventkitui)

Choose and implement the appropriate Calendar access level in your app.

### Events and reminders

[Creating events and reminders](/documentation/EventKit/creating-events-and-reminders)

Create and modify events and reminders in a person’s database.

[Retrieving events and reminders](/documentation/EventKit/retrieving-events-and-reminders)

Fetch events and reminders from the Calendar database.

[Updating with notifications](/documentation/EventKit/updating-with-notifications)

Register for notifications about changes and keep your app up to date.

[Managing location-based reminders](/documentation/EventKit/managing-location-based-reminders)

Access reminders set up with geofence-enabled alarms on a person’s calendars.

[`EKEvent`](/documentation/EventKit/EKEvent)

A class that represents an event in a calendar.

[`EKReminder`](/documentation/EventKit/EKReminder)

A class that represents a reminder in a calendar.

### Calendars

[`EKCalendar`](/documentation/EventKit/EKCalendar)

A class that represents a calendar in EventKit.

[`EKParticipant`](/documentation/EventKit/EKParticipant)

A class that represents person, group, or room invited to a calendar event.

### Recurrence

[Creating a recurring event](/documentation/EventKit/creating-a-recurring-event)

Set up an event or reminder that repeats.

[`EKRecurrenceDayOfWeek`](/documentation/EventKit/EKRecurrenceDayOfWeek)

A class that represents the day of the week.

[`EKRecurrenceEnd`](/documentation/EventKit/EKRecurrenceEnd)

A class that defines the end of a recurrence rule.

[`EKRecurrenceRule`](/documentation/EventKit/EKRecurrenceRule)

A class that describes the pattern for a recurring event.

### Alarms

[Setting an alarm](/documentation/EventKit/setting-an-alarm)

Alert users of events and reminders with an alarm.

[`EKAlarm`](/documentation/EventKit/EKAlarm)

A class that represents an alarm.

[`EKStructuredLocation`](/documentation/EventKit/EKStructuredLocation)

`A` class that specifies a geofence to activate the alarm of a calendar item.

### Common objects

[`EKCalendarItem`](/documentation/EventKit/EKCalendarItem)

An abstract superclass for calendar events and reminders.

[`EKObject`](/documentation/EventKit/EKObject)

An abstract superclass for all EventKit classes that have persistent instances.

[`EKSource`](/documentation/EventKit/EKSource)

An abstract superclass that represents the account a calendar belongs to.

### Virtual conferences

[Implementing a virtual conference extension](/documentation/EventKit/implementing-a-virtual-conference-extension)

Support adding a virtual conference room to an event in Calendar.

[`EKVirtualConferenceProvider`](/documentation/EventKit/EKVirtualConferenceProvider)

An object that associates virtual conferencing details with an event object in a user’s calendar.

[`EKVirtualConferenceDescriptor`](/documentation/EventKit/EKVirtualConferenceDescriptor)

Details about a virtual conference that uses a custom room type.

[`EKVirtualConferenceRoomTypeDescriptor`](/documentation/EventKit/EKVirtualConferenceRoomTypeDescriptor)

Details about a room where virtual conferences take place.

### Errors

[`EKError`](/documentation/EventKit/EKError)

An EventKit error.

[`Code`](/documentation/EventKit/EKError/Code)

Error codes for EventKit errors.

[`EKErrorDomain`](/documentation/EventKit/EKErrorDomain)

A string that identifies the EventKit error domain.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)

# Calendar

Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.

## Discussion

The `.calendar` domain defines app schemas that provide a
structured representation for common calendar actions and content.
Apply schemas in the `.calendar` domain to make your app’s calendar functionality available to Apple Intelligence and Siri.

The following table maps example phrases that apply to each schema:

|Calendar intent schemas                                                                     |Example phrases                                                       |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
|``doc://com.apple.AppIntents/documentation/AppIntents/AppSchema/CalendarIntent/createEvent``|“Create an event.” or “Schedule a meeting with Bill tomorrow at 2 PM.”|
|``doc://com.apple.AppIntents/documentation/AppIntents/AppSchema/CalendarIntent/deleteEvent``|“Delete this event.” or “Cancel the meeting.”                         |
|``doc://com.apple.AppIntents/documentation/AppIntents/AppSchema/CalendarIntent/updateEvent``|“Reschedule the meeting.” or “Move the meeting to tomorrow.”          |

> Tip: Xcode generates a template implementation when you type `calendar_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [Apple Intelligence and Siri AI](/documentation/AppIntents/apple-intelligence-and-siri-ai).

## Topics

### Essentials

[Integrating your calendar app with Apple Intelligence](/documentation/AppIntents/integrating-your-calendar-app-with-apple-intelligence)

Adopt calendar schemas so people can create, find, and manage events with Siri.

### Actions

[`createEvent`](/documentation/AppIntents/AppSchema/CalendarIntent/createEvent)

An intent schema that creates a calendar event.

[`deleteEvent`](/documentation/AppIntents/AppSchema/CalendarIntent/deleteEvent)

An intent schema that deletes a calendar event.

[`updateEvent`](/documentation/AppIntents/AppSchema/CalendarIntent/updateEvent)

An intent schema that updates a calendar event.

[`CalendarIntent`](/documentation/AppIntents/AppSchema/CalendarIntent)

Identifies intent schemas in the calendar domain.

### Content and parameter types

[`attendee`](/documentation/AppIntents/AppSchema/CalendarEntity/attendee)

An entity schema for an attendee.

[`calendar`](/documentation/AppIntents/AppSchema/CalendarEntity/calendar)

An entity schema for a calendar.

[`event`](/documentation/AppIntents/AppSchema/CalendarEntity/event)

An entity schema for an event.

[`CalendarEntity`](/documentation/AppIntents/AppSchema/CalendarEntity)

Identifies entity schemas in the calendar domain.

### Types for static parameters

[`attendeeStatus`](/documentation/AppIntents/AppSchema/CalendarEnum/attendeeStatus)

An enum schema for an attendee status parameter.

[`attendeeType`](/documentation/AppIntents/AppSchema/CalendarEnum/attendeeType)

An enum schema for an attendee type parameter.

[`eventSpan`](/documentation/AppIntents/AppSchema/CalendarEnum/eventSpan)

An enum schema for an event span parameter.

[`eventStatus`](/documentation/AppIntents/AppSchema/CalendarEnum/eventStatus)

An enum schema for an event status parameter.

[`CalendarEnum`](/documentation/AppIntents/AppSchema/CalendarEnum)

Identifies enum schemas in the calendar domain.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)

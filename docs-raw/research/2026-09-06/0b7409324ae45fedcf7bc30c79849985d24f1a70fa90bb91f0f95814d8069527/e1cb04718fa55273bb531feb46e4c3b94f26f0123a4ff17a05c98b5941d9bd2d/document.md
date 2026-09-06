# Setting an alarm

Alert users of events and reminders with an alarm.

## Discussion

An easy way to alert users of their upcoming events is to give them the option of setting alarms for their calendar items. Regardless of the app that’s currently running, alarms come to the foreground as a notification and remind users of the scheduled event. If an alarm is set to a calendar event, the notification comes from the Calendar app; if an alarm is set to a reminder, the notification comes from the Reminders app.

Alarms can be time-based, firing at a specified time, or location-based, firing when crossing a geofence (for more information about geofences, see “`Configure Geofences`”). Alarms can be applied to both calendar events and reminders.

> Note:
> An alarm is not intended to serve as a <doc://com.apple.documentation/documentation/UIKit/UILocalNotification>. An alarm requires you to create an event or reminder that is visible in the user’s Calendar or Reminders app. A <doc://com.apple.documentation/documentation/UIKit/UILocalNotification> is better suited for general purposes that don’t involve the Calendar database.

### Add and Remove Alarms

Add an alarm to an event with the [`addAlarm(_:)`](/documentation/EventKit/EKCalendarItem/addAlarm(_:)) method.

Alarms can be created with an absolute date or with an offset relative to the start date of the event. Alarms created with a relative offset must occur before or at the start date of the event.

In OS X, you can trigger an action alongside the alarm. For example, you can set properties such as:

- [`emailAddress`](/documentation/EventKit/EKAlarm/emailAddress) to send an email.
- [`soundName`](/documentation/EventKit/EKAlarm/soundName) to play a sound.
- [`url`](/documentation/EventKit/EKAlarm/url) to open a URL.

Remove an alarm from an event with the [`removeAlarm(_:)`](/documentation/EventKit/EKCalendarItem/removeAlarm(_:)) method.

### Configure Geofences

A geofence is a virtual border surrounding a geographic location that, when crossed, triggers an alarm for an event. You specify the latitude and longitude of the center and the radius of the geofence.

While geofence-enabled alarms can be applied to events, they are more practical for reminders. Geofences are a useful way to remind users of tasks they need to do when entering or exiting a certain region. For example, when a user leaves their workplace, an alarm can remind them to stop by the grocery store.

> Note:
> Geofences are supported on both macOS and iOS, but they are more effective on mobile devices.

Configure a geofence for an event by creating an alarm and setting its structured location and proximity. Call the [`init(title:)`](/documentation/EventKit/EKStructuredLocation/init(title:)) method to create a structured location. To set longitude and latitude coordinates, pass a <doc://com.apple.documentation/documentation/CoreLocation/CLLocation> to the [`geoLocation`](/documentation/EventKit/EKStructuredLocation/geoLocation) property of the structured location returned. A value of `0` for the radius property will use the system’s default radius; to choose a radius of your own, specify a value in meters.

---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)

# Client

An opaque type that maintains Endpoint Security client state, and functions related to this type.

## Discussion

Create an Endpoint Security client with [`es_new_client(_:_:)`](/documentation/EndpointSecurity/es_new_client(_:_:)), then use this client to subscribe to event types of interest to your app or system extension. When Endpoint Security monitors an event your client subscribes to, it sends a message that describes the event to your client. When you no longer need the client, remove it with [`es_delete_client(_:)`](/documentation/EndpointSecurity/es_delete_client(_:)).

The following code creates a client and handles any errors returned by [`es_new_client(_:_:)`](/documentation/EndpointSecurity/es_new_client(_:_:)). If client creation succeeds, the code subscribes the client to the [`ES_EVENT_TYPE_AUTH_EXEC`](/documentation/EndpointSecurity/ES_EVENT_TYPE_AUTH_EXEC) event. The handler passed to [`es_new_client(_:_:)`](/documentation/EndpointSecurity/es_new_client(_:_:)) allows any such event to proceed.

```c
// Create the client.
es_client_t *client = NULL;
es_new_client_result_t newClientResult =
es_new_client(&client,
              ^(es_client_t * client, const es_message_t * message) {
    switch (message->event_type) {
        case ES_EVENT_TYPE_AUTH_EXEC:
            es_respond_auth_result(client, message, ES_AUTH_RESULT_ALLOW, true);
            break;
        default:
            panic("Found unexpected event type: %i", message->event_type);
            break;
    }
});

// Handle any errors encountered while creating the client.
switch (newClientResult) {
    case ES_NEW_CLIENT_RESULT_SUCCESS:
        // Client created successfully; continue.
        break;
    case ES_NEW_CLIENT_RESULT_ERR_NOT_ENTITLED:
        panic("Extension is missing entitlement.");
        break;
    case ES_NEW_CLIENT_RESULT_ERR_NOT_PRIVILEGED:
        panic ("Extension is not running as root.");
        break;
    case ES_NEW_CLIENT_RESULT_ERR_NOT_PERMITTED:
        // Prompt user to perform Transparency, Consent,
        // and Control (TCC) approval.
        // This error is recoverable; the user can try again after
        // approving the TCC prompt.
        return YOUR_NEW_CLIENT_ERROR_CODE_PROMPT_TCC;
        break;
    case ES_NEW_CLIENT_RESULT_ERR_INVALID_ARGUMENT:
        panic ("Invalid argument to es_new_client(); client or handler was null.");
        break;
    case ES_NEW_CLIENT_RESULT_ERR_TOO_MANY_CLIENTS:
        panic ("Exceeded maximum number of simultaneously-connected ES clients.");
        break;
    case ES_NEW_CLIENT_RESULT_ERR_INTERNAL:
        panic ("Failed to connect to the Endpoint Security subsystem.");
        break;
}

// Subscribe the client to the ES_EVENT_TYPE_AUTH_EXEC event.
// When the client receives a message with this event type, it must authorize
// (allow or deny) the event.
es_event_type_t eventTypes[1] = { ES_EVENT_TYPE_AUTH_EXEC };
es_return_t subscribeResult = es_subscribe(client, eventTypes, sizeof(eventTypes));
if (subscribeResult != ES_RETURN_SUCCESS) {
    panic ("Client failed to subscribe to event."); 
}
```

## Topics

### Creating a Client

[`es_client_t`](/documentation/EndpointSecurity/es_client_t)

An opaque type that stores the Endpoint Security client state.

[`es_new_client`](/documentation/EndpointSecurity/es_new_client(_:_:))

Creates a new client instance and connects it to the Endpoint Security system.

[`es_handler_block_t`](/documentation/EndpointSecurity/es_handler_block_t)

A block that handles a message received from Endpoint Security.

[`es_new_client_result_t`](/documentation/EndpointSecurity/es_new_client_result_t)

The result of an attempt to create a new client.

### Destroying a Client

[`es_delete_client`](/documentation/EndpointSecurity/es_delete_client(_:))

Destroys and disconnects a client instance from the Endpoint Security system.

### Subscribing to Events

[`es_subscribe`](/documentation/EndpointSecurity/es_subscribe(_:_:_:))

Subscribes a client to a set of events.

[`es_subscriptions`](/documentation/EndpointSecurity/es_subscriptions(_:_:_:))

Returns a list of the client’s subscriptions.

[`es_unsubscribe`](/documentation/EndpointSecurity/es_unsubscribe(_:_:_:))

Unsubscribes the provided client from a set of events.

[`es_event_type_t`](/documentation/EndpointSecurity/es_event_type_t)

A type used to identify a message’s event type and subscribe to events of that type.

[`es_unsubscribe_all`](/documentation/EndpointSecurity/es_unsubscribe_all(_:))

Unsubscribes a client from all events.

### Responding to Events

[`es_respond_auth_result`](/documentation/EndpointSecurity/es_respond_auth_result(_:_:_:_:))

Responds to an event that requires an authorization response.

[`es_auth_result_t`](/documentation/EndpointSecurity/es_auth_result_t)

Values used when responding to an authorization event.

[`es_respond_flags_result`](/documentation/EndpointSecurity/es_respond_flags_result(_:_:_:_:))

Responds to an event that requires authorization flags as a response.

[`es_respond_result_t`](/documentation/EndpointSecurity/es_respond_result_t)

Values that indicate the result of responding to a message.

### Managing Cached Results

[`es_clear_cache`](/documentation/EndpointSecurity/es_clear_cache(_:))

Clears all cached results for all clients.

[`es_clear_cache_result_t`](/documentation/EndpointSecurity/es_clear_cache_result_t)

Values that indicate the result of clearing a cache.

### Muting Events

[`es_mute_process`](/documentation/EndpointSecurity/es_mute_process(_:_:))

Suppresses events from a given process.

[`es_mute_process_events`](/documentation/EndpointSecurity/es_mute_process_events(_:_:_:_:))

Suppresses a subset of events from a given process.

[`es_muted_processes_t`](/documentation/EndpointSecurity/es_muted_processes_t)

A structure for a set of muted processes.

[`es_release_muted_processes`](/documentation/EndpointSecurity/es_release_muted_processes(_:))

Frees resources associated with a set of previously-retrieved muted processes.

[`es_muted_processes_events`](/documentation/EndpointSecurity/es_muted_processes_events(_:_:))

Retrieve a list of all muted processes.

[`es_mute_path`](/documentation/EndpointSecurity/es_mute_path(_:_:_:))

Suppresses events from executables that match a given path.

[`es_mute_path_events`](/documentation/EndpointSecurity/es_mute_path_events(_:_:_:_:_:))

Suppresses a subset of events from executables that match a given path.

[`es_mute_path_type_t`](/documentation/EndpointSecurity/es_mute_path_type_t)

The type of a path argument, such as a prefix or a path literal.

[`es_muted_paths_events`](/documentation/EndpointSecurity/es_muted_paths_events(_:_:))

Retrieve a list of all muted paths.

[`es_muted_paths_t`](/documentation/EndpointSecurity/es_muted_paths_t)

A structure for a set of muted paths.

[`es_release_muted_paths`](/documentation/EndpointSecurity/es_release_muted_paths(_:))

Frees resources associated with a set of previously-retrieved muted paths.

### Unmuting Events

[`es_unmute_process`](/documentation/EndpointSecurity/es_unmute_process(_:_:))

Restores event delivery from a previously-muted process.

[`es_unmute_process_events`](/documentation/EndpointSecurity/es_unmute_process_events(_:_:_:_:))

Restores event delivery of a subset of events from a previously-muted process.

[`es_unmute_path`](/documentation/EndpointSecurity/es_unmute_path(_:_:_:))

Restores event delivery from a previously-muted path.

[`es_unmute_path_events`](/documentation/EndpointSecurity/es_unmute_path_events(_:_:_:_:_:))

Restores event delivery of a subset of events from a previously-muted path.

[`es_mute_path_type_t`](/documentation/EndpointSecurity/es_mute_path_type_t)

The type of a path argument, such as a prefix or a path literal.

[`es_unmute_all_paths`](/documentation/EndpointSecurity/es_unmute_all_paths(_:))

Restores event delivery from previously-muted paths.

### Deprecated Functions

[`es_muted_processes`](/documentation/EndpointSecurity/es_muted_processes(_:_:_:))

Generates a list of muted processes.

[`es_mute_path_literal`](/documentation/EndpointSecurity/es_mute_path_literal(_:_:))

Suppresses events from executables matching a path literal.

[`es_mute_path_prefix`](/documentation/EndpointSecurity/es_mute_path_prefix(_:_:))

Suppresses events from executables matching a path prefix.

### Supporting Types

[`es_return_t`](/documentation/EndpointSecurity/es_return_t)

Values that indicate the result of an Endpoint Security action that can only succeed or fail.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)

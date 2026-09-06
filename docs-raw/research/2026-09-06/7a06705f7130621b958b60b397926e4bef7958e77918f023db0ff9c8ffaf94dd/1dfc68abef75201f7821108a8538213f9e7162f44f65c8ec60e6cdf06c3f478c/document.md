# XPC connections

Create and manage connections to services using connection-based APIs.

## Discussion

Use these APIs to work with XPC connections and related types — for example, when a framework function that you call returns an [`xpc_connection_t`](/documentation/XPC/xpc_connection_t).

But, in most situations, the listener- and session-based APIs are a better choice for designing XPC communication protocols. For more information, see [Creating XPC services](/documentation/XPC/creating-xpc-services).

## Topics

### Creation

[`xpc_connection_t`](/documentation/XPC/xpc_connection_t)

A type that represents a connection to a named service.

[`xpc_connection_create`](/documentation/XPC/xpc_connection_create(_:_:))

Creates a new connection object.

[`xpc_connection_create_from_endpoint`](/documentation/XPC/xpc_connection_create_from_endpoint(_:))

Creates a new connection from the specified endpoint.

[`xpc_connection_create_mach_service`](/documentation/XPC/xpc_connection_create_mach_service(_:_:_:))

Creates a new connection object that represents a Mach service.

[`xpc_connection_set_target_queue`](/documentation/XPC/xpc_connection_set_target_queue(_:_:))

Sets the target queue of the connection.

[`XPC_CONNECTION_MACH_SERVICE_LISTENER`](/documentation/XPC/XPC_CONNECTION_MACH_SERVICE_LISTENER)

A flag that indicates the caller is the listener for the named service.

[`XPC_CONNECTION_MACH_SERVICE_PRIVILEGED`](/documentation/XPC/XPC_CONNECTION_MACH_SERVICE_PRIVILEGED)

A flag that indicates the job advertising the service name belongs to a launch daemon rather than a launch agent.

### Event handling

[`xpc_connection_set_event_handler`](/documentation/XPC/xpc_connection_set_event_handler(_:_:))

Sets the event handler block for the connection.

[`xpc_handler_t`](/documentation/XPC/xpc_handler_t)

The type of block that the XPC connection APIs accept.

[`xpc_connection_handler_t`](/documentation/XPC/xpc_connection_handler_t)

The type of the function to invoke for a bundled XPC service when there’s a new connection on the service.

### Life cycle

[`xpc_main`](/documentation/XPC/xpc_main(_:))

Starts listening for incoming connections and processes them with the specified event handler.

[`xpc_connection_activate`](/documentation/XPC/xpc_connection_activate(_:))

Activates a new connection.

[`xpc_connection_suspend`](/documentation/XPC/xpc_connection_suspend(_:))

Suspends the connection so the event handler block doesn’t fire and the connection doesn’t attempt to send any messages it has in its queue.

[`xpc_connection_resume`](/documentation/XPC/xpc_connection_resume(_:))

Resumes a suspended connection.

[`xpc_connection_cancel`](/documentation/XPC/xpc_connection_cancel(_:))

Cancels the connection and ensures that its event handler doesn’t fire again.

[`xpc_transaction_begin`](/documentation/XPC/xpc_transaction_begin())

Informs the XPC runtime when a transaction begins, indicating that the service isn’t idle.

[`xpc_transaction_end`](/documentation/XPC/xpc_transaction_end())

Informs the XPC runtime when a transaction ends.

[`xpc_connection_copy_invalidation_reason`](/documentation/XPC/xpc_connection_copy_invalidation_reason(_:))

### Messages

[`xpc_connection_send_message`](/documentation/XPC/xpc_connection_send_message(_:_:))

Sends a message over the connection to the destination service.

[`xpc_connection_send_barrier`](/documentation/XPC/xpc_connection_send_barrier(_:_:))

Issues a barrier against the connection’s message-send activity.

[`xpc_connection_send_message_with_reply`](/documentation/XPC/xpc_connection_send_message_with_reply(_:_:_:_:))

Sends a message over the connection to the destination service and associates a handler to invoke when the remote service sends a reply message.

[`xpc_connection_send_message_with_reply_sync`](/documentation/XPC/xpc_connection_send_message_with_reply_sync(_:_:))

Sends a message over the connection and blocks the caller until it receives a reply.

[`xpc_main`](/documentation/XPC/xpc_main(_:))

Starts listening for incoming connections and processes them with the specified event handler.

### Remote peer information

[`xpc_connection_get_name`](/documentation/XPC/xpc_connection_get_name(_:))

Returns the name of the remote service that creates the connection.

[`xpc_connection_get_euid`](/documentation/XPC/xpc_connection_get_euid(_:))

Returns the EUID of the remote peer.

[`xpc_connection_get_egid`](/documentation/XPC/xpc_connection_get_egid(_:))

Returns the EGID of the remote peer.

[`xpc_connection_get_pid`](/documentation/XPC/xpc_connection_get_pid(_:))

Returns the PID of the remote peer.

[`xpc_connection_get_asid`](/documentation/XPC/xpc_connection_get_asid(_:))

Returns the audit session identifier of the remote peer.

[`xpc_connection_set_peer_entitlement_exists_requirement`](/documentation/XPC/xpc_connection_set_peer_entitlement_exists_requirement(_:_:))

Sets a requirement that the executable for the peer process has a valid code signature that contains an entitlement.

[`xpc_connection_set_peer_entitlement_matches_value_requirement`](/documentation/XPC/xpc_connection_set_peer_entitlement_matches_value_requirement(_:_:_:))

Sets a requirement that the executable for the peer process has a valid code signature that contains an entitlement with a specific value.

[`xpc_connection_set_peer_lightweight_code_requirement`](/documentation/XPC/xpc_connection_set_peer_lightweight_code_requirement(_:_:))

Sets a requirement that the executable for the peer process has a valid code signature that matches the lightweight code requirement.

[`xpc_connection_set_peer_platform_identity_requirement`](/documentation/XPC/xpc_connection_set_peer_platform_identity_requirement(_:_:))

Sets a requirement that the executable for the peer process has a valid code signature that identifies it as an Apple-signed binary with the given signing identifier.

[`xpc_connection_set_peer_team_identity_requirement`](/documentation/XPC/xpc_connection_set_peer_team_identity_requirement(_:_:))

Sets a requirement that the executable for the peer process has a valid code signature and is signed by the same team identifier as the calling process.

[`xpc_connection_set_peer_code_signing_requirement`](/documentation/XPC/xpc_connection_set_peer_code_signing_requirement(_:_:))

### Context

[`xpc_connection_set_context`](/documentation/XPC/xpc_connection_set_context(_:_:))

Sets a context on the connection.

[`xpc_connection_get_context`](/documentation/XPC/xpc_connection_get_context(_:))

Returns the context for the connection.

[`xpc_connection_set_finalizer_f`](/documentation/XPC/xpc_connection_set_finalizer_f(_:_:))

Sets the finalizer for the connection.

[`xpc_finalizer_t`](/documentation/XPC/xpc_finalizer_t)

A function to invoke when tearing down a connection and freeing its context.

### Endpoints

[`xpc_endpoint_create`](/documentation/XPC/xpc_endpoint_create(_:))

Creates a new endpoint from a connection that is suitable for embedding into messages.

[`xpc_endpoint_t`](/documentation/XPC/xpc_endpoint_t)

A type that represents a connection in serialized form.

### Errors

[`XPC_ERROR_CONNECTION_INVALID`](/documentation/XPC/XPC_ERROR_CONNECTION_INVALID-swift.var)

An error that sends to the connection’s event handler to indicate that the connection is no longer usable.

[`XPC_ERROR_CONNECTION_INTERRUPTED`](/documentation/XPC/XPC_ERROR_CONNECTION_INTERRUPTED-swift.var)

An error that sends to the connection’s event handler when the remote service exits.

[`XPC_ERROR_TERMINATION_IMMINENT`](/documentation/XPC/XPC_ERROR_TERMINATION_IMMINENT-swift.var)

An error that sends to a peer connection’s event handler when the XPC runtime determines that the program needs to exit and that all outstanding transactions must wind down.

[`XPC_ERROR_CONNECTION_INVALID`](/documentation/XPC/XPC_ERROR_CONNECTION_INVALID-c.macro)

An error that sends to the connection’s event handler to indicate that the connection is no longer usable.

[`XPC_ERROR_CONNECTION_INTERRUPTED`](/documentation/XPC/XPC_ERROR_CONNECTION_INTERRUPTED-c.macro)

An error that sends to the connection’s event handler when the remote service exits.

[`XPC_ERROR_TERMINATION_IMMINENT`](/documentation/XPC/XPC_ERROR_TERMINATION_IMMINENT-c.macro)

An error that sends to a peer connection’s event handler when the XPC runtime determines that the program needs to exit and that all outstanding transactions must wind down.



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)

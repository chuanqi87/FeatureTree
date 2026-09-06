# GooglePlayGames. BasicApi. Nearby. IDiscoveryListener

# GooglePlayGames.BasicApi.Nearby.IDiscoveryListener

Interface for receiving notifications about discovered endpoints.

## Summary

| Public functions | |
| --- | --- |
| `OnEndpointFound(EndpointDetails discoveredEndpoint)` | `void`  Called when an endpoint is found during discovery. |
| `OnEndpointLost(string lostEndpointId)` | `void`  Called when an endpoint is lost during discovery. |

## Public functions

### OnEndpointFound

```
void OnEndpointFound(
  EndpointDetails discoveredEndpoint
)
```

Called when an endpoint is found during discovery.

Details | || Parameters | |  |  | | --- | --- | | `discoveredEndpoint` | The details of the discovered endpoint. | |

### OnEndpointLost

```
void OnEndpointLost(
  string lostEndpointId
)
```

Called when an endpoint is lost during discovery.

Details | || Parameters | |  |  | | --- | --- | | `lostEndpointId` | The ID of the lost endpoint. | |

# Play Games Services

# Play Games Services

Native API for Play Games Services.

## Summary

| Typedefs | |
| --- | --- |
| `PgsAchievementsClient` | typedef `struct PgsAchievementsClient`  An opaque handle to the Achievements Client. |
| `PgsGameStatsClient` | typedef `struct PgsGameStatsClient`  An opaque handle to the GameStats Client. |
| `PgsGamesSignInClient` | typedef `struct PgsGamesSignInClient`  An opaque handle to the GamesSignIn Client. |
| `PgsLeaderboardsClient` | typedef `struct PgsLeaderboardsClient`  An opaque handle to the Leaderboards Client. |
| `PgsRecallClient` | typedef `struct PgsRecallClient`  An opaque handle to the Recall Client. |
| `PgsSnapshotsClient` | typedef `struct PgsSnapshotsClient`  An opaque handle to the Snapshots Client. |

| Functions | |
| --- | --- |
| `PgsAchievementsClient_create(jobject activity)` | `PgsAchievementsClient *`  Creates a new Achievements Client instance. |
| `PgsAchievementsClient_destroy(PgsAchievementsClient *achievements_client)` | `void`  Destroys an Achievements Client instance. |
| `PgsGameStatsClient_create(jobject activity)` | `PgsGameStatsClient *`  Creates a new GameStats Client instance. |
| `PgsGameStatsClient_destroy(PgsGameStatsClient *game_stats_client)` | `void`  Destroys a GameStats Client instance. |
| `PgsGamesSignInClient_create(jobject activity)` | `PgsGamesSignInClient *`  Creates a new GamesSignIn Client instance. |
| `PgsGamesSignInClient_destroy(PgsGamesSignInClient *games_sign_in_client)` | `void`  Destroys a GamesSignIn Client instance. |
| `PgsLeaderboardsClient_create(jobject activity)` | `PgsLeaderboardsClient *`  Creates a new Leaderboards Client instance. |
| `PgsLeaderboardsClient_destroy(PgsLeaderboardsClient *leaderboards_client)` | `void`  Destroys a Leaderboards Client instance. |
| `PgsRecallClient_create(jobject activity)` | `PgsRecallClient *`  Creates a new Recall Client instance. |
| `PgsRecallClient_destroy(PgsRecallClient *recall_client)` | `void`  Destroys a Recall Client instance. |
| `PgsSnapshotsClient_create(jobject activity)` | `PgsSnapshotsClient *`  Creates a new Snapshots Client instance. |
| `PgsSnapshotsClient_destroy(PgsSnapshotsClient *snapshots_client)` | `void`  Destroys a Snapshots Client instance. |
| `Pgs_destroy()` | `void`  Shuts down the Play Games Services native SDK. |
| `Pgs_initialize(JavaVM *vm, jobject context)` | `jint`  Initializes the Play Games Services native SDK. |

## Typedefs

### PgsAchievementsClient

```
struct PgsAchievementsClient PgsAchievementsClient
```

An opaque handle to the Achievements Client.

### PgsGameStatsClient

```
struct PgsGameStatsClient PgsGameStatsClient
```

An opaque handle to the GameStats Client.

### PgsGamesSignInClient

```
struct PgsGamesSignInClient PgsGamesSignInClient
```

An opaque handle to the GamesSignIn Client.

### PgsLeaderboardsClient

```
struct PgsLeaderboardsClient PgsLeaderboardsClient
```

An opaque handle to the Leaderboards Client.

### PgsRecallClient

```
struct PgsRecallClient PgsRecallClient
```

An opaque handle to the Recall Client.

### PgsSnapshotsClient

```
struct PgsSnapshotsClient PgsSnapshotsClient
```

An opaque handle to the Snapshots Client.

## Functions

### PgsAchievementsClient\_create

```
PgsAchievementsClient * PgsAchievementsClient_create(
  jobject activity
)
```

Creates a new Achievements Client instance.

This function creates a client handle for interacting with the achievements API.

Details | || Parameters | |  |  | | --- | --- | | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsAchievementsClient handle, or NULL on failure. This handle must be released with [PgsAchievementsClient\_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga3ab2b8387edbfe3768119f94fd3ca358). |

### PgsAchievementsClient\_destroy

```
void PgsAchievementsClient_destroy(
  PgsAchievementsClient *achievements_client
)
```

Destroys an Achievements Client instance.

This function releases all resources associated with the client handle. The handle becomes invalid after this call.

Details | || Parameters | |  |  | | --- | --- | | `achievements_client` | The client handle to destroy. | |

### PgsGameStatsClient\_create

```
PgsGameStatsClient * PgsGameStatsClient_create(
  jobject activity
)
```

Creates a new GameStats Client instance.

Details | || Parameters | |  |  | | --- | --- | | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsGameStatsClient handle, or NULL on failure. This handle must be released with [PgsGameStatsClient\_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga7cf1239c0035ff7f90748e29d5331bfa). |

### PgsGameStatsClient\_destroy

```
void PgsGameStatsClient_destroy(
  PgsGameStatsClient *game_stats_client
)
```

Destroys a GameStats Client instance.

Details | || Parameters | |  |  | | --- | --- | | `game_stats_client` | The client handle to destroy. | |

### PgsGamesSignInClient\_create

```
PgsGamesSignInClient * PgsGamesSignInClient_create(
  jobject activity
)
```

Creates a new GamesSignIn Client instance.

This function creates a client handle for interacting with the GamesSignIn API.

Details | || Parameters | |  |  | | --- | --- | | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsGamesSignInClient handle, or NULL on failure. This handle must be released with [PgsGamesSignInClient\_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga9cba93bc35798c2bb4491a23dc9d3287). |

### PgsGamesSignInClient\_destroy

```
void PgsGamesSignInClient_destroy(
  PgsGamesSignInClient *games_sign_in_client
)
```

Destroys a GamesSignIn Client instance.

This function releases all resources associated with the client handle. The handle becomes invalid after this call.

Details | || Parameters | |  |  | | --- | --- | | `games_sign_in_client` | The client handle to destroy. | |

### PgsLeaderboardsClient\_create

```
PgsLeaderboardsClient * PgsLeaderboardsClient_create(
  jobject activity
)
```

Creates a new Leaderboards Client instance.

This function creates a client handle for interacting with the Leaderboards API.

Details | || Parameters | |  |  | | --- | --- | | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsLeaderboardsClient handle, or NULL on failure. This handle must be released with [PgsLeaderboardsClient\_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga9e0468b2dc577647903becf99dc43103). |

### PgsLeaderboardsClient\_destroy

```
void PgsLeaderboardsClient_destroy(
  PgsLeaderboardsClient *leaderboards_client
)
```

Destroys a Leaderboards Client instance.

This function releases all resources associated with the client handle. The handle becomes invalid after this call.

Details | || Parameters | |  |  | | --- | --- | | `leaderboards_client` | The client handle to destroy. | |

### PgsRecallClient\_create

```
PgsRecallClient * PgsRecallClient_create(
  jobject activity
)
```

Creates a new Recall Client instance.

Details | || Parameters | |  |  | | --- | --- | | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsRecallClient handle, or NULL on failure. This handle must be released with [PgsRecallClient\_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1gaf6a9487b7684d715d789c263bc14ad26). |

### PgsRecallClient\_destroy

```
void PgsRecallClient_destroy(
  PgsRecallClient *recall_client
)
```

Destroys a Recall Client instance.

Details | || Parameters | |  |  | | --- | --- | | `recall_client` | The client handle to destroy. | |

### PgsSnapshotsClient\_create

```
PgsSnapshotsClient * PgsSnapshotsClient_create(
  jobject activity
)
```

Creates a new Snapshots Client instance.

Details | || Parameters | |  |  | | --- | --- | | `activity` | A JNI reference to a valid Android Activity. | |
| **Returns** | A new PgsSnapshotsClient handle, or NULL on failure. This handle must be released with [PgsSnapshotsClient\_destroy()](https://developer.android.com/games/services/cpp/v2/api/group/play-games#group__play__games_1ga61b4877cdfae489eebe20353b75fa4d1). |

### PgsSnapshotsClient\_destroy

```
void PgsSnapshotsClient_destroy(
  PgsSnapshotsClient *snapshots_client
)
```

Destroys a Snapshots Client instance.

Details | || Parameters | |  |  | | --- | --- | | `snapshots_client` | The client handle to destroy. | |

### Pgs\_destroy

```
void Pgs_destroy()
```

Shuts down the Play Games Services native SDK.

This should be called once when the application is closing to clean up all global references.

### Pgs\_initialize

```
jint Pgs_initialize(
  JavaVM *vm,
  jobject context
)
```

Initializes the Play Games Services native SDK.

This must be called once at application startup before any other SDK functions.

Details | || Parameters | |  |  | | --- | --- | | `vm` | The `JavaVM` pointer obtained. | | `context` | An Android `Activity` object. | |
| **Returns** | `JNI_OK` on success, or `JNI_ERR` on failure. |

#!/usr/bin/env python3
"""Author the games domain taxonomy."""

import _bootstrap  # noqa: F401
from featuretree.taxonomy_authoring import bind, feature, merge_bindings, pending, write_domain


def A(symbol, url, kind="class"):
    return bind("android", kind, symbol, url)


def I(symbol, url, kind="framework"):
    return bind("ios", kind, symbol, url)


def H(symbol, url, kind="module"):
    return bind("harmonyos", kind, symbol, url)


AXIS_L2 = "games_capability_family"


def B(a=None, i=None, h=None):
    parts = []
    if a:
        parts.append(A(a[0], a[1], a[2] if len(a) > 2 else "class"))
    else:
        parts.append(pending("android"))
    if i:
        parts.append(I(i[0], i[1], i[2] if len(i) > 2 else "framework"))
    else:
        parts.append(pending("ios"))
    if h:
        parts.append(H(h[0], h[1], h[2] if len(h) > 2 else "module"))
    else:
        parts.append(pending("harmonyos"))
    return merge_bindings(*parts)


def leaf(f, fid, parent, axis, zh, en, definition, includes, excludes, bindings, legacy=None, level="L3", privacy="none"):
    f.append(feature(
        fid, parent=parent, level=level, zh=zh, en=en, definition=definition,
        includes=includes, excludes=excludes, sibling_axis=axis,
        granularity="atomic", bindings=bindings,
        legacy=legacy or {"disposition": "new", "sources": []},
        privacy_class=privacy,
    ))


def build() -> list[dict]:
    f: list[dict] = []
    f.append(feature(
        "games", parent=None, level="L1",
        zh="游戏服务", en="Game Services",
        definition="玩家账号、成就排行、多人会话与游戏引擎系统服务；不含完整游戏引擎编辑器。",
        includes=['玩家、成就、多人、引擎系统服务'],
        excludes=['完整 Unity/Unreal 引擎本体', '通用推送见 notifications'],
        legacy={'disposition': 'new', 'sources': []},
    ))
    l2 = [
        ('games.player', '玩家与登录', 'Player and Sign-In', '玩家身份、登录与游戏存档。', ['登录、玩家资料、存档'], ['成就见 achievements'], []),
        ('games.achievements', '成就与排行', 'Achievements and Leaderboards', '成就、排行榜与事件。', ['成就、排行榜、事件'], ['多人见 multiplayer'], []),
        ('games.multiplayer', '多人会话', 'Multiplayer Sessions', '实时/回合多人与房间匹配。', ['实时、回合、匹配'], ['近场快传见 distributed.nearby'], []),
        ('games.engine_services', '引擎系统服务', 'Engine System Services', '游戏模式、帧速率、性能提示等系统服务。', ['Game Mode、性能提示'], ['完整引擎编辑器排除'], []),
    ]
    for fid, zh, en, definition, includes, excludes, sources in l2:
        if isinstance(sources, dict):
            legacy = sources
        else:
            legacy = {"disposition": "kept" if sources else "new", "sources": sources}
        f.append(feature(
            fid, parent="games", level="L2", zh=zh, en=en, definition=definition,
            includes=includes, excludes=excludes, sibling_axis=AXIS_L2,
            legacy=legacy,
        ))

    # --- games.player ---
    leaf(f, "games.player.sign_in", "games.player", "player_operation", "游戏玩家登录", "Game Player Sign-In",
         "登录游戏中心/游戏服务玩家账号。", ['GamesSignIn / GKLocalPlayer'], ['资料见 profile'],
         B(('Play Games Services Sign-in', 'https://developer.android.com/games/pgs/android/android-start', 'guide'), ('GameKit', 'https://developer.apple.com/documentation/gamekit', 'framework'), ('Game Service', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-kit-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "games.player.profile", "games.player", "player_operation", "玩家资料", "Player Profile",
         "读取玩家昵称、头像等资料。", ['player profile'], ['登录见 sign_in'],
         B(('PlayersClient', 'https://developer.android.com/games/pgs/android/android-start', 'guide'), ('GKLocalPlayer', 'https://developer.apple.com/documentation/gamekit/gklocalplayer', 'class'), ('Game Service', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-kit-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.player.saved_games", "games.player", "player_operation", "游戏云存档", "Cloud Saved Games",
         "保存与加载云端游戏进度。", ['Saved Games / GKSavedGame'], ['登录见 sign_in'],
         B(('Saved Games', 'https://developer.android.com/games/pgs/android/saved-games', 'guide'), ('GKSavedGame', 'https://developer.apple.com/documentation/gamekit/gksavedgame', 'protocol'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.player.friends", "games.player", "player_operation", "玩家好友列表", "Player Friends",
         "读取游戏好友与授权。", ['friends'], ['多人邀请见 multiplayer'],
         B(('PlayersClient.loadFriends', 'https://developer.android.com/games/pgs/android/android-start', 'guide'), ('GKLocalPlayer.loadFriends', 'https://developer.apple.com/documentation/gamekit/gklocalplayer', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="runtime_permission")
    leaf(f, "games.player.identity_verify", "games.player", "player_operation", "玩家身份校验", "Player Identity Verify",
         "服务端校验玩家身份令牌。", ['server auth code / identityVerification'], ['登录见 sign_in'],
         B(('Games auth code', 'https://developer.android.com/games/pgs/android/android-start', 'guide'), ('fetchItems forIdentityVerificationSignature', 'https://developer.apple.com/documentation/gamekit/gklocalplayer', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- games.achievements ---
    leaf(f, "games.achievements.unlock", "games.achievements", "achievements_operation", "成就解锁进度", "Achievement Unlock Progress",
         "解锁成就或更新成就进度。", ['AchievementsClient / GKAchievement'], ['排行榜见 leaderboards'],
         B(('AchievementsClient', 'https://developer.android.com/games/pgs/android/achievements', 'guide'), ('GKAchievement', 'https://developer.apple.com/documentation/gamekit/gkachievement', 'class'), ('Game Service', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-kit-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.achievements.leaderboards", "games.achievements", "achievements_operation", "排行榜分数", "Leaderboard Scores",
         "提交与查询排行榜分数。", ['LeaderboardsClient / GKLeaderboard'], ['成就见 unlock'],
         B(('LeaderboardsClient', 'https://developer.android.com/games/pgs/android/leaderboards', 'guide'), ('GKLeaderboard', 'https://developer.apple.com/documentation/gamekit/gkleaderboard', 'class'), ('Game Service', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-kit-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.achievements.events", "games.achievements", "achievements_operation", "游戏事件", "Game Events",
         "记录可触发成就的游戏事件。", ['EventsClient'], ['成就见 unlock'],
         B(('EventsClient', 'https://developer.android.com/games/pgs/android/events', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.achievements.ui", "games.achievements", "achievements_operation", "成就排行榜界面", "Achievements Leaderboards UI",
         "展示系统成就/排行榜界面。", ['UI intents'], ['提交见 unlock/leaderboards'],
         B(('AchievementsClient.getAchievementsIntent', 'https://developer.android.com/games/pgs/android/achievements', 'guide'), ('GKGameCenterViewController', 'https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.achievements.challenges", "games.achievements", "achievements_operation", "挑战", "Challenges",
         "向好友发起分数或成就挑战。", ['GKChallenge'], ['好友见 player.friends'],
         B(None, ('GKChallenge', 'https://developer.apple.com/documentation/gamekit/gkchallenge', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- games.multiplayer ---
    leaf(f, "games.multiplayer.realtime", "games.multiplayer", "multiplayer_operation", "实时多人", "Realtime Multiplayer",
         "建立实时多人房间并收发消息。", ['Real-time multiplayer / GKMatch'], ['回合制见 turn_based'],
         B(('Real-time multiplayer', 'https://developer.android.com/games/pgs/android/realtime-multiplayer', 'guide'), ('GKMatch', 'https://developer.apple.com/documentation/gamekit/gkmatch', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.multiplayer.turn_based", "games.multiplayer", "multiplayer_operation", "回合制多人", "Turn-Based Multiplayer",
         "回合制对局托管与回合提交。", ['TurnBasedMultiplayer / GKTurnBasedMatch'], ['实时见 realtime'],
         B(('Turn-based multiplayer', 'https://developer.android.com/games/pgs/android/turnbased-multiplayer', 'guide'), ('GKTurnBasedMatch', 'https://developer.apple.com/documentation/gamekit/gkturnbasedmatch', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.multiplayer.matchmaking", "games.multiplayer", "multiplayer_operation", "匹配排队", "Matchmaking",
         "按规则匹配玩家进入对局。", ['matchmaking'], ['房间见 realtime'],
         B(('Real-time matchmaking', 'https://developer.android.com/games/pgs/android/realtime-multiplayer', 'guide'), ('GKMatchmaker', 'https://developer.apple.com/documentation/gamekit/gkmatchmaker', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.multiplayer.invites", "games.multiplayer", "multiplayer_operation", "对局邀请", "Match Invites",
         "发送与接收对局邀请。", ['invitations'], ['好友见 player.friends'],
         B(('Invitations', 'https://developer.android.com/games/pgs/android/realtime-multiplayer', 'guide'), ('GKInvite', 'https://developer.apple.com/documentation/gamekit/gkinvite', 'class'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.multiplayer.nearby_transfer", "games.multiplayer", "multiplayer_operation", "近场游戏快传", "Nearby Game Transfer",
         "近场传递游戏内容或对局。", ['nearby game transfer'], ['通用近场见 distributed.nearby'],
         B(('Nearby Connections', 'https://developers.google.com/nearby/connections/overview', 'guide'), ('Multipeer Connectivity', 'https://developer.apple.com/documentation/multipeerconnectivity', 'framework'), ('Share Kit', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-kit-guide')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")

    # --- games.engine_services ---
    leaf(f, "games.engine_services.game_mode", "games.engine_services", "engine_services_operation", "游戏模式", "Game Mode",
         "声明并查询系统游戏模式。", ['GameModeManager'], ['性能提示见 performance_hint'],
         B(('Game Mode', 'https://developer.android.com/games/gamemode/gamemode-api', 'guide'), None, ('Game quality', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/game-quality')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.engine_services.performance_hint", "games.engine_services", "engine_services_operation", "性能提示会话", "Performance Hint Session",
         "向系统提供帧速率等性能提示。", ['PerformanceHintManager / AGDK'], ['游戏模式见 game_mode'],
         B(('Performance Hint API', 'https://developer.android.com/games/optimize/performance-hint', 'guide'), None, ('GPM', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/game-quality')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.engine_services.frame_pacing", "games.engine_services", "engine_services_operation", "帧节奏控制", "Frame Pacing",
         "控制游戏帧节奏与垂直同步策略。", ['Android Frame Pacing'], ['性能提示见 performance_hint'],
         B(('Android Frame Pacing', 'https://developer.android.com/games/sdk/frame-pacing', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.engine_services.game_activity", "games.engine_services", "engine_services_operation", "游戏活动宿主", "Game Activity Host",
         "使用游戏专用 Activity/宿主集成原生引擎。", ['GameActivity'], ['完整引擎排除'],
         B(('GameActivity', 'https://developer.android.com/games/agdk/game-activity', 'guide'), None, None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.engine_services.input_sdk", "games.engine_services", "engine_services_operation", "游戏输入服务", "Game Input Services",
         "游戏手柄与触控手势游戏输入服务。", ['GameController / AGDK input'], ['通用输入见 input'],
         B(('Game Controller', 'https://developer.android.com/games/sdk/game-controller', 'guide'), ('GCController', 'https://developer.apple.com/documentation/gamecontroller', 'framework'), None), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")
    leaf(f, "games.engine_services.quality_telemetry", "games.engine_services", "engine_services_operation", "游戏质量遥测", "Game Quality Telemetry",
         "采集游戏卡顿/温度等质量遥测。", ['GPM / AGDK telemetry'], ['通用指标见 observability.metrics'],
         B(('Android GPU Inspector hooks', 'https://developer.android.com/agp', 'guide'), None, ('GPM', 'https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/game-quality')), {'disposition': 'new', 'sources': []}, level="L3", privacy="none")


    leaf(f, "games.player.player_stats", "games.player", "player_operation", "玩家统计", "Player Stats",
         "读取玩家游戏统计数据。", ["PlayerStats"], ["资料见 profile"],
         B(("PlayerStatsClient", "https://developer.android.com/games/pgs/android/stats", "guide"), None, None))
    leaf(f, "games.player.recall_token", "games.player", "player_operation", "玩家召回令牌", "Player Recall Token",
         "获取用于召回安装的玩家令牌。", ["recall tokens"], ["登录见 sign_in"],
         B(("RecallClient", "https://developer.android.com/games/pgs/android/android-start", "guide"), None, None))
    leaf(f, "games.achievements.incremental", "games.achievements", "achievements_operation", "增量成就", "Incremental Achievements",
         "更新需要多步完成的增量成就。", ["incremental achievements"], ["解锁见 unlock"],
         B(("AchievementsClient increment", "https://developer.android.com/games/pgs/android/achievements", "guide"),
           ("GKAchievement percentComplete", "https://developer.apple.com/documentation/gamekit/gkachievement", "class"), None))
    leaf(f, "games.achievements.hidden", "games.achievements", "achievements_operation", "隐藏成就揭示", "Reveal Hidden Achievements",
         "揭示隐藏成就。", ["reveal achievement"], ["解锁见 unlock"],
         B(("AchievementsClient reveal", "https://developer.android.com/games/pgs/android/achievements", "guide"),
           ("GKAchievement", "https://developer.apple.com/documentation/gamekit/gkachievement", "class"), None))
    leaf(f, "games.multiplayer.reliable_msg", "games.multiplayer", "multiplayer_operation", "可靠消息通道", "Reliable Message Channel",
         "在实时对局中发送可靠消息。", ["reliable messages"], ["实时见 realtime"],
         B(("Real-time messages", "https://developer.android.com/games/pgs/android/realtime-multiplayer", "guide"),
           ("GKMatch sendData", "https://developer.apple.com/documentation/gamekit/gkmatch", "class"), None))
    leaf(f, "games.multiplayer.unreliable_msg", "games.multiplayer", "multiplayer_operation", "不可靠消息通道", "Unreliable Message Channel",
         "在实时对局中发送低延迟不可靠消息。", ["unreliable messages"], ["可靠见 reliable_msg"],
         B(("Real-time messages", "https://developer.android.com/games/pgs/android/realtime-multiplayer", "guide"),
           ("GKMatch sendData", "https://developer.apple.com/documentation/gamekit/gkmatch", "class"), None))
    leaf(f, "games.engine_services.thermal", "games.engine_services", "engine_services_operation", "游戏热状态", "Game Thermal State",
         "监听热状态以调节游戏负载。", ["thermal state"], ["性能提示见 performance_hint"],
         B(("PowerManager thermal", "https://developer.android.com/reference/android/os/PowerManager"),
           ("ProcessInfo.ThermalState", "https://developer.apple.com/documentation/foundation/processinfo/thermalstate", "struct"), None))
    leaf(f, "games.engine_services.loading_overlay", "games.engine_services", "engine_services_operation", "游戏加载提示", "Game Loading Hint",
         "向系统声明游戏加载阶段以优化调度。", ["loading hints"], ["游戏模式见 game_mode"],
         B(("Game Mode", "https://developer.android.com/games/gamemode/gamemode-api", "guide"), None, None))
    leaf(f, "games.engine_services.vulkan_loader", "games.engine_services", "engine_services_operation", "游戏图形加载器服务", "Game Graphics Loader Service",
         "游戏侧图形 API 加载器系统服务入口（非完整引擎）。", ["graphics loader hooks"], ["帧节奏见 frame_pacing"],
         B(("AGDK", "https://developer.android.com/games/agdk", "guide"),
           ("Metal", "https://developer.apple.com/documentation/metal", "framework"), None))
    leaf(f, "games.achievements.leaderboard_span", "games.achievements", "achievements_operation", "排行榜时间跨度", "Leaderboard Time Span",
         "按日/周/全时查询排行榜。", ["time span"], ["分数见 leaderboards"],
         B(("LeaderboardsClient", "https://developer.android.com/games/pgs/android/leaderboards", "guide"),
           ("GKLeaderboard.TimeScope", "https://developer.apple.com/documentation/gamekit/gkleaderboard/timescope", "enum"), None))
    leaf(f, "games.player.plus_profile", "games.player", "player_operation", "玩家主页界面", "Player Profile UI",
         "展示系统玩家主页/比较界面。", ["compare profile UI"], ["资料见 profile"],
         B(("PlayersClient.getCompareProfileIntent", "https://developer.android.com/games/pgs/android/android-start", "guide"),
           ("GKGameCenterViewController", "https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller", "class"), None))
    leaf(f, "games.multiplayer.automatch", "games.multiplayer", "multiplayer_operation", "自动补位匹配", "Automatch Fill-In",
         "用自动匹配填满房间空位。", ["automatch"], ["匹配见 matchmaking"],
         B(("Real-time automatch", "https://developer.android.com/games/pgs/android/realtime-multiplayer", "guide"),
           ("GKMatchRequest", "https://developer.apple.com/documentation/gamekit/gkmatchrequest", "class"), None))


    leaf(f, "games.multiplayer.participant_status", "games.multiplayer", "multiplayer_operation", "参与者状态", "Participant Status",
         "查询对局参与者连接与回合状态。", ["participant status"], ["实时见 realtime"],
         B(("Real-time multiplayer", "https://developer.android.com/games/pgs/android/realtime-multiplayer", "guide"),
           ("GKPlayer", "https://developer.apple.com/documentation/gamekit/gkplayer", "class"), None))
    leaf(f, "games.engine_services.orientation_lock", "games.engine_services", "engine_services_operation", "游戏方向锁定提示", "Game Orientation Lock Hint",
         "向系统提示游戏方向锁定偏好。", ["orientation hint"], ["游戏模式见 game_mode"],
         B(("Game Mode", "https://developer.android.com/games/gamemode/gamemode-api", "guide"), None, None))

    return f


def main():
    nodes = build()
    dedup = {}
    for node in nodes:
        dedup[node["id"]] = node
    nodes = list(dedup.values())
    path = write_domain("games", nodes)
    print(f"wrote {len(nodes)} nodes -> {path}")


if __name__ == "__main__":
    main()
